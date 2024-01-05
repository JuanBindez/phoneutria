# phoneutria

![PyPI - Downloads](https://img.shields.io/pypi/dm/phoneutria)
![PyPI - License](https://img.shields.io/pypi/l/phoneutria)
![PyPI - Version](https://img.shields.io/pypi/v/phoneutria)

## Description

Python 3 library providing security testing capabilities for webservers, enabling GET and POST requests, and incorporating checks against common vulnerabilities such as XSS, SQL Injection, and CSRF.


## install:

    pip install phoneutria

-----------------

## install in ubuntu:

    pip install phoneutria --break-system-packages
----------

## Command line usage:

### Google Hacking:

    phoneutria --google_hacking access.logs

### To make a POST request:

    phoneutria -t https://api.example.com --post "key1=value1&key2=value2"


### To make a GET request:

    phoneutria -t https://api.example.com --get name email
