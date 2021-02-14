from functions import get_relevant_html
from functions import create_pdf_object
from functions import download_pdfs

form_input = input("Enter Tax Form Name:\n")
form_name = form_input.strip()

years_input = input("Enter Range of Years (Separated by '-'):\n")
min_year = years_input.split('-')[0]
max_year = years_input.split('-')[-1]
years_list_int = list(range(int(min_year),int(max_year)+1))
years_list = [str(year) for year in years_list_int]


relevant_html = get_relevant_html(form_name)
pdf_object = create_pdf_object(relevant_html, years_list)
download_pdfs(pdf_object, form_name)

print('Completed! '+str(len(pdf_object))+' PDFs Were Downloaded.' )