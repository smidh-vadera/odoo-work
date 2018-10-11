# -*- coding: utf-8 -*-

{
    'name': 'Work Location',
    'version': '1.1',
    'category': 'Human Resources',
    'summary': 'Enable user to assign worklocation for an employee',
    'description': "Enable user to assign worklocation for an employee per company or branch.",
    'author': "HashMicro",
    'website':"www.hashmicro.com",
    'maintainer': 'HashMicro',
    'depends': ['hr'],
    'data': [
        'views/hr_view.xml',
        'views/work_location.xml',
    ],    
    'installable': True,
    'application': False,
    
}