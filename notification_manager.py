class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    # TODO: modify this class so that it doesn't send text msgs but instead
    #  prints to console when there is a price difference found.
    #  The SMS should include the departure airport IATA code, destination airport
    #  IATA code, departure city, destination city, flight price and flight dates,etc
    def __init__(self, flight_data):
        self.flight_data = flight_data

    def send_notification(self):
        # Send notification using self.flight_data
        pass
