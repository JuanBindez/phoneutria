.. _install:

Installation of phoneutria
======================

This guide assumes you already have python and pip installed.

To install phoneutria, run the following command in your terminal::

    $ pip install phoneutria

Get the Source Code
-------------------

phoneutria is actively developed on GitHub, where the source is `available <https://github.com/JuanBindez/phoneutria>`_.

You can either clone the public repository::

    $ git clone git://github.com/JuanBindez/phoneutria.git

Or, download the `tarball <https://github.com/JuanBindez/phoneutria/tarball/master>`_::

    $ curl -OL https://github.com/JuanBindez/phoneutria/tarball/master
    # optionally, zipball is also available (for Windows users).

Once you have a copy of the source, you can embed it in your Python package, or install it into your site-packages by running::

    $ cd phoneutria
    $ python -m pip install .
