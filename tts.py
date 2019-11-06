#!/usr/bin/python
# coding:utf-8
import sys, getopt, os
#audio filename and identifier
Code = {'1': 'satu.mp3',
	'2': 'dua.mp3',
	'3': 'tiga.mp3',
	'4': 'empat.mp3',
	'5': 'lima.mp3',
	'6': 'enam.mp3',
	'7': 'tujuh.mp3',
	'8': 'delapan.mp3',
	'9': 'sembilan.mp3',
	'10': 'sepuluh.mp3',
	'11': 'sebeleas.mp3',
	'100': 'seratus.mp3',
	'belas': 'belas.mp3',
	'puluh': 'puluh.mp3',
	'ratus': 'ratus.mp3',}
	
bilangan = int(input("masukan bilangan: "))
print(bilangan)
dir = ''

if(bilangan < 12):
	file = dir + Code[str(bilangan)]
	os.system('mpg321 "'+file+'"')
if(bilangan > 11) & (bilangan < 20):
	file = dir+Code[str(bilangan%10)]
	os.system('mpg321 "'+file+'"')
	file = dir+Code['belas']
	os.system('mpg321 "'+file+'"')
if(bilangan > 19) & (bilangan < 100):
	file = dir+Code[str(bilangan/10)]
	os.system('mpg321 "'+file+'"')
	file = dir+Code['puluh']
	os.system('mpg321 "'+file+'"')
	if(bilangan%10 != 0):
		file = dir+Code[str(bilangan%10)]
		os.system('mpg321 "'+file+'"')
if(bilangan > 99) & (bilangan < 999):
	a = bilangan % 100
	if(bilangan/100 == 1):
		file = dir+Code['100']
		os.system('mpg321 "'+file+'"')
	else:
		file = dir+Code[str(bilangan/100)]
		os.system('mpg321 "'+file+'"')
		file = dir+Code['ratus']
		os.system('mpg321 "'+file+'"')
	if(bilangan%100 != 0):
		if(a < 12):
			file = dir+Code[str(a)]
			os.system('mpg321 "'+file+'"')
		elif(a > 11 & a < 100):
			if((a/10) > 1):
				file = dir+Code[str(a/10)]
				os.system('mpg321 "'+file+'"')
				file = dir+Code['puluh']
				os.system('mpg321 "'+file+'"')
			if(a%10 != 0):
				file = dir+Code[str(a%10)]
				os.system('mpg321 "'+file+'"')
			else:
				file = dir+Code[str(a%10)]
				os.system('mpg321 "'+file+'"')
				file = dir+Code['belas']
				os.system('mpg321 "'+file+'"')