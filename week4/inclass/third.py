import logging
logging.basicConfig(level=logging.DEBUG)

squares = [value ** 2 for value in range(1,11)]

logging.debug("squares")
logging.debug(squares)

capitalized = [   name.title()      for name in ['chris', 'tom','joe','suzy']          ]
logging.debug("capitalized:")
logging.debug(capitalized)

