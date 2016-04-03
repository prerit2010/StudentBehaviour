(function(){
	var app = angular.module('demoapp', [ ]);


app.controller('DemoCtrl', ['$scope', function($scope){

	$scope.num = 0;

	$scope.save = function(){
		$(".data").html("click : " + $scope.num);
		$scope.num += 1;

	};

}]);
})();

// alert("lol");