#create deployment and service
import subprocess

def apply_kubernetes_manifest(file_name):
    """Applies a Kubernetes YAML file using kubectl."""
    result = subprocess.run(["kubectl", "apply", "-f", file_name], capture_output=True, text=True)
    print(f"Applied {file_name}:\n{result.stdout}\n{result.stderr}")

def get_pods():
    """Fetches the list of running pods."""
    result = subprocess.run(["kubectl", "get", "pods"], capture_output=True, text=True)
    print("Current Pods:\n", result.stdout)

def main():
    print("🚀 Deploying application to Kubernetes...")
    apply_kubernetes_manifest("deployment.yaml")
    apply_kubernetes_manifest("service.yaml")
    get_pods()

if __name__ == "__main__":
    main()


