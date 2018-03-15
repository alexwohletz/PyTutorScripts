def minmp(filename, compound_formula):
    """(str, str) -> (str, int)
    When passed a filename with a listing of elements 
    and properties and a compound_formula. Returns a 
    tuple where the first element is the lowest melting point 
    element in the compound and the second element is it's 
    corresponding melting point.
    >>>minmp("elements.txt", "K1Fe4")
    'K', 336
    >>>minmp("elements.txt", "Fe6Cr1")
    'Fe', 1811

    this is the file:
    <html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;"># This file lists several elements by symbol and their melting point
# in Kelvin and density in grams per cubic centimeter.
# Source: https://en.wikipedia.org/wiki/Chemical_element
Element    Melt. Pt.    Density
K    336    0.862
Ca    1115    1.55
Sc    1814    2.985
Ti    1941    4.506
V    2183    6.0
Cr    2180    7.19
Mn    1519    7.21
Fe    1811    7.874
Co    1768    8.90
Ni    1728    8.908
Cu    1357    8.96
Zn    692    7.14
END</pre></body></html>
    """


import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.angstromsciences.com/melting-points-of-elements-reference"
page = requests.get(url)
soup = BeautifulSoup(page.content)
table = soup.find("tbody")

elm_dict = {}
throwaway = []
for i in table.findAll("td"):
    text = i.get_text()

    if len(text) <= 2 and text.isalpha():
        elm_dict[text] = throwaway
        throwaway = []
    else:
        throwaway.append(text)


with open('output.csv', 'w', newline='') as csvfile:
    sw = csv.writer(csvfile, delimiter=',')

# write header row then loop
    sw.writerow(['element', 'number', 'melt K', 'melt C', 'melt F', 'name'])
    for key in elm_dict:
        sw.writerow([key] + elm_dict[key])
