import requests

with open("web scrapper/valid_proxies.txt","r") as f :
    proxies = f.read().split("\n")

sites_to_check = ["https://timesofindia.indiatimes.com/city/delhi","https://timesofindia.indiatimes.com/city/mumbai"]

counter = 0

for site in sites_to_check :
    try :
        print("Using proxy : ${proxies[counter]}")
        res = requests.get(site,proxies={"http":proxies[counter],
                                         "https":proxies[counter]})
        print(res.status_code)
    except :
        print("Failed")
    finally :
        counter += 1