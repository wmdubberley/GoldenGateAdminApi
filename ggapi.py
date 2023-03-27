import requests
import yaml
import datetime

with open("config.yml", "r") as config_file:
    config = yaml.safe_load(config_file)

username = config["username"]
password = config["password"]
base_url = config["base_url"]


def list_extracts():
    endpoint = f"{base_url}/extracts"
    response = requests.get(endpoint, auth=(username, password))
    return response.json()

def start_extract(extract_name):
    endpoint = f"{base_url}/commands/execute"
    data = {"name": "start", "processName": extract_name}
    response = requests.post(endpoint, json=data, auth=(username, password))
    return response.json()

def stop_extract(extract_name):
    endpoint = f"{base_url}/commands/execute"
    data = {"name": "stop", "processName": extract_name}
    response = requests.post(endpoint, json=data, auth=(username, password))
    return response.json()

def get_extract_Stats(extract_name):
    endpoint = f"{base_url}/mpoints/{extract_name}/statisticsExtract"
    response = requests.get(endpoint, auth=(username, password))
    return response.json()

def get_extract_status(extract_name):
    endpoint = f"{base_url}/extracts/{extract_name}/info/status"
    response = requests.get(endpoint, auth=(username, password))
    return response.json()

# Function to view extract report file
def view_extract_report_file(extract_name):
    url = f"{base_url}/extracts/{extract_name}/info/reports/{extract_name}.rpt"
    response = requests.get(url, auth=(username, password), headers={"Content-Type": "application/json", "Accept": "application/json"})
    response.raise_for_status()
    now = datetime.datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    with open(f"{extract_name}-{current_date}.rpt", "w") as f:
        for i in response.json()['response']['lines']:
            f.write(i)
            f.write("\n")
        # f.writelines(extract_report_file)
    f.close()

def start_replicat(replicat_name):
    endpoint = f"{base_url}/commands/execute"
    data = {"name": "start", "processName": replicat_name}
    response = requests.post(endpoint, json=data, auth=(username, password))
    return response.json()

def stop_replicat(replicat_name):
    endpoint = f"{base_url}/commands/execute"
    data = {"name": "stop", "processName": replicat_name}
    response = requests.post(endpoint, json=data, auth=(username, password))
    return response.json()

def get_replicat_Stats(replicat_name):
    endpoint = f"{base_url}/mpoints/{replicat_name}/statisticsReplicat"
    response = requests.get(endpoint, auth=(username, password))
    return response.json()

def list_replicats():
    endpoint = f"{base_url}/replicats"
    response = requests.get(endpoint, auth=(username, password))
    return response.json()

def get_extract_details(extract_name):
    url = f"{base_url}/extracts/{extract_name}"
    response = requests.get(url, auth=(username, password), headers={"Content-Type": "application/json", "Accept": "application/json"})
    response.raise_for_status()
    return response.json()

def get_replicat_status(replicat_name):
    url = f"{base_url}/replicats/{replicat_name}/info/status"
    response = requests.get(url, auth=(username, password), headers={"Content-Type": "application/json", "Accept": "application/json"})
    response.raise_for_status()
    return response.json()

# Function to retrieve details of a replicat
def get_replicat_details(replicat_name):
    url = f"{base_url}/replicats/{replicat_name}"
    response = requests.get(url, auth=(username, password), headers={"Content-Type": "application/json", "Accept": "application/json"})
    response.raise_for_status()
    return response.json()

def view_replicat_report_file(replicat_name):
    url = f"{base_url}/replicats/{replicat_name}/info/reports/{replicat_name}.rpt"
    response = requests.get(url, auth=(username, password), headers={"Content-Type": "application/json", "Accept": "application/json"})
    response.raise_for_status()
    now = datetime.datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    with open(f"{replicat_name}-{current_date}.rpt", "w") as f:
        for i in response.json()['response']['lines']:
            f.write(i)
            f.write("\n")
    f.close()

