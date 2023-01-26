import csv
'''with open('original_file.csv', 'r') as f:
    reader = csv.DictReader(f)
    with open('new_file.csv', 'w', newline='') as f:
        fieldnames = ['first_name']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            writer.writerow({'first_name': row['first_name']})'''

class file_sort:
    def __init__(self, file_name):
        self.file_name = file_name
        self.updated_format = []
        self.creating_new = ''

    def __str__(self):
        return f'this class can open, transform and write files'

    def open_file(self):
        with open(self.file_name) as file:
            self.updated_format = csv.DictReader(file)
            for row in self.updated_format:
                print(row['firstName'])

    def create_new_file(self):
        new_file = open('testing.csv', 'w')
        self.updated_format = new_file
        new_file.close()

    def get_first_name(self):
        
        for a in self.updated_format:
            self.updated_format.write(a)

    def get_last_name(self):
        with open(self.updated_format, 'a') as new_file:
            for a in self.updated_format[2]:
                self.updated_format.write(a)

    def get_first_part_email(self):
        pass



if __name__ == '__main__':
    file = file_sort('user_details.csv')
    file.open_file()
    print(file)
    print(file.updated_format)