from types import SimpleNamespace
import random

def get_service_metrics(service_name):
    return SimpleNamespace(
        cpu_usage=random.uniform(0, 100),
        memory_usage=random.uniform(0, 100),
        latency_ms=random.uniform(10, 500),
        status="healthy" if random.random() > 0.2 else "unhealthy"
    )
