from kubernetes import client
from typing import TypedDict

class Service(TypedDict): 
    name: str
    namespace: str
    type: str
    cluster_ip: str
    
# List all services in a specific namespace
def list_services(namespace: str) -> list:
    """Get a list of services in the specified namespace"""
    services_list = []
    v1 = client.CoreV1Api()
    services = v1.list_namespaced_service(namespace)

    for service in services.items:
        service_info = Service(
            name=service.metadata.name,
            namespace=service.metadata.namespace,
            type=service.spec.type,
            cluster_ip=service.spec.cluster_ip,
        )
        services_list.append(service_info)

    return services_list
