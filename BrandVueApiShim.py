import requests
import csv
import io

base_url = 'http://localhost:8082'
api_key = 'ThisIsTheDebugApiKey'

# Helper functions to fetch data from the API
def fetch_json(endpoint):
    url = f"{base_url}{endpoint}"
    response = requests.get(url, headers={'Authorization': f'Bearer {api_key}'})
    response.raise_for_status()
    return response.json()

def fetch_csv(endpoint):
    url = f"{base_url}{endpoint}"
    response = requests.get(url, headers={'Authorization': f'Bearer {api_key}'})
    response.raise_for_status()
    csv_data = response.text
    csv_reader = csv.DictReader(io.StringIO(csv_data))
    return list(csv_reader)

def get_weightings(surveyset, date):
    date_str = date.strftime("%Y-%m-%d")
    print(f"Fetching weightings for {surveyset} on {date_str}")
    return fetch_json(f"/api/surveysets/{surveyset}/averages/Monthly/weights/{date_str}")

def get_survey_responses(surveyset, entity, date):
    date_str = date.strftime("%Y-%m-%d")
    print(f"Fetching survey responses for {surveyset} {entity} on {date_str}")
    return fetch_csv(f"/api/surveysets/{surveyset}/classes/{entity}/answers/{date_str}")

def get_survey_respondents(surveyset, date):
    date_str = date.strftime("%Y-%m-%d")
    print(f"Fetching survey respondents for {surveyset} on {date_str}")
    return fetch_csv(f"/api/surveysets/{surveyset}/profile/answers/{date_str}")