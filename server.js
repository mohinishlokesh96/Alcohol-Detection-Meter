//var http = require('http');
var express = require('express')
var bodyParser = require('body-parser');
var multer = require('multer')
var upload = multer();
var app = express();
var fs = require('fs');


app.use(bodyParser.json()); // for parsing application/json
app.use(bodyParser.urlencoded({ extended: true })); // for parsing application/x-www-form-urlencoded
app.use(upload.array()); // for parsing multipart/form-data
app.use(express.static('public'));

app.post('/', function(req, res){
    console.log(req.body);
    res.send("recieved your request!");
});

app.get("/:var1",function(req,res){
	var var1 = req.params.var1;
	console.log(var1);
	res.send("request recieved");
});

app.all("*",function(req,res){
	console.log("got a request");
	console.log(req.body);
	res.send("Some request");
});

app.listen(8080);
console.log("Server running at http://127.0.0.1:8080.");



