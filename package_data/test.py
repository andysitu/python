import os, shelve, re

def open_py_data(func):
    loc_data = {}

    try:
    # Tries to open py_data folder, which is where the converted data should be stored.
        os.chdir('py_data')
    except (FileNotFoundError):
    # If the folder is not found, then it'll create the directory.
        os.chdir('..')
        os.mkdir('py_data')
        os.chdir('py_data')


##    file = open(py_filename, 'r')
##    t = file.read()
##    print(type(t))
##    file.close()

    try:
        db = shelve.open('newest')

        data = db["data"]

        func(data)
    except KeyError as e:
        print("ERROR: " + str(e))
        return 1

    db.close()

# s = "USLA.A.S01.001.001"
# loc_re = re.compile("\.")
#
# t = loc_re.split(s)
# print(t, s)

# print(re.compile("\b[A-Z]{2,}\b"))

def count_products(data):
    num_items = 0
    for item_code in data:
        num_items += data[item_code]["item quantity"]
    print("TOTAL # OF ITEMS: ", num_items)

# open_py_data(count_products)

def count_products_by_location(data):
    items_list = {}
    loc_reg = re.compile("\.")
    for item_code in data:
        loc_list = loc_reg.split(data[item_code]["location code"])
        area = loc_list[1]
        if area in items_list:
            items_list[area] += data[item_code]["item quantity"]
        else:
            items_list[area] = data[item_code]["item quantity"]
    for i in items_list:
        print(i, items_list[i])
    return items_list

# open_py_data(count_products_by_location)

def count_item_types(data):
    items_list = {}
    item_types = 0
    for item_code in data:
        item_type = data[item_code]["item code"]
        if item_type not in items_list:
            items_list[item_type] = True
            item_types += 1
    print("TOTAL # TYPES OF ITEMS: ", item_types)

# open_py_data(count_item_types)

def count_item_types_by_area(data):
    items_list = {}
    item_types = {}
    loc_reg = re.compile("\.")

    for item_code in data:
        loc_list = loc_reg.split(data[item_code]["location code"])
        area = loc_list[1]

        item_type = data[item_code]["item code"]
        if area not in items_list:
            items_list[area] = {}
        if item_type not in items_list[area]:
            items_list[area][item_type] = True
    for areas in items_list:
        print(areas, len(items_list[areas].keys()))

# open_py_data(count_item_types_by_area)

def find_empty_s_areas(data):
    s_area = {}

    # Create areas and mark them all with False
    for aisle in range(1, 57):
        s_area[aisle] = {}
        if aisle <= 10:
            for row in range(1, 34):
                s_area[aisle][row] = {}
                for level in range(1, 7):
                    s_area[aisle][row][level] = False
        else:
            for row in range(1, 43):
                s_area[aisle][row] = {}
                if row >= 27 and row <= 42:
                    for level in range(1, 6):
                        s_area[aisle][row][level] = False
                else:
                    for level in range(1, 7):
                        s_area[aisle][row][level] = False

    loc_reg = re.compile("USLA\.(?P<area>S|H)\.(S|H)(?P<aisle>\d+)\.(?P<row>\d+)\.(?P<level>\d+)")
    loc_reg2 = re.compile("USLA\.(\w+)\.([\w\d]+)\.(\d+)\.(\d+)")
    # for item_code in data:
    #     loc_list = loc_reg.split(data[item_code]["location code"])
    #     area = loc_list[1]
    #     if area in items_list:
    #         items_list[area] += data[item_code]["item quantity"]
    #     else:
    #         items_list[area] = data[item_code]["item quantity"]
    # for i in items_list:
    #     print(i, items_list[i])

    for item_code in data:
        loc = data[item_code]["location code"]
        results = re.match(loc_reg, loc)
        if results:
            area = results.group('area')
            aisle = int(results.group('aisle'))
            row = int(results.group('row'))
            level = int(results.group('level'))
            s_area[aisle][row][level] = True

    for aisle, a in s_area.items():
        for row, r in a.items():
            for level, l, in r.items():
                if l == False:
                    print(aisle, ", ",  row, ", ", level)


# open_py_data(find_empty_s_areas)

def find_num_customers(data):
    cust_list = {}
    cust_num = 0
    for item_code in data:
        cust_id = data[item_code]['customer id']
        if cust_id not in cust_list:
            cust_list[cust_id] = True
            cust_num += 1
    print("# CUSTOMERS", cust_num)

# open_py_data(find_num_customers)

import operator

def find_top_customers_type(data):
    item_list = {}
    cust_list = {}
    for item_code in data:
        item_type = data[item_code]["item code"]
        cust_id = data[item_code]['customer id']
        if item_type not in item_list:
            item_list[item_type] = cust_id
    for item_id, cust_id in item_list.items():
        if cust_id not in cust_list:
            cust_list[cust_id] = 1
        else:
                cust_list[cust_id] += 1
    sorted_list = sorted(cust_list.items(), key=operator.itemgetter(1))
    sorted_list = sorted_list[::-1][0:10]
    print("TOP 10 CUSTOMERS BY ITEM TYPE")
    for x, y in sorted_list:
        print(x, y)

# open_py_data(find_top_customers_type)

def find_top_customers_item(data):
    item_list = {}
    cust_list = {}
    for item_code in data:
        item_type = data[item_code]["item code"]
        cust_id = data[item_code]['customer id']
        num_items = data[item_code]["item quantity"]
        if item_type not in item_list:
            item_list[item_type] = (cust_id, num_items)
        else:
            tup = item_list[item_type]
            item_list[item_type] = (cust_id, tup[1] + num_items)
    for item_id, tup in item_list.items():
        cust_id = tup[0]
        item_count = tup[1]
        if cust_id in cust_list:
            cust_list[cust_id] += item_count
        else:
            cust_list[cust_id] = item_count
    sorted_list = sorted(cust_list.items(), key=operator.itemgetter(1))
    sorted_list = sorted_list[::-1][0:10]
    print("TOP 10 CUSTOMERS BY ITEM COUNT")
    for x, y in sorted_list:
        print(x, y)

# open_py_data(find_top_customers_item)

