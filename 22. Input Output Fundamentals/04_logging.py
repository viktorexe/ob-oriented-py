# Logging is basically keeping a record of whatever the program does
# Whatever 
# - Errors
# - Scraping
# - Saving to mongo
# Whenever code does some thing it has to be looged, like a log of attendance of students 
# We can sync logs to a txt file somewhere in directory 

import logging
logging.basicConfig(filename = 'mylogging.txt', level=logging.INFO) # File to log into

logging.info('Loading')
logging.warning('API key exposed')
logging.error('API not found')