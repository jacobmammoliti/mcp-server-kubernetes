from kubernetes import client
from typing import TypedDict

class Deployment(TypedDict):
    name: str
    namespace: str
    selector: dict

# List all deployments in a specific namespace
def list_deployments(namespace: str) -> list:
    """Get a list of deployments in the specified namespace"""
    deployments_list = []
    v1 = client.CoreV1Api()
    deployments = v1.list_namespaced_deployment(namespace)

    for deployment in deployments.items:
        deployment_info = Deployment(
            name=deployment.metadata.name,
            namespace=deployment.metadata.namespace,
            selector=deployment.spec.selector,
        )
        deployments_list.append(deployment_info)

    return deployments_list
