""" This is my first python program. """

import logging

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)

my_name = "Chris"  # But you can put your own name in here.

output = f"Hello, {my_name}"

logging.debug(output)
