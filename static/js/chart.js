var config_firebase = {
    apiKey: "AIzaSyDHEPLFgaTRQyxWifIhl3qQPcALMIrgfqM",
    authDomain: "smart-farm-27e2b.firebaseapp.com",
    databaseURL: "https://smart-farm-27e2b.firebaseio.com",
    projectId: "smart-farm-27e2b",
    storageBucket: "smart-farm-27e2b.appspot.com",
    messagingSenderId: "788362802638"
  };

firebase.initializeApp(config_firebase);
var status = 0;
var database = firebase.database();
var chartColors = {
	red: 'rgb(255, 99, 132)',
	orange: 'rgb(255, 159, 64)',
	yellow: 'rgb(255, 205, 86)',
	green: 'rgb(75, 192, 192)',
	blue: 'rgb(54, 162, 235)',
	purple: 'rgb(153, 102, 255)',
	grey: 'rgb(201, 203, 207)'
};

var color1 = Chart.helpers.color;
var config1 = {
	type: 'line',
	data: {
		datasets: [{
			label: 'โหนดX',
			backgroundColor: color1(chartColors.red).alpha(0.5).rgbString(),
			borderColor: chartColors.red,
			fill: true,
			cubicInterpolationMode: 'monotone',
			data: []
        }
        , {
			label: 'โหนดA',
			backgroundColor: color1(chartColors.blue).alpha(0.5).rgbString(),
			borderColor: chartColors.blue,
			fill: true,
			cubicInterpolationMode: 'monotone',
			data: []
        },
        {
			label: 'โหนดB',
			backgroundColor: color1(chartColors.green).alpha(0.5).rgbString(),
			borderColor: chartColors.green,
			fill: true,
			cubicInterpolationMode: 'monotone',
			data: []
        },
        {
			label: 'โหนดC',
			backgroundColor: color1(chartColors.purple).alpha(0.5).rgbString(),
			borderColor: chartColors.purple,
			fill: true,
			cubicInterpolationMode: 'monotone',
			data: []
        }
    ]
	},
	options: {
		elements: {
      point:{
      	radius: 0
      }
    },
		responsive: true,
		maintainAspectRatio: true,
		title: {
			display: true,
			text: 'อุณหภูมิของอากาศ'
		},
		scales: {
			xAxes: [{
				type: 'realtime',
				realtime: {
					duration: 6*60*60000,
					ttl: 6*67*60000,
					refresh: 1500,
					delay: 0,
					pause: false,
				}
			}],
			yAxes: [{
				type: 'linear',
				display: true,
				scaleLabel: {
					display: true,
					labelString: 'องศาเซลเซียส (C)'
				},
				ticks: {
                	beginAtZero:true,
                }
			}]
		},
		 legend: {
            display: true,
            labels: {
                boxWidth:30, 
            }
           
        },
		tooltips: {
			mode: 'nearest',
			intersect: false
		},
		hover: {
			mode: 'nearest',
			intersect: true
		},
		plugins: {
			streaming: {
				frameRate: 60
			},
		},
	}
};

var color2 = Chart.helpers.color;
var config2 = {
	type: 'line',
	data: {
		datasets: [{
			label: 'โหนดX',
			backgroundColor: color2(chartColors.red).alpha(0.5).rgbString(),
			borderColor: chartColors.red,
			fill: true,
			cubicInterpolationMode: 'monotone',
			data: []
        }
        , {
			label: 'โหนดA',
			backgroundColor: color2(chartColors.blue).alpha(0.5).rgbString(),
			borderColor: chartColors.blue,
			fill: true,
			cubicInterpolationMode: 'monotone',
			data: []
        },
        {
			label: 'โหนดB',
			backgroundColor: color2(chartColors.green).alpha(0.5).rgbString(),
			borderColor: chartColors.green,
			fill: true,
			cubicInterpolationMode: 'monotone',
			data: []
        },
        {
			label: 'โหนดC',
			backgroundColor: color2(chartColors.purple).alpha(0.5).rgbString(),
			borderColor: chartColors.purple,
			fill: true,
			cubicInterpolationMode: 'monotone',
			data: []
        }
    ]
	},
	options: {
		elements: {
      point:{
      	radius: 0
      }
    },
		responsive: true,
		maintainAspectRatio: true,
		title: {
			display: true,
			text: 'ความชื้นของอากาศ'
		},
		scales: {
			xAxes: [{
				type: 'realtime',
				realtime: {
					duration: 6*60*60000,
					ttl: 6*67*60000,
					refresh: 1500,
					delay: 0,
					pause: false,
				}
			}],
			yAxes: [{
				type: 'linear',
				display: true,
				scaleLabel: {
					display: true,
					labelString: 'เปอร์เซ็น (%)'
				},
				ticks: {
                	beginAtZero:true,
                }
			}]
		},
		 legend: {
            display: true,
            labels: {
                boxWidth:30, 
            }
           
        },
		tooltips: {
			mode: 'nearest',
			intersect: false
		},
		hover: {
			mode: 'nearest',
			intersect: true
		},
		plugins: {
			streaming: {
				frameRate: 60
			},
		},
	}
};

