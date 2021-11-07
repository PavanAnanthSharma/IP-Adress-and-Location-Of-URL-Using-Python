import socket
from ip2geotools.databases.noncommercial import DbIpCity
url = input("Enter the URL you want to track : ")
ip = socket.gethostbyname(url)
reponse = DbIpCity.get(ip, api_key = 'free')
print("IP: ", ip)
print("City: ",response.city)
print("Region: ",response.region)
print("Coutry: ",response.country)
