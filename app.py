from flask import Flask, render_template_string
from monitor.monitor import get_service_metrics
from predictor.predictor import predict_health
from detector.failure_detector import detect_failure
from orchestrator.orchestrator import orchestrate

app = Flask(__name__)

services = ["user-service", "payment-service", "notification-service"]

@app.route("/")
def dashboard():
    results = []

    for service in services:
        metrics = get_service_metrics(service)
        prediction = predict_health(metrics)
        is_failure = detect_failure(prediction, metrics.status)

        action = "Healthy"
        if is_failure:
            orchestrate(service)
            action = "Healing Action Taken"

        results.append({
            "name": service,
            "metrics": metrics,
            "status": metrics.status,
            "prediction": "Unhealthy" if prediction else "Healthy",
            "action": action
        })

    html = """
    <h1>🩺 Microservices Health Dashboard</h1>
    <table border="1" cellpadding="10">
        <tr>
            <th>Service</th>
            <th>Status</th>
            <th>Prediction</th>
            <th>CPU</th>
            <th>Memory</th>
            <th>Latency (ms)</th>
            <th>Action</th>
        </tr>
        {% for r in results %}
        <tr>
            <td>{{ r.name }}</td>
            <td>{{ r.status }}</td>
            <td>{{ r.prediction }}</td>
            <td>{{ "%.2f"|format(r.metrics.cpu_usage) }}</td>
            <td>{{ "%.2f"|format(r.metrics.memory_usage) }}</td>
            <td>{{ "%.2f"|format(r.metrics.latency_ms) }}</td>
            <td>{{ r.action }}</td>
        </tr>
        {% endfor %}
    </table>
    """

    return render_template_string(html, results=results)

if __name__ == "__main__":
    app.run(debug=True)
