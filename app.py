import requests

from flask import Flask, jsonify, abort

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['JSON_SORT_KEYS'] = False


@app.route("/github_keys/<username>")
def get_keys(username: str):
    """
    Take username as a string, send get request to GitHub endpoint,
    parse results type/key values, return JSON object.
    :param username: github username
    :return: user list of keys (JSON)
    """

    request = requests.get(f"https://github.com/{username}.keys")
    key_data = request.text.split("\n")
    parsed_keys = list()
    if key_data[0] == "Not Found":  # no such user (key_data = ['Not Found'])
        abort(404)

    for key in key_data:
        if key:  # check if list with type/key is not empty
            key_type = key.split(" ")[0]
            key_value = key.split(" ")[1]
            parsed_keys.append(
                {
                    "type": key_type,
                    "key": key_value
                }
            )

    return jsonify(parsed_keys)


if __name__ == "__main__":
    app.run(debug=False)
