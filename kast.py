#!/usr/bin/env python
# -*- coding: utf8 -*-

w = int(raw_input("Sisestage kasti kõrgus: "))
h = int(raw_input("Sisestage kasti laius: "))

y = 1

while y <= h:
        x = 1
        while x <= w:
                if (x + y) % 2 == 0:
					print "#",
                else:
					print "#",
                x = x + 1
        
        print
        y = y + 1
