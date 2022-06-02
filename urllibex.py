import urllib.request
value = input("Please enter a Website Adress with https/http:\n")
url=urllib.request.urlopen(value)
print(url.geturl())
print(url.info())
header = url.info()
print(header.as_string())
print(url.getcod())
 
  
   