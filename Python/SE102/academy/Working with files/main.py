from datetime import datetime
from statistics import mean

FILE_NAME_SP500 = "SP500.txt"

with open(FILE_NAME_SP500, "r") as f:
    f.readline()

    mean_SP = []
    max_interest = []

    for line in f.readlines():
        # unpack all data
        Date, SP500, Dividend, Earnings, Consumer_Price_Index, Long_Interest_Rate, Real_Price, Real_Dividend, Real_Earnings, PE10 = line.split(",")

        # create date-object
        month, day, year = Date.split("/")
        date = datetime(int(year), int(month), int(day))

        # Specified date-range
        if datetime(2016, 5, 1) <= date < datetime(2017, 5, 1):
            mean_SP.append(float(SP500))
            max_interest.append(float(Long_Interest_Rate))

    mean_SP = mean(mean_SP)
    max_interest = max(max_interest)

