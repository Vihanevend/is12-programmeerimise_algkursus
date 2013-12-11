#!/usr/bin/env python
# -*- coding: utf8 -*-

korgus = int(raw_input("Sisestage kasti kõrgus: "))
laius = int(raw_input("Sisestage kasti laius: "))

def kast(korgus, laius):
        y = 0
        while y < korgus:
                x = 0
                y = y + 1
                while x < laius:
                        print "#",
                        x = x + 1
                print
                        
print kast(korgus, laius)
