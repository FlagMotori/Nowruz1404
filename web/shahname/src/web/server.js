#!/usr/bin/env node

const path = require("path");
const fs = require("fs");
const express = require("express");
const app = express();
const port = process.env.PORT || 1337;

app.set("view engine", "ejs");
app.use(express.json());

const PICTURES = JSON.parse(fs.readFileSync("pictures.json").toString());

app.get("/", async (req, res) => {
	let count = req.query.count || 1;
	res.render("index.ejs", {count})
})


app.get("/random", async (req, res) => {
	res.set("Content-type", "application/json");
	let picture = PICTURES[Math.floor(Math.random() * PICTURES.length)];
	res.send(JSON.stringify(picture));
})

app.listen(port, () => {
	console.log(`Server listenning on ::${port}`)
})
