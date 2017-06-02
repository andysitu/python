import PyPDF2

# pdfFileObj = open('cameronmoll_bio.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#
# print(pdfReader.numPages)
# pageObj = pdfReader.getPage(0)
# print(pageObj.extractText())

import ffile
import os
import openpyxl

def read_pdf(filename):
    pass

def make_pdf_file(pdfwriter, pdf_filename):
    pdfOutputFile = open(pdf_filename, 'wb')
    pdfwriter.write(pdfOutputFile)
    pdfOutputFile.close()

def open_pdf():
    ffile.move_dir("unread_pdf")

    try:
        wb = openpyxl.load_workbook('index.xlsx')
    except FileNotFoundError:
        print("index.xlsx was not found")
        return 0

    sheet_list = wb.get_sheet_names()
    sheetname = sheet_list[0]
    sheet = wb.get_sheet_by_name(sheetname)

    max_columns = sheet.max_column

    for col in range(1, max_columns, 2):
        pdf_name = str(sheet.cell(row=1, column=col).value) + '.pdf'
        num_pages = sheet.cell(row=2, column=col).value

        try:
            pdfFile = open(pdf_name, 'rb')
        except FileNotFoundError:
            continue

        pdfReader = PyPDF2.PdfFileReader(pdfFile)

        pdf_pages = pdfReader.numPages

        if pdf_pages != num_pages:
            raise Exception('num_pages != pdf_pages of file ' + pdf_name)

        pages_col_num = col + 1

        prev_rcv_filename = ""
        prev_pdfwriter = PyPDF2.PdfFileWriter()

        for page in range(1, num_pages + 1):
            rcv_name = str(sheet.cell(row = page, column=pages_col_num).value)

            # print("RCV NAME", rcv_name, prev_rcv_filename)

            if rcv_name != "-":
                if page != 1:
                    # print(page, "TEST",prev_pdfwriter, prev_rcv_filename)
                    #Write previous RCV PDF
                    make_pdf_file(prev_pdfwriter, prev_rcv_filename)

                prev_rcv_filename = 'RCV' + rcv_name + '.pdf'
                prev_pdfwriter = PyPDF2.PdfFileWriter()


            pageObj = pdfReader.getPage(page - 1)
            prev_pdfwriter.addPage(pageObj)

        make_pdf_file(prev_pdfwriter, prev_rcv_filename)

    ffile.dir_back()

open_pdf()