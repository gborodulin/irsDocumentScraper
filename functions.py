import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

def get_relevent_html(form_number):

    url = "https://apps.irs.gov/app/picklist/list/priorFormPublication.html?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow=0&criteria=formNumber&value="+'+'.join(form_number.split())+"&isDescending=false"

    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("tr", {'class': ['even', 'odd']})

    relevent_rows = []

    for cur in containers:
        if cur.td.a.text == form_number:
            relevent_rows.append(cur)

    return relevent_rows

def create_object_from_html(html):
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

