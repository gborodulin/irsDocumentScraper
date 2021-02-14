from functions import get_relevant_html
from functions import create_object_from_html


user_input = input("Enter List of Tax Form Names (Seperated by ','):\n")
input_list = user_input.split(',')

form_list = []

for form_name in input_list:
    relevant_html = get_relevant_html(form_name.strip())
    form_object = create_object_from_html(relevant_html)
    form_list.append(form_object)


print('Completed! Following Forms Were Found:')
print({"form_list" : form_list})




