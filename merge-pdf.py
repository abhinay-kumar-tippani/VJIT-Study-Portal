# from PyPDF2 import PdfMerger

# merge = PdfMerger()

# merge.append("edc-pyq1.pdf")
# merge.append("edc-pyq2.pdf")
# merge.append("edc-pyq3.pdf")

# merge.write("edc-pyq1.pdf")

# merge.close()


import os

os.remove("edc-pyq2.pdf")
os.remove("edc-pyq3.pdf")




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