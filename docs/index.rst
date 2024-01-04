.. phoneutria documentation master file,

phoneutria
======
Release v\ |version|. (:ref:`Installation<install>`)


.. image:: https://img.shields.io/pypi/v/phoneutria.svg
  :alt: Pypi
  :target: https://pypi.python.org/pypi/phoneutria/

.. image:: https://img.shields.io/pypi/pyversions/phoneutria.svg
  :alt: Python Versions
  :target: https://pypi.python.org/pypi/phoneutria/


**phoneutria** Python 3 library providing security testing capabilities for webservers, enabling GET and POST requests, and incorporating checks against common vulnerabilities such as XSS, SQL Injection, and CSRF..

-------------------

**Behold, a perfect balance of simplicity versus flexibility**::

    from phoneutria import Chelicera

    url = "testphp.vulnweb.com"

    ch = Chelicera(url)
    make_get_request(wordlist)

The User Guide
--------------
This part of the documentation begins with some background information about
the project, then focuses on step-by-step instructions for getting the most out
of phoneutria.

.. toctree::
   :maxdepth: 2

   user/install
   user/cli

The API Documentation
-----------------------------

If you are looking for information on a specific function, class, or method,
this part of the documentation is for you.

.. toctree::
   :maxdepth: 2

   api

