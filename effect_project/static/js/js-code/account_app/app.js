// Define the `accountApp` module
var accountApp = angular.module('accountApp', []);

accountApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('$');
    $interpolateProvider.endSymbol('$');
});
