const puppeteer = require('puppeteer')

const FLAG = process.env.FLAG || "FMCTF{FAKE_FLAG}"
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms))

async function visit(url, friend_hook) {
    try {
        let browser = await puppeteer.launch({
            pipe: true,
            args: [
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--js-flags=--noexpose_wasm,--jitless",
                "--ignore-certificate-errors",
            ],
            executablePath: "/usr/bin/google-chrome",
            headless: 'new'
        })
        let page = await browser.newPage()
        await page.goto(url, {timeout: 2000, waitUntil: "domcontentloaded"})
        await sleep(3000)
    } catch (e) {
        console.log(e)
    }
    try {await browser.close()} catch (e) {}
}

module.exports = { visit }
