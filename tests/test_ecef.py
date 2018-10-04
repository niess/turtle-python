#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cturtle import Ecef

r = Ecef().from_geodetic(45., 3., 0.)
print r.to_geodetic()

u = Ecef().from_horizontal(45., 3., 0., 0.)
print u.to_horizontal(45., 3.)
