#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cturtle import Map

map = Map(path="share/data/egm96.png")
print map.elevation(3.8, 45.3)
print map.node(0, 0)
map.create(nx=101, ny=101, x=(-100., 100.), y=(-100., 100.), z=(0, 256))
