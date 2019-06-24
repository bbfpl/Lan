#  locust -f ./locust11.py -P 8090
from locust import HttpLocust, Locust, TaskSet, TaskSequence, task, seq_task

__all__ = [
    'HttpLocust',
    'Locust',
    'TaskSet',
    'TaskSequence',
    'task',
    'seq_task'
]
