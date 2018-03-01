"""
Copyright C.C.:
    Emiliano Hernandez Laos
    https://github.com/emhlaos/
    28/02/2018
"""

from urllib.request import urlopen
import os
from io import BytesIO
from zipfile import ZipFile

#LOAD FUNCTION:
currentdirectory = os.getcwd()
xbrldirectory = currentdirectory+"/xbrl"
if not os.path.exists(xbrldirectory): os.makedirs(xbrldirectory)
db = open(currentdirectory+"/babycaw.txt","r").read()
matrix = {}
rows = db.split("\n")
matrix["R.TIME"] = {}
n = 0
for t in rows[0].split(",")[1:]:
    matrix["R.TIME"][n] = t
    n=n+1
print(rows[1]," $$ ",rows[1].split(","))
for row in rows[1:]:
    columns = row.split(",")
    ticker = columns[0]
    matrix[ticker]={}
    n=0
    for cell in columns[1:]:
        matrix[ticker][n] = cell
        n=n+1

#DOWNLOAD INFO:
revenue_matrix = matrix
allread = []
stocks = list(matrix.keys())[1:]
n=len(list(matrix["R.TIME"].keys()))
print(n,"\n",stocks)
for stock in stocks:
    allread.append(stock)
    for m in range(n):
        print("Reading about "+stock)
        if ".zip" in matrix[stock][m]:
            with urlopen(matrix[stock][m]) as pzip:
                with ZipFile(BytesIO(pzip.read())) as zp:
                    for file in zp.namelist():
                        print(file)
                        print("Dowloading: "+ stock + "_" + matrix["R.TIME"][m] + ".json")
                        try:
                            pjson = open(xbrldirectory+"/" + stock + "_" + matrix["R.TIME"][m] + ".json", "wb")
                            pjson.write(zp.read(file))
                            pjson.close()
                        except Exception as args:
                            print(args,"you got {}%".format(len(allread)/n))
                            teencow = open(currentdirectory+"/teencaw.txt", "w")
                            for riadboe in allread:
                                teencow.write(riadboe,"\n")
                            allread=[]

        elif ".json"  in matrix[stock][m]:
            jsonurl = matrix[stock][m]
            jsonresp = urlopen(jsonurl)
            with urlopen(matrix[stock][m]) as pjson:
                try:
                    print("Downloading",stock + "_" + matrix["R.TIME"][m] + ".json")
                    tempjson = open(xbrldirectory+"/" + stock + "_" + matrix["R.TIME"][m] + ".json", "wb")
                    tempjson.write(pjson.read())
                    tempjson.close()
                except Exception as args:
                    print(args, "you got {}%".format(len(allread) / n),"ending at a json file JSUUN")
                    teencow = open(currentdirectory+"/teencaw.txt", "w")
                    for riadboe in allread:
                        teencow.write(riadboe, "\n")
                    allread = []
