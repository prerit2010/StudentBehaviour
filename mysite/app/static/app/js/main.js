(function(){
	var app = angular.module('app', [ ]);

app.controller('DemoCtrl', function ($scope, $http){
	$scope.selectedOption = null;

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

	$scope.itemSelected = function(student_id, points){
		var req = {
		 method: 'POST',
		 url: '/api/points/',
		 headers: {
		   'Content-Type': "application/json"
		 },
		 data: { "student_id" : student_id, "points_obtained" : points }
		}
		$http(req).then(function(response){});

		var req = {
		 method: 'POST',
		 url: '/api/attendance/',
		 headers: {
		   'Content-Type': "application/json"
		 },
		 data: { "student_id" : student_id }
		}
		$http(req).then(function(response){});
	};

});
})();