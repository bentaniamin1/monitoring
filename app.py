from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/metrics', methods=['GET'])
def metric():
    # # Example metric data
    # data = {
    #     'cpu_usage': '70%',
    #     'memory_usage': '65%'
    # }
    # return jsonify(data)

@app.route('/healthy', methods=['GET'])
def healthy():
    return jsonify({'status': 'healthy OK'})

if __name__ == '__main__':
    app.run(debug=True)