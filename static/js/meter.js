var x_air_temperature = new JustGage({
  id: "x_air_temperature",
  value : x_air_temperature,
  min: 0,
  max: 100,
  label: "เซลเซียส (C)",
  gaugeWidthScale: 0.6,
  customSectors: {
    percents: true,
    ranges: [{
      color : "#43bf58",
      lo : 0,
      hi : 50
    },{
      color : "#ff3b30",
      lo : 51,
      hi : 100
    }]
  },
  counter: true
});
    
var x_air_humidity = new JustGage({
  id: "x_air_humidity",
  value : x_air_humidity,
  min: 0,
  max: 100,
  label: "เปอร์เซ็น (%)",
  gaugeWidthScale: 0.6,
  customSectors: {
    percents: true,
    ranges: [{
      color : "#43bf58",
      lo : 0,
      hi : 50
    },{
      color : "#ff3b30",
      lo : 51,
      hi : 100
    }]
  },
  counter: true
});
    
var x_soil_moisure = new JustGage({
  id: "x_soil_moisure",
  value : x_soil_moisure,
  min: 0,
  max: 100,
  label: "เปอร์เซ็น (%)",
  gaugeWidthScale: 0.6,
  customSectors: {
    percents: true,
    ranges: [{
      color : "#43bf58",
      lo : 0,
      hi : 50
    },{
      color : "#ff3b30",
      lo : 51,
      hi : 100
    }]
  },
  counter: true
});

var x_soil_temperature= new JustGage({
  id: "x_soil_temperature",
  value : x_soil_temperature,
  min: 0,
  max: 100,
  label: "เซลเซียส (C)",
  gaugeWidthScale: 0.6,
  customSectors: {
    percents: true,
    ranges: [{
      color : "#43bf58",
      lo : 0,
      hi : 50
    },{
      color : "#ff3b30",
      lo : 51,
      hi : 100
    }]
  },
  counter: true
});

// Node A
var a_air_temperature = new JustGage({
  id: "a_air_temperature",
  value : a_air_temperature,
  min: 0,
  max: 100,
  label: "เซลเซียส (C)",
  gaugeWidthScale: 0.6,
  customSectors: {
    percents: true,
    ranges: [{
      color : "#43bf58",
      lo : 0,
      hi : 50
    },{
      color : "#ff3b30",
      lo : 51,
      hi : 100
    }]
  },
  counter: true
});
    
var a_air_humidity = new JustGage({
  id: "a_air_humidity",
  value : a_air_humidity,
  min: 0,
  max: 100,
  label: "เปอร์เซ็น (%)",
  gaugeWidthScale: 0.6,
  customSectors: {
    percents: true,
    ranges: [{
      color : "#43bf58",
      lo : 0,
      hi : 50
    },{
      color : "#ff3b30",
      lo : 51,
      hi : 100
    }]
  },
  counter: true
});
    
var a_soil_moisure = new JustGage({
  id: "a_soil_moisure",
  value : a_soil_moisure,
  min: 0,
  max: 100,
  label: "เปอร์เซ็น (%)",
  gaugeWidthScale: 0.6,
  customSectors: {
    percents: true,
    ranges: [{
      color : "#43bf58",
      lo : 0,
      hi : 50
    },{
      color : "#ff3b30",
      lo : 51,
      hi : 100
    }]
  },
  counter: true
});

var a_soil_temperature= new JustGage({
  id: "a_soil_temperature",
  value : a_soil_temperature,
  min: 0,
  max: 100,
  label: "เซลเซียส (C)",
  gaugeWidthScale: 0.6,
  customSectors: {
    percents: true,
    ranges: [{
      color : "#43bf58",
      lo : 0,
      hi : 50
    },{
      color : "#ff3b30",
      lo : 51,
      hi : 100
    }]
  },
  counter: true
});

// Node B
var b_air_temperature = new JustGage({
  id: "b_air_temperature",
  value : b_air_temperature,
  min: 0,
  max: 100,
  label: "เซลเซียส (C)",
  gaugeWidthScale: 0.6,
  customSectors: {
    percents: true,
    ranges: [{
      color : "#43bf58",
      lo : 0,
      hi : 50
    },{
      color : "#ff3b30",
      lo : 51,
      hi : 100
    }]
  },
  counter: true
});
    
var b_air_humidity = new JustGage({
  id: "b_air_humidity",
  value : b_air_humidity,
  min: 0,
  max: 100,
  label: "เปอร์เซ็น (%)",
  gaugeWidthScale: 0.6,
  customSectors: {
    percents: true,
    ranges: [{
      color : "#43bf58",
      lo : 0,
      hi : 50
    },{
      color : "#ff3b30",
      lo : 51,
      hi : 100
    }]
  },
  counter: true
});
    
