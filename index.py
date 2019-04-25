from flask import Flask, jsonify, request
from services import controller
from numpy import array

app = Flask(__name__)


@app.route("/api/v1/unit-breakdown", methods=["POST"])
def unit_breakdown():
    data = request.get_json()
    try:
        gr = array(data["GR"])
        tvd = array(data["TVD"])
    except KeyError:
        return parse_response("Field Missing", False), 400

    try:
        data = controller.unit_breakdown(gr, tvd)
        print(data)
    except Exception as e:
        print(str(e))
        return parse_response("Internal Server Error", False), 500

    return parse_response(list(data))


@app.route("/api/v1/expert-rule", methods=["POST"])
def expert_rule():
    data = request.get_json()
    try:
        for item in ["GR", "Depth", "TVD", "Boundary_flag"]:
            if item not in data.keys():
                return parse_response("Field Missing", False), 400
        for key in data.keys():
            data.update({key: array(data[key])})
        res = controller.expert_rule(data)

    except Exception as e:
        print(str(e))
        return parse_response("Internal Server Error", False), 500

    return parse_response(jsonify(res))


def parse_response(data, success=True):
    if success:
        return jsonify({
            "success": True,
            "payload": data
        })
    else:
        return jsonify({
            "success": False,
            "message": data
        })


if __name__ == '__main__':
    app.run(debug=True, port=9999)
