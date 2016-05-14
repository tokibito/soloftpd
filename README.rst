========
soloftpd
========

config:

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

command::

   $ soloftpd --config=/etc/soloftpd.conf
