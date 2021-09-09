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

import sys
import json
import netaddr

try:
    import urllib.request
except ImportError:
    import urllib
    import urllib2

goog_url = "https://www.gstatic.com/ipranges/goog.json"
cloud_url = "https://www.gstatic.com/ipranges/cloud.json"


def read_url_py2(url):
    try:
        return urllib.urlopen(url).read()
    except urllib2.HTTPError:
        print("Invalid HTTP response from %s" % url)
        return {}


def read_url_py3(url):
    try:
        return urllib.request.urlopen(url).read()
    except urllib.error.HTTPError:
        print("Invalid HTTP response from %s" % url)
        return {}

def read_url(url):
    try:
        if sys.version_info.major == 3:
            json_text = read_url_py3(url)
        else:
            json_text = read_url_py2(url)
        return json.loads(json_text)
    except json.decoder.JSONDecodeError:
        print("Could not parse HTTP response from %s" % url)
        return {}

def get_ip_address(url):
    json_data = read_url(url)
    network_cidrs = {
        'ipv4': netaddr.IPSet(),
        'ipv6': netaddr.IPSet(),
    }
    if json_data:
        print("{} published: {}".format(url, json_data.get('creationTime')))
        for e in json_data['prefixes']:
            if e.get('ipv4Prefix'):
                network_cidrs['ipv4'].add(e.get('ipv4Prefix'))
            if e.get('ipv6Prefix'):
                network_cidrs['ipv6'].add(e.get('ipv6Prefix'))
    return network_cidrs

def main():
    print('Python version ' + sys.version)
    goog_cidrs = get_ip_address(goog_url)
    cloud_cidrs = get_ip_address(cloud_url)
    print("IP ranges for Google APIs and services default domains:")
    for key in ['ipv4', 'ipv6']:
        for i in goog_cidrs[key].difference(cloud_cidrs[key]).iter_cidrs():
            print(i)


if __name__ == '__main__':
    main()