var color3 = Chart.helpers.color;
var config3 = {
	type: 'line',
	data: {
		datasets: [{
			label: 'โหนดX',
			backgroundColor: color3(chartColors.red).alpha(0.5).rgbString(),
			borderColor: chartColors.red,
			fill: true,
			cubicInterpolationMode: 'monotone',
			data: []
        }
        , {
			label: 'โหนดA',
			backgroundColor: color3(chartColors.blue).alpha(0.5).rgbString(),
			borderColor: chartColors.blue,
			fill: true,
			cubicInterpolationMode: 'monotone',
			data: []
        },
        {
			label: 'โหนดB',
			backgroundColor: color3(chartColors.green).alpha(0.5).rgbString(),
			borderColor: chartColors.green,
			fill: true,
			cubicInterpolationMode: 'monotone',
			data: []
        },
        {
			label: 'โหนดC',
			backgroundColor: color3(chartColors.purple).alpha(0.5).rgbString(),
			borderColor: chartColors.purple,
			fill: true,
			cubicInterpolationMode: 'monotone',
			data: []
        }
    ]
	},
	options: {
		elements: {
      point:{
      	radius: 0
      }
    },
		responsive: true,
		maintainAspectRatio: true,
		title: {
			display: true,
			text: 'อุณหภูมิในดิน'
		},
		scales: {
			xAxes: [{
				type: 'realtime',
				realtime: {
					duration: 6*60*60000,
					ttl: 6*67*60000,
					refresh: 1500,
					delay: 0,
					pause: false,
				}
			}],
			yAxes: [{
				type: 'linear',
				display: true,
				scaleLabel: {
					display: true,
					labelString: 'องศาเซลเซียส (C)'
				},
				ticks: {
                	beginAtZero:true,
                }
			}]
		},
		 legend: {
            display: true,
            labels: {
                boxWidth:30, 
            }
           
        },
		tooltips: {
			mode: 'nearest',
			intersect: false
		},
		hover: {
			mode: 'nearest',
			intersect: true
		},
		plugins: {
			streaming: {
				frameRate: 60
			},
		},
	}
};

var color4 = Chart.helpers.color;
var config4 = {
	type: 'line',
	data: {
		datasets: [{
			label: 'โหนดX',
			backgroundColor: color4(chartColors.red).alpha(0.5).rgbString(),
			borderColor: chartColors.red,
			fill: true,
			cubicInterpolationMode: 'monotone',
			data: []
        }
        , {
			label: 'โหนดA',
			backgroundColor: color4(chartColors.blue).alpha(0.5).rgbString(),
			borderColor: chartColors.blue,
			fill: true,
			cubicInterpolationMode: 'monotone',
			data: []
        },
        {
			label: 'โหนดB',
			backgroundColor: color4(chartColors.green).alpha(0.5).rgbString(),
			borderColor: chartColors.green,
			fill: true,
			cubicInterpolationMode: 'monotone',
			data: []
        },
        {
			label: 'โหนดC',
			backgroundColor: color4(chartColors.purple).alpha(0.5).rgbString(),
			borderColor: chartColors.purple,
			fill: true,
			cubicInterpolationMode: 'monotone',
			data: []
        }
    ]
	},
	options: {
		elements: {
      point:{
      	radius: 0
      }
    },
		responsive: true,
		maintainAspectRatio: true,
		title: {
			display: true,
			text: 'ความชื้นในดิน'
		},
		scales: {
			xAxes: [{
				type: 'realtime',
				realtime: {
					duration: 6*60*60000,
					ttl: 6*67*60000,
					refresh: 1500,
					delay: 0,
					pause: false,
				}
			}],
			yAxes: [{
				type: 'linear',
				display: true,
				scaleLabel: {
					display: true,
					labelString: 'เปอร์เซ็น (%)'
				},
				ticks: {
                	beginAtZero:true,
                }
			}]
		},
		 legend: {
            display: true,
            labels: {
                boxWidth:30, 
            }
           
        },
		tooltips: {
			mode: 'nearest',
			intersect: false
		},
		hover: {
			mode: 'nearest',
			intersect: true
		},
		plugins: {
			streaming: {
				frameRate: 60
			},
		},
	}
};

var x = window.matchMedia("(max-width: 767px)");
var ctx = document.getElementById('airtempChart').getContext('2d');
var ctx2 = document.getElementById('airhumidChart').getContext('2d');
var ctx3 = document.getElementById('soiltempChart').getContext('2d');
var ctx4 = document.getElementById('soilhumidChart').getContext('2d');
if (!x.matches) {
  ctx.canvas.height = 130;
  ctx2.canvas.height = 130;
  ctx3.canvas.height = 130;
  ctx4.canvas.height = 130;
}else{
  ctx.canvas.height = 300;
  ctx2.canvas.height = 300;
  ctx3.canvas.height = 300;
  ctx4.canvas.height = 300;
}
window.myChart1 = new Chart(ctx, config1);
window.myChart2 = new Chart(ctx2, config2);
window.myChart3 = new Chart(ctx3, config3);
window.myChart4 = new Chart(ctx4, config4);
  	
