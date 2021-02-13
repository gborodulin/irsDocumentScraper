from functions import get_relevent_html
from functions import create_object_from_html


user_input = input("Enter list of tax form names seperated by a comma:\n")
input_list = user_input.split(',')

form_list = []

for form_name in input_list:
    relevent_html = get_relevent_html(form_name.strip())
    form_object = create_object_from_html(relevent_html)
    form_list.append(form_object)


print({"form_list" : form_list})




