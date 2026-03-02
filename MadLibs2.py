# Array of testable objects
libs_arr = ["firstlib"]
# blank symbol
blank_sym = "___"

# mad libs methods
def Madlib(a_str = "at the large ___" ):
    arr_split_string = a_str.split()
    my_strings = ["apple", "banana", "cherry"]

    #arrays go 0,1,2,3,4,5
    idx = 0

    for i in range(len(arr_split_string)):
        if arr_split_string[i].strip() == blank_sym:
            print("hi")
            arr_split_string[i]=my_strings[idx]

            idx += 1
    return " ".join(arr_split_string)


print(Madlib())