function create_graph(state,node,air_temperature, air_humidity, soil_moisure, soil_temperature){
		if(state == "py"){
		  
    		myChart1.data.datasets[node].data = air_temperature;
    		myChart2.data.datasets[node].data = air_humidity;
    		myChart3.data.datasets[node].data = soil_temperature;
    		myChart4.data.datasets[node].data = soil_moisure;   
		}else{
			myChart1.data.datasets[node].data.push(air_temperature);
			myChart2.data.datasets[node].data.push(air_humidity);
			myChart3.data.datasets[node].data.push(soil_temperature);
			myChart4.data.datasets[node].data.push(soil_moisure);
		}
  
  	myChart1.update({
		preservation: true
  	});
    myChart2.update({
      preservation: true
    });
    myChart3.update({
      preservation: true
    });
    myChart4.update({
      preservation: true
    });
}
var ref1 = database.ref("X");
ref1.orderByChild("time").limitToLast(1).on("child_added", function(snapshot) {
  	var changedData = snapshot.val();
  	var js_air_temperature = {
  		'x': changedData.time*1000,
  		'y': changedData.data.air_temperature
  	}
  	var js_air_humidity = {
  		'x': changedData.time*1000,
  		'y': changedData.data.air_humidity
  	}
  	var js_soil_moisure = {
  		'x': changedData.time*1000,
  		'y': changedData.data.soil_moisure
  	}
  	var js_soil_temperature = {
  		'x': changedData.time*1000,
  		'y': changedData.data.soil_temperature
  	}
  	create_graph("js",0, js_air_temperature, js_air_humidity, js_soil_moisure, js_soil_temperature)
})
var ref2 = database.ref("A");
ref2.orderByChild("time").limitToLast(1).on("child_added", function(snapshot) {
  	var changedData = snapshot.val();
  	var js_air_temperature = {
  		'x': changedData.time*1000,
  		'y': changedData.data.air_temperature
  	}
  	var js_air_humidity = {
  		'x': changedData.time*1000,
  		'y': changedData.data.air_humidity
  	}
  	var js_soil_moisure = {
  		'x': changedData.time*1000,
  		'y': changedData.data.soil_moisure
  	}
  	var js_soil_temperature = {
  		'x': changedData.time*1000,
  		'y': changedData.data.soil_temperature
  	}
  	create_graph("js",1, js_air_temperature, js_air_humidity, js_soil_moisure, js_soil_temperature)
})
var ref3 = database.ref("B");
ref3.orderByChild("time").limitToLast(1).on("child_added", function(snapshot) {
  	var changedData = snapshot.val();
  	var js_air_temperature = {
  		'x': changedData.time*1000,
  		'y': changedData.data.air_temperature
  	}
  	var js_air_humidity = {
  		'x': changedData.time*1000,
  		'y': changedData.data.air_humidity
  	}
  	var js_soil_moisure = {
  		'x': changedData.time*1000,
  		'y': changedData.data.soil_moisure
  	}
  	var js_soil_temperature = {
  		'x': changedData.time*1000,
  		'y': changedData.data.soil_temperature
  	}
  	create_graph("js",2, js_air_temperature, js_air_humidity, js_soil_moisure, js_soil_temperature)
})
var ref4 = database.ref("C");
ref4.orderByChild("time").limitToLast(1).on("child_added", function(snapshot) {
  	var changedData = snapshot.val();
  	var js_air_temperature = {
  		'x': changedData.time*1000,
  		'y': changedData.data.air_temperature
  	}
  	var js_air_humidity = {
  		'x': changedData.time*1000,
  		'y': changedData.data.air_humidity
  	}
  	var js_soil_moisure = {
  		'x': changedData.time*1000,
  		'y': changedData.data.soil_moisure
  	}
  	var js_soil_temperature = {
  		'x': changedData.time*1000,
  		'y': changedData.data.soil_temperature
  	}
  	create_graph("js",3, js_air_temperature, js_air_humidity, js_soil_moisure, js_soil_temperature)
})
window.onload = function() {
    //python send
    create_graph("py",0, x_air_temperature, x_air_humidity, x_soil_moisure, x_soil_temperature)
    create_graph("py",1, a_air_temperature, a_air_humidity, a_soil_moisure, a_soil_temperature)
    create_graph("py",2, b_air_temperature, b_air_humidity, b_soil_moisure, b_soil_temperature)
    create_graph("py",3, c_air_temperature, c_air_humidity, c_soil_moisure, c_soil_temperature)
}


