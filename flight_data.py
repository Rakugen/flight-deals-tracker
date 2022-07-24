import datetime

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

HOME_CITY = "LAX"
today = datetime.datetime.now()
tomorrow = today + datetime.timedelta(days=1)


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, data):
        self.data = data

    def create_params(self):
        search_params = []
        for k, v in self.data.items():
            params = {
                "fly_from": f"city:{HOME_CITY}",
                "fly_to": f"city:{v['IATA Code']}",
                "date_from": today.strftime("%d/%m/%Y"),
                "date_to": tomorrow.strftime("%d/%m/%Y"),
                "one_for_city": 1,
                "curr": "USD",
                "adults": 1,
                "children": 0,
                "selected_cabins": "M"
            }
            search_params.append(params)
        return search_params
