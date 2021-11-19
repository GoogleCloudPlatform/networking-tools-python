# python-docs-samples-networking-cidr


<!-- Note: This code will be moved to https://github.com/GoogleCloudPlatform/python-docs-samples under networking/samples. Folder structure as per https://github.com/googleapis/python-compute/tree/main/samples/snippets -->


## Description

Google publishes the complete list of outbound IP address ranges that it makes available to users on the internet in goog.json.

Google also publishes a list of global and regional external IP addresses ranges available for customer's Google Cloud resources in cloud.json.

Goal of this script is to identify & show the available CIDRs. To learn more about CIDR check at [Link](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)

This Script compatible to both Py27 & Py36.

### Officially Supported Python Versions
Python 2.7 & Python 3.6, 3.7, 3.8, 3.9, 3.10


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
python cidr.py
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
