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
# [START mediacdn_generate_ed25519_keys]
import base64
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization


def generate_ed25519_keypair() -> None:
    """Generate Ed25519 Keys Pairs."""
    private_key = ed25519.Ed25519PrivateKey.generate()
    public_key = private_key.public_key()

    private_key_str = private_key.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption(),
    )
    print("Private Key:\t", base64.urlsafe_b64encode(private_key_str))

    public_key_str = public_key.public_bytes(
        encoding=serialization.Encoding.Raw, format=serialization.PublicFormat.Raw
    )
    print("Public Key:\t", base64.urlsafe_b64encode(public_key_str))

    with open("private.key", "wb") as fp:
        fp.write(base64.urlsafe_b64encode(private_key_str))

    with open("public.pub", "wb") as fp:
        fp.write(base64.urlsafe_b64encode(public_key_str))


# [END mediacdn_generate_ed25519_keys]
if __name__ == "__main__":
    generate_ed25519_keypair()