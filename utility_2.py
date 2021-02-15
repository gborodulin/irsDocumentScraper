import os
from functions import get_relevant_html
from functions import create_pdf_object
from functions import download_pdfs

# Receive input for form name
form_input = input("Enter Tax Form Name:\n")
form_name = form_input.strip()

# Get relevant html for provided form name. If none exists, exit the program
relevant_html = get_relevant_html(form_name)
if len(relevant_html) == 0:
    print('No Forms Were Found With That Name. Please Check Spelling')
    os._exit(0)

# Get input for range of years and check to see if it's valid
years_input = input("Enter Range of Years (Separated by '-'):\n")
try:
    min_year = int(years_input.split('-')[0].strip())
    max_year = int(years_input.split('-')[-1].strip())
except ValueError:
    print("Input for Range of Years must be Two Numbers Seperated by a '-' ")
    os._exit(0)

# Create list of all possible years in given range and convert list to strings
years_list_int = list( range(min_year , max_year+1))
years_list = [str(year) for year in years_list_int]

# Get pdf links only for the years in the range. If some exist, download them to a folder
pdf_object = create_pdf_object(relevant_html, years_list)
if len(pdf_object) == 0:
    print('A Form Exists With That Name But No PDFs Were Available Within Those Years.')
else:
    download_pdfs(pdf_object, form_name)
    print('Completed. '+str(len(pdf_object))+' PDFs Were Downloaded.' )

    