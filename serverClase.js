var express = require('express');
var server = express();
var bodyParser = require('body-parser');
var sqlite3 = require('sqlite3');
var db = new sqlite3.Database('Sensors.db');


var urlencoded = bodyParser.urlencoded({extended: false});

server.get('/index.html', function(request, response){
	response.sendFile(__dirname + "/" + "index.html");
});

server.get('/miGet', function(request, response){
	//response.send("Hola");
	db.all('SELECT * FROM Locations', function(error, rows){
		response.send(rows);
	});
});

server.post('/miPost', urlencoded ,function(request, response){
	data = {
		"locationName": request.body.locationName
	};	
	data_db = [request.body.locationName];
	
	db.run('INSERT INTO Locations(LocationName) VALUES (?)', data_db, function(error, status){
			console.log("Data inserted into table");	
	});	
	console.log(data);
	response.send(JSON.stringify(data));
});

server.listen(5000, function(){
	console.log("Server running");
});