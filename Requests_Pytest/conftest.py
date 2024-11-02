import json
import os

import pytest
from datetime import datetime


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # for unique report name generation
    report_directory = 'reports'
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_directory}/reports_{now}.html"


@pytest.fixture(scope='session', autouse=True)
def setup_teardown():
    print("starting")
    yield
    print("end")


@pytest.fixture
def load_json_data():
    # json_file_path = os.path.join(os.getcwd(), "data", "test_data.json")
    json_file_path = "C:\\Users\\soundarr\\Desktop\\RestAPI\\Requests_Pytest\\data\\test_data.json"
    with open(json_file_path) as f:
        data = json.load(f)
    return data






