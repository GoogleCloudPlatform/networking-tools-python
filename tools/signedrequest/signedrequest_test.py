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
import base64
import unittest

from cryptography.hazmat.primitives.asymmetric import ed25519

import signedrequest


def get_sign(text: bytes) -> bytes:
    """Generate Ed25519 hash using private key."""
    test_private_key = ed25519.Ed25519PrivateKey.from_private_bytes(
        base64.urlsafe_b64decode(open("private.key", "rb").read())
    )
    return test_private_key.sign(text)


def is_valid(signed_text: bytes, text: bytes) -> bool:
    """Validate input string using only public key."""
    test_public_key = ed25519.Ed25519PublicKey.from_public_bytes(
        base64.urlsafe_b64decode(open("public.pub", "rb").read())
    )
    try:
        test_public_key.verify(signed_text, text)
        return True
    except Exception as err:
        raise Exception("Validation Failed")
        return False


class BaseClass(unittest.TestCase):
    @classmethod
    def setUp(cls):
        signedrequest.generate_ed25519_keypair()

    @classmethod
    def tearDown(cls):
        os.remove("private.key")
        os.remove("public.pub")


class TestHttpRequests(BaseClass):
    def test_basic_text_check(self):
        text = b"hello world!"
        test_sign = get_sign(text)
        is_valid(test_sign, text)

    def test_basic_signedurl_check(self):
        text = b"http://www.example.com/some/path?some=query&another=param"
        test_sign = get_sign(text)
        is_valid(test_sign, text)

    def test_basic_signedurl_ipcheck(self):
        text = b"http://35.186.234.33/index.html?Expires=1650848400&KeyName=my-key&"
        test_sign = get_sign(text)
        is_valid(test_sign, text)