var b_soil_moisure = new JustGage({
  id: "b_soil_moisure",
  value : b_soil_moisure,
  min: 0,
  max: 100,
  label: "เปอร์เซ็น (%)",
  gaugeWidthScale: 0.6,
  customSectors: {
    percents: true,
    ranges: [{
      color : "#43bf58",
      lo : 0,
      hi : 50
    },{
      color : "#ff3b30",
      lo : 51,
      hi : 100
    }]
  },
  counter: true
});

var b_soil_temperature= new JustGage({
  id: "b_soil_temperature",
  value : b_soil_temperature,
  min: 0,
  max: 100,
  label: "เซลเซียส (C)",
  gaugeWidthScale: 0.6,
  customSectors: {
    percents: true,
    ranges: [{
      color : "#43bf58",
      lo : 0,
      hi : 50
    },{
      color : "#ff3b30",
      lo : 51,
      hi : 100
    }]
  },
  counter: true
});

// Node C
var c_air_temperature = new JustGage({
  id: "c_air_temperature",
  value : c_air_temperature,
  min: 0,
  max: 100,
  label: "เซลเซียส (C)",
  gaugeWidthScale: 0.6,
  customSectors: {
    percents: true,
    ranges: [{
      color : "#43bf58",
      lo : 0,
      hi : 50
    },{
      color : "#ff3b30",
      lo : 51,
      hi : 100
    }]
  },
  counter: true
});
    
var c_air_humidity = new JustGage({
  id: "c_air_humidity",
  value : c_air_humidity,
  min: 0,
  max: 100,
  label: "เปอร์เซ็น (%)",
  gaugeWidthScale: 0.6,
  customSectors: {
    percents: true,
    ranges: [{
      color : "#43bf58",
      lo : 0,
      hi : 50
    },{
      color : "#ff3b30",
      lo : 51,
      hi : 100
    }]
  },
  counter: true
});
    
var c_soil_moisure = new JustGage({
  id: "c_soil_moisure",
  value : c_soil_moisure,
  min: 0,
  max: 100,
  label: "เปอร์เซ็น (%)",
  gaugeWidthScale: 0.6,
  customSectors: {
    percents: true,
    ranges: [{
      color : "#43bf58",
      lo : 0,
      hi : 50
    },{
      color : "#ff3b30",
      lo : 51,
      hi : 100
    }]
  },
  counter: true
});

var c_soil_temperature= new JustGage({
  id: "c_soil_temperature",
  value : c_soil_temperature,
  min: 0,
  max: 100,
  label: "เซลเซียส (C)",
  gaugeWidthScale: 0.6,
  customSectors: {
    percents: true,
    ranges: [{
      color : "#43bf58",
      lo : 0,
      hi : 50
    },{
      color : "#ff3b30",
      lo : 51,
      hi : 100
    }]
  },
  counter: true
});

var refX = database.ref("X");
refX.orderByChild("time").limitToLast(1).on("child_added", function(snapshot) {
	var changedData = snapshot.val();
	var air_temperature = changedData.data.air_temperature;
	var air_humidity = changedData.data.air_humidity;
	var soil_moisure = changedData.data.soil_moisure;
	var soil_temperature = changedData.data.soil_temperature;
  x_air_temperature.refresh(air_temperature);
  x_air_humidity.refresh(air_humidity);
  x_soil_moisure.refresh(soil_moisure);
  x_soil_temperature.refresh(soil_temperature);
});

var refA = database.ref("A");
refA.orderByChild("time").limitToLast(1).on("child_added", function(snapshot) {
	var changedData = snapshot.val();
	var air_temperature = changedData.data.air_temperature;
	var air_humidity = changedData.data.air_humidity;
	var soil_moisure = changedData.data.soil_moisure;
	var soil_temperature = changedData.data.soil_temperature;
  a_air_temperature.refresh(air_temperature);
  a_air_humidity.refresh(air_humidity);
  a_soil_moisure.refresh(soil_moisure);
  a_soil_temperature.refresh(soil_temperature);
});

var refB = database.ref("B");
refB.orderByChild("time").limitToLast(1).on("child_added", function(snapshot) {
	var changedData = snapshot.val();
	var air_temperature = changedData.data.air_temperature;
	var air_humidity = changedData.data.air_humidity;
	var soil_moisure = changedData.data.soil_moisure;
	var soil_temperature = changedData.data.soil_temperature;
  b_air_temperature.refresh(air_temperature);
  b_air_humidity.refresh(air_humidity);
  b_soil_moisure.refresh(soil_moisure);
  b_soil_temperature.refresh(soil_temperature);
});

var refC = database.ref("C");
refC.orderByChild("time").limitToLast(1).on("child_added", function(snapshot) {
	var changedData = snapshot.val();
	var air_temperature = changedData.data.air_temperature;
	var air_humidity = changedData.data.air_humidity;
	var soil_moisure = changedData.data.soil_moisure;
	var soil_temperature = changedData.data.soil_temperature;
  c_air_temperature.refresh(air_temperature);
  c_air_humidity.refresh(air_humidity);
  c_soil_moisure.refresh(soil_moisure);
  c_soil_temperature.refresh(soil_temperature);
});