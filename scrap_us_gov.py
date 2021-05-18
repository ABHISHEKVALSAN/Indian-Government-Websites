import requests
from bs4 import BeautifulSoup

def getUrl(ext):
	url="https://www.usa.gov"+str(ext)
	resp=requests.get(url)
	if resp.status_code==200:
		soup=BeautifulSoup(resp.text,'html.parser')
		sites =soup.findAll("section")
		for i in sites:
			heading=i.find("h3")
			try:
				if heading.text=="Website:":
					filename="tempUS.txt"
				       	f=open(filename,"a+")
					f.write(i.find("a")['href'])
					print i.find("a")['href']
					f.close()
			except:
				pass

def main(s):
	url="https://www.usa.gov/federal-agencies/"+str(s)
	resp=requests.get(url)
	if resp.status_code==200:
		soup=BeautifulSoup(resp.text,'html.parser')
		sites =soup.findAll("a",{"class":"url"})
		sites=sites[7:]
		for i in sites:
			getUrl(i['href']) 

if __name__=="__main__":
	s="abcdefghijklmnoprstuvw"
	for i in s:
		main(i)
