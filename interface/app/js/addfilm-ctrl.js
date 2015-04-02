////------------[Controllers]
function Movie(id_imdb, i_movie) {
    if (angular.isDefined(i_movie)) {
        this.title = i_movie.title;
        this.poster_path = i_movie.poster_path;
        this.genres = i_movie.genres;
        this.synopsis = i_movie.overview;
        this.spoken_languages = [];
        for (var l in i_movie.spoken_languages)
            this.spoken_languages[this.spoken_languages.length] = i_movie.spoken_languages[l];
        this.imdb_id = id_imdb;
        this.release_date = new Date(i_movie.release_date);
    }
}

powzfilmControllers.controller('AddFilmCtrl', ['$scope', '$location', '$routeParams', '$http', '$timeout', '$log', '$q',
    function ($scope, $location, $routeParams, $http, $timeout, $log, $q) {
        //IMDB search control
        var self = this;
        $scope.page = 1;
        self.selectedItem = null;
        self.searchText = null;
        self.querySearch = querySearch;
        function querySearch(query) {
            var results = query ? [] : deferred;
            deferred = $q.defer();
            $http.get(API_URLS.search_movie
                    .replace('<search>', query).replace('<page>', $scope.page))
                    .success(function (res) {
                        for (var r in res.results) {
                            res.results[r].release_date = new Date(res.results[r].release_date);
                            results.push(res.results[r]);
                        }
                        deferred.resolve(results);
                        return deferred.promise;
                    });
            return results;
        };
        self.selectedItemChange = function(item) {
            if (angular.isDefined(item))
                $http.get(API_URLS.detail_movie.replace('<id_movie>', item.id)).success(function (res) {
                    $scope.new_movie = new Movie(item.id, res);
                });
            else
                $scope.new_movie = undefined;
        };
        
        // Genre control
        $scope.genreAdd = undefined;
        $scope.addGenre = function (){
            var gId = parseInt($scope.genreAdd);
            for (var g in $scope.genres)
                if ($scope.genres[g].id === gId){
                    $scope.new_movie.genres.push($scope.genres[g]);
                    break;
                }
            $scope.genreAdd = undefined;
        };
        $scope.removeGenre = function (genre) {
            if (angular.isDefined($scope.new_movie))
                for (var g in $scope.new_movie.genres)
                    if ($scope.new_movie.genres[g].id === genre.id)
                        return $scope.new_movie.genres.splice(g, 1);
        };
        $scope.genreNoExist = function (genre) {
            if (angular.isDefined($scope.new_movie))
                for (var g in $scope.new_movie.genres)
                    if ($scope.new_movie.genres[g].id === genre.id)
                        return false;
            return true;
        };
        $http.get(API_URLS.genres).success(function (res) {$scope.genres = res['genres'];});
    }
]);
