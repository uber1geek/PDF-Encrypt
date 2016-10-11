import PyPDF2
import os
import glob
import argparse

os.chdir('/Users/Pathfinder/PDF')   #Specify the directory containing PDF files.

def set_password(input_pdf, user_pass, owner_pass):
    """
    Creates a temporary pdf and assigns the specified password 
    to it and renames it with original file name.
    """

    path, filename = os.path.split(input_pdf)
    output_pdf = os.path.join(path, "temp_" + filename)

    output = PyPDF2.PdfFileWriter()

    input_file = PyPDF2.PdfFileReader(open(input_pdf, "rb")) #Reads the file in binary mode

    for i in range(0, input_file.getNumPages()):
        output.addPage(input_file.getPage(i))

    output_file = open(output_pdf, "wb")  #Writes the file in binary mode

    #Set password to the pdf file
    output.encrypt(user_pass, owner_pass, use_128bit=True)
    output.write(output_file)
    output_file.close()

    #Rename the temp output file with the original filename
    os.rename(output_pdf, input_pdf)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--user_password', required=True,
                        help='User Password')
    parser.add_argument('-o', '--owner_password', default=None,
                        help='Owner Password')
    args = parser.parse_args()

    for file in glob.glob('*.pdf'):
        set_password(file, args.user_password, args.owner_password)

if __name__ == "__main__":
    main()
