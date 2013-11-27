#!/usr/bin/env python
# -*- coding: utf8 -*-

# 1 ülesanne
tekst = raw_input("Palun sisestage tekst: ")

if tekst == str(tekst.lower()) and any(c.isdigit() for c in tekst):
	print "Väiketähed ja numbrid"
elif tekst == str(tekst.lower()):
	print "Väiketähed ja numbriteta"
elif tekst == str(tekst.upper()) and any(c.isdigit() for c in tekst):
	print "Suurtähed ja numbrid" 
elif tekst == str(tekst.upper()):
	print "Suurtähed ja numbriteta"
elif any(c.isdigit() for c in tekst):
	print "Suur-väiketähed ja numbrid"
else:
	print "Suur-väiketähed ja numbriteta"

print
# 2 ülesanne
arv1 = int(raw_input("Sisestage esimene arv: "))
arv2 = int(raw_input("Sisestage teine arv: "))
muut = 3
def arvud(arv1, arv2, muut):
	if arv1 > arv2:	
		arv1,arv2 = arv2,arv1	
		arv1 = arv1 + (muut - (arv1 % muut))
		return [i for i in range(arv1, arv2, muut)]

tulemus = [i for i in range((arv1 + (muut - (arv1 % muut))),arv2, muut)]
print "Nende arvude vahel on " + str(len(tulemus)) + " arvu, mis jaguvad 3-ga"

