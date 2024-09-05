import os
import re

INVOICE_FOLDER = "invoices"
MONTH_MATCHER = r"\w+_(\w+).pdf$"
INVOICES = list(filter(
    lambda i: not os.path.isdir(
        os.path.join(INVOICE_FOLDER, i)
    ),
    os.listdir(INVOICE_FOLDER)
))
print(INVOICES)


def create_dir(month):
    path = os.path.join(INVOICE_FOLDER, month)
    if not os.path.exists(path):
        os.mkdir(path)


def move_file(filename, month):
    origin = os.path.join(INVOICE_FOLDER, filename)
    dst = os.path.join(INVOICE_FOLDER, month)

    if os.path.exists(origin) and os.path.exists(dst):
        os.rename(origin, os.path.join(dst, filename))


def extract_month(filename):
    if not len(filename.split("_")) == 3 or not len(filename.split(".")) == 2:
        print("Poorly formatted file.")
        return None

    return re.match(MONTH_MATCHER, filename).group(1)


if __name__ == "__main__":
    for invoice in INVOICES:
        month = extract_month(invoice)

        if month is None:
            continue
            
        create_dir(month)
        move_file(invoice, month)
