#!/usr/bin/env python
# -*- coding: utf-8 -*-

import openpyxl, pprint

import os, sys
import shelve

def convert_excel_to_py(excel_filename, py_filename='excel_data'):
    dir_name = 'excel_files'
    os.chdir(dir_name)

    wb = openpyxl.load_workbook(excel_filename)

    sheet_names = wb.get_sheet_names()
    sheet_name = sheet_names[0]
    print('Sheet names: ', sheet_names)

    sheet = wb.get_sheet_by_name(sheet_name)
    print(sheet)

    excel_data = {}

    inv_ids = []

    for row in range(2, sheet.max_row + 1):
        inven_id =          sheet['A' + str(row)].value
        loc_code =          sheet['C' + str(row)].value
        avail_quantity =    sheet['AR' + str(row)].value
        item_quantity =     sheet['K' + str(row)].value
        shipping_quantity = sheet['AC' + str(row)].value
        customer_id =       sheet['AH' + str(row)].value

        # Encoded to perserve Chinese characters.
        item_name =         str((sheet['AN' + str(row)].value)).encode(sys.stdout.encoding, errors='replace')
        # print(item_name)
        last_out_date =     sheet['AK' + str(row)].value
        item_date =         sheet['J' + str(row)].value
        RCV_code =          sheet['N' + str(row)].value
        item_code =         sheet['AB' + str(row)].value

        excel_data[inven_id] = {
            'invetory id': inven_id,
            'location code': loc_code,
            'available quantity': avail_quantity,
            'shipping quantity': shipping_quantity,
            'item quantity': item_quantity,
            'customer id': customer_id,
            'item name': item_name,
            'last out date': last_out_date,
            'item date': item_date,
            'RCV code': RCV_code,
            'item code': item_code
        }

    try:
        os.chdir('../py_data')
    except (FileNotFoundError):
        os.chdir('..')
        os.mkdir('py_data')
        os.chdir('py_data')


    # save_file = open(py_filename + '.py', 'w')
    # save_file.write('data = ' + pprint.pformat(excel_data))
    # save_file.close()
    shelfFile = shelve.open(py_filename)
    shelfFile['data'] = excel_data
    shelfFile.close()

convert_excel_to_py('newest.xlsx', 'newest')
