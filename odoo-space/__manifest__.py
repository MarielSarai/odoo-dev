# -*- coding: utf-8 -*-

{
        'name': 'Misión Espacial',
        'summary': """Odoo Inc. está intentando visitar la luna""",
        
        'description': """
        Modulo de Misión espacial que permite organizar la logistica.""",
        
        'author': 'Odoo',
    
        'website': 'https://www.odoo.com',
    
        'category': 'logistica',
        'version':'1.0',
    
        'depends': ['base'],
    
        'data': [

            'security/space_security.xml',
            'security/ir.model.access.csv',
            'views/space_views.xml',
            'views/space_menuitems.xml',
            
        ],
    
        'demo':[
            
            'demo/space_demo.xml'
        ],
}