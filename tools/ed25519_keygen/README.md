# Ed25519 Keygen

Simmilar to `ssh-keygen`, `ed25519_keygen` is a simple python script for generation of keyvalue pair using Python3. As the name suggests, the key values pairs generated using [Ed25519 Crypto Algorithm](https://en.wikipedia.org/wiki/EdDSA#Ed25519).

> Note: This script uses python cryptography library.


### Officially Supported Python Versions
Python 3.6, 3.7, 3.8, 3.9 & 3.10


## How to Run?


(Optional) Using `virtualenv` is an effective to ensure script executions without disturbing your existing local environment. To step your virtualenv, run the following steps

```python3
pip3 install virtualenv
virtualenv --python python3 py3
source py3/bin/activate
````

To install the requirements

```python3
pip install -r requirements.txt
```

To run the script
```python
python ed25519_keygen.py
```

To exit the virtualenv

```python
deactivate
```


## How to run testcases?

Create a python virtual environment `py3`
```python3
pip3 install virtualenv
virtualenv --python python3 py3
```

Install requirements and run testcases
```
source py3/bin/activate
pip install -r requirements.txt -r dev-requirements.txt
python3 -m pytest
# Test for multiple python version
nox
```

