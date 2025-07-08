import yaml
from monitor.monitor import get_service_metrics
from predictor.predictor import predict_health
from detector.failure_detector import detect_failure
from orchestrator.orchestrator import orchestrate
from utils.logger import log

def load_services():
    with open("config/services.yaml", "r") as f:
        return yaml.safe_load(f)["services"]

def main():
    services = load_services()

    for service in services:
        name = service["name"]
        metrics = get_service_metrics(name)
        prediction = predict_health(metrics)
        if detect_failure(prediction, metrics["status"]):
            orchestrate(name)
            log(name, metrics, "Healing Action Taken")
        else:
            log(name, metrics, "Healthy")

if __name__ == "__main__":
    main()
