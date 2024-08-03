from PyPDF2 import PdfReader, PdfWriter


def copy_pdf_file(file_name, file_name_copy):
    with open(file_name, "rb") as file:
        reader = PdfReader(file)

        with open(file_name_copy, "wb") as file_copy:
            writer = PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            writer.write(file_copy)


def main():
    copy_pdf_file("resume.pdf", "resume-copy.pdf")


if __name__ == "__main__":
    main()
