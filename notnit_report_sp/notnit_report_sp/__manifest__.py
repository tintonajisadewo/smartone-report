# -*- coding: utf-8 -*-
# Part of Odoo, odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Report QWEB Invoice and Delivery Slip Add Signature',
    'author': 'Tinton Aji Sadewo',
    'version': '15.0.0',
    "license": "AGPL-3",
    'category': 'Report QWEB Invoice and Delivery Slip',
    'price': '12.0',
    'currency': 'USD',
    'summary': """
       Report QWEB Invoice and Delivery Slip Add Signature""",
    'description': """
Report QWEB Invoice and Delivery Slip Add Signature
""",
    'website': 'https://tintonajisadewo.github.io/',
    'images': ['static/description/__manifest__.png', ],
    'depends': ['sale', ],
    'data': [
        'report/notnit_report_sp_head.xml',
        'report/report_notnit_report_sp_doc.xml',
        'report/notnit_report_inv_head.xml',
        'report/report_notnit_report_inv_doc.xml',
        'report/report.xml',

    ],
}
