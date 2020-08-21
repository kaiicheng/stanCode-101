"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    # Compare the rank of certain name which already exists in the name_data dictionary.
    final_rank = int(rank)

    if name in name_data:
        if year in name_data[name]:
            old_rank = int(name_data[name][year])

            new_rank = int(final_rank)
            if new_rank <= old_rank:
                final_rank = new_rank
            else:  # 200 > 90
                final_rank = old_rank

    # Store new data into name_data list
    if name not in name_data:
        new_dict = {year: str(final_rank)}
        name_data[name] = new_dict
    else:
        name_data[name][year] = str(final_rank)

    # if name == 'Hellen':
    #     print(f'year: {year}, rank:{rank}, name:{name}')
    #     print(name_data[name])


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """
    with open(filename, 'r') as f:
        for line in f:
            if len(line) <= 5:
                year = str(line)
                year = str(year.strip())
            else:
                word_list = line.split(',')

                rank = word_list[0]
                name1 = word_list[1]
                name2 = word_list[2]

                rank = rank.strip()
                name1 = name1.strip()
                name2 = name2.strip()

                add_data_for_name(name_data, year, rank, name1)
                add_data_for_name(name_data, year, rank, name2)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}

    for i in range(len(filenames)):
        add_file(name_data, str(filenames[i]))
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """

    # Target with all lower characters
    target1 = target.lower()

    # Target with all upper characters
    ans = ''
    target2 = target.lower()
    for i in range(len(target2)):
        # print(i)   # a
        # if ch == target2[0]:
        if i == 0:
            first_ch = target2[0]
            first_ch = first_ch.upper()
            ans += first_ch
        else:
            ch = target2[i]
            ans += ch
    target2 = ans

    # Change name_data dictionary into list
    ls = []
    for key in name_data.keys():
        ls.append(key)

    # Create a new_ls list to store the name which containing the target word.
    new_ls = []
    # print(new_ls)
    for i in range(len(ls)):
        # print(ls[i])
        if target1 in ls[i]:
            new_ls.append(ls[i])
            # new_ls += str(ls[i])
        if target2 in ls[i]:
            new_ls.append(ls[i])
            # new_ls += str(ls[i])
        else:
            pass

    return new_ls


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
