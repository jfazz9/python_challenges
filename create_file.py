import csv
import os

class file_sort_csv:
    def __init__(self, file_name):
        self.file_name = file_name
        self.temp_open = ''
        self.file_reader = ''
        self.columns = []
        self.list_format = []

    def __str__(self):
        return f'this class can open, transform, write and delete files'

    def open_file(self):
        '''call on this function to open the file so that self.file_reader can contain 
        the DictReader class and iterate over each time'''
        try:
            self.temp_open = open(self.file_name)
            self.file_reader = csv.reader(self.temp_open, delimiter=',') 
            for row in self.file_reader:
                self.list_format.append(row)       
        except FileNotFoundError as fnfe:
            print("Error is: ", fnfe)

    def close_file(self):
        try:
            self.temp_open.close()
        except:
            print('didn\'t close anything')

    def add_column(self, col_no):
        '''choose a column that you want to add'''
        for row in self.list_format:    
            self.columns.append(row[col_no])


    def add_column_info_certain_criteria(self, column, splitter = '@'):
        pass

    def check_file(self):
        for row in self.file_reader:
            print(row)

    def check_variables(self):
        print(f'this is the current compilation {self.list_format}')
        print(f'columns of file {self.columns}')
        print(f'This is the file reader: {self.file_reader}')

    def add_all_info(self):
        with open('testing.csv', 'w', newline='') as file:
            headers = ['firstName', 'lastName', 'email']
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for row in self.file_reader:
                email_first = row['email'].split('@')
                writer.writerow({'firstName': row['firstName'], 'lastName': row['lastName'], 'email': email_first[0]})

    def break_columns(self, column_name):
        compiler = self.list_format.split(column_name)
 


    def write(self):
        with open('testing.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for row in self.list_format:
                writer.writerow(self.columns)


    def delete_file(self, filename):
        if os.path.exists(filename):
            os.remove(filename)


if __name__ == '__main__':
    file = file_sort_csv('user_details.csv')
    file.open_file()
    # file.check_variables()
    file.add_column(1)
    file.add_column(2)
    file.add_column(4)
    file.write()
    file.check_variables()










    