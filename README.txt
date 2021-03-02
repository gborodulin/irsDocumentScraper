# Greg Borodulin

Written in Python 3.9.1

Using library BeautifulSoup (pip install bs4)

## Utility 1
### Taking a list of tax form names, searching the website and returning some informational results

Within the repository, run the following in the command line:
python3 utility_1.py 

You will be asked to enter a list of tax form names (case sensitive) separated by a comma (','). 
*Example: Form W-2,Publ 1,Form 56-F*

The utility will print the results to the console in json format

## Utility 2
### Taking a tax form name and a range of years, downloads all PDFs available within that range

Within the repository, run the following in the command line:
python3 utility_2.py 

You will be asked to enter a tax form name (case sensitive).
*Example: Form W-2*

If the form exists, you will then be asked to enter a range of years separated by a dash ('-').
*Example: 2018-2020*

The utility will create a folder in the repository with the same name as the tax form and download all PDFs within the given range to the folder.


