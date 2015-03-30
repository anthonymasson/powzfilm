var DELAY_SEARCH = 1000;
var LIMIT_LENGTH_SEARCH = 3;
var API_HOST = 'http://127.0.0.1:4242';

var API_URLS = {
    search_movie: API_HOST + '/mdb/search/movie/<search>/<page>',
    detail_movie: API_HOST + '/mdb/movie/<id_movie>',
    image: 'https://image.tmdb.org/t/p/w185'
};