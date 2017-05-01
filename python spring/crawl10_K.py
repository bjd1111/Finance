import os, csv, urllib2, time, re
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

##### Section 1: Extract the	URLs	from each	firms'	search	results	returned by	Edgar
os.chdir('C:\R_Python\ComputationalFinance_Python\code_CAR_4_25')
companyListFile = "CompanyTickerList.csv"  # a csv file with the list of company ticker symbols and names
IndexLinksFile = "IndexLinks10K.csv"  # a csv file (output of the current script) with the list of index links for each firm


def getIndexLink(companyListFile, FormType):
    csvFile = open(companyListFile, "r")
    csvReader = csv.reader(csvFile, delimiter=",")
    csvData = list(csvReader)

    Full_List = []
    for rowData in csvData[1:]:
        tickerCode = rowData[0]

        urlLink = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=" + tickerCode + "&type=" + FormType + "&dateb=&owner=exclude&count=100"
        pageRequest = urllib2.Request(urlLink)
        pageOpen = urllib2.urlopen(pageRequest)
        pageRead = pageOpen.read()

        soup = BeautifulSoup(pageRead, "html.parser")

        # Check if there is a table to extract / code exists in edgar database
        try:
            table = soup.find("table", {"class": "tableFile2"})
        except:
            print "No tables found or no matching ticker symbol for ticker symbol for" + tickerCode
            return -1

        docIndex = 1
        for row in table.findAll("tr"):
            cells = row.findAll("td")
            if len(cells) == 5:
                if cells[0].text.strip() == FormType:
                    link = cells[1].find("a", {"id": "documentsbutton"})
                    docLink = "https://www.sec.gov" + link['href']
                    description = cells[2].text.encode(
                        'utf8').strip()
                    filingDate = cells[3].text.encode('utf8').strip()
                    newfilingDate = filingDate.replace("-", "_")  ### <=== Change date format from 2012-1-1 to 2012_1_1 so it can be used as part of 10-K file names
                    docIndex = docIndex + 1
                    rows = [tickerCode, docIndex, docLink, description, filingDate, newfilingDate]
                    Full_List.append(rows)

    headers = ['Ticker', 'DocIndex', 'IndexLink', 'Description', 'FilingDate', 'NewFilingDate']
    data_links = pd.DataFrame(Full_List, columns=headers)
    data_links.to_csv(IndexLinksFile, index=False)

FormType = "10-K" ### <=== Change to other type if needed. For now, we extract "10-K" report

csvOutput = open(IndexLinksFile, "a+b")
csvOutput.truncate()

getIndexLink(companyListFile, FormType)

print "done!"

#### Section2:	Extracts the	URLs	for	each	firm's 10-K	reports

Form10qListFile = "List10K.csv"  # a csv file (output of the current script) with the list of 10-K links for each firm

def get10qLink(IndexLinksFile, FormType):
    csvFile = open(IndexLinksFile, "r")
    csvReader = csv.reader(csvFile, delimiter=",")
    csvData = list(csvReader)

    Full_List = []
    i = 1
    for rowData in csvData[1:]:
        Ticker = rowData[0]
        DocIndex = rowData[1]
        DocLink = rowData[2]
        Description = rowData[3]
        FileDate = rowData[4]
        NewFileDate = rowData[5]

        pageRequest = urllib2.Request(DocLink)
        pageOpen = urllib2.urlopen(pageRequest)
        pageRead = pageOpen.read()

        soup = BeautifulSoup(pageRead, "html.parser")

        # Check if there is a table to extract / code exists in edgar database
        try:
            table = soup.find("table", {"summary": "Document Format Files"})
        except:
            print "No tables found for link " + DocLink

        for row in table.findAll("tr"):
            cells = row.findAll("td")
            if len(cells) == 5:
                if cells[3].text.strip() == FormType:
                    link = cells[2].find("a")
                    FormLink= "https://www.sec.gov" + link['href']
                    FormName = link.text.encode('utf8').strip()
        rows = [Ticker, DocIndex, DocLink, Description, FileDate, NewFileDate, FormLink, FormName]
        Full_List.append(rows)

        nbDocPause = 10  ### <=== Type your number of documents to download in one batch
        nbSecPause = 1  ### <=== Type your pausing time in seconds between each batch
        if i % nbDocPause == 0:
            print i
            print "Pause for " + str(nbSecPause) + " second .... "
            time.sleep(float(nbSecPause))
        i = i + 1

    headers = ['Ticker', 'DocIndex', 'IndexLink', 'Description', 'FilingDate', 'NewFilingDate', 'Form10KLink', 'Form10KName']
    data_links = pd.DataFrame(Full_List, columns=headers)
    data_links.to_csv(Form10qListFile, index=False)

