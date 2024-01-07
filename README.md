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

    phoneutria -gh access.logs

### Occurrence of the word in website:

    phoneutria -t https://api.example.com -w word

### To make a GET request of the all links in website:

    phoneutria -t https://api.example.com --links
