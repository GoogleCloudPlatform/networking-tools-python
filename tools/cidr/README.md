# python-docs-samples-networking-cidr


<!-- Note: This code will be moved to https://github.com/GoogleCloudPlatform/python-docs-samples under networking/samples. Folder structure as per https://github.com/googleapis/python-compute/tree/main/samples/snippets -->


## Description

Google publishes the complete list of outbound IP address ranges that it makes available to users on the internet in `goog.json`.

Google also publishes a list of global and regional external IP addresses ranges available for customer's Google Cloud resources in `cloud.json`.

Goal of this script is to identify & show the available CIDRs. To learn more about CIDR check at [Link](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)

This script is Python 2 (2.7) and 3 (3.6+) compatible.

### Officially Supported Python Versions
Python 2.7 & Python 3.6, 3.7, 3.8, 3.9, 3.10


## How to Run?


(Optional) Using `virtualenv` is an effective to ensure script executions without disturbing your existing local environment. Run the following steps to execute the script safely in a Python 3 environment—a similar technique can be used to run it in Python 2:

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

## Troubleshooting

If you're on a Mac where local SSH certificates haven't been installed yet, you may get this error:

```
(py3) $ python cidr.py
ERROR: Invalid HTTP response from https://www.gstatic.com/ipranges/goog.json
ERROR: Invalid HTTP response from https://www.gstatic.com/ipranges/cloud.json
IP ranges for Google APIs and services default domains:
Traceback (most recent call last):
  File "/tmp/networking-tools-python/tools/cidr/cidr.py", line 65, in <module>
    main()
  File "/tmp/networking-tools-python/tools/cidr/cidr.py", line 60, in main
    for ip in (cidrs["goog"] - cidrs["cloud"]).iter_cidrs():
TypeError: unsupported operand type(s) for -: 'NoneType' and 'NoneType'
```

If this is the case, run the command shown below (Python 3.9 example):

    (py3) $ open /Applications/Python\ 3.9/Install\ Certificates.command

A window will pop up, run a few commands, then automatically close. Once that happens, you should be able to run `python cidr.py` again and have it work. If you don't use the command-line, then follow [these instructions](https://stackoverflow.com/a/53310545/305689) from your computer screen.
