(function(){
	var app = angular.module('app', [ ]);


app.controller('DemoCtrl', function ($scope, $http){

	$scope.loadstudents = function(){
		$http.get('/api/students/').then(function(response){
			$scope.resp = response.data;
			$scope.students = $scope.resp.objects;
			
		});

	};
	$scope.loadstudents();

	$scope.selected_item = "Mark Behaviour";

	$scope.loadbehaviour = function(){
		$http.get('/api/behaviour/').then(function(response){
			$scope.resp = response.data;
			$scope.behaviours = $scope.resp.objects;
			
		});

	};
	$scope.loadbehaviour();

	$scope.itemSelected = function(item){
		$scope.selected_item = item;

	};

});
})();

// alert("lol");