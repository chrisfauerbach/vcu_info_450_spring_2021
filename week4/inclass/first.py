import logging
logging.basicConfig(level=logging.DEBUG)
cars = ['bmw', 'audi', 'toyota', 'subaru']
logging.debug("Original list.")
logging.debug(cars)
cars.reverse()   # Reverse the order of the list
logging.debug("Permanent reversed cars: ")
logging.debug(cars)

# After here is reverse order.
# DEBUG:root:['subaru', 'toyota', 'audi', 'bmw']

logging.debug("-1, last item in list")
logging.debug(cars[-1])         # Get the last item from the list


logging.debug("0 first item in list.")
logging.debug(cars[0])       # Get the first item in the list

logging.debug("0:1")
logging.debug(cars[0:1])        # Get a SLICE of the list (notice the type printed)
logging.debug("1:3")
logging.debug(cars[1:3])        # Get a slice with more than one element
# cars[55]         # Don't access items that don't exist!
logging.debug("1:")
logging.debug(cars[1:])

logging.debug(":2")
logging.debug(cars[:2])
