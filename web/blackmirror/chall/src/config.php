<?php

error_reporting(false); 
function dbconnect() {
    $db = mysqli_connect(
        "db",
        "root",
        getenv("MYSQL_ROOT_PASSWORD"),
        getenv("MYSQL_DATABASE")
    );
    if (!$db) {
        die("Database Connection failed!");
    }
    return $db;
}