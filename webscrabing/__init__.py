import os
import sys
from bs4 import BeautifulSoup
import requests
import re

	
def getRevenue(page_link):
	
	page_response = requests.get(page_link, timeout=5)
	#here, we fetch the content from the url, using the requests library
	page_content = BeautifulSoup(page_response.content, "html.parser")
	#we use the html parser to parse the url content and store it in a variable.
	all_tr=page_content.find_all('tr')
	all_tr_length=len(all_tr)
	#start to scan the HTML website code to find the required informations
	for i in range(0,all_tr_length):
		all_th_for_tr=all_tr[i].find_all("th")
		all_th_length=len(all_th_for_tr)
		for j in range(0,all_th_length):
			if(all_th_for_tr[j].text=="Revenue"):
				all_span_length=len(all_tr[i].find_all("span"))
				# money in DKK= ($ dollars * 647.20 ) /100
				return str(float("{0:.3f}".format((float(re.findall(r'\d+\.\d+',all_tr[i].find("span").text)[0]) *647.20)/100)))+ " " +all_tr[i].find("span").text.split()[1]

def getOperatingIncome(page_link):
	page_response = requests.get(page_link, timeout=5)
	#here, we fetch the content from the url, using the requests library
	page_content = BeautifulSoup(page_response.content, "html.parser")
	#we use the html parser to parse the url content and store it in a variable.
	all_tr=page_content.find_all('tr')
	all_tr_length=len(all_tr)
	#start to scan the HTML website code to find the required informations
	for i in range(0,all_tr_length):
		all_th_for_tr=all_tr[i].find_all('th')
		all_th_length=len(all_th_for_tr)
		for j in range(0,all_th_length):
			if(all_th_for_tr[j].text=="Operating income"):
				# money in DKK= ($ dollars * 647.20 ) /100
				return str(float("{0:.3f}".format((float(re.findall(r'\d+\.\d+',all_tr[i].find("span").text)[0]) *647.20)/100)))+ " " +all_tr[i].find("span").text.split()[1]
				
def getNetIncome(page_link):
	page_response = requests.get(page_link, timeout=5)
	#here, we fetch the content from the url, using the requests library
	page_content = BeautifulSoup(page_response.content, "html.parser")
	#we use the html parser to parse the url content and store it in a variable.
	all_tr=page_content.find_all('tr')
	all_tr_length=len(all_tr)
	#start to scan the HTML website code to find the required informations
	for i in range(0,all_tr_length):
		all_th_for_tr=all_tr[i].find_all('th')
		all_th_length=len(all_th_for_tr)
		for j in range(0,all_th_length):
			if(all_th_for_tr[j].text=="Net income"):
				# money in DKK= ($ dollars * 647.20 ) /100
				return str(float("{0:.3f}".format((float(re.findall(r'\d+\.\d+',all_tr[i].find("span").text)[0])*647.20)/100)))+ " " +all_tr[i].find("span").text.split()[1]

def getTotalAssets(page_link):
	page_response = requests.get(page_link, timeout=5)
	#here, we fetch the content from the url, using the requests library
	page_content = BeautifulSoup(page_response.content, "html.parser")
	#we use the html parser to parse the url content and store it in a variable.
	all_tr=page_content.find_all('tr')
	all_tr_length=len(all_tr)
	#start to scan the HTML website code to find the required informations
	for i in range(0,all_tr_length):
		all_th_for_tr=all_tr[i].find_all('th')
		all_th_length=len(all_th_for_tr)
		for j in range(0,all_th_length):
			all_span_for_th=all_th_for_tr[j].find_all("span")
			span_length=len(all_span_for_th)
			for z in range(0,span_length):
				if(all_span_for_th[z].text=="Total assets"):
					# money in DKK= ($ dollars * 647.20 ) /100
					return str(float("{0:.3f}".format((float(re.findall(r'\d+\.\d+',all_tr[i].find("td").find("span").text)[0]) *647.20)/100)))+ " " +all_tr[i].find("td").find("span").text.split()[1]
					
def getTotalEquity(page_link):
	page_response = requests.get(page_link, timeout=5)
	#here, we fetch the content from the url, using the requests library
	page_content = BeautifulSoup(page_response.content, "html.parser")
	#we use the html parser to parse the url content and store it in a variable.
	all_tr=page_content.find_all('tr')
	all_tr_length=len(all_tr)
	#start to scan the HTML website code to find the required informations
	for i in range(0,all_tr_length):
		all_th_for_tr=all_tr[i].find_all('th')
		all_th_length=len(all_th_for_tr)
		for j in range(0,all_th_length):
			all_span_for_th=all_th_for_tr[j].find_all("span")
			span_length=len(all_span_for_th)
			for z in range(0,span_length):
				if(all_span_for_th[z].text=="Total equity"):
					# money in DKK= ($ dollars * 647.20 ) /100
					return str(float("{0:.3f}".format((float(re.findall(r'\d+\.\d+',all_tr[i].find("td").find("span").text)[0]) *647.20)/100)))+ " " +all_tr[i].find("td").find("span").text.split()[1]
