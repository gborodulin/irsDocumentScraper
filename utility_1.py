from functions import get_relevant_html
from functions import create_info_object

# Receive input from user and seperate each name into a list
user_input = input("Enter List of Tax Form Names (Seperated by ','):\n")
input_list = user_input.split(',')

# Get list of relevant html containers and create an info object for each provided form name
form_list = []

for form_name in input_list:
    relevant_html = get_relevant_html(form_name.strip())

    if len(relevant_html) > 0:
        form_object = create_info_object(relevant_html)
        form_list.append(form_object)
    

if len(form_list) > 0:
    print('Completed. Following Forms Were Found:\n', {"form_list" : form_list})
else:
    print('No Forms Were Found With Those Names. Please Check Spelling')
    




