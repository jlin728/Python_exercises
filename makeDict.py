list1 = ["key1", "key2", "key3"]
list2 = ["val1", "val2", "val3"]

def makeDict(list1, list2):
    new_dict = {}
    new_dict = zip(list1, list2)

    print new_dict

makeDict(list1, list2)
