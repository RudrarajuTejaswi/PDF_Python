import PyPDF2

#opening the file, 'rb' mode is to read the file in binary format
# as the machines can read only binary code
with open('PDFs/dummy.pdf',mode='rb') as dummy_file:
    print(dummy_file)
    #reading the content in the file
    reader = PyPDF2.PdfFileReader(dummy_file)
    #numPages - gets the no of pages
    print(reader.numPages)
    #getPage() - gets the required page object based on the value passed else Index out of range err
    print(reader.getPage(0))

    #rotate the text in PDF
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('PDFs/tiltFile.pdf',mode='wb') as new_file:
        writer.write(new_file)