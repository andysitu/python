from test import *

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

def find_empty_p_areas(data):
    p_area = {}
    for aisle in range(1, 28):
        if aisle != 27:
            p_area[aisle] = {}
            for row in range(1, 24):
                p_area[aisle][row] = {}
                for level in range(1, 4):
                    p_area[aisle][row][level] = False
        else:
            p_area[aisle] = {}
            for row in range(1, 18):
                p_area[aisle][row] = {}
                for level in range(1, 4):
                    p_area[aisle][row][level] = False
    loc_reg = re.compile("USLA\.(?P<area>PH|PA)\.(?P<aisle>\d+)\.(?P<row>\d+)\.(?P<level>\d+)")

    for item_code in data:
        loc = data[item_code]["location code"]
        results = re.match(loc_reg, loc)
        if results:
            area = results.group('area')
            aisle = int(results.group('aisle'))
            row = int(results.group('row'))
            level = int(results.group('level'))
            p_area[aisle][row][level] = True

    for aisle, a in p_area.items():
        for row, r in a.items():
            for level, l, in r.items():
                if l == False:
                    print(aisle, ", ",  row, ", ", level)

# open_py_data(find_empty_p_areas)

def p_areas_with_one_item(data):
    p_area = {}
    for aisle in range(1, 28):
        if aisle != 27:
            p_area[aisle] = {}
            for row in range(1, 24):
                p_area[aisle][row] = {}
                for level in range(1, 4):
                    p_area[aisle][row][level] = []
        else:
            p_area[aisle] = {}
            for row in range(1, 18):
                p_area[aisle][row] = {}
                for level in range(1, 4):
                    p_area[aisle][row][level] = []
    loc_reg = re.compile("USLA\.(?P<area>PH|PA)\.(?P<aisle>\d+)\.(?P<row>\d+)\.(?P<level>\d+)")

    for item_code in data:
        item_type = data[item_code]["item code"]
        loc = data[item_code]["location code"]
        results = re.match(loc_reg, loc)
        if results:
            area = results.group('area')
            aisle = int(results.group('aisle'))
            row = int(results.group('row'))
            level = int(results.group('level'))
            if item_code not in p_area[aisle][row][level]:
                p_area[aisle][row][level].append(item_code)

    for aisle, a in p_area.items():
        for row, r in a.items():
            for level, l, in r.items():
                if len(l) == 1:
                    print(aisle, ", ",  row, ", ", level)

# open_py_data(p_areas_with_one_item)

def get_p_customer_code(data):
    p_cust_dict = {}
    loc_reg = re.compile("USLA\.(?P<area>PH|PA)\.(?P<aisle>\d+)\.(?P<row>\d+)\.(?P<level>\d+)")

    for item_code in data:
        cust_id = data[item_code]['customer id']
        loc = data[item_code]["location code"]
        num_items = data[item_code]["item quantity"]
        results = re.match(loc_reg, loc)
        if results:
            if cust_id not in p_cust_dict:
                p_cust_dict[cust_id] = num_items
            else:
                p_cust_dict[cust_id] += num_items
    sorted_list = sorted(p_cust_dict.items(), key=operator.itemgetter(1))
    sorted_list = sorted_list[::-1]
    for customer_id, item_num in sorted_list:
        print(customer_id, item_num)

# open_py_data(get_p_customer_code)

def get_s_customer_code(data):
    s_cust_dict = {}
    loc_reg = re.compile("USLA\.(?P<area>S|H)\.(S|H)(?P<aisle>\d+)\.(?P<row>\d+)\.(?P<level>\d+)")
    # loc_reg2 = re.compile("USLA\.(?P<area>S|H)\.(?P<aisle>\d+)\.(?P<row>\d+)\.(?P<level>\d+)")

    for item_code in data:
        cust_id = data[item_code]['customer id']
        loc = data[item_code]["location code"]
        num_items = data[item_code]["item quantity"]
        results = re.match(loc_reg, loc)
        # results2 = re.match(loc_reg2, locx)
        if results:
            if cust_id not in s_cust_dict:
                s_cust_dict[cust_id] = num_items
            else:
                s_cust_dict[cust_id] += num_items
    sorted_list = sorted(s_cust_dict.items(), key=operator.itemgetter(1))
    sorted_list = sorted_list[::-1]
    for customer_id, item_num in sorted_list:
        print(customer_id, item_num)

open_py_data(get_s_customer_code)