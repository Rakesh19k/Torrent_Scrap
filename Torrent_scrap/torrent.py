import requests,os,json
from bs4 import BeautifulSoup
import pprint
import time


def torrent(no):
		url = ("https://www.torrentdownload.info/search?q=books&p="+str(no))

		if os.path.exists("torrent"+str(no)+".json"):
			file=open("torrent"+str(no)+".json","r")
			data=file.read()
			return data
		

		page = requests.get(url)
		soup = BeautifulSoup(page.text,"html.parser")



		time.sleep(3)
		
		main_div = soup.find_all("table", class_="table2" )
		trs = main_div[1].find_all("tr")
		books_list=[]
		
		for tr in trs[1:]:
			Books_dic={}
			td = tr.find("td", class_="tdleft")
			div = td.find("div", class_="tt-name").a.get_text()
			Books=div
		
			peer=tr.find("td",class_="tdleech").get_text()
			# print(peer)

			seeds=tr.find("td",class_="tdseed").get_text()
			# print(seeds)

			hash_key = tr.find("div",class_="tt-name").a["href"][1:41]
			
			size=tr.find_all("td",class_="tdnormal")
			size=size[1].get_text()


			Books_dic["Books_name"] = Books
			Books_dic["peer"]=peer
			Books_dic["seeds"]=seeds
			Books_dic["hash_key"]="magnet:?xt=urn:btih:"+hash_key
			Books_dic["size"]=size

			books_list.append(Books_dic)
			

		file=open("torrent"+str(no)+".json","w")
		data=json.dump(books_list,file)

		return books_list 


for no in range(1,21):
	pprint.pprint(torrent(no))