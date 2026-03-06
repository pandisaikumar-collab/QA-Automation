"""
test_realpython.py
"""

import pytest
import requests
import os
import json 
import yaml 
import logging
from models.rest.realpython import RealPython
from models.rest.utils.realpython_util import RealPythonUtil

log = logging.getLogger(os.path.basename(__file__))
log.setLevel(logging.INFO)

current_dir = os.path.dirname(os.path.abspath(__file__))
end_pionts = os.path.join(current_dir, '../../config/endpoints.yaml')
with open(end_pionts, 'r') as file:
    endpoints = yaml.safe_load(file)
#@pytest.mark.skip
def test_get_request():
    realpython_obj = RealPython()
    get_url = endpoints['REALPYTHON_GET']
    response = realpython_obj.get(get_url)

    if response.status_code == 200:
        data = response.json()
        log.info(f"Response data: {data}")
        log.info(f"Response content: {response.content}")
        log.info(f"Response headers: {response.headers}")
        log.info(f"Response elapsed time: {response.elapsed.total_seconds()} seconds")
        log.info(f"Response URL: {response.url}")
        log.info(f"Response encoding: {response.encoding}")
        log.info(f"Response reason: {response.reason}")
        log.info(f"Response text: {response.text}")

    else:
        log.info(f"Response content: {response.content}")
        log.info(f"Response headers: {response.headers}")
        log.info(f"Response text: {response.text}")
        pytest.fail(f"GET request failed with status code: {response.status_code}")

#@pytest.mark.skip
def test_post_realpython():
    realpython_obj = RealPython()
    put_url = endpoints['REALPYTHON_POST']

    payload = {
        "userId": 1,
        "title": "Saikumar Pandi",
        "completed": False
    }

    response = realpython_obj.post(put_url, json=payload)

    if response.status_code == 201:
        log.info("POST Success:")
        log.info(response.json())
        log.info(response.text)
    else:
        log.error(f"PUT failed with status code: {response.status_code}")
        log.error(response.text)
        pytest.fail("Failed PUT request.")
#@pytest.mark.skip
def test_put_realpython():
    realpython_obj = RealPython()
    put_url = endpoints['REALPYTHON_PUT']
    api_payload = {
        "userId": [1000],
        "title": ["Saikumar Pandi"],
        "completed": [False]
    }
    payload = {
        "userId": api_payload["userId"][0],
        "title": api_payload["title"][0],
        "completed": api_payload["completed"][0]
    }
    response = realpython_obj.put(put_url, json=payload)

    if response.status_code == 200:
        log.info("PUT Success:")
        log.info(response.json())
        log.info(response.text)
    else:
        log.error(f"PUT failed with status code: {response.status_code}")
        log.error(response.text)
        pytest.fail("Failed PUT request.")


def test_delete_realpython():
    realpython_obj = RealPython()
    delete_url = endpoints['REALPYTHON_DELETE']

    response = realpython_obj.delete(delete_url)

    if response.status_code == 200:
        log.info("DELETE Success:")
        log.info(f"Response: {response.text}")
    else:
        log.error(f"DELETE failed with status code: {response.status_code}")
        log.error(response.text)
        pytest.fail("Failed DELETE request.")


