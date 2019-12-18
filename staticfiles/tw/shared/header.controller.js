(function () {
    'use strict';

    angular
        .module('app')
        .controller('headerController', headerController);

        headerController.$inject = ['$location', 'AuthenticationService', 'FlashService','$scope'];
    function headerController($location, AuthenticationService, FlashService,$scope) {
        $scope.logout = function () {
            localStorage.removeItem('tw_auth_details');
            window.location = '/login.html'
       }
    }
})();
