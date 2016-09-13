// Define the `accountApp` module
var accountApp = angular.module('accountApp', [], function($httpProvider) {
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

accountApp.config(function($interpolateProvider) {
   $interpolateProvider.startSymbol('$');
   $interpolateProvider.endSymbol('$');
});

// Directive that is used in order to show as default value of <input> the value or the ng-model value
accountApp.directive('ngInitial', function() {
  return {
  restrict: 'A',
  controller: [
    '$scope', '$element', '$attrs', '$parse', function($scope, $element, $attrs, $parse) {
      var getter, setter, val;
      val = $attrs.ngInitial || $attrs.value;
      getter = $parse($attrs.ngModel);
      setter = getter.assign;
      setter($scope, val);
    }
  ]
  };
});
