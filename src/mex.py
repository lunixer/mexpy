'''
 mex.py
 v0.1-b
 lunixer@zoho.com
 https://github.com/lunixer/mexpy
'''

import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# create a file handler
handler = logging.FileHandler('console.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

logger.info(' Booting script....')

exec(compile(source=open('src/libs/config.py').read(), filename='src/libs/config.py', mode='exec'))
logger.info(' Booting done....')

#records = {'john': 55, 'tom': 66}
#logger.debug(' Records: %s', records)
