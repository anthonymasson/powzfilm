var powzfilmApp = angular.module('powzfilmApp', [
    'ngRoute',
    'ngTouch',
    'ngCookies',
    'powzfilmControllers',
    'ngMaterial',
    'ngMdIcons'
]).directive('thumbailEffect', function() {
    return function(scope, element, attrs) {
        update_thumbnail_effect();
    };
});;

//'ui.bootstrap.tabs',

powzfilmApp.config(['$routeProvider',
    '$locationProvider',
    function($routeProvider) {
        $routeProvider.
            when('/home', {
                templateUrl: 'app/partials/home.html',
                controller: 'HomeCtrl'
            }).
            when('/film/add', {
                templateUrl: 'app/partials/add_film.html',
                controller: 'AddFilmCtrl'
            }).
            otherwise({
                redirectTo: '/home'
            });
    }]);
var powzfilmControllers = angular.module('powzfilmControllers', ['ngRoute', 'ngCookies']);
