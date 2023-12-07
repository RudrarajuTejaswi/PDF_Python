import PyPDF2

# Read the watermark
watermark = PyPDF2.PdfFileReader("PDFs/wtr.pdf")

# Read the page without watermark
reader = PyPDF2.PdfFileReader("PDFs/mergerFile.pdf")
writer = PyPDF2.PdfFileWriter()
print(reader.numPages)

for i in range(reader.numPages):
    print(i)
    page = reader.pages[i]
    # Add the watermark to the page
    page.mergePage(watermark.pages[0])
    # Add the page to the writer object
    writer.addPage(page)
    # finally, write the new document with a watermark
    with open("PDFs/waterMark.pdf", "wb") as fp:
        writer.write(fp)

#220 lil different answer