#! python3

import openpyxl

excel_file_name = input('Please input name of the excel file: ')

try:
    wb = openpyxl.load_workbook(excel_file_name)
except (FileNotFoundError):
    print('Your file was not found.')
    exit()

exit_status = False

while not exit_status:
    inp = input("Please input a command. Type 'exit' to exit.")
    if inp == 'exit':
        exit_status = True