#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import datetime
from tabulate import tabulate
from requests.auth import HTTPBasicAuth
from typing import List, Dict
import logging
import io , sys
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

logging.getLogger().setLevel(logging.INFO)
log = logging.getLogger(__name__)

class GoldengateRestApiHelper():
    """
    A class for interacting with the GoldenGate API.
    """
 
    def __init__(self, base_url: str, metrics_url: str,username: str, password: str) -> None:
        """
        Initializes a new instance of the GoldenGateAPI class.

        Args:
            base_url (str): The base URL of the GoldenGate API.
            metrics_url (str): The metrics URL of the GoldenGate API.
            username (str): The username to use for authentication.
            password (str): The password to use for authentication.
        """
        self.base_url = base_url
        self.metrics_url = metrics_url
        self.auth = HTTPBasicAuth(username, password)

    def start_extract(self, extract_name: str) -> Dict:
        """
        Starts an extract.

        Args:
            extract_name (str): The name of the extract to start.

        Returns:
            dict: A dictionary containing the response from the API.
        """
        endpoint = f"{self.base_url}/commands/execute"
        data = {"name": "start", "processName": extract_name}
        response = requests.post(endpoint, json=data, auth=self.auth)
        return response.json()

    def stop_extract(self, extract_name: str) -> Dict:
        """
        Stops an extract.

        Args:
            extract_name (str): The name of the extract to stop.

        Returns:
            dict: A dictionary containing the response from the API.
        """
        endpoint = f"{self.base_url}/commands/execute"
        data = {"name": "stop", "processName": extract_name}
        response = requests.post(endpoint, json=data, auth=self.auth)
        return response.json()

    def start_replicat(self, replicat_name: str) -> Dict:
        """
        Starts a replicat.

        Args:
            replicat_name (str): The name of the replicat to start.

        Returns:
            dict: A dictionary containing the response from the API.
        """
        endpoint = f"{self.base_url}/commands/execute"
        data = {"name": "start", "processName": replicat_name}
        response = requests.post(endpoint, json=data, auth=self.auth)
        return response.json()

    def stop_replicat(self, replicat_name: str) -> Dict:
        """
        Stops a replicat.

        Args:
            replicat_name (str): The name of the replicat to stop.

        Returns:
            dict: A dictionary containing the response from the API.
        """
        endpoint = f"{self.base_url}/commands/execute"
        data = {"name": "stop", "processName": replicat_name}
        response = requests.post(endpoint, json=data, auth=self.auth)
        return response.json()

    def list_extracts(self) -> Dict:
        """
        Lists all extracts.

        Returns:
            dict: A dictionary containing the response from the API.
        """
        endpoint = f"{self.base_url}/extracts"
        response = requests.get(endpoint, auth=self.auth)
        return response.json()

    def list_replicats(self) -> Dict:
        """
        Lists all replicats.

        Returns:
            dict: A dictionary containing the response from the API.
        """
        endpoint = f"{self.base_url}/replicats"
        response = requests.get(endpoint, auth=self.auth)
        return response.json()

    def get_extract_status(self, extract_name: str) -> Dict:
        """
        Gets the status of an extract.

        Args:
            extract_name (str): The name of the extract to get the status of.

        Returns:
            dict: A dictionary containing the response from the API.
        """
        endpoint = f"{self.base_url}/extracts/{extract_name}/info/status"
        response = requests.get(endpoint, auth=self.auth)
        return response.json()

    def get_extract_details(self, extract_name: str) -> Dict:
        """
        Gets the details of a specific extract from the GoldenGate Deployment.
        
        Parameters:
            extract_name (str): The name of the extract to get details for.
        
        Returns:
            Dict: A dictionary containing the details of the specified extract.
        """
        url = f"{self.base_url}/extracts/{extract_name}"
        response = requests.get(url, auth=self.auth, headers={"Content-Type": "application/json", "Accept": "application/json"})
        response.raise_for_status()
        return response.json()

    def get_replicat_status(self, replicat_name: str) -> Dict:
        """
        Gets the status of a specific replicat from the GoldenGate Deployment.
        
        Parameters:
            replicat_name (str): The name of the replicat to get status for.
        
        Returns:
            Dict: A dictionary containing the status of the specified replicat.
        """
        url = f"{self.base_url}/replicats/{replicat_name}/info/status"
        response = requests.get(url, auth=self.auth, headers={"Content-Type": "application/json", "Accept": "application/json"})
        response.raise_for_status()
        return response.json()

    def get_replicat_details(self, replicat_name: str) -> Dict:
        """
        Gets the details of a specific replicat from the GoldenGate Deployment.
        
        Parameters:
            replicat_name (str): The name of the replicat to get details for.
        
        Returns:
            Dict: A dictionary containing the details of the specified replicat.
        """
        url = f"{self.base_url}/replicats/{replicat_name}"
        response = requests.get(url, auth=self.auth, headers={"Content-Type": "application/json", "Accept": "application/json"})
        response.raise_for_status()
        return response.json()

    # Function to view extract report file
    def view_extract_report_file(self, extract_name: str) -> None:
        """
        Views the extract report file for a specific extract from the GoldenGate Deployment.
        Writes the extract report to a file with the name <extract_name>-<current_date>.rpt
        
        Parameters:
            extract_name (str): The name of the extract to get the report for.
        """
        url = f"{self.base_url}/extracts/{extract_name}/info/reports/{extract_name}.rpt"
        response = requests.get(url, auth=self.auth, headers={"Content-Type": "application/json", "Accept": "application/json"})
        response.raise_for_status()
        now = datetime.datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        with open(f"{extract_name}-{current_date}.rpt", "w") as f:
            for i in response.json()['response']['lines']:
                f.write(str(i).encode("utf-8").decode("latin1") + '\n')

    # Function to view replicat report file
    def view_replicat_report_file(self, replicat_name: str) -> None:
        """
        Downloads a replication report file from the given replicat name and saves it locally.
        
        Args:
        - replicat_name: A string representing the name of the replicat whose report file needs to be downloaded.
        
        Returns:
        - None
        """
        url = f"{self.base_url}/replicats/{replicat_name}/info/reports/{replicat_name}.rpt"
        response = requests.get(url, auth=self.auth, headers={"Content-Type": "application/json", "Accept": "application/json"})
        response.raise_for_status()
        now = datetime.datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        with open(f"{replicat_name}-{current_date}.rpt", "w") as f:
            for i in response.json()['response']['lines']:
                f.write(str(i).encode("utf-8").decode("latin1") )
                f.write("\n")
            # f.writelines(extract_report_file)
        f.close()

    def getStatus(self, typeOf: str, extract_Name: str) -> List:
        """
        Gets the status of an extract or a replicat and returns a list containing the status details.
        
        Args:
        - typeOf: A string representing the type of object (extract or replicat).
        - extract_Name: A string representing the name of the extract or replicat.
        
        Returns:
        - A list containing the following items:
            * typeOf: A string representing the type of object (extract or replicat).
            * extract_Name: A string representing the name of the extract or replicat.
            * status: A string representing the status of the extract or replicat.
            * lastStarted: A string representing the date and time when the extract or replicat was last started.
            * lag: An integer representing the lag time of the extract or replicat.
            * mappedTotalInserts: An integer representing the total number of inserts in the extract or replicat.
            * mappedTotalUpdates: An integer representing the total number of updates in the extract or replicat.
            * mappedTotalDeletes: An integer representing the total number of deletes in the extract or replicat.
        """
        staticType='statisticsExtract'    
        if typeOf == 'replicats':
            staticType='statisticsReplicat' 
        extract_status = requests.get(f'{self.base_url}/{typeOf}/\{extract_Name}/info/status',auth = self.auth).json()['response']
        if 'response' in requests.get(f'{self.metrics_url}/mpoints/{extract_Name}/{staticType}',auth = self.auth).json():
            extract_stats = requests.get(f'{self.metrics_url}/mpoints/{extract_Name}/{staticType}',auth = self.auth).json()['response']
        else:
            extract_stats = {'mappedTotalInserts': 0,'mappedTotalUpdates': 0,'mappedTotalDeletes': 0}
        return [typeOf,extract_Name,extract_status['status'],extract_status['lastStarted'],extract_status['lag'],extract_stats["mappedTotalInserts"],extract_stats["mappedTotalUpdates"],extract_stats["mappedTotalDeletes"]]

    def getAllNames(self, typeOf: str) -> List[str]:
        """
        Retrieves a list of names for all extracts or replicats.

        Args:
            typeOf (str): The type of object to retrieve the names for (either 'extracts' or 'replicats').

        Returns:
            A list of strings representing the names of all extracts or replicats.
        """
        listOfExtracts = requests.get(f'{self.base_url}/{typeOf}',auth = self.auth).json()['response']
        return listOfExtracts['items']

    def monitor_deployment(self) -> None:
        """
        Prints a table displaying the status and statistics for all extracts and replicats.
        
        Returns:
            None
        """
        ggTable = []
        ggTable.append(['Type','Name','Status','Last Started','lag','Inserts','Updates','Deletes'])
        for p in ['extracts','replicats']:
            for item in self.getAllNames(p):
                name=item['name']
                ggTable.append(self.getStatus(p,name))

        print((tabulate(ggTable, headers='firstrow', tablefmt='fancy_grid')))


