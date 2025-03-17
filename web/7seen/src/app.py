import json
import base64

from flask import Flask, render_template, session, request, jsonify
from flask_session import Session


app = Flask(
	__name__,
	template_folder="./templates",
	static_folder="./static",
	static_url_path="/static"
)
app.secret_key = "some-random-secret-keeeeey-2123"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "cachelib"
Session(app)

with open("symbols.json") as symbols_file:
	SYMBOLS = json.load(symbols_file)


# Seen 2,3,5
@app.get("/")
def index():
	symbols = session.get("symbols", [])
	flag_parts = [{"id": i, "name": f"seen{i}", "class": "disabled"} for i in range(1, 8)]
	for symbol in symbols:
		flag_parts[symbol["id"]]["name"] = symbol["seen"]
		flag_parts[symbol["id"]].pop("class")

	return (
		render_template(
			"index.html",
			symbols=symbols,
			flag_parts=flag_parts,
			cmnt=list(SYMBOLS.keys())[3],
			plch=list(SYMBOLS.keys())[2],
		),
		{"Seen": base64.b64encode(list(SYMBOLS.keys())[5].encode()).decode()}
	)


@app.post("/prepare")
def prepare_7seen():
	seen = request.json.get("seen")
	if not seen:
		return jsonify({"status": False, "message": "The 'Seen' is required"})
	if not isinstance(seen, str):
		return jsonify({"status": False, "message": "'Seen' should be string"})
	symbol = SYMBOLS.get(seen)
	if not symbol:
		return jsonify({"status": False, "message": "Sorry, but it's not a valid symbol"})

	if not session.get("symbols"):
		session["symbols"] = []
	if symbol in session["symbols"]:
		return jsonify({"status": False, "message": "Already putted!"})
	session["symbols"].append(symbol)
	return jsonify({"status": True})


# Seen 0
@app.get("/robots.txt")
def robots():
	return "User-Agent: *\nDisallow: /ohhh-ive-seen-a-seen\n\n# our site map is under construction", {"content-type": "text/plain"}

@app.get("/ohhh-ive-seen-a-seen")
def seen_sabze_value():
	return list(SYMBOLS.keys())[0]


# Seen 1
@app.get("/sitemap.xml")
def sitemap():
	return f"""
	<sitemapindex xmlns="http://www.google.com/schemas/sitemap/0.84">
	<sitemap>
	<loc>%s</loc>
	</sitemap>
	<sitemap>
	<loc>/haft-seen</loc>
	</sitemap>
	</sitemapindex>
	""" % list(SYMBOLS.keys())[1], {"content-type": "text/xml"}


# Seen 4
@app.get("/xor-key")
def xor_key():
	return list(SYMBOLS.keys())[4] + ", also one of the 'Seen's"


# Seen 6
@app.get("/haft-seen")
def haft_seeeen():
	headers = {"content-type": "text/plain"}

	req_dest = request.headers.get("Sec-Fetch-Dest", "\"empty\"")
	if req_dest != "7seen":
		return f"Only the request's destination to '7seen' can continue!, current: {req_dest}", headers
	if request.args.get("name", "").lower() != "hajji firuz":
		return "What's the ?name= of our famous character, that comes near the nowruz (the new year), like Santa. /^[a-z]{5} [a-z]{5}$/", headers

	response = f"Oh wait, you reached one after diging more, but it was encrypted with '/xor-key': {xor(list(SYMBOLS.keys())[6])}"
	return response, {"content-type": "text/plain"}


def xor(txt):
	key = list(SYMBOLS.keys())[4]
	finall = ""
	for i in range(len(txt)):
		finall += chr(ord(txt[i]) ^ ord(key[i % len(txt)]))
	return base64.b64encode(finall.encode()).decode()