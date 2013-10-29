#!/usr/bin/env python
# -*- coding: utf8 -*-

# kahe arvu keskmine

def keskmine():
        arvud = (3544,624)
        keskmine = sum(arvud)/float(len(arvud))
        return keskmine
print str(keskmine())

print "___________________________________"

# fibonacci

def fjada():
    arv = 65
    esimene, teine = 0, 1
    while esimene<arv:
        print esimene,
        esimene, teine = teine, esimene+teine

fjada ()
print ""
print "___________________________________"

# ruutvõrrand

def ruutfn():
        a = 1
        b = -5
        c = -6
        print ""
        juur = (b*b)-4*(a*c)
        ac = 4*(a*c)
        bb = b*b
        a2 = a*2
        if juur < ac:
                print "Lahendid puuduvad!"
        else:
                ruutjuur = juur**.5
                x1=-(float(b))+ruutjuur
                x2=-(float(b))-ruutjuur
                x1=float(x1)/float(a2)
                x2=float(x2)/float(a2)
                print "Ruutvõrrandi lahendid on:"
                print [x1,x2]


ruutfn ()


