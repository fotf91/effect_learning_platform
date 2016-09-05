// Define the `PersonalProfileController` controller on the `accountApp` module
accountApp.controller('PersonalProfileController', function PersonalProfileController($scope, $http) {
//    $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8';

    $scope.edit_flag = false;

    $scope.updateProfile = function(){
      $http.post("/account/profile/", $scope.profile)
        .success(function(data, status, headers, config) {
            $scope.data = data;
        }).error(function(data, status, headers, config) {
            $scope.status = status;
      });
    }// updateProfile()

    function editForm(){
      if($scope.edit_flag){
        $scope.edit_flag = false;
      }else{
        $scope.edit_flag = true;
      }
    }// editForm()

    $scope.editForm = function(){
      console.log('editForm');
      editForm();
    }// editForm()
});
