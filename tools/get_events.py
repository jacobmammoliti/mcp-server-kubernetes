from kubernetes import client
from typing import TypedDict

class Event(TypedDict):
    type: str
    reason: str
    message: str
    involved_object: dict
    count: int

# List all pods in a specific namespace
def get_events(namespace: str) -> list:
    """Get a list of events in the specified namespace"""
    events_list = []
    v1 = client.CoreV1Api()
    events = v1.list_namespaced_event(namespace)

    for event in events.items:
        event_info = Event(
            type=event.type,
            reason=event.reason,
            message=event.message,
            involved_object=event.involved_object,
            count=event.count,
        )
        events_list.append(event_info)

    return events_list
