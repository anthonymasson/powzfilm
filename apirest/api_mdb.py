from bottle import route, run, response, hook, request
from properties import *
import json as j
import requests as r


# MDB SEARCH
# MDB TV
@route('/mdb/search/tv/<search>')
@route('/mdb/search/tv/<search>/<page>')
def get_mdb_tv_search(search, page="1"):
    log_api.info(request.method + '/mdb/tv/' + search + '/' + page)
    return j.dumps(r.get(MovieDB.search_tv.replace('{query}', search).replace('{page}', page)).json())


@route('/mdb/poster/tv/<id_movie>')
def get_mdb_poster_movie_detail(id_movie):
    log_api.info(request.method + '/mdb/movie/' + id_movie)
    tv = r.get(MovieDB.detail_tv.replace('{id}', id_movie)).json()
    return j.dumps({'path': MovieDB.poster_185 + tv['poster_path'], 'id': id_movie})


@route('/mdb/tv/genres')
def get_mdb_tv_genres():
    log_api.info(request.method + '/mdb/tv/genres')
    return j.dumps(r.get(MovieDB.genre_tv_list).json())


# MDB Movie
@route('/mdb/search/movie/<search>')
@route('/mdb/search/movie/<search>/<page>')
def get_mdb_movie_search(search, page="1"):
    log_api.info(request.method + '/mdb/movie/' + search + '/' + page)
    return j.dumps(r.get(MovieDB.search_movie.replace('{query}', search).replace('{page}', page)).json())


@route('/mdb/movie/<id_movie>')
def get_mdb_movie_detail(id_movie):
    log_api.info(request.method + '/mdb/movie/' + id_movie)
    return j.dumps(r.get(MovieDB.detail_movie.replace('{id}', id_movie)).json())


@route('/mdb/poster/movie/<id_movie>')
def get_mdb_poster_movie_detail(id_movie):
    log_api.info(request.method + '/mdb/movie/' + id_movie)
    movie = r.get(MovieDB.detail_movie.replace('{id}', id_movie)).json()
    return j.dumps({'path': MovieDB.poster_185 + movie['poster_path'], 'id': id_movie})


@route('/mdb/movie/genres')
def get_mdb_movie_genres():
    log_api.info(request.method + '/mdb/movie/genres')
    return j.dumps(r.get(MovieDB.genre_movie_list).json())


@route('/mdb/genre/<id_genre>/movie')
@route('/mdb/genre/<id_genre>/movie/<page>')
def get_mdb_movie_genres(id_genre, page="1"):
    log_api.info(request.method + '/mdb/genre/' + id_genre + '/movie/' + page)
    return j.dumps(r.get(MovieDB.movie_by_genre_list.replace('{id}', id_genre).replace('{page}', page)).json())