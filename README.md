# GoldenGate API CLI

The GoldenGate API CLI is a command-line interface for interacting with the GoldenGate REST API. It allows users to start/stop extracts and replicats, list extracts/replicats, and get their status and details. The CLI also provides options to view the extract/replicat report files and monitor the deployment.
Installation

## To use the GoldenGate API CLI, follow these steps:

### Clone the repository:

~~~bash

git clone https://github.com/wmdubberley/GoldenGateAdminApi.git

~~~

### Install the required Python packages:

~~~bash
pip install -r requirements.txt
~~~

### Configuration

Before using the CLI, you need to create a configuration file in YAML format. The configuration file should contain the following fields:

    deployments: a list of deployments with their names, base URL, username, and password.

#### Example configuration file:

~~~yaml

deployments:
  - deployment: my-deployment
    baseURL: https://example.com/goldengate
    username: my-username
    password: my-password
~~~
Save the configuration file as config.yml in the same directory as the ggapi.py script.
Usage


## To use the CLI, run the following command:

~~~shell
python ggapi.py [-h] -d DEPLOYMENT [-e EXTRACT_NAME] [-r REPLICAT_NAME] [--Monitor-Deployment]
                      [--start-extract] [--stop-extract] [--start-replicat] [--stop-replicat]
                      [--list-extracts] [--list-replicats] [--extract-status] [--extract-details]
                      [--replicat-status] [--replicat-details] [--view-extract-report]
                      [--view-replicat-report]
~~~
Arguments:

    -h, --help: show the help message and exit.
    -d DEPLOYMENT, --deployment DEPLOYMENT: name of the deployment (required).
    -e EXTRACT_NAME, --extract_name EXTRACT_NAME: name of the extract process.
    -r REPLICAT_NAME, --replicat_name REPLICAT_NAME: name of the replicat process.
    --Monitor-Deployment: start monitoring the deployment.
    --start-extract: start an extract process.
    --stop-extract: stop an extract process.
    --start-replicat: start a replicat process.
    --stop-replicat: stop a replicat process.
    --list-extracts: list all extract processes.
    --list-replicats: list all replicat processes.
    --extract-status: get the status of an extract process.
    --extract-details: get the details of an extract process.
    --replicat-status: get the status of a replicat process.
    --replicat-details: get the details of a replicat process.
    --view-extract-report: view the extract report file.
    --view-replicat-report: view the replicat report file.

## Example usage:

~~~bash

python ggapi.py -d my-deployment --start-extract -e my-extract

~~~

This command starts the my-extract process in the my-deployment deployment.
n.
