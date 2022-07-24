import requests

KIWI_API_KEY = "9gFYAzi4YC14e6JoYYortu_RvPe3pKzw"
kiwi_search_endpoint = "https://tequila-api.kiwi.com/v2/search"
headers = {
    "apikey": KIWI_API_KEY
}


# This class is responsible for talking to the Flight Search API.
class FlightSearch:
    def __init__(self, params):
        self.params = params

    # FIXME: fix problem with certain results giving prices way too high, ie: $18,000.
    #  Possible problem with parameters in request.
    def search(self):
        new_city_data = {}
        for city in self.params:
            response = requests.get(
                url=kiwi_search_endpoint,
                params=city,
                headers=headers)
            iata_code = city["fly_to"].split("city:")[1]
            # Parse response data and store price into a dictionary
            try:
                # city_dict = {iata_code: response.json()["data"][0]["price"]}
                new_city_data[iata_code] = response.json()["data"][0]["price"]
            except IndexError:
                # Since no flight prices were found, use 0 as an indicator
                # city_dict = {iata_code: 0}
                # new_city_data.append(city_dict)
                new_city_data[iata_code] = 0
        return new_city_data
