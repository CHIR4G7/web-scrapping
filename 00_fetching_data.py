import requests

# function that will get the html content from the website and store it a new file.
def fetchAndSaveToFile(url,path) :
    r = requests.get(url)
    with open(path,"w") as f :
        f.write(r.text)

url = "https://timesofindia.indiatimes.com/city/delhi"

fetchAndSaveToFile(url,"web scrapper/data/times.html")