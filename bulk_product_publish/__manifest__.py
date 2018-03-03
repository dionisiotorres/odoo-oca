# -*- coding: utf-8 -*-
{
    'name': 'Bulk Products Publish',
    'version': '1.0',
    'category': 'Website',
    "author": "PPTS [India] Pvt.Ltd.",
    "website": "http://www.pptssolutions.com",
    'license': 'LGPL-3',
    'support': 'business@pptservices.com',
    'description':"""
                Publishing/Unpublishing bulk products  
                      """,
    'depends': ['base','product','sale','website_sale', 'website_mail','decimal_precision','mail','report'],
    'data': [
                'wizard/product_publish_wizard_view.xml',
                'views/product_publish_view.xml',         
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}