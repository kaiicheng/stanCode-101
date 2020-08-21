"""
File: Milestone1.py
Name: 
-----------------------
This file tests the milestone 1 for
our babyname.py project
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    # Compare the rank of certain name which already exists in the name_data dictionary.
    final_rank = int(rank)
    #print(name_data[name])
    # print(class(rank))   # Why this code cannot be executed?
    print(type(rank))
    # What's the class of rank?

    if name in name_data:
        if year in name_data[name]:
            old_rank = int(name_data[name][year])
            #print(old_rank)
            new_rank = int(final_rank)
            #print(new_rank)
            # Why equation still working when rank isn't int?
            # No ERROR without int(rank)
            # We can compare
            #字串比較 => 比第一個數字
            if new_rank <= old_rank:
                final_rank = new_rank
                # print(final_rank)
                # Input constant number cannot be changed? Like rank?
            else:   # 200 > 90
                final_rank = old_rank
                # print(final_rank)
    # print(final_rank)

    # Store new data into name_data list
    if name not in name_data:
        new_dict = {year: str(final_rank)}
        # new_dict = {}
        # new_dict[year] = rank
        name_data[name] = new_dict
    else:
        name_data[name][year] = str(final_rank)


# ------------- DO NOT EDIT THE CODE BELOW THIS LINE ---------------- #

def test1():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    print('--------------------test1----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test2():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test2----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test3():
    name_data = {'Kylie': {'2010': '57'}, 'Sammy': {'1980': '451', '1990': '90'}}
    add_data_for_name(name_data, '1990', '200', 'Sammy')
    print('-------------------test3-----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test4():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    add_data_for_name(name_data, '2000', '108', 'Kate')
    add_data_for_name(name_data, '1990', '200', 'Sammy')
    add_data_for_name(name_data, '1990', '90', 'Sammy')
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test4----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def main():
    args = sys.argv[1:]
    if len(args) == 1 and args[0] == 'test1':
        test1()
    elif len(args) == 1 and args[0] == 'test2':
        test2()
    elif len(args) == 1 and args[0] == 'test3':
        test3()
    elif len(args) == 1 and args[0] == 'test4':
        test4()


if __name__ == "__main__":
    main()
