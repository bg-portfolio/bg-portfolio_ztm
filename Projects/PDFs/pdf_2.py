import sys
import PyPDF2
# pdfs merger for pdfs names specified in console

# 1
# inputs = sys.argv[1:]


# def pdf_combiner(list_pdfs):
#     merger = PyPDF2.PdfFileMerger()
#     for pdf in list_pdfs:
#         merger.append(pdf)
#     merger.write("merged.pdf")


# pdf_combiner(inputs)


# 2
# def pdf_water():
#     template = PyPDF2.PdfFileReader(open("merged.pdf", "rb"))
#     watermark = PyPDF2.PdfFileReader(open("wtr.pdf", "rb"))
#     output = PyPDF2.PdfFileWriter()
#     for i in range(template.getNumPages()):
#         page = template.getPage(i)
#         page.mergePage(watermark.getPage(0))
#         output.addPage(page)
#     with open("watermarked.pdf", "wb") as file:
#         output.write(file)


# pdf_water()
