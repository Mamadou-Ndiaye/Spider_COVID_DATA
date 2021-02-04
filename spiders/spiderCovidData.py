import scrapy
from urllib import request

class SpiderCovidData(scrapy.Spider):
    name = 'africaCovidData'
    #start_urls = ['https://raw.githubusercontent.com/CodeForAfrica/covid19-in-africa/master/datasets/africa_historic_data.csv']
    start_urls = ['https://ourworldindata.org/coronavirus-source-data']
   

    def parse(self,response):
        items = dict()
        pays = ['senegal','mali','benin','burkina faso','gabon']
        body = response.css('.wp-block-column div div div a')
        urlCSV =""
        #liste = []
        for a in body:
            url=a.xpath('@href').get()
            if url.endswith(".csv"):
                urlCSV = url
                break
            continue
        # Retrieve the webpage as a string
        reponse = request.urlopen(urlCSV)
        csv = reponse.read()

        # Save the string to a file
        csvstr = str(csv).strip("b")

        lines = csvstr.split("\\n")
        #lignes = lines.split("\\n")
##        fcamers = open("CamersData.csv", "w")
##        fcamers.write(lines[0].replace('"','')+"\n")
##        for line in lines[1:]:
##            elts=line.split(",")
##            if len(elts)>2:
##                if elts[2].lower() in pays:
##                    fcamers.write(line+"\n")

##        fcamers.close()
        
        fsen = open("senegal.csv", "w")
        fmli = open("mali.csv", "w")
        fben = open("benin.csv", "w")
        fbur = open("burkina_faso.csv", "w")
        fgbn = open("gabon.csv", "w")
                 
        fsen.write(lines[0].replace('"','')+"\n")
        fmli.write(lines[0].replace('"','')+"\n")
        fben.write(lines[0].replace('"','')+"\n")
        fbur.write(lines[0].replace('"','')+"\n")
        fgbn.write(lines[0].replace('"','')+"\n")
        for line in lines[1:]:
            elts=line.split(",")
            if len(elts)>2:
                if elts[2].lower() == "senegal":
                    fsen.write(line+"\n")
                if elts[2].lower() == "mali":
                    fmli.write(line+"\n")
                if elts[2].lower() == "benin":
                    fben.write(line+"\n")
                if elts[2].lower() == "burkina faso":
                    fbur.write(line+"\n")
                if elts[2].lower() == "gabon":
                    fgbn.write(line+"\n")
        fsen.close()
        fben.close()
        fgbn.close()
        fbur.close()
        fmli.close()
        
       
       
        
