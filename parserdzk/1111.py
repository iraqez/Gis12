#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Juergen Weichand'

from owslib.wms import WebMapService
bboxw =

wms = WebMapService('http://212.26.144.110/geowebcache/service/wms', version='1.1.1')

wms.getfeatureinfo(
    layers='kadastr',
    query_layers='kadastr',
    feature_count='1',
    info_format='application/vnd.ogc.gml',
    srs='EPSG:900913',
)