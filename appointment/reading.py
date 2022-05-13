import csv
import os

# filepath = 'input.csv'

filepath = os.path.join('app/static/csv/usainput.csv')
# filepath = os.path.join('input.csv')

class ReadWrite:
    data_list = []
    def __init__(self):
        pass

    def read_data(self):
        """ Read data csv file """

        with open(filepath) as csvfile:
            thereader = csv.DictReader(csvfile)
            for item in thereader:
                user_name = item['User Name']
                pass_word = item['Password']
                year = item['Year']
                month = item['Month']


                self.data_list.append({'User Name': user_name,
                                       'Password': pass_word,
                                       'Year': year,
                                       'Month': month
                                       })



# if __name__ == "__main__":
#     bot = ReadWrite()
#     bot.read_data()
