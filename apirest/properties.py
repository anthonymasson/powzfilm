import logging
import argparse

#Arugment parsing
parser = argparse.ArgumentParser(description='Get images from site')
parser.add_argument('-eshost', '-e', type=str, help="host es", default='127.0.0.1:9200')
parser.add_argument('-index', '-i', type=str, help="index es", default='powzfilm')
parser.add_argument('-port', '-p', type=int, help="server port", default=4242)
parser.add_argument('-log', '-l', type=str, help="log filename", default='powzfilm.log')
config = parser.parse_args()


#Logger
logger = logging.getLogger('powzfilm') #fichier
log_api = logging.getLogger('powzfilm') #console
logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=config.log, filemode='w')
logging.getLogger("requests").setLevel(logging.WARNING)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter('%(name)-5s: %(levelname)-8s %(message)s'))
logging.getLogger('').addHandler(console)

#Complementary Information
config.es = config.eshost + '/' + config.index + '/'

#Print config
log_api.info('Start with ES : ' + config.es);
