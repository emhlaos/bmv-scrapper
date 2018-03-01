"""
Copyright C.C.:
    Emiliano Hernandez Laos
    https://github.com/emhlaos/
    28/02/2018
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get("http://www.bmv.com.mx/es/emisoras/archivos-estadar-xbrl")
driver.execute_script(
    "document.querySelector('.submit').click();"
    )
tickers = []
dates = []
lndlinks = []
n=0
while True:
    try:
        print("Now trying tableCapital_next")
        element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#tableCapital_next")))
        print("tableCapital_next SUCCESSFUL now trying lnk-download")
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "lnk-download")))
        print("lnk-download SUCCESSFUL now trying sorting_1")

        for m in driver.find_elements_by_class_name("sorting_1"):
            tickers.append(m.text)
        print("sorting_1 SUCCESSFUL now trying RETRIEVE")

        blups = driver.find_elements_by_partial_link_text("Información Del Trimestre")
        dates = dates + [(n.text.split(" Trimestre ")[1].split(" Del ")[0]+"-"+n.text.split(" Año ")[1].split(" para ")[0]) for n in blups]
        lndlinks = lndlinks + ["http://www.bmv.com.mx/docs-pub"+n.get_attribute("href").split("docins=..")[1] for n in blups]
        print(dates[n],tickers[n],lndlinks[n])
        n = n + 10
        if 'disable' not in driver.find_element_by_css_selector("#tableCapital_next").get_attribute('class'):
            driver.execute_script("document.querySelector('#tableCapital_next').click();")
        else:
            print("Reached end...")
            break
    except Exception as args:
        print(args)


print(len(lndlinks),len(tickers))
matrix = {}
for n in range(len(lndlinks)):
    print("Adding... ["+tickers[n]+"]["+dates[n]+"]=",lndlinks[n])
    if tickers[n] in matrix.keys():
        matrix[tickers[n]][dates[n]] = lndlinks[n]
    else:
        matrix[tickers[n]] = {}
        matrix[tickers[n]][dates[n]] = lndlinks[n]
tops = []
for n in list(matrix.keys()):
    for m in list(matrix[n].keys()):
        if m not in tops:
            tops.append(m)
baby = open("babycaw.txt","w")
print("TICKER",tops)
baby.write("TICKER")
for n in tops: baby.write(","+n)
baby.write("\n")
for n in list(matrix.keys()):
    print(n,end="")
    baby.write(n)
    for m in tops:
        if m not in list(matrix[n].keys()):
            matrix[n][m] = ""
            print(",",end=" ")
            baby.write(",")
        else:
            print(","+matrix[n][m]+"",end=" ")
            baby.write(","+matrix[n][m]+"")
    print("")
    baby.write("\n")
baby.close()