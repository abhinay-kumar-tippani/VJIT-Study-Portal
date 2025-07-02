# from PyPDF2 import PdfMerger

# merge = PdfMerger()

# merge.append("m2-unit3-ans.pdf")
# merge.append("m2-unit4-ans.pdf")
# merge.append("m2-unit5-ans.pdf")

# merge.write("m2-unit3-ans.pdf")

# merge.close()


# import os

# os.remove("m2-unit4-ans.pdf")
# os.remove("m2-unit5-ans.pdf")




import os

old = "m2-unit3-ans.pdf"
new = "m2-unit3-4-5-ans.pdf"

os.rename(old,new)


# # from PIL import Image

# # img = Image.open("ap_imp.jpg")

# # if img.mode == 'RGBA':
# #     img = img.convert('RGB')

# # pdf_path = "ap-imp.pdf"

# # img.save(pdf_path,"PDF")