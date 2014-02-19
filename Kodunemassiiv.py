#!/usr/bin/env python
# -*- coding: utf-8 -*-

filmid = [
['Bad Grandpa', 'huumor', '2013'],
['Forgetting Sarah Marshall', 'huumor', '2008'],
['Get Him to the Creek', 'huumor', '2010'],
['Titanic', 'kurb', '1992'],
['Avatar', 'ulme', '2011'],
['HDAigari seiklused', 'draama', '2014']
]

def lisa():
	nimi = raw_input("Pealkiri: ")
	zanr = raw_input("Zanr: ")
	aasta = raw_input("Aasta: ")
	
	filmid.append([nimi, zanr, aasta])
	
def eemalda():
	number = int(raw_input("Filmi number: "))	
	
	del filmid[number]

print "Algne andmebaas:"
		
def naita():
	for element in filmid:
		print element
naita()	

print

while True:
	valik = raw_input("Tee valik: " + "add - lisa | " + "rm - eemalda | " + " ls - näita listi | " + "või q - lõpeta. ")
	
	if valik == 'add':
		lisa()
	elif valik == 'ls':
		naita()
	elif valik == 'rm':
		eemalda()
	elif valik == 'q':
		print "Jällenägemiseni!"
		break
	else:
		print "Vigane valik, proovige uuesti."
