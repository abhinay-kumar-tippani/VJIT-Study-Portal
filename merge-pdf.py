# from PyPDF2 import PdfMerger

# merge = PdfMerger()

# merge.append("ese-pyq.pdf")
# merge.append("ese-pyq1.pdf")
# merge.append("ese-pyq2.pdf")

# merge.write("ese-pyq.pdf")

# merge.close()


import os

os.remove("ese-pyq1.pdf")
os.remove("ese-pyq2.pdf")
os.remove("ese-pyq2.docx")
# os.remove("ap-pyq3.pdf")




# import os

# old = "m2-unit3-ans.pdf"
# new = "m2-unit3-4-5-ans.pdf"

# os.rename(old,new)


# # from PIL import Image

# # img = Image.open("ap_imp.jpg")

# # if img.mode == 'RGBA':
# #     img = img.convert('RGB')

# # pdf_path = "ap-imp.pdf"

# # img.save(pdf_path,"PDF")


# from docx2pdf import convert

# convert("ese-pyq2.docx", "ese-pyq2.pdf")