from bottle import route, run, response, hook, request
from properties import *
import json as j
import requests as r

@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

#TEST working
@route('/')
def get_test():
    log_api.info(request.method + '/')
    return j.dumps({'test': 'ok'})

#---- MDB SEARCH
@route('/mdb/search/movie/<search>')
@route('/mdb/search/movie/<search>/<page>')
def get_mdb_movie_search(search, page="1"):
    log_api.info(request.method + '/mdb/movie/' + search + '/' + page)
    return j.dumps(r.get(MovieDB.Urls.search_movie.replace('{query}', search).replace('{page}', page)).json())


@route('/mdb/search/tv/<search>')
@route('/mdb/search/tv/<search>/<page>')
def get_mdb_tv_search(search, page="1"):
    log_api.info(request.method + '/mdb/tv/' + search + '/' + page)
    return j.dumps(r.get(MovieDB.Urls.search_tv.replace('{query}', search).replace('{page}', page)).json())


@route('/mdb/movie/<id>')
def get_mdb_movie_detail(id):
    log_api.info(request.method + '/mdb/movie/' + id)
    return j.dumps(r.get(MovieDB.Urls.detail_movie.replace('{id}', id)).json())


@route('/mdb/poster/movie/<id>')
def get_mdb_poster_movie_detail(id):
    log_api.info(request.method + '/mdb/movie/' + id)
    return j.dumps({'path': MovieDB.Urls.poster_185 + r.get(MovieDB.Urls.detail_movie.replace('{id}', id)).json()['poster_path'], 'id': id})


@route('/mdb/poster/tv/<id>')
def get_mdb_poster_movie_detail(id):
    log_api.info(request.method + '/mdb/movie/' + id)
    return j.dumps({'path': MovieDB.Urls.poster_185 + r.get(MovieDB.Urls.detail_tv.replace('{id}', id)).json()['poster_path'], 'id': id})


@route('/mdb/movie/genres')
def get_mdb_movie_genres():
    log_api.info(request.method + '/mdb/movie/genres')
    return j.dumps(r.get(MovieDB.Urls.genre_movie_list).json())


@route('/mdb/genre/<id>/movie/')
@route('/mdb/genre/<id>/movie/<page>')
def get_mdb_tv_genres(id, page="1"):
    log_api.info(request.method + '/mdb/genre/' + id + '/movie/' + page)
    return j.dumps(r.get(MovieDB.Urls.movie_by_genre_list.replace('{id}', id).replace('{page}', page)).json())

#---- MDB SEARCH

#Start api
run(host='0.0.0.0', port=config.port, debug=True)
