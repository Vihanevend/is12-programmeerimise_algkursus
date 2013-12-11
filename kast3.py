#!/usr/bin/env python
# -*- coding: utf8 -*-

korlai = int(raw_input("Sisestage kasti kõrgus-laius: "))

x = 1
while x < korlai + 1:
        y = 0
        while y < x:
                print "#",
                y = y + 1
        y = korlai
        while x < y:
                print "#",
                y = y - 1
        print
        x = x + 1
