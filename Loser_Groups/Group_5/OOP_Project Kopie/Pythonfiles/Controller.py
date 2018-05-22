import requests
from math import sin, cos, sqrt, atan2, radians
import webbrowser


class Controller:

    def __init__(self, model, view):
        """
        Initializes Controller with Model and View
        Deletes all requests and related info for requests that are older than 12h
        :param model:
        :param view:
        """
        self.model = model
        self.view = view
        self.model.delete_requests()

    def quit_or_restart(self):
        """
        Accepts the view.input on whether to quit or restart
        :return:
        """
        u_input = self.view.end_or_back()
        if u_input == 1:
            raise SystemExit
        elif u_input == 2:
            self.view.print_restart()
            return self.get_userloc()

    def get_userloc(self):
        """
        Accepts the view.input for the address
        :return:
        """
        user_location = self.view.get_ulocation()
        return self.get_geocode(user_location)

    def get_geocode(self, user_location):
        """
        Uses the google geocoding API to get latitude and longitude of the users address
        :param user_location:
        :return:
        """
        akey_GC = 'AIzaSyAFNp6uuBwOa0w6f9N9en36EYhbCjugYpc'
        url_GC = 'https://maps.googleapis.com/maps/api/geocode/json?'
        params = dict(
            key=akey_GC,
            address=user_location)
        r = requests.get(url_GC, params=params).json()

        return self.geocode_error(r)

    def geocode_error(self, geocode):
        """
        Checks for a geocode api error, goes back if it detects one, otherwise returns latitude and longitude
        :param geocode:
        :return:
        """
        r = geocode
        if r['status'] == 'OK':
            lat = r['results'][0]['geometry']['location']['lat']
            lng = r['results'][0]['geometry']['location']['lng']
            return self.get_category(lat, lng)
        else:
            self.view.renew_ulocation()
            return self.get_geocode(self.view.get_ulocation())

    def get_category(self, lat, lng):
        """
        Gets all categories from the DB through the model and returns it to the view, and then accepts an input for the
        category and starts the distance requests
        :param lat:
        :param lng:
        :return:
        """
        cat = self.model.select_categories()
        user_category = self.view.view_cat(cat)
        return self.distance_requests(lat, lng, user_category)

    def distance_requests(self, lat, lng, category):
        """
        First it acquires all requests until now from the DB through the model, then checks whether there were any to
        begin with. If no, it goes and and gets the venues. If yes, it checks whether there is a request matching
        the newly made one. If yes, it displays the results of the old request. If no, it start a new venue request.
        It also inserts the request if need be into the DB
        :param lat:
        :param lng:
        :param category:
        :return:
        """

        req = self.model.select_requests()
        if len(req) == 0:
            self.model.insert_request(lat, lng, category)
            coordinates = '{},{}'.format(lat, lng)
            return self.wait(coordinates), self.list_venues(coordinates, category), self.select_one()
        else:

            lat0 = radians(lat)
            lng0 = radians(lng)

            for i in req:
                lat1 = radians(float(i['latitude']))
                lng1 = radians(float(i['longitude']))
                ## then calculate all the pairs of coordinates maybe dictionary comprehension ?
                R = 6373.0

                dlng = lng1 - lng0
                dlat = lat1 - lat0

                a = sin(dlat / 2) ** 2 + cos(lat0) * cos(lat1) * sin(dlng / 2) ** 2
                c = 2 * atan2(sqrt(a), sqrt(1 - a))

                distance = R * c
                if distance < 0.4 and i['categories_category_id'] == category:  # 12 hours in secs
                    return self.view.show_data(
                        self.model.select_old_request(i['request_id'], self.view.getuFilter(), self.view.ascdesc(),
                                                      self.view.get_row_number())), self.select_one()
                else:
                    continue

            self.model.insert_request(lat, lng, category)
            coordinates = '{},{}'.format(lat, lng)

            return self.wait(coordinates), self.list_venues(coordinates, category), self.select_one()

    def wait(self, coordinates):
        """
        Placeholder function to circumvent an issue
        :param coordinates:
        :return:
        """
        return self.get_weather(coordinates)

    def get_weather(self, coordinates):
        """
        Get the weather from the darksky api, parses it into a list and the tells the model to insert the weather into
        the DB.
        :param coordinates:
        :return:
        """

        weather_key = 'b534ec1802ded7f8017fb1d6ed523e85'
        params = dict(
            units='si',
            exclude='flags,minutely'
        )

        url_weather = 'https://api.darksky.net/forecast/{}/{}?'.format(weather_key, coordinates)
        r = requests.get(url_weather, params=params).json()

        forecast = []
        forecast.append((
            r['currently']['summary'],
            r['currently']['temperature'],
            r['currently']['humidity'],
            r['currently']['uvIndex'],
            r['daily']['data'][0]['summary'],
            r['daily']['data'][0]['temperatureHigh'],
            r['daily']['data'][0]['temperatureLow'],
            r['daily']['data'][0]['humidity'],
            r['daily']['data'][0]['uvIndex'],
            r['daily']['data'][1]['summary'],
            r['daily']['data'][1]['temperatureHigh'],
            r['daily']['data'][1]['temperatureLow'],
            r['daily']['data'][1]['humidity'],
            r['daily']['data'][1]['uvIndex'],
            r['daily']['data'][2]['summary'],
            r['daily']['data'][2]['temperatureHigh'],
            r['daily']['data'][2]['temperatureLow'],
            r['daily']['data'][2]['humidity'],
            r['daily']['data'][2]['uvIndex'],
            r['daily']['summary']))

        return self.model.insert_weather(forecast)

    def select_weather(self, venue_id):
        """
        Selects the weather according to a venue id, which is used to get the request id
        :param venue_id:
        :return:
        """
        venue = self.model.select_one(venue_id)
        weather = self.model.select_weather(venue['requests_request_id'])
        weather_list = []
        weather_list.append(weather)
        return self.view.show_data(weather_list)

    #
    def get_venues(self, coordinates, category, offset):
        """
        Get the venues from the Yelp API
        :param coordinates:
        :param category:
        :param offset:
        :return:
        """
        header = {"Authorization": 'Bearer qgwM2L8hevGosZuML4fFq-YD7wXtNUq4Qk2FHeo4N9mMpChXuXrk'
                                   '-ZxbUf1kqn1RThsMuPDk3g3oSFoiJfzSudnaNNqm4l9xMhAdmEiuWaWXE6rA9JkeOKFA_2bwWnYx'}
        params = {'location': coordinates, 'categories': category, 'offset': offset, 'limit': 50}
        r = requests.get('https://api.yelp.com/v3/businesses/search?', params=params, headers=header).json()
        return r

    def list_venues(self, coordinates, category):
        """
        Gets the venues from the Yelp API by looping through the offset to get 1000 instead of 50 results max.
        :param coordinates:
        :param category:
        :return:
        """
        list_venues = []
        for j in range(0, 1000, 50):
            d = self.get_venues(coordinates, category, j)
            for i in d['businesses']:
                list_venues.append((
                    i['id'],
                    i['location']['address1'],
                    i['location']['city'],
                    i['coordinates']['latitude'],
                    i['coordinates']['longitude'],
                    i['name'],
                    i['rating'],
                    i['url'],
                    i['phone'],
                    i['distance']))
        self.model.insert_venues(list_venues)

        row = self.view.get_row_number()  # improve view
        ufilter = self.view.getuFilter()
        ascdesc = self.view.ascdesc()
        lastreqid = self.model.select_request()

        return self.view.show_data(self.model.select_old_request(lastreqid['request_id'], ufilter, ascdesc, row))

    def select_one(self):
        """
        Selects a venue according to the id, which the user inputs, and checks whether it is a valid id
        :return:
        """
        self.view.print_select_one()
        while True:
            answer = self.model.select_one(self.view.select_one())
            if answer is not None:
                answer_list = []
                answer_list.append(answer)
                return self.view.show_data(answer_list), self.get_direction(answer['venue_id']), self.select_weather(
                    answer['venue_id'])
            else:
                self.view.valid_id()

    def get_direction(self, venue_id):
        """
        Opens google maps in a browser to show directions from location to the venue
        :param venue_id:
        :return:
        """
        url_map = 'https://www.google.com/maps/dir/?api=1&parameters'

        transport = self.view.get_transportmethod()
        venue = self.model.select_one(venue_id)
        destination = '{},{}'.format(venue['latitude'], venue['longitude'])
        req = self.model.select_req_acc_id(venue['requests_request_id'])
        origin = '{},{}'.format(req['latitude'], req['longitude'])
        # transport can be either 'driving' (default), 'walking', 'bicycling', 'transit'

        params = dict(
            origin=origin,
            destination=destination,
            units='metric',
            travelmode=transport

        )
        r = requests.get(url_map, params=params).url
        webbrowser.open(r)

        return self.quit_or_restart()


