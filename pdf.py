import PyPDF2

f=open("Faheem_resume.pdf","rb")

pdf_reader=PyPDF2.PdfFileReader(f)

print(len(pdf_reader(pdf_reader)))

page_one=pdf_reader.getPage(0)

page_one_text=page_one.extractText()

print(page_one_text)