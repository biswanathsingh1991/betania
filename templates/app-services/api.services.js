
(function () {
    'use strict';

    angular
        .module('app')
        .factory('ApiService', ApiService);

        ApiService.$inject = ['$http'];
    function ApiService($http) {
        var service = {};

        service.GetAll = GetAll;
      
        return service;

        function GetAll() {
            return $http.get('http://15.206.55.22:8000/getData/6/').then(handleSuccess, handleError('Error getting all users'));
        }








      








          // private functions

        function handleSuccess(res) {
            return res.data;
        }

        function handleError(error) {
            return function () {
                return { success: false, message: error };
            };
        }
    }

})();
