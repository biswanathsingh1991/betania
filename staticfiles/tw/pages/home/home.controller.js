(function() {
  "use strict";

  angular.module("app").controller("HomeController", HomeController);

  HomeController.$inject = [
    "UserService",
    "$rootScope",
    "$scope",
    "ApiService"
  ];
  function HomeController(UserService, $rootScope, $scope, ApiService) {
    localStorage.users = `[{"firstName":"admin","lastName":"admin","username":"admin","password":"password","id":1}]`;

    $scope.isLoad = 1;
    initController();

    function initController() {
      if ($scope.isLoad == 1) {
        $scope.isLoad = 0;
        loadAllSku();
      }
    }

    function loadAllSku() {
      ApiService.GetAllSku().then(function (sukdata) { 
        console.log(sukdata)
        $scope.SkuList = sukdata;
        $scope.selectsku = $scope.SkuList[0].uid;
        $scope.selectskupie = $scope.SkuList[0].uid;
        loadChartData($scope.selectsku);
        loadPieChart($scope.selectskupie);
      });
    }

    $scope.labels = new Array();
    $scope.series = new Array();
    $scope.data = new Array();
    $scope.ul = 0;
    $scope.ll = 0;



    
    function loadChartData(sukid) {
      ApiService.GetAll(sukid).then(function(sukdata) {
        console.log(sukdata);

        $scope.location = sukdata.Location;
        $scope.plant_name = sukdata.plant_name;
        let ul = new Array();
        let ll = new Array();
        let bw = new Array();
        $scope.series = ["Upper Limit", "SUK", "Lower Limit"];
        $scope.data.length = 0;
        $scope.labels.length = 0;

        angular.forEach($scope.SkuList, function(value, key) {
          if (value.uid == $scope.selectsku) {
            $scope.ul = value.ul;
            $scope.ll = value.ll;
          }
        });

        angular.forEach(sukdata.data, function(value, key) {
          ul.push($scope.ul);
          bw.push(value.box_weight);
          ll.push($scope.ll);
          $scope.labels.push(
            moment(new Date(value.timestamp_created)).format(
              "MM/DD/YYYY hh:mm A"
            )
          );
        });

        $scope.data.push(ul);
        $scope.data.push(bw);
        $scope.data.push(ll);
        // console.log($scope.data)
      });
    }

    $scope.changeSku = sukid => {
      loadChartData(sukid);
    };

    $scope.onClick = function(points, evt) {
      console.log(points, evt);
    };

    $scope.datasetOverride = [{ yAxisID: "y-axis-1" }];
    $scope.options = {
      responsive: true,
      maintainAspectRatio: true,
      legend: {
        display: false,
        labels: {
          fontColor: "rgb(255, 99, 132)"
        }
      },
      scales: {
        yAxes: [
          {
            type: "linear",
            display: true,
            position: "left",
            id: "y-axis-1",
            gridLines: {
              display: false
            },
            labels: {
              show: true
            },
            ticks: {
              max: 350,
              min: 100,
              stepSize: 50
            }
          }
        ]
      }
    };

    $scope.width = "";
    $scope.height = "100";
    if (
      /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
        navigator.userAgent
      )
    ) {
      $scope.width = "100";
      $scope.height = "100";
    }

    $scope.changeSkuPie = sukid => {
       loadPieChart(sukid);
    }
 $scope.pieoptions = {
        responsive: true,
        barValueSpacing: 2,
        legend: {
          display: true,
          labels: {
            fontColor: "rgb(255, 99, 132)"
          }
        }
      };
    function loadPieChart(sukid) {
      $scope.piedata = [];
      $scope.pielabels = ["Ok", "Overweight", "Underweight", "Rejected"];
      angular.forEach($scope.SkuList, function(value, key) {
        if (value.uid == sukid) {
          $scope.piedata.push(value.total_msg_accept)
          $scope.piedata.push(value.ul)
            $scope.piedata.push(value.ll)
           $scope.piedata.push(value.total_msg_reject)
          }
        });
      
     
    }

    $scope.datatb = [
      [
        "Tiger Nixon",
        "System Architect",
        "Edinburgh",
        "5421",
        "2011/04/25",
        "$320,800"
      ],
      [
        "Garrett Winters",
        "Accountant",
        "Tokyo",
        "8422",
        "2011/07/25",
        "$170,750"
      ],
      [
        "Ashton Cox",
        "Junior Technical Author",
        "San Francisco",
        "1562",
        "2009/01/12",
        "$86,000"
      ],
      [
        "Cedric Kelly",
        "Senior Javascript Developer",
        "Edinburgh",
        "6224",
        "2012/03/29",
        "$433,060"
      ],
      ["Airi Satou", "Accountant", "Tokyo", "5407", "2008/11/28", "$162,700"],
      [
        "Brielle Williamson",
        "Integration Specialist",
        "New York",
        "4804",
        "2012/12/02",
        "$372,000"
      ],
      [
        "Herrod Chandler",
        "Sales Assistant",
        "San Francisco",
        "9608",
        "2012/08/06",
        "$137,500"
      ],
      [
        "Rhona Davidson",
        "Integration Specialist",
        "Tokyo",
        "6200",
        "2010/10/14",
        "$327,900"
      ],
      [
        "Colleen Hurst",
        "Javascript Developer",
        "San Francisco",
        "2360",
        "2009/09/15",
        "$205,500"
      ],
      [
        "Sonya Frost",
        "Software Engineer",
        "Edinburgh",
        "1667",
        "2008/12/13",
        "$103,600"
      ]
    ];

    $scope.dataTableOpt = {
      //custom datatable options
      // or load data through ajax call also
      aLengthMenu: [
        [10, 50, 100, -1],
        [10, 50, 100, "All"]
      ]
    };

    $(".datatables-demo").dataTable();
  }
})();
