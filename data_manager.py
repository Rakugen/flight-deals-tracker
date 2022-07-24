from flight_data import FlightData
import requests
import pprint

# This class is responsible for talking to the Google Sheet.
# Generate city_data from Google sheets info:
# "Paris": {
#         "IATA Code": "PAR",
#         "Lowest Price": 54
#         },

sheety_endpoint = "https://api.sheety.co/118287e6c87cb25fb133738436e4c01a/flightDeals/prices"
headers = {
    "Authorization": "Bearer LittleIsAPotato"
}
city_rows = {
    "PAR": 2,
    "BER": 3,
    "TYO": 4,
    "SYD": 5,
    "IST": 6,
    "KUL": 7,
    "NYC": 8,
    "SFO": 9,
    "CPT": 10
}


class DataManager:
    def __init__(self):
        self.sheet_data = {}

    # Get data from sheety
    def get_data(self):
        response = requests.get(
            url=f"{sheety_endpoint}",
            headers=headers
        )
        pprint.pprint(response.json())
        # Format response.json() data
        new_city_data = {}
        for city in response.json()["prices"]:
            city_name = city["city"]
            iata_code = city["iataCode"]
            low_price = city["lowestPrice"]
            new_city_data[city_name] = {
                "IATA Code": iata_code,
                "Lowest Price": low_price
            }
        self.sheet_data = new_city_data

    def show_data(self):
        for k, v in self.sheet_data.items():
            print(f"{v['IATA Code']}: Low: {v['Lowest Price']}")

    # TODO: create method that will update each row in sheety with new prices
    # Update data on sheety
    # update_params formatted: [{'PAR': 638}, {'BER': 0}, {'TYO': 0}...]
    def update_data(self, update_params):

        for k, v in self.sheet_data.items():
            iata_code = v["IATA Code"]

            new_price = update_params[iata_code]
            if (new_price < v["Lowest Price"]) and (new_price != 0):
                print(f"Low price found: {iata_code}, {new_price} < {v['Lowest Price']}")
                # Found new low price, now need to update sheety
                # FIXME: get sheety to properly update spreadsheet
                new_params = {
                    "price": {
                        "Lowest Price": new_price
                    }
                }
                print(f"URL: {sheety_endpoint}")
                print(f"ROW:{city_rows[iata_code]}")
                response = requests.put(
                    url=f"{sheety_endpoint}/{city_rows[iata_code]}",
                    json=new_params,
                    headers=headers
                )
                print(response.text)
