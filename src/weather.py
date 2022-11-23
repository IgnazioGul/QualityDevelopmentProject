from src.call import check,geo,weather

class WeatherCall:

    def __init__(self, key: str) -> None:
        self.key = key

    def check_key(self) -> None:
        """
        check_key method checks if the key is correct for the API call
        :return:  if the error occurs, the method returns an exception
        """
        response = check(self.key)
        if response == 401:
            raise TypeError("Invalid Key")

    def get_coordinates(self, city: str, limit: int) -> dict | None:
        """
        the get_coordinates method executes an API call which, given a city, returns its coordinates
        :param city: the city taken to have its coordinates
        :param limit:the maximum number of values chosen
        :return: the json containing the coordinates
        """
        response = geo(self.key, city, limit)
        if "cod" in response:
            raise TypeError("Error Call")
        return response

    def get_weather(self, lat: float, lon: float) -> dict | None:
        """
        the get_weather method executes an API call which, given latitude and longitude, returns its weather
        :param lat: latitude
        :param lon: longitude
        :return: the json containing all the information on the weather of the city
        """
        response = weather(self.key, lat, lon)
        if "cod" in response and response['cod'] == 401:
            raise TypeError("Error Call")
        return response
        