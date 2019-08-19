<?php

function getdb(){	
$servername = "localhost";
$username = "root";
$password = "";
$database = "sapster_hrms";

// Create connection
$conn = new mysqli($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
// "Connected successfully";
return $conn;
}
?>