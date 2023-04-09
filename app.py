from flask import Flask, jsonify
# Basic Python Flask app designed to return a custom JSON URL.
app = Flask('__name__')


@app.route('/')
def __main__():
    return jsonify({'hello': 'world'})


if __name__ == '__main__':
    app.run()