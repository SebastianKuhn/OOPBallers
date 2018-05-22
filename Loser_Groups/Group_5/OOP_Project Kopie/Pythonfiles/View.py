import pandas as pd
import webbrowser
import os

class View:

    def __init__(self):
        print('Welcome! \n'
              'To begin searching for venues and places near you, enter an address:')

    def back_to_start(self):
        """
        Print message displayed when you restart the program
        :return:
        """
        print("Welcome back to the start of the program! \n"
              "Please enter an address:")

    def get_ulocation(self):
        """
        Aquires the input for the users location
        :return:
        """
        ulocation = input()
        return ulocation

    def renew_ulocation(self):
        """
        ERROR MESSAGE if geocoding API return an error
        :return:
        """
        print("It seems like the address you entered could not be found. \n "
              "Optimally the format would be similar to 'Dufourstrasse 55 9000 St. Gallen'")

    def view_cat(self, categories):
        """
        Displays all categories and acquires user input for the chosen location.
        All known exceptions prevented.
        :param categories:
        :return:
        """
        for i in categories:
            print('{}. {}'.format(i['category_id'], i['category_name']))
        print("Which category are you interested in?")
        while True:
            try:
                user_input = int(input())
                while user_input > 22 or user_input < 1:
                    print("Your answer is supposed to be a number between 1 and 22.")
                    user_input = int(input())
            except ValueError:
                print("Please choose a Number [1-22].")
                continue
            else:
                return user_input
                break

    def get_transportmethod(self):
        """
        Acquires user input for a chosen transportmethod, only allows for driving, walking, bicycling or transit
        :return:
        """
        print("How would you like to travel to your destination? \n"
              "You have the following options: \n"
              "Driving, Walking, Bicycling or Transit (Public Transport)")
        while True:
            user_input = str.lower(input())
            if user_input == 'driving' or user_input == 'walking' or user_input == 'bicycling' or user_input == 'transit':
                return user_input
                break
            else:
                print("Please choose one of the following: \n"
                      "Driving, Walking, Bicycling or Transit")

    def getuFilter(self):
        """
        Acquires user input for the chosen sorting method: distance or rating. Also only allows for distance or rating
        :return:
        """
        print("How do you want to sort the results? \n"
              "Your options are: Distance or Rating")
        while True:
            user_input = str.lower(input())
            if user_input == 'distance' or user_input == 'rating':
                return 'venue.'+user_input
            else:
                print("Please choose between distance and rating.")

    def show_data(self, data):
        """
        Transforms the 'data' into a panda dataframe, which is then opened in a new browser window.
        :param data:
        :return:
        """
        df = pd.DataFrame(data)

        data_table = df.to_html(float_format=lambda x: '%6.2f' % x,
                                classes="table display")  # The to_html() method forces a html table border of 1 pixel. # I use 0 in my table so I change the html, since there is no # border argument in the to_html() method.
        data_table = data_table.replace('border="1"',
                                        'border="0"')  # I alson like to display blanks instead on nan. data_table = data_table.replace('nan', '')
        from urllib.request import pathname2url  # Python 3.x
        file = open('test.html', 'w+', encoding='latin-1')
        file.write(data_table)
        file.write(""""<style>
                table { border-collapse: collapse; border: 3px solid #eee; }
                table tr th:first-child { background-color: #eeeeee; color: #333; font-weight: bold }
                table thead th { background-color: #eee; color: #000; }
                tr, th, td { border: 1px solid #ccc; border-width: 2px 0 0 1px; border-collapse: collapse;
                padding: 3px; font-family: arial; font-size: 15px }</style>""")
        url = 'file:{}'.format(pathname2url(os.path.abspath('test.html')))
        webbrowser.open(url)
        file.close()

    def back(self):
        """
        NOT YET INCLUDED
        FOR FUNCTIONALITY: PORTRAY LIST AGAIN
        :return:
        """

        answer = input('If you wanna see the list again type "back"')
        return(answer)

    @staticmethod
    def print_select_one():
        """
        Prints the statement before selection of specific venue
        :return:
        """
        print("Please select the ID of the venue you are interested in: (Right-most column)")

    def select_one(self):
        """
        Acquires user input for venue ID. Only allows for integers
        :param self:
        :return:
        """
        while True:
            try:
                user_input = int(input())
            except ValueError:
                print("Please choose a Number.")
                continue
            else:
                return user_input
                break


    def get_row_number(self):
        """
        Acquires user input for amount of rows user wants to look at. only allows for integer and below 1000
        :param self:
        :return:
        """
        print("How many entries would you like to see?")
        while True:
            try:
                user_input = int(input())
                while user_input > 1000:
                    print("The maximum amount of listings at the moment is 1000. \n"
                          "Please choose a number below 1001")
                    user_input = int(input())
            except ValueError:
                print("Please choose a Number.")
            else:
                return user_input
                break

    def ascdesc(self):
        """
        Acquires user input for whether the list should be portrayed in ascending or descending order
        :param self:
        :return:
        """
        print("How do you want to sort the entries? \n"
              "Your options are: \n"
              "Low to High (ascending) \n"
              "High to low (descending)")
        while True:
            u_input = str.lower(input())
            if u_input == 'ascending':
                return 'asc'
            elif u_input == 'descending':
                return 'desc'
            else:
                print("Please choose between ascending or descending.")

    def end_or_back(self):
        """
        Final message, asks user for input on whether to quit or to restart
        :param self:
        :return:
        """
        print("Would you like to quit the program or start a new request? \n"
              "Your choices are: Quit and Restart")
        while True:
            u_input = str.lower(input())
            if u_input == 'quit':
                return 1
            elif u_input == 'restart':
                return 2
            else:
                print("Please choose between quit or restart.")

    def valid_id(self):
        """
        Error message if an invalid venue_id was chosen
        :param self:
        :return:
        """
        print("Please choose a valid ID.")

    def print_restart(self):
        """
        Print statement if program is restarted
        :param self:
        :return:
        """
        print("Welcome Back! \n"
              "Please type in an address:")

