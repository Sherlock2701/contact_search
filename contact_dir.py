from trie_ds import Trie
import re


def check_input(input_string):
    """
    check if entered input is valid or not
    :param input_string:
    :return:
    """
    if len(input_string) > 50:  # check if length of name is less than 50 ir not
        return False
    else:
        return bool(re.match('[a-zA-Z\s]+$', input_string))  # check is input contains only chars and spaces


def add_input(input_string, trie):
    """
    Add valid input to contact list
    :param input_string:
    :return:
    """
    trie.insert(input_string) # add name to Trie


def get_serach_output(search_string, trie):
    """
    Get input as search string and return found contacts
    :param search_string:
    :return:
    """
    search_output = trie.query(search_string) #Search name by prefix in trie
    if len(search_output) > 0:
        return "\n".join(search_output)
    else:
        return "No contact with {} this name".format(search_string)


if __name__ == "__main__":
    name = ""
    t = Trie()
    while True:
        user_ip = input("1: Add contact 2:Search 3:Exit\n")
        if user_ip == "1":
            name = input("Enter Name:")
            if check_input(name):
                add_input(name, t)
            else:
                print("Enter valid name")
        elif user_ip == "2":
            name = input("Enter Name:")
            if check_input(name):
                print(get_serach_output(name, t))
            else:
                print("Enter valid name")
        elif user_ip == "3":
            print("Happy Searching")
            break
        else:
            print("Please enter valid input")
