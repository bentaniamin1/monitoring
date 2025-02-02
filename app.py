from prometheus_client import generate_latest, CollectorRegistry, Counter, Gauge
import psutil

from flask import Flask, jsonify

app = Flask(__name__)

REQUEST_COUNTER = Counter('http_requests_total', 'Total HTTP Requests')
CPU_USAGE = Gauge('cpu_usage_percent', 'CPU Usage in Percent')



def update_cpu_usage():
    cpu_percent = psutil.cpu_percent()
    CPU_USAGE.set(cpu_percent)
   
@app.route('/metrics', methods=['GET'])
def metric():
    update_cpu_usage()
    return generate_latest()

@app.route('/health', methods=['GET'])
def healthy():
    return jsonify({'status': 'healthy OK'})

@app.route('/')
def home():
    REQUEST_COUNTER.inc()  
    return "Hello, Prometheus!"


if __name__ == '__main__':
    app.run(debug=True)