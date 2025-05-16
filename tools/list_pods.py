from kubernetes import client
from typing import TypedDict

class Pod(TypedDict):
    name: str
    namespace: str

# List all pods in a specific namespace
def list_pods(namespace: str) -> list:
    """Get a list of pods in the specified namespace"""
    pods_list = []
    v1 = client.CoreV1Api()
    pods = v1.list_namespaced_pod(namespace)

    for pod in pods.items:
        pod_info = Pod(
            name=pod.metadata.name,
            namespace=pod.metadata.namespace,
        )
        pods_list.append(pod_info)

    return pods_list
