========
soloftpd
========

Config
======

.. code-block:: json

   {
     "address": "127.0.0.1",
     "port": 21,
     "passive-ports": [30000, 50000],
     "masquerade-address": null,
     "username": "spam",
     "password": "egg",
     "directory": "/path/to/user/",
     "permission": "elradfmw"
   }

Command
=======

start server::

   $ soloftpd

using custom config file(default: /etc/soloftpd.conf)::

   $ soloftpd --config=/path/to/soloftpd.conf

override config with command line option::

   $ soloftpd --username=ham --address=10.0.0.1

make password hash::

   $ python -m soloftpd.authorizers your_password

License
=======

* MIT License (See the LICENSE file.)
