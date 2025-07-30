
import os, sys, logging, time,json, requests 
from datetime import datetime, timedelta 

from st2common.runners.base_action import Action 

class ListIncidentsAction(Action):
    def run(self, team_id=None, team_key=None): 
        """
        List incidents based on the provided parameters.
        """
        # Initialize logging
        logging.basicConfig(level=logging.INFO)
        
        # Log the input parameters
        
        self.team_id = team_id
        self.team_key = team_key
        self.base_url = "https://api.example.com/incidents"  # Replace with actual API endpoint
        self.headers = {
            'Authorization': f"Token token={self.team_key}",
            'Accept': 'application/vnd.pagerduty+json;version=2',
            'Content-Type': 'application/json'
        }
        self.params = {
            'team_ids[]': f"{self.team_id}",
            'statuses[]': ['triggered', 'acknowledged', 'resolved'],
            'sort_by': 'created_at:desc'
        }

        try:
            response = requests.get(url = self.base_url, 
                                    params=self.params,
                                    headers=self.headers)
            
            response.raise_for_status()  # Raise an error for HTTP errors
            incidents = response.json()['incidents']
            for i in incidents:
                print(i['title'])
        except requests.RequestException as e:
            logging.error(f"Error fetching incidents: {e}")
            
            # Filter incidents based on team_id and team_key if provided

        # Log the fetched incidents
        # logging.info(f"Fetched incidents: {incidents}")
        
        return incidents