import os
import shutil
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

# Returns html containers that relate to the provided form name 
def get_relevant_html(form_name):

    url = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow=0&criteria=formNumber&value="+'+'.join(form_name.split())+"&isDescending=false"

    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("tr", {'class': ['even', 'odd']})

    relevant_rows = []

    for cur in containers:
        if cur.td.a.text == form_name:
            relevant_rows.append(cur)

    return relevant_rows

# Parses html and returns an object with info about the form
def create_info_object(html):
    form_object = {
        "form_number": "",
        "form_title": "",
        "min_year": "",
        "max_year": ""
    }

    years_lst = []

    for row in html:

        if len(years_lst) > 0:
            form_object["form_number"] = row.find("td", {"class": "LeftCellSpacer"}).text.strip()
            form_object["form_title"] = row.find("td", {"class": "MiddleCellSpacer"}).text.strip()
        
        years_lst.append(row.find("td", {"class": "EndCellSpacer"}).text.strip())

    
    form_object["min_year"] = years_lst[-1]
    form_object["max_year"] = years_lst[0]

    return form_object

# Parses html and returns object with a key:value pair of 'year':'pdf_link'
def create_pdf_object(html, years_list):
    pdf_object = {}

    for row in html:
        cur_year = row.find("td", {"class": "EndCellSpacer"}).text.strip()
        pdf_link = row.find("td", {"class": "LeftCellSpacer"}).a["href"]

        if cur_year in years_list:
            pdf_object[cur_year] = pdf_link
            
    return pdf_object

# Downloads pdfs for each year and saves them in seperate directory
def download_pdfs(pdf_object, form_name):
    path = os.getcwd()
    folder =  path + '/'+form_name
    try:
        os.mkdir(folder)
    except FileExistsError:
        shutil.rmtree(folder)
        os.mkdir(folder)



    for year,pdf_link in pdf_object.items():
        response = uReq(pdf_link)
        file = open(folder+"/"+form_name+" - "+year+".pdf", 'wb')
        file.write(response.read())
        file.close()