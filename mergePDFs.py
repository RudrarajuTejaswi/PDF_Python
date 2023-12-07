import PyPDF2

input = ['PDFs/dummy.pdf','PDFs/tiltFile.pdf','PDFs/twopage.pdf']

def combine_pdfs(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('PDFs/mergerFile.pdf')



combine_pdfs(input)