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

::

   $ soloftpd --config=/etc/soloftpd.conf

License
=======

* MIT License (See the LICENSE file.)
