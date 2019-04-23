#coding=utf-8
import PySimpleGUI as sg
import os

import parse

layout = [ [sg.Text("请依次选择两个需要对比的xml", font=("Monaco"))],
           [sg.InputText(key = '_XML1_', font=("Monaco")),sg.FileBrowse("选择", font=("Monaco"))],
           [sg.InputText(key = '_XML2_', font=("Monaco")),sg.FileBrowse("选择", font=("Monaco"))],
           [sg.Text("There are [] different items betweens both of the xmls", font=("Monaco"), key = '_TITLE_')],
           [sg.Multiline(default_text='here will display the difference',font=("Monaco", 10), size=(150,30), key = '_SUMMARY_')],
           [sg.Text("+" * 100)],
           [sg.Submit(),sg.Cancel()]
        ]

window = sg.Window("Xml hash 比较工具").Layout(layout)

x = parse.parseXml()

while True:
    event,values = window.Read()
    if event is None or event == 'Cancel':
        break
    if os.path.exists(values['_XML1_']) and os.path.exists(values['_XML2_']):
        file1 = x.parse_xml_hash(values['_XML1_'])
        file2 = x.parse_xml_hash(values['_XML2_'])
        resultName = x.compare_hash(file1, file2)
        with open(resultName, 'r') as fd:
            detailInfo = fd.read()
            fd.seek(0)
            total = len(fd.readlines())
            window.FindElement('_TITLE_').Update("There are [" + str(total) + "] different items betweens both of the xmls")
            window.FindElement('_SUMMARY_').Update(detailInfo)

window.Close()

