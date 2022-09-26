# Import the required modules
import xml.etree.ElementTree as Xet
import pandas as pd

# Defining the Column headers for CSV file
cols = ["FinInstrmGnlAttrbts.Id", "FinInstrmGnlAttrbts.FullNm", 
        "FinInstrmGnlAttrbts.ClssfctnTp", "FinInstrmGnlAttrbts.CmmdtyDerivInd", 
        "FinInstrmGnlAttrbts.NtnlCcy", "Issr"]
rows = []

# Parsing the XML file
xmlparse = Xet.parse('DLTINS_20210117_01of01.xml')
root = xmlparse.getroot()

# For loop to find & append attributes values in the rows
for i in root.findall('./FinInstrmGnlAttrbts'): 
	Id = i.find("Id").text
	FullNm = i.find("FullNm").text
	ClssfctnTp = i.find("ClssfctnTp").text
	CmmdtyDerivInd = i.find("CmmdtyDerivInd").text
	NtnlCcy = i.find("NtnlCcy").text

	rows.append({"FinInstrmGnlAttrbts.Id": Id,
				"FinInstrmGnlAttrbts.FullNm": FullNm,
				"FinInstrmGnlAttrbts.ClssfctnTp": ClssfctnTp,
				"FinInstrmGnlAttrbts.CmmdtyDerivInd": CmmdtyDerivInd,
				"FinInstrmGnlAttrbts.NtnlCcy": NtnlCcy})
            

for i in root.findall('./TermntdRcrd'):
    Issr = i.find("Issr").text

    rows.append({"Issr": Issr})

df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to csv
df.to_csv('output.csv')
