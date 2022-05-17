#!/usr/bin/python

__author__ = "Juan Ramon Santana"
__copyright__ = "Copyright 2022, Grupo de Ingenieria Telematica, Universidad de Cantabria"
__license__ = "MIT"
__version__ = "0.1"

import sys, os, inspect
import configparser
import logging
from logging.handlers import RotatingFileHandler

############# CONSTANTS ##############

PROGRAM_NAME = inspect.stack()[0][1].split('.py', 1)[0].split('/')[-1]
PROGRAM_PATH = os.path.dirname(os.path.realpath(__file__))

# Get variables from config file
config = configparser.ConfigParser()
config.read(PROGRAM_PATH + '/' + PROGRAM_NAME + '.conf')

# Logging related variables
LOG_LEVEL = config.getint('general','LOG_LEVEL')    # NOTSET:0, DEBUG:10, INFO:20, WARNING:30, ERROR:40
LOG_MAX_FILE_SIZE_BYTES = config.getint('general','LOG_MAX_FILE_SIZE_BYTES')
LOG_MAX_NUMBER_FILES = config.getint('general','LOG_MAX_NUMBER_FILES')

# Setup loggers
logger = logging.getLogger(PROGRAM_NAME + "_logger")
if not os.path.exists(PROGRAM_PATH + '/logs/'):
    os.makedirs(PROGRAM_PATH + '/logs/')

handler = RotatingFileHandler(PROGRAM_PATH + '/logs/' + PROGRAM_NAME + '.log',
                              maxBytes=LOG_MAX_FILE_SIZE_BYTES,
                              backupCount=LOG_MAX_NUMBER_FILES)
formatter = logging.Formatter('%(asctime)s %(levelname)s\t| %(filename)s:%(lineno)s\t[%(funcName)s()]\t| %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(LOG_LEVEL)

############# PROGRAM ##############

def main(args):
    logger.info('Python Script Boilerplate')
    # Returns POSIX standard code
    return os.EX_OK

# Call the main function if this program is not being imported
if __name__ == '__main__':
    # main does not access to sys to get the cli arguments, but instead they are passed as parameters.
    sys.exit(main(sys.argv))
