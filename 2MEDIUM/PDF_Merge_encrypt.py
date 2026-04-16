from os import read, write
from PyPDF2 import PdfReader, PdfWriter

merger = PdfWriter()
for pdf in ["01doc.pdf", "02doc.pdf", "03doc.pdf"]:
    merger.append(pdf)

    merger.write("main_combined.pdf")
    merger.close()

reader = PdfReader("main_combined.pdf")
writer = PdfWriter()
for page in reader.pages:
    writer.add_page(page)

    writer.encrypt("")

    with open("Encrypt_main_file.pdf", "wb") as f:
        writer.write(f)
