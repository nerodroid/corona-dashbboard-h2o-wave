import json
import requests
from datetime import datetime

def dateConvo(date):
    return  datetime.strptime(date, '%m/%d/%y').strftime('%m/%d/%Y')

def requestDataByCountry(country):

    api_url = f'https://corona.lmao.ninja/v2/historical/{country}?lastdays=30'
    response = requests.get(api_url)
    if response.status_code == 200:

        case_data = response.json()['timeline']['cases']
        death_data = response.json()['timeline']['deaths']
        recovered_data = response.json()['timeline']['recovered']
        all_cases = case_data.items()
        all_deaths = death_data.items()
        all_recovered = recovered_data.items()

        case_list = [(dateConvo(date),cases) for date,cases in all_cases]
        death_list = [(dateConvo(date),cases) for date,cases in all_deaths]
        recovered_list = [(dateConvo(date), cases) for date, cases in all_recovered]

        return [case_list , death_list , recovered_list]

    elif response.status_code == 404:
        print("Result not found!")
        return None

#requestCaseData('Sri Lanka')

def requestCountrySummaryData(country):

    api_url = f'https://corona.lmao.ninja/v2/countries/{country}?yesterday'
    response = requests.get(api_url)
    if response.status_code == 200:

        countryInfo = response.json()
        updated = datetime.fromtimestamp( response.json()['updated']/1000 )

        result_dict = {
            'country' :response.json()['country'] ,
            'flag':countryInfo['countryInfo']['flag'],
            'updatedAt':updated.strftime("%m/%d/%Y , %H:%M"),
            'cases':countryInfo['cases'],
            'todayCases':countryInfo['todayCases'],
            'deaths':countryInfo['deaths'],
            'todayDeaths':countryInfo['todayDeaths'],
            'active':countryInfo['active'],
            'tests':countryInfo['tests'],
            'population':countryInfo['population']

        }
        return result_dict

    elif response.status_code == 404:
        print("Result not found!")
