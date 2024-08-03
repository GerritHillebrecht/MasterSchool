import PyPDF2

FILE_NAME_ORIG = "olympic-medals.csv"
FILE_NAME_COPY = "olympic-medals-copy.csv"
FILE_NAME_SHORT = "olympic-medals-short.csv"
FILE_NAME_N = "olympic-medals-n.csv"

# 1. copy file
with open(FILE_NAME_ORIG, "r") as f:
    orig_data = f.read()

with open(FILE_NAME_COPY, "w") as f:
    f.write(orig_data)

# 2. shorten file
with open(FILE_NAME_SHORT, "w") as f:
    f.write(orig_data[:10])

# 3. Medals n
with open(FILE_NAME_ORIG, "r") as f:
    orig_headline = f.readline()
    orig_lines = f.readlines()

with open(FILE_NAME_N, "w") as f:
    f.write(orig_headline)
    for line in orig_lines:
        # ignore the faulty formats.
        # team, gold, silver, bronze = line.split(",")
        if line.split(",")[0].startswith("N"):
            f.write(line)


# 4.

# BONUS - work with binary files
def copy_binary_file(file_name, file_name_copy, repeated_content=1, max_length_content=0):
    with open(file_name, "rb") as file:
        file_data = file.read()

    with open(file_name_copy, "wb") as file:
        for i in range(repeated_content):
            file.write(file_data) if max_length_content == 0 else file.write(file_data[:max_length_content])


copy_binary_file("sample.mp3", "sample-copy.mp3", 2)
copy_binary_file("baseball.jpg", "baseball_copy.jpg", max_length_content=30000)
