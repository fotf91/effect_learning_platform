// Define the `PersonalProfileController` controller on the `accountApp` module
accountApp.controller('IndexController', function IndexController($scope) {
    $scope.test = 'test text';

    $scope.updateProfileGType = function(){
        alert('ok');
    }
});