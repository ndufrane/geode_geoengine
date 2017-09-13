# -*- coding: utf-8 -*-
# Copyright 2017 Nicolas Dufrane (Geode Sprl)
{'name': 'Geode custom Geospatial support for Odoo',
 'version': '10.0.1.0.0',
 'category': 'GIS',
 'author': "Geode SPRL",
 'license': 'AGPL-3',
 'website': 'http://www.opengeode.be',
 'depends': [
     'base_geoengine'
 ],
 'init_xml': [],
 'data': [
     'views/geode_geoengine_view.xml',
 ],
 'external_dependencies': {
     'python': ['shapely',
                'geojson'],
 },
 'qweb': ["static/src/xml/geoengine.xml"],
 'installable': True,
}
