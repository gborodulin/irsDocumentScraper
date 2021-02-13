from functions import get_relevent_html
import os
from urllib.request import urlopen as uReq


def create_pdf_list(html, years_list):
    pdf_list = []

    for row in html:
        if row.find("td", {"class": "EndCellSpacer"}).text.strip() in years_list:
            pdf_link = row.find("td", {"class": "LeftCellSpacer"}).a["href"]
            pdf_list.append(pdf_link)

    return pdf_list

def download_pdfs(pdf_list, form_name,years_list):
    path = os.getcwd()
    folder =  path + '/'+form_name+' PDFs'
    os.mkdir(folder)

    for i in range(len(pdf_list)):
        response = uReq(pdf_list[i])
        file = open(folder+"/"+form_name+" - "+years_list[i]+".pdf", 'wb')
        file.write(response.read())
        file.close()


form_input = input("Enter tax form name:\n")
form_name = form_input.strip()
# form_name = 'Form W-2'

years_input = input("Enter range of years you want pdfs for *Example(2018-2020)*:\n")
min_year = years_input.split('-')[0]
max_year = years_input.split('-')[-1]
years_list_int = list(range(int(min_year),int(max_year)+1))
years_list = [str(year) for year in years_list_int]
years_list.reverse()
# years_list = ['2018', '2019', '2020']


relevent_html = get_relevent_html(form_name)
pdf_list = create_pdf_list(relevent_html, years_list)
download_pdfs(pdf_list, form_name, years_list)