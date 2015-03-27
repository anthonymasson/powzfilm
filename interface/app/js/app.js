var powzfilmApp = angular.module('powzfilmApp', [
    'ngRoute',
    'ngTouch',
    'ngCookies',
    'powzfilmControllers'
]);

//'ui.bootstrap.tabs',

powzfilmApp.config(['$routeProvider',
    '$locationProvider',
    function($routeProvider) {
        $routeProvider.
            when('/home', {
                templateUrl: 'app/partials/home.html',
                controller: 'HomeCtrl'
            }).
            otherwise({
                redirectTo: '/home'
            });
    }]);

var powzfilmControllers = angular.module('powzfilmControllers', ['ngRoute', 'ngCookies']);