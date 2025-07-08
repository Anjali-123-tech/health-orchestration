
def predict_health(metrics):
    return (
        metrics.cpu_usage > 70 or
        metrics.memory_usage > 75 or
        metrics.latency_ms > 300
    )

    prediction = model.predict(features)
    return prediction[0]  # healthy or unhealthy
