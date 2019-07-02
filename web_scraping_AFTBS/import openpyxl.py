import openpyxl
import os

os.chdir('D:\\Python\\web_scraping')




workbook = openpyxl.load.workbook('fruits.xlsx')
type(workbook)
workbook.get_sheet_by_name('Sheet1')
type(sheet)
workbook.get.sheet_names()