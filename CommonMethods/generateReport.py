# -*- coding: utf-8 -*-
import xlsxwriter
from CommonMethods import globalData, relatedTime, Data

def generate_report():
    time = relatedTime.reporttime()
    file = globalData.PATH + '/TestResult/TestReport' + '_' + time + '.xlsx'
    image = globalData.PATH + '/TestData/app.png'

    #新建工作簿
    workbook = xlsxwriter.Workbook(file)
    #新建工作表：环境
    summary = workbook.add_worksheet('Summary')
    #新建工作表：概况
    analysis = workbook.add_worksheet('Analysis')
    #新建工作表：模块明细
    modules = []
    for i in range(0, len(globalData.EXECUTED)):
        modules.append(workbook.add_worksheet(globalData.EXECUTED[i].keys()[0]))

    #格式设定
    #设置工作表Summary单元格的宽高
    summary.set_column('A:B', 40)
    for i in range(20, 24):
        summary.set_row(i, 20)
    #设置工作表analysis单元格的宽高
    analysis.set_column('A:G', 15)
    for i in range(1, 50):
        analysis.set_row(i, 20)
    #设置工作表单元格的宽高
    for i in range(0, len(modules)):
        modules[i].set_column('A:B', 15)

    title_format = workbook.add_format({
    'bold': 2,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'font_name': u'黑体',
    'font_size': 20})

    info_format = workbook.add_format({
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'font_name': u'黑体',
        'font_size': 11})

    table_format = workbook.add_format({
        'bold': 0,
        'border': 0,
        'align': 'center',
        'valign': 'vcenter',
        'font_name': u'黑体',
        'font_size': 11})


    header = [{'header': 'Moudule', 'total_string': 'Totals', 'format': table_format},
              {'header': 'Total', 'total_function': 'sum','format': table_format},
              {'header': 'Pass', 'total_function': 'sum','format': table_format},
              {'header': 'Fail', 'total_function': 'sum','format': table_format},
              {'header': 'Not Executed', 'total_function': 'sum','format': table_format},
              {'header': 'Result', 'format': table_format}
              ]

    module_header = [{'header': 'Case NO.', 'format': table_format}, {'header': 'Result', 'format': table_format}]

    title = {
        'name': u'用例执行概况',
        'name_font': {'size': 14, 'bold': True},
        'num_font':  {'黑体': True },
    }

    module_title = {
        'name': u'模块用例执行概况',
        'name_font': {'size': 14, 'bold': True},
        'num_font':  {'黑体': True },
    }


    url_format = workbook.add_format({
    'font_color': 'blue',
    'underline':  1,
    'bold': 0,
    'border': 0,
    'align': 'center',
    'valign': 'vcenter',
    'font_name': u'黑体',
    'font_size': 11
    })

    #获取用例执行数据
    data = []
    for i in range(0, len(globalData.EXECUTED)):
        module = globalData.EXECUTED[i].keys()[0]
        Total, Pass, Fail, Notexecuted, Result = get_module_result(globalData.EXECUTED[i].values()[0])
        data.append([module, Total, Pass, Fail, Notexecuted, Result])
    #获取总的用例执行结果
    result = ''
    for i in range(0, len(data)):
        if(data[i][5] == 'Fail'):
            result = 'Fail'
            break
    if(result == ''):
        result = 'Pass'

    #制作封面
    version = globalData.VERSION
    summary.merge_range('A1:B2', u'自动化测试报告', title_format)
    summary.merge_range('A3:B20', '', title_format)
    summary.insert_image('A3', image, {'x_scale': 1.5, 'y_scale': 1.5, 'x_offset': 175, 'y_offset': 45})
    summary.write("A21", u'产品', info_format)
    summary.write("B21", u'Bapp-经纪宝', info_format)
    summary.write("A22", u'环境', info_format)
    summary.write("B22", u'测试环境', info_format)
    summary.write("A23", u'APP版本', info_format)
    summary.write("B23", version, info_format)
    summary.write("A24", u'执行结果', info_format)
    summary.write("B24", result, info_format)
    summary.write("A25", u'执行日期', info_format)
    summary.write("B25", relatedTime.currenttime()[0:10], info_format)

    #绘制用例执行概况表格
    rows = len(globalData.EXECUTED)
    analysis.add_table("A2:F" + str(rows +3), {'data': data, 'columns': header, 'style': 'Table Style Light 11', 'total_row': 1})
    analysis.merge_range('A1:F1', u'用例执行概况', title_format)
    analysis.write("F" + str(rows + 3), result, table_format)
    #绘制模块用例执行明细的超链接
    for i in range(0, len(globalData.EXECUTED)):
        analysis.write_url('A' + str(i + 3), 'internal:' + globalData.EXECUTED[i].keys()[0] + '!A1', url_format, globalData.EXECUTED[i].keys()[0])

    #绘制用例执行概况饼状图
    analysis_pie_chart = workbook.add_chart({'type': 'pie'})
    analysis_pie_chart.add_series({
        'categories': '=(Analysis!$C$2:$E$2)',
        'values':     '=(Analysis!$C$' + str(rows + 3) + ':$E$' + str(rows + 3) + ')',
        'data_labels': {'value': True, 'percentage': True}
    })
    analysis_pie_chart.set_title(title)
    analysis_pie_chart.set_size({'width': 400, 'height': 400})
    analysis.insert_chart('A' + str(rows + 7), analysis_pie_chart)

    #绘制模块用例执行概况柱形图
    analysis_column_chart = workbook.add_chart({'type': 'column', 'subtype': 'percent_stacked'})

    analysis_column_chart.add_series({
        'name': '=Analysis!$C$2',
        'categories': '=Analysis!$A$3:$A$' + str(rows + 2),
        'values':     '=Analysis!$C$3:$C$' + str(rows + 2),
        'data_labels': {'value': True, 'percentage': True}
    })

    analysis_column_chart.add_series({
        'name': '=Analysis!$D$2',
        'categories': '=Analysis!$A$3:$A$' + str(rows + 2),
        'values':     '=Analysis!$D$3:$D$' + str(rows + 2),
        'data_labels': {'value': True, 'percentage': True}
    })

    analysis_column_chart.add_series({
        'name': '=Analysis!$E$2',
        'categories': '=Analysis!$A$3:$A$' + str(rows + 2),
        'values':     '=Analysis!$E$3:$E$' + str(rows + 2),
        'data_labels': {'value': True, 'percentage': True}
    })

    analysis_column_chart.set_x_axis({'name': u'模块'})
    analysis_column_chart.set_y_axis({'name': u'百分比'})
    analysis_column_chart.set_title(module_title)
    analysis_column_chart.set_style(10)
    analysis_column_chart.set_size({'width': 600, 'height': 400})
    analysis.insert_chart('A' + str(rows + 25), analysis_column_chart)

    #绘制模块用例执行情况明细表
    for i in range(0, len(modules)):
        case_count = Data.getCasenumber(globalData.EXECUTED[i].keys()[0])
        module_data = []
        for j in range(0, len(globalData.EXECUTED[i].values()[0])):
            module_data.append([j + 1, globalData.EXECUTED[i].values()[0][j]])
        modules[i].add_table("A1:B" + str(case_count + 1), {'data': module_data, 'columns': module_header, 'style': 'Table Style Light 11'})

    #关闭工作簿
    workbook.close()






def get_module_result(data):
    Total = len(data)
    Pass = 0
    Fail = 0
    Notexecuted = 0
    Result = ''
    for i in range(0, len(data)):
        if(data[i] == 'Pass'):
            Pass = Pass + 1
        elif(data[i] == 'Fail'):
            Fail = Fail + 1
        elif(data[i] == 'Not Executed'):
            Notexecuted = Notexecuted + 1
    if(Pass != Total):
        Result = 'Fail'
    else:
        Result = 'Pass'
    return Total, Pass, Fail, Notexecuted, Result

if __name__ == '__main__':
    generate_report()