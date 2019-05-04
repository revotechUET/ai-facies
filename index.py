from flask import Flask, jsonify, request
from services import controller
from numpy import array
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api/v1/unit-breakdown", methods=["POST"])
def unit_breakdown():
    try:
        data = request.get_json()

        for item in ["GR", "TVD"]:
            if not data or item not in data.keys():
                return parse_response("Field Missing", False, 400)

        gr = array(data["GR"])
        tvd = array(data["TVD"])
        data = controller.unit_breakdown(gr, tvd)
        print(data)
        return parse_response(list(data))

    except Exception as e:
        print(str(e))
        return parse_response("Internal Server Error", False, 500)


@app.route("/api/v1/expert-rule", methods=["POST"])
def expert_rule():
    try:
        data = request.get_json()

        for item in ["GR", "MUD_VOLUME", "TVD", "Boundary_flag"]:
            if not data or item not in data.keys():
                return parse_response("Field Missing", False, 400)
        for key in data.keys():
            data.update({key: array(data[key])})
        res = controller.expert_rule(data)
        return parse_response(res)

    except Exception as e:
        print(str(e))
        return parse_response("Internal Server Error", False, 500)


def parse_response(data, success=True, code=200):
    if success:
        return jsonify({
            "reason": "Success",
            "content": data,
            "code": code
        })
    else:
        return jsonify({
            "reason": data,
            "content": "",
            "code": code
        })


if __name__ == '__main__':
    app.run(port=9999, host="0.0.0.0")
