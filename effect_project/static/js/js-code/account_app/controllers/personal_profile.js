// Define the `PersonalProfileController` controller on the `accountApp` module
accountApp.controller('PersonalProfileController', function PersonalProfileController($scope, $http) {
	//    $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8';

	$scope.edit_avatar_flag = false; // true: avatar is being edite, false: avatar is not being edited
	$scope.edit_main_flag = false; // true: data are being edited, false: data are not edited
	$scope.django_data_flag = true; // true: show django data, false: show ng-model variables
	$scope.profile = {}; // empty form object
	$scope.filter_edu = true; // true: show education elements
	$scope.filter_exp = true; // true: show experience elements


	$scope.updateProfile = function(){
		$http.post("/account/profile/", JSON.stringify($scope.profile))
		.success(function(data, status, headers, config) {
			$scope.data = data;
			console.log($scope.profile.last_name);
			$scope.django_data_flag = false;
			editForm();
		}).error(function(data, status, headers, config) {
			$scope.status = status;
		});
	}// updateProfile()

	function editForm(){
		if($scope.edit_main_flag){
			$scope.edit_main_flag = false;
		}else{
			$scope.edit_main_flag = true;
		}
	}// editForm()

	$scope.editForm = function(){
		editForm();
	}// editForm()

	function editAvatar(){
		if($scope.edit_avatar_flag){
			$scope.edit_avatar_flag = false;
		}else{
			$scope.edit_avatar_flag = true;
		}
	}// editAvatar()

	$scope.editAvatar = function(){
		editAvatar();
	}// editAvatar()

	$scope.filterEdu = function(){
	    $scope.filter_exp = true;
	    $scope.filter_edu = false;
	}// filterEdu()

    $scope.filterExp = function(){
        $scope.filter_edu = true;
	    $scope.filter_exp = false;
	}// filterExp()

	$scope.filterAll = function(){
	    $scope.filter_edu =
	    $scope.filter_exp = true;
	}
});
