import os
from fpdf import FPDF
from PIL import Image
from files import check_dir, check_extention


def makePdf(output, path):
    output = check_extention(output, ".pdf")
    pdf = FPDF()
    dirs = sorted(os.listdir(path))
    cover = Image.open("{}/{}".format(path, dirs[0]))
    width, height = cover.size
    pdf = FPDF(unit="pt", format=[width, height])
    check_dir("pdfs")
    for image in dirs:
        pdf.add_page()
        pdf.image("{}/{}".format(path, image), 0, 0)
    pdf.output("pdfs/" + output, "F")
    print("Created a new pdf in pdfs/{}".format(output))
