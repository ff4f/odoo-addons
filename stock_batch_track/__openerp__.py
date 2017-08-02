# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (c) 2010-Today Elico Corp. All Rights Reserved.
#    Author: Andy Lu <andy.lu@elico-corp.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Picking Batch Processing',
    'version': '1.0',
    'category': 'Generic Modules/Stock',
    'description': """
        Batch Processing for the following functions:
            * Set Pack
            * Cancel Availability
            * Check Availability
            * Force Availability
            * Auto Process to finish
    """,
    'author': 'Elico Corp.',
    'website': 'http://www.openerp.com.cn',
    'depends': ['stock'],
    'init_xml': [],
    'update_xml': ['wizard/stock_batch_track_view.xml',
        'stock_batch_track_report_view.xml'],
    'demo_xml': [],
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: