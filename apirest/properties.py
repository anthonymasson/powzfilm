from api_key import API_KEY
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

class MovieDB:
    api_key = API_KEY
    api = 'http://api.themoviedb.org/3'
    class Urls:
        pass
    Urls.genre_movie_list = api + '/genre/movie/list?api_key=' + api_key
    Urls.movie_by_genre_list = api + '/genre/{id}/movie/list?page={page}&api_key=' + api_key
    Urls.genre_tv_list = api + '/genre/tv/list?api_key=' + api_key
    Urls.search_movie = api + '/search/movie?query={query}&page={page}&api_key=' + api_key
    Urls.detail_movie = api + '/movie/{id}?api_key=' + api_key
    Urls.search_tv = api + '/search/tv?query={query}&page={page}&api_key=' + api_key
    Urls.detail_tv = api + '/tv/{id}?api_key=' + api_key
    Urls.poster_185 = 'https://image.tmdb.org/t/p/w185'
    Urls.poster_500 = 'https://image.tmdb.org/t/p/w500'

#Print config
log_api.info('Start with ES : ' + config.es);

