# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle 
#
##############################################################################

{
    'name': 'Account Cancel Invoice/Journal Entries',
    'version': '14.0.1.0',
    'sequence': 1,
    'category': 'Generic Modules/Accounting',
    'description':
         """
 odoo app allow to cancel account invoice and cancel journal entries for specific users.
        
        Account cancel invoice 
        Account vendro bills 
        Cancel Journal entries 
        Odoo Cancel customer invoice
        Odoo cancel vendor bill
        odoo cancel supplier invoice
        odoo journal entries 
        odoo cancel moves 
        odoo cancel right account
        odoo account cancel rights
        odoo accounting move cancel rights
Account cancel rights
Odoo account cancel rights
For Helping allow user can cancel access right.
Odoo For Helping allow user can cancel access right.
this apps use to allow users are cancel invoice.
Odoo this apps use to allow users are cancel invoice.
Account cancel
Odoo account cancel
Cancel customer invoice
Odoo cancel customer invoice
Cancel vendor bill
Odoo cancel vendor bill
Cancel journal entry
Odoo cancel journal entry
Manage account cancel
Odoo manage account sales
Manage cancel customer invoice
Odoo mange cancel customer invoice
Manage cancel vendor bill
Odoo manage cancel vendor bill
Manage cancel journal entry
Odoo manage cancel journal entry
         """,
    'summary': 'odoo app allow to cancel account invoice and cancel journal entries for specific users | cancel invoice allows only access user | Cancel account invoice | cancel vendor bill | cancel journal entries | cancel customer invoice | cancel invoice',
    'depends': ['account'],
    'data': [

        'security/security_file.xml',
        'views/account_views.xml',
    ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    
    #author and support Details
    'author': 'DevIntelle Consulting Service Pvt.Ltd',
    'website': 'http://www.devintellecs.com',    
    'maintainer': 'DevIntelle Consulting Service Pvt.Ltd', 
    'support': 'devintelle@gmail.com',
    'price':15.0,
    'currency':'EUR',
    #'live_test_url':'https://youtu.be/A5kEBboAh_k',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