FormType = "10-K" ### <=== Change to other type if needed. For now, we extract "10-K" report

csvOutput = open(Form10qListFile, "a+b")
csvOutput.truncate()

get10qLink(IndexLinksFile, FormType)
print "done!"

##### Section 3: Downloads the	10-K	reports	as	HTML	files
SubPath = "./10-K report/HTML/"  # <===The subfolder with the 10-K files in HTML format
logFile = "DownloadLog10K.csv"  # a csv file (output of the current script) with the download history of 10-K forms

def dowmload10q(Form10qListFile, FormYears):
    csvFile = open(Form10qListFile, "r")
    csvReader = csv.reader(csvFile, delimiter=",")
    csvData = list(csvReader)

    Full_List = []
    i = 1
    for rowData in csvData[1:]:
        Ticker = rowData[0]
        DocIndex = rowData[1]
        IndexLink = rowData[2]
        Description = rowData[3]
        FilingDate = rowData[4]
        NewFilingDate = rowData[5]
        FormLink = rowData[6]
        FormName = rowData[7]

        for year in FormYears:
            if year in FilingDate:
                pageRequest = urllib2.Request(FormLink)
                pageOpen = urllib2.urlopen(pageRequest)
                pageRead = pageOpen.read()

                if ".htm" in FormName:
                    try:
                        htmlname = Ticker + "_" + DocIndex + "_" + NewFilingDate + ".htm"
                        htmlpath = SubPath + htmlname
                        htmlfile = open(htmlpath, 'wb')
                        htmlfile.write(pageRead)
                        htmlfile.close()
                        rows = [Ticker, DocIndex, IndexLink, Description, FilingDate, NewFilingDate, FormLink, FormName, htmlname, ""]
                    except:
                        rows = [Ticker, DocIndex, IndexLink, Description, FilingDate, NewFilingDate, FormLink, FormName, "not downloaded"]
                elif ".txt" in FormName:
                    try:
                        textname = Ticker + "_" + DocIndex + "_" + NewFilingDate + ".txt"
                        textpath = SubPath + textname
                        textfile = open(textpath, 'wb')
                        textfile.write(pageRead)
                        textfile.close()
                        rows = [Ticker, DocIndex, IndexLink, Description, FilingDate, NewFilingDate, FormLink, FormName, textname, ""]
                    except:
                        rows = [Ticker, DocIndex, IndexLink, Description, FilingDate, NewFilingDate, FormLink, FormName, "not downloaded"]
                else:
                    rows = [Ticker, DocIndex, IndexLink, Description, FilingDate, NewFilingDate, FormLink, FormName, "", "No form"]
                Full_List.append(rows)

        nbDocPause = 10  ### <=== Type your number of documents to download in one batch
        nbSecPause = 1  ### <=== Type your pausing time in seconds between each batch
        if i % nbDocPause == 0:
            print i
            print "Pause for " + str(nbSecPause) + " second .... "
            time.sleep(float(nbSecPause))
        i = i + 1
    headers = ['Ticker', 'DocIndex', 'IndexLink', 'Description', 'FilingDate', 'NewFilingDate', 'Form10KLink', 'Form10KName', "FileName", "Note"]
    data_links = pd.DataFrame(Full_List, columns=headers)
    data_links.to_csv(logFile, index=False)

if not os.path.isdir(SubPath):
    os.makedirs(SubPath)

FormYears = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']  ### <=== Type the years of documents you wish to download here, now we only
                                                ### download files for all these years listed.

csvOutput = open(logFile, "a+b")
csvOutput.truncate()

dowmload10q(Form10qListFile, FormYears)
print "done!"