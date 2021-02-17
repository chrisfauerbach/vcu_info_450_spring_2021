import logging
logging.basicConfig(level=logging.DEBUG)
magicians = ['alice', 'pat', 'pallavi', 'sam']
# For loop helps us iterate the list. 
# Can be thought of as: "for each item in the list, do something with that item"
# In this example, the individual item will be assigned to the variable: magician
# for each magician in the list of magicians, let's log it
for magician in magicians:
    logging.debug("Somethign for this magician.")
    logging.debug(magician)
logging.debug("DONE")

logging.debug("Start students.")
students = []
for student in students:
    logging.debug("Is there a student?")
    logging.debug(student)
logging.debug("Done students.")