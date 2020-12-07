import os
import datetime
import csv

class CsvHandler:
    def __init__(self, filename):
        self.filename = filename
    
    # Save it as csv file
    def store_into_csv(self, collections):
        relative_path = os.getcwd() + "/csv"
        _file_name = relative_path + "/{}.csv".format(self.filename)
        file_exists = os.path.isfile(_file_name)

        with open(_file_name, 'w') as _csvFile:
            _fieldnames = ['Subject', 'Start Date']
            writer = csv.DictWriter(_csvFile, fieldnames=_fieldnames)

            if not file_exists:
                writer.writeheader()
            writer.writerows(collections)
    
