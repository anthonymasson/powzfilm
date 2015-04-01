////------------[Controllers]
function Movie(id_imdb, i_movie){
    if (angular.isDefined(i_movie)){
        this.title = i_movie.title;
        this.poster_path = i_movie.poster_path;
        this.genres = {};
        for (var g in i_movie.genres)
            this.genres[i_movie.genres[g]['id']] = i_movie.genres[g];
        this.synopsis = i_movie.overview;
        this.spoken_languages = [];
        for (var l in i_movie.spoken_languages)
            this.spoken_languages[this.spoken_languages.length] = i_movie.spoken_languages[l];
        this.imdb_id = id_imdb;
        this.release_date = i_movie.release_date;
    }
}

powzfilmControllers.controller('AddFilmCtrl', ['$scope', '$location', '$routeParams', '$http', '$timeout',
    function ($scope, $location, $routeParams, $http, $timeout) {
        var nb_elem_row = 4;
        $scope.selected_imdb = false;
        $scope.search_imdb = "harry";
        $scope.imdb_res = [];
        $scope.select_imdb = function(id){
            $http.get(API_URLS.detail_movie.replace('<id_movie>', id)).success(function (res){
                $scope.selected_imdb = id;
                $scope.new_movie = new Movie(id, res);
            }).error(function (res){
               console.log(res); 
            });
        };
        $http.get(API_URLS.genres).success(function (res){
                $scope.genres = {};
                for (var r in res['genres'])
                    $scope.genres[res['genres'][r]['id']] = res['genres'][r];
            }).error(function (res){
               console.log(res); 
            });
        
        $scope.unselectGenre = function(id){delete $scope.new_movie.genres[id];};
        
        $scope.change_selected_imdb = function(){$scope.selected_imdb = false;};
        var filterTextTimeout;
        $scope.$watch('search_imdb', function (val) {
            if (filterTextTimeout) $timeout.cancel(filterTextTimeout);
            filterTextTimeout = $timeout(function() {
                $scope.page = 1;
                if ($scope.search_imdb.length > LIMIT_LENGTH_SEARCH){
                    $scope.selected_imdb = null;
                    $http.get(API_URLS.search_movie
                            .replace('<search>', $scope.search_imdb)
                            .replace('<page>', $scope.page))
                        .success(function (res){
                            var results = {};
                            for (var r in res.results)
                                results[res.results[r].id] = res.results[r];
                            res.results = results;
                            $scope.imdb_res = res;
                        }).error(function (res){
                            console.log(res);
                        });
                    } else {
                        $scope.imdb_res = [];
                    }
            }, DELAY_SEARCH);
        });
    }
]);
