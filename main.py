from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
import requests
import datetime

# KIWI_API_KEY = "9gFYAzi4YC14e6JoYYortu_RvPe3pKzw"
# HOME_CITY = "LAX"
# kiwi_search_endpoint = "https://tequila-api.kiwi.com/v2"
# city_data = {
#     "Paris": {
#         "IATA Code": "PAR",
#         "Lowest Price": 54
#     },
#     "Berlin": {
#         "IATA Code": "BER",
#         "Lowest Price": 42
#     },
#     "Tokyo": {
#         "IATA Code": "TYO",
#         "Lowest Price": 485
#     },
#     "Sydney": {
#         "IATA Code": "SYD",
#         "Lowest Price": 551
#     },
#     "Istanbul": {
#         "IATA Code": "IST",
#         "Lowest Price": 95
#     },
#     "Kuala Lumpur": {
#         "IATA Code": "KUL",
#         "Lowest Price": 414
#     },
#     "New York": {
#         "IATA Code": "NYC",
#         "Lowest Price": 240
#     },
#     "San Francisco": {
#         "IATA Code": "SFO",
#         "Lowest Price": 260
#     },
#     "Cape Town": {
#         "IATA Code": "CPT",
#         "Lowest Price": 378
#     }
# }

# today = datetime.datetime.now()
# tomorrow = today + datetime.timedelta(days=1)


# TODO: Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the
#  cities in the Google Sheet.

# search_params = []
# for k, v in city_data.items():
#     params = {
#         "fly_from": "city:LAX",
#         "fly_to": f"city:{v['IATA Code']}",
#         "date_from": today.strftime("%d/%m/%Y"),
#         "date_to": tomorrow.strftime("%d/%m/%Y"),
#         "one_for_city": 1,
#         "curr": "USD"
#     }
#     search_params.append(params)

# print(search_params)

# simple_search_params = [
#     {
#         "fly_from": "LAX",
#         "fly_to": "NYC",
#         "date_from": "16/7/2022",
#         "date_to": "17/7/2022",
#         "one_for_city": 1,
#         "curr": "USD"
#     },
#     {
#         "fly_from": "LAX",
#         "fly_to": "TYO",
#         "date_from": "16/7/2022",
#         "date_to": "17/7/2022",
#         "one_for_city": 1,
#         "curr": "USD"
#     }
# ]

# headers = {
#     "apikey": KIWI_API_KEY
# }


# response = requests.get(url="https://tequila-api.kiwi.com/v2/search", params=simple_search_params, headers=headers)
#
#
# print(response.json())


# TODO: If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number
#  with the Twilio API. The SMS should include the departure airport IATA code, destination airport IATA code,
#  departure city, destination city, flight price and flight dates. e.g.

# Get data from sheets and save into dict


# Use Data Manager to Create Flight Data

# Initialize a DataManager object with data from Sheety
data_manager = DataManager()
data_manager.get_data()
#
# # Create a FlightData object with Sheety data
# flight_data = FlightData(data_manager.sheet_data)
#
# # Create new search params formatted for kiwi
# search_params = flight_data.create_params()
#
# # New FlightSearch object that interacts with kiwi
# flight_search = FlightSearch(search_params)
#
# # Calls search function to grab new price data from kiwi
# print("Original Data: ")
# data_manager.show_data()
# new_data = flight_search.search()
# print("New Data: ")
# print(new_data)
#
# # Update sheets with new search results
# data_manager.update_data(new_data)

# Show results


