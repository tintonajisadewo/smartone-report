# -*- coding: utf-8 -*-
# Part of Odoo, odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'smartone_report_sp',
    'author': 'Tinton Aji Sadewo',
    'version': '16.0.0',
    "license": "AGPL-3",
    'category': 'Report Invoice and Delivery Slip',
    'price': '10',
    'currency':'USD',
    'summary': """
        Add Signature in report sale invoice and Delivery Slip""",
    'description': """
Add Signature in report sale invoice and Delivery Slip
""",
    'website': 'https://tintonajisadewo.github.io/',
    'images': ['static/description/__manifest__.png',],
    'depends': ['sale', ],
    'data': [
        'report/smartone_report_sp_head.xml',
        'report/report_smartone_report_sp_doc.xml',
        'report/smartone_report_inv_head.xml',
        'report/report_smartone_report_inv_doc.xml',
        'report/report.xml',

    ],
}
