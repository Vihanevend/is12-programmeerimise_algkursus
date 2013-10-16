#!/usr/bin/env python
# -*- coding: utf8 -*-

from random import randint

kuulid = ['s']*5 + ['m']*6 + ['v']*7

eri = 0
korrad = 0
for i in xrange(10000):
	min = 0
	max = len(kuulid)-1
	kuul = randint(min, max)
	kuul1 = kuulid[kuul]
	del kuulid[kuul]
	
	min = 0
	max = len(kuulid)-1
	kuul = randint(min, max)
	kuul2 = kuulid[kuul]
	del kuulid[kuul]
	
	if kuul1 == kuul2:
		eri = eri + 1
	korrad = korrad + 1
	
	kuulid = kuulid + [kuul1] + [kuul2]

print 100*eri/korrad

