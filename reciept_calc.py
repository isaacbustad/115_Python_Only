# recipt book
# every index is an integer
# indexes start at 0


# list of all the items bought
# index 0 in each list corisponds to item x price x count
# string list of product names
itemLst = ["Apple fruit","Bannna", "Orramg", "Chaqueta"]

# list of all item prices
# list of float values
priceLst = [.97,.65,.8,49.99]

# list of all item ammounts
# list integers / count
amtLst = [5.0,4.0,3.0,2.0]

# Zero input method
# calculates entire recipt
def calc_recipt():
    # the current total all lines
    total_all_lines = 0

    # get the total spent on each item
    for i in range(len(itemLst)):
        # calculate the total spent on each item
        total_all_lines += calc_recipt_line(priceLst[i], amtLst[i], itemLst[i])

    # return the total spent on all items
    return total_all_lines

# calculate a single of a recipt based on the input
def calc_recipt_line(price, amt, item):
    ret_total = amt * price

    #return the calculated line total
    return ret_total

# array input




# calculates entire recipt
def calc_recipt(a_item_lst = itemLst, a_amt_lst = amtLst, a_priceLst = priceLst):
    # the current total all lines
    total_all_lines = 0
    # used to store lines of the recipt
    total_line_str = ""

    # get the total spent on each item
    for i in range(len(a_item_lst)):
        # calculate the total spent on each item
        # price, amt, item
        total_all_lines += calc_recipt_line(a_priceLst[i], a_amt_lst[i], a_item_lst[i])

    # new logic or method call here
    for x in range(len(a_item_lst)):
        # append 1 full line line to print
        total_line_str += a_item_lst[x] + ": " + str(a_priceLst[x]) + "-- " + str(a_amt_lst[x]) + "-- " + str(calc_recipt_line(a_priceLst[x], a_amt_lst[x], a_item_lst[x])) + "\n"
    print(total_line_str)


    # return the total spent on all items
    print("is running")
    return total_all_lines
## function test calls
print(calc_recipt(itemLst,amtLst,priceLst))