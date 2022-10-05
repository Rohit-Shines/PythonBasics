import logging

logging.basicConfig(filename='console.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

logging.warning('This is a warning message')

logging.error('This is an error message')

logging.debug('This is a debug message')