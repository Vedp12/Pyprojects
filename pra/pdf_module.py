from PyPDF2 import PdfReader

# * Getting pages and Extracting text

with open("Notex.pdf", "rb") as Pdf_file:
    reader = PdfReader(Pdf_file)
    total_pages = len(reader.pages)
    print(total_pages)
    for page in reader.pages:
        print(page.extract_text())


# * Meta Data

with open("home/tux_106/Documents/oop.pdf", "rb") as pdf_file:
    reader = PdfReader(pdf_file)

    meta_data = reader.metadata
    print(f"Author: {meta_data.author} ")
    print(f"Title:  {meta_data.title}")
    print(f"Createion Date: {meta_data.creation_date}")


#! Extract images from pdf PDF file

reader = PdfReader("oop.pdf")

page = reader.pages[0]

for page_index, page in enumerate(reader.pages):
    count = 1
    
    for image_file in page.images:
        filename = f"{count}_{page_index}_{image_file.name}"  #^ Filename that must ends with .name for giving the images name
        with open(filename, "wb") as fp:
            fp.write(image_file.data)
            count += 1
