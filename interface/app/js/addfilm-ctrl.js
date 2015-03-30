////------------[Controllers]
powzfilmControllers.controller('AddFilmCtrl', ['$scope', '$location', '$routeParams', '$http', '$timeout',
    function ($scope, $location, $routeParams, $http, $timeout) {
        var nb_elem_row = 4;
        $scope.selected_imdb = false;
        $scope.search_imdb = "harry";
        $scope.imdb_res = [];
        
        $scope.select_imdb = function(id){
            $scope.selected_imdb = id;
        };
        
        $scope.change_selected_imdb = function(){
            $scope.selected_imdb = false;
        };
        
        var filterTextTimeout;
        $scope.$watch('search_imdb', function (val) {
            if (filterTextTimeout) $timeout.cancel(filterTextTimeout);
            filterTextTimeout = $timeout(function() {
                $scope.page = 1;
                if ($scope.search_imdb.length > LIMIT_LENGTH_SEARCH){
                    $scope.selected_imdb = null;
                    $http.get(API_URLS.search_movie.replace('<search>', $scope.search_imdb).replace('<page>', $scope.page))
                        .success(function (res){
                            var results = {};
                            for (var r in res.results)
                                results[res.results[r].id] = res.results[r];
                            res.results = results;
                            $scope.imdb_res = res;
                        }).error(function (res){
                            $scope.imdb_res = res;
                        });
                    } else {
                        $scope.imdb_res = [];
                    }
            }, DELAY_SEARCH);
        });
    }
]);
