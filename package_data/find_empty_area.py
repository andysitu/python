from test import *

import excel_maker

def find_empty_s_areas(data):
    s_area = {}

    # Create areas and mark them all with False
    total_count = 0
    for aisle in range(1, 57):
        s_area[aisle] = {}
        if aisle <= 10:
            for row in range(1, 34):
                s_area[aisle][row] = {}
                for level in range(1, 7):
                    s_area[aisle][row][level] = False
                    total_count += 1
        else:
            for row in range(1, 43):
                s_area[aisle][row] = {}
                if row >= 27 and row <= 42:
                    for level in range(1, 6):
                        s_area[aisle][row][level] = False
                        total_count += 1
                else:
                    for level in range(1, 7):
                        s_area[aisle][row][level] = False
                        total_count += 1

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

    excel_dic = {"empty_s_area": []}
    empty_s_area = excel_dic["empty_s_area"]

    empty_count = 0
    empty_s_area.append(["Aisle", "Row", "Level"])
    for aisle, a in s_area.items():
        for row, r in a.items():
            for level, l, in r.items():
                if l == False:
                    row_list = [aisle, row, level,]
                    empty_s_area.append(row_list)
                    print(aisle, ", ",  row, ", ", level)
                    empty_count += 1
    empty_s_area.append(["total s places", total_count])
    empty_s_area.append(["empty s places", empty_count])

    excel_maker.make_excel_file(excel_dic, "empty_s_area.xlsx", "excel_data",)


# open_py_data(find_empty_s_areas)

def find_empty_p_areas(data):

    p_area = {}

    total_count = 0
    for aisle in range(1, 28):
        if aisle != 27:
            p_area[aisle] = {}
            for row in range(1, 24):
                p_area[aisle][row] = {}
                for level in range(1, 4):
                    p_area[aisle][row][level] = False
                    total_count += 1
        else:
            p_area[aisle] = {}
            for row in range(1, 18):
                p_area[aisle][row] = {}
                for level in range(1, 4):
                    p_area[aisle][row][level] = False
                    total_count += 1

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

    excel_dic = {"empty_p_area": []}
    empty_p_area = excel_dic["empty_p_area"]

    empty_count = 0
    empty_p_area.append(["Aisle", "Row", "Level"])
    for aisle, a in p_area.items():
        for row, r in a.items():
            for level, l, in r.items():
                if l == False:
                    row_list = [aisle, row, level,]
                    empty_p_area.append(row_list)
                    print(aisle, ", ",  row, ", ", level)
                    empty_count += 1
    empty_p_area.append(["total p places", total_count])
    empty_p_area.append(["empty p places", empty_count])

    excel_maker.make_excel_file(excel_dic, "empty_p_area.xlsx", "excel_data",)

# open_py_data(find_empty_p_areas)

def p_areas_with_one_item(data):

    p_area = {}

    total_count = 0
    for aisle in range(1, 28):
        if aisle != 27:
            p_area[aisle] = {}
            for row in range(1, 24):
                p_area[aisle][row] = {}
                for level in range(1, 4):
                    p_area[aisle][row][level] = []
                    total_count += 1
        else:
            p_area[aisle] = {}
            for row in range(1, 18):
                p_area[aisle][row] = {}
                for level in range(1, 4):
                    p_area[aisle][row][level] = []
                    total_count += 1

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

    excel_dic = {"p_area_1": []}
    p_area_1 = excel_dic["p_area_1"]

    one_count = 0
    p_area_1.append(["Aisle", "Row", "Level"])
    for aisle, a in p_area.items():
        for row, r in a.items():
            for level, l, in r.items():
                if len(l) == 1:
                    row_list = [aisle, row, level,]
                    p_area_1.append(row_list)
                    print(aisle, ", ",  row, ", ", level)
                    one_count += 1
    p_area_1.append(["total p places", total_count])
    p_area_1.append(["p places with 1 type of product", one_count])

    excel_maker.make_excel_file(excel_dic, "p_area_one_item.xlsx", "excel_data",)

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

    excel_dic = {"p_customer_count": []}

    p_cust_list = excel_dic["p_customer_count"]

    p_cust_list.append(["Customer ID", "# Items",])

    for customer_id, item_num in sorted_list:
        print(customer_id, ":", item_num)
        p_cust_list.append([customer_id, item_num,])

    excel_maker.make_excel_file(excel_dic, "p_customers.xlsx", "excel_data",)

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

    excel_dic = {"s_customer_count": []}

    s_cust_list = excel_dic["s_customer_count"]

    s_cust_list.append(["Customer ID", "# Items",])

    for customer_id, item_num in sorted_list:
        print(customer_id, ":", item_num)
        s_cust_list.append([customer_id, item_num,])

    excel_maker.make_excel_file(excel_dic, "s_customers.xlsx", "excel_data",)

# open_py_data(get_s_customer_code)