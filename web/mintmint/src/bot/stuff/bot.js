#!/usr/bin/env node
const puppeteer = require('puppeteer')

const flag = process.env.FLAG || 'ASIS{test-flag}';
const webDomain = process.env.WEB_DOMAIN || 'localhost';

async function visit(url){
	let browser;

	if(!/^https?:\/\//.test(url)){
		return;
	}

	try{
		browser = await puppeteer.launch({
		    pipe: true,
		    args: [
		        "--no-sandbox",
		        "--disable-setuid-sandbox",
		        "--js-flags=--noexpose_wasm,--jitless",
		        "--ignore-certificate-errors",
		    ],
		    executablePath: "/usr/bin/google-chrome-stable",
		    headless: 'new'
		});

		let page = await browser.newPage();

		await page.setCookie({
			httpOnly: false,
			secure: false,
			name: 'flag',
			value: flag,
			domain: webDomain,
			sameSite: 'Lax'
		});

		page = await browser.newPage();
		await page.goto(url,{ waitUntil: 'domcontentloaded', timeout: 2000 });
		await new Promise(r=>setTimeout(r,3000));
	}catch(e){ console.log(e) }
	try{await browser.close();}catch(e){}
	process.exit(0)
}

visit(JSON.parse(process.argv[2]))
