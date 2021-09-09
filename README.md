# python-docs-samples-networking-cidr


Note: This code will be moved to https://github.com/GoogleCloudPlatform/python-docs-samples under networking/samples. Folder structure as per https://github.com/googleapis/python-compute/tree/main/samples/snippets

## Description

Google publishes the complete list of outbound IP address ranges that it makes available to users on the internet in goog.json.

Google also publishes a list of global and regional external IP addresses ranges available for customer's Google Cloud resources in cloud.json.

Goal of this script is to identify & show the available CIDRs. To learn more about CIDR check at [Link](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)

This Script compatible to both Py27 & Py36


## How to Run?


(Optional) Using `virtualenv` is an effective to ensure script executions without disturbing your existing local environment. To step your virtualenv, run the following steps

```python3
pip3 install virtualenv
virtualenv --python python3 name-of-your-virtualenv
source name-of-your-virtualenv/bin/activate
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
