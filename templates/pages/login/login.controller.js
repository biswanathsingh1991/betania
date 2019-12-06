(function () {
    'use strict';

    angular
        .module('app')
        .controller('LoginController', LoginController);

    LoginController.$inject = ['$location', 'AuthenticationService', 'FlashService'];
    function LoginController($location, AuthenticationService, FlashService) {
        var vm = this;

        localStorage.users =null;

        localStorage.users = `[{"firstName":"admin","lastName":"admin","username":"admin","password":"password","id":1}]`;


        vm.login = login;

        (function initController() {
            // reset login status
            AuthenticationService.ClearCredentials();
        })();

        function login() {
            vm.dataLoading = true;
            AuthenticationService.Login(vm.username, vm.password, function (response) {
                if (response.success) {
                    AuthenticationService.SetCredentials(vm.username, vm.password);
                    $location.path('/');
                } else {
                    FlashService.Toaster(response.message,'error','Invalid Credentials')
                    // FlashService.Error(response.message);
                    vm.dataLoading = false;
                }
            });
        };
    }

})();
