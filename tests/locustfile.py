import time
import random
from locust import HttpUser, task, between

# Run locust 
# Test app running locally
# locust --host "http://localhost:8000"
# Test app deployed to Azure Webapps: 
# locust --host "https://ik-udes-proj6.azurewebsites.net:443"
# Go to http://localhost:8089/


def _generate_example():
    """
    Return test example
    """
    # return {"CHAS":{"0":0},"RM":{"0":6.575},"TAX":{"0":296.0},"PTRATIO":{"0":15.3},"B":{"0":396.9},"LSTAT":{"0":4.98}}
    return {
        "CHAS": {
            "0": 0
        }, 
        "RM": {
            "0": random.uniform(0, 10)
        }, 
        "TAX": {
            "0": random.uniform(100, 300)
        },
        "PTRATIO": {
            "0": random.uniform(0, 20)
        },
        "B": {
            "0": random.uniform(0, 400)
        },
        "LSTAT": {
            "0": random.normalvariate(0, 10)
        }
    }


class TestUser(HttpUser):
    """
    Implementation of client requests to the Web API
    """
    wait_time = between(1, 3)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @task
    def request_prediction(self):
        """
        Request prediction
        """
        test_example = _generate_example()
        print("Example: %s" % test_example)
        
        res = self.client.post("/predict", json=test_example)
        res.raise_for_status()
        print("Prediction: % s" % res.json())
