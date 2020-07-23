from flask import Flask, request, escape, Response
import json


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	name = request.args.get("name", "World")
	return f"Hello, {escape(name)}"

@app.route("/functions", methods = ["GET", "POST"])
def agave_functions():
	print(f"{request.method} /functions")
	if request.method == "POST":
		data = request.get_data(as_text = True)
		print("Body=" + data)
		requestPayloadObj = request.get_json(force=True)
		print("FunctionId=" + requestPayloadObj.get("id"))
		responseText = json.dumps({
			"post-result": 5
		})
	else:
		responseText = json.dumps({
			"get-result": 10
		})

	response = Response(responseText)
	response.headers["Content-Type"] = "application/json"
	response.headers["Access-Control-Allow-Origin"] = "*"
	return response

if __name__ == "__main__":
	app.run()
