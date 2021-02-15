import os
from functions import get_relevant_html
from functions import create_pdf_object
from functions import download_pdfs

form_input = input("Enter Tax Form Name:\n")
form_name = form_input.strip()

years_input = input("Enter Range of Years (Separated by '-'):\n")

try:
    min_year = int(years_input.split('-')[0].strip())
    max_year = int(years_input.split('-')[-1].strip())
except ValueError:
    print("Input For Year Range Must Be Two Numbers Seperated by a '-' ")
    os._exit(0)

years_list_int = list( range(min_year , max_year+1))
years_list = [str(year) for year in years_list_int]

relevant_html = get_relevant_html(form_name)
if len(relevant_html) == 0:
    print('No Forms Were Found With That Name. Please Check Spelling')
    os._exit(0)

pdf_object = create_pdf_object(relevant_html, years_list)
if len(pdf_object) == 0:
    print('A Form Exists With That Name But No PDFs Were Available Within Those Years.')
else:
    download_pdfs(pdf_object, form_name)
    print('Completed. '+str(len(pdf_object))+' PDFs Were Downloaded.' )

    