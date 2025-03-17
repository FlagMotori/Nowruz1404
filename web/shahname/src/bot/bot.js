#!/usr/bin/env node

const express = require("express")
const bodyParser = require('body-parser')
const { visit } = require("./visit");

const app = express()
app.use(bodyParser.urlencoded({ extended: true }));

const PORT = process.env.PORT || 1336
const URL_REGEX = /^https?:\/\//

app.get("/", (_, res) => {
    return res.sendFile(__dirname + "/index.html")
})


app.post("/visit", async (req, res) => {
    res.setHeader("Content-type", "text/plain")
    let url = req.body.url
    if (!url || typeof url != "string" || !URL_REGEX.test(url)) {
        return res.send("Bad URL!")
    }

    res.send("Admin will visit your url")
    await visit(url)
})

app.listen(PORT, () => {
    console.log(`Bot listening at ::${PORT}`)
})
