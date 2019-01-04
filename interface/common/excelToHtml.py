#!/usr/bin/env Python
# coding=utf-8
import pandas as pd
import codecs


def execlToHTml(excelPath, htmlPath):
    xd = pd.ExcelFile(excelPath)
    df = xd.parse()
    with codecs.open(htmlPath, 'w', 'utf-8') as html_file:
        html_file.write(df.to_html(header=True, index=False, na_rep=""))
