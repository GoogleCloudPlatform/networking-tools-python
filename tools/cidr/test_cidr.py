# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import socket
import sys
import threading
import unittest

# Third party
import requests

import cidr


def get_free_port():
    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
    s.bind(("localhost", 0))
    address, port = s.getsockname()
    s.close()
    return port


# Global Variables
mock_server_port = get_free_port()
# Override Urls to use Mock Test Urls
cidr.IPRANGE_URLS = {
    "goog": "http://localhost:{}/ipranges/goog.json".format(mock_server_port),
    "cloud": "http://localhost:{}/ipranges/cloud.json".format(mock_server_port),
}


class MockServerRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(requests.codes.ok)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if self.path.endswith("goog.json"):
            fname = "samplefiles/goog.json"
            with open(fname) as fp:
                self.wfile.write(bytes(fp.read(), "utf-8"))
        elif self.path.endswith("cloud.json"):
            fname = "samplefiles/cloud.json"
            with open(fname) as fp:
                self.wfile.write(bytes(fp.read(), "utf-8"))
        else:
            mock_page = [
                "<html>",
                "<head><title>Mock Test</title></head>",
                "<body>",
                "<p>This is a test page.</p>",
                "You accessed path: {}",
                "</body>",
                "</html>",
            ]
            self.wfile.write(bytes("".join(mock_page).format(self.path), "utf-8"))
        return


class BaseClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configure mock server.
        cls.mock_server_port = mock_server_port
        cls.mock_server = HTTPServer(
            ("localhost", cls.mock_server_port), MockServerRequestHandler
        )
        cls.mock_server_thread = threading.Thread(target=cls.mock_server.serve_forever)
        cls.mock_server_thread.setDaemon(True)
        cls.mock_server_thread.start()
        print("Running Server")

    def setup_method(self, test_method):
        """To setup mock values for http requests"""
        os.environ["BUILD_SPECIFIC_GCLOUD_PROJECT"] = "random"


class TestHttpRequests(BaseClass):
    def test_request_response(self):
        url = "http://localhost:{port}/HealthCheck".format(port=mock_server_port)
        # Send a request to the mock API server and store the response.
        response = requests.get(url)
        # Confirm that the request-response cycle completed successfully.
        self.assertTrue(
            response.ok, msg="Failed to run test server! Install dev-requirements.txt"
        )

    def test_goog_url(self):
        output = cidr.read_url(cidr.IPRANGE_URLS["goog"])
        with open("samplefiles/goog.json") as fp:
            expected_output = json.loads(fp.read())
            self.assertEqual(
                sorted(output.items()),
                sorted(expected_output.items()),
                msg="Url Data Mistmatch!",
            )

    def test_cloud_url(self):
        output = cidr.read_url(cidr.IPRANGE_URLS["cloud"])
        with open("samplefiles/cloud.json") as fp:
            expected_output = json.loads(fp.read())
            self.assertEqual(
                sorted(output.items()),
                sorted(expected_output.items()),
                msg="Url Data Mistmatch!",
            )

    def test_main(self):
        try:
            import StringIO as io
        except ModuleNotFoundError:
            import io
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        cidr.main()
        sys.stdout = sys.__stdout__
        current_output = capturedOutput.getvalue().strip()
        with open("samplefiles/output.txt") as fp:
            expected_output = fp.read().strip()
        self.assertEqual(
            set(expected_output) - set(current_output), set(), msg="Output Mistmatch!"
        )


if __name__ == "__main__":
    unittest.main()
