////------------[Controllers]
powzfilmControllers.controller('LeftCtrl', function ($scope, $timeout, $mdSidenav, $log, $location) {
    $scope.links = [
        {id: 1, title: "Add", link: "#/film/add"}
    ];
    $scope.close = function () {
        $mdSidenav('left').toggle()
                .then(function () {
                    $log.debug("close LEFT is done");
                });
    };
}).controller('RightCtrl', function ($scope, $timeout, $mdSidenav, $log) {
    $scope.links = [];
    $scope.close = function () {
        $mdSidenav('right').toggle()
                .then(function () {
                    $log.debug("close RIGHT is done");
                });
    };
}).controller('ToolbarCtrl', function ($scope, $timeout, $mdSidenav, $log) {
    $scope.toggleLeft = function () {
        $mdSidenav('left').toggle().then(function () {
            $log.debug("toggle left is done");
        });
    };
    $scope.toggleRight = function () {
        $mdSidenav('right').toggle().then(function () {
            $log.debug("toggle left is done");
        });
    };
});