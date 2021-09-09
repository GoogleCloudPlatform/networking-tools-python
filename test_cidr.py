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

import os
import sys
import json

import cidr

from mock import Mock


class BaseClass:
    def setup_method(self, test_method):
        """To setup mock values for http requests"""
        os.environ['BUILD_SPECIFIC_GCLOUD_PROJECT'] = 'random'
        mock_values = {
            cidr.goog_url: open("samplefiles/goog.json"),
            cidr.cloud_url: open("samplefiles/cloud.json"),
        }
        _mock_fns = Mock()
        _mock_fns.side_effect = lambda x: mock_values.get(x)
        if sys.version_info.major == 3:
            cidr.urllib.request.urlopen = _mock_fns
        else:
            cidr.urllib.urlopen = _mock_fns


class TestHttpRequests(BaseClass):
    def test_goog_url(self):
        output = cidr.read_url(cidr.goog_url)
        expected_output = json.loads(open("samplefiles/goog.json").read())
        assert sorted(output.items()) == sorted(expected_output.items())

    def test_cloud_url(self):
        output = cidr.read_url(cidr.cloud_url)
        expected_output = json.loads(open("samplefiles/cloud.json").read())
        assert sorted(output.items()) == sorted(expected_output.items())


class TestMain(BaseClass):
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
        expected_output = open("samplefiles/output.txt").read().strip()
        assert len(set(expected_output) - set(current_output)) == 0
