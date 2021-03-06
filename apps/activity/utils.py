from __future__ import unicode_literals
import os
from django.conf import settings
from django.core.files import File
from django.utils.text import slugify
import xlwt


def generate_excel_report(report):
    report_name = 'report_%s_%d.xls' % (
        unicode(report.month.get_month_display()),
        report.month.year,
    )
    sub_path = 'reports/%s/%s/%s/%s' % (
        slugify(unicode(report.contract.actor)),
        slugify(unicode(report.contract.client.organisation)),
        slugify(unicode(report.contract.client)),
        report_name
    )
    file_name = os.path.join(settings.MEDIA_ROOT, sub_path)
    heading_xf = xlwt.easyxf('font: bold on; '
                             'align: vert centre, horiz center')
    heading_content_xf = xlwt.easyxf('font: italic on; '
                                     'align: vert centre, horiz left')
    content_xf = xlwt.easyxf('align: vert centre, horiz left')
    book = xlwt.Workbook()
    sheet = book.add_sheet('Activity Report')
    # Business context block
    sheet.write_merge(1, 1, 1, 2, 'Business context', heading_xf)
    sheet.write(2, 1, 'Organisation', heading_xf)
    sheet.write(2, 2, report.contract.client.organisation.name, 
                heading_content_xf)
    sheet.write(3, 1, 'Client', heading_xf)
    sheet.write(3, 2, report.contract.client.name, heading_content_xf)
    sheet.write(4, 1, 'Project', heading_xf)
    if report.contract.project:
        sheet.write(4, 2, report.contract.project, heading_content_xf)
    sheet.write(5, 1, 'Mission', heading_xf)
    sheet.write(5, 2, report.contract.mission, heading_content_xf)
    # Report figures block
    sheet.write_merge(1, 1, 3, 4, 'Report figures', heading_xf)
    sheet.write(2, 3, 'Worked days', heading_xf)
    sheet.write(2, 4, report.worked_days, heading_content_xf)
    sheet.write(3, 3, 'Days with Activity', heading_xf)
    sheet.write(3, 4, report.days_with_activity, heading_content_xf)
    sheet.write(4, 3, 'Off days', heading_xf)
    sheet.write(4, 4, report.off_days, heading_content_xf)
    sheet.write(5, 3, 'Public holidays', heading_xf)
    sheet.write(5, 4, report.off_days, heading_content_xf)
    directory = '/'.join(file_name.split('/')[:-1])
    if not os.path.exists(directory.decode(settings.FS_ENCODING)):
        os.makedirs(directory)
    if os.path.isfile(file_name.decode(settings.FS_ENCODING)):
        os.remove(file_name)
    book.save(file_name)
    if os.path.isfile(file_name.decode(settings.FS_ENCODING)):
        report.excel_file = file_name
