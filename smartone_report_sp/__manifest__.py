# -*- coding: utf-8 -*-
# Part of Odoo, odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'smartone_report_sp',
    'author': 'Tinton Aji Sadewo',
    'version': '1.1',
    'category': 'Report Invoice and Delivery Slip',
    'summary': """
        Add Signature in report sale invoice and Delivery Slip""",
    'description': """
Add Signature in report sale invoice and Delivery Slip
""",
    'website': 'https://tintonajisadewo.github.io/',
    'depends': ['sale', ],
    'data': [
        'report/smartone_report_sp_head.xml',
        'report/report_smartone_report_sp_doc.xml',
        'report/smartone_report_inv_head.xml',
        'report/report_smartone_report_inv_doc.xml',
        'report/report.xml',

    ],
}
