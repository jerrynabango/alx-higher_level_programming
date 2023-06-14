#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda new_list: replace if search == new_list
                    else new_list, my_list))
