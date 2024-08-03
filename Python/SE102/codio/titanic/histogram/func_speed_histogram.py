from math import ceil
from matplotlib import pyplot as plt


def save_file_speed_histogram(ships: list) -> None:
    """
    Saves a .png file with a histogram of ship speeds.
    :param ships: List of ships imported from json.
    """
    # Filtering the lowest and highest value for statistical accuracy,
    # highest speed of 130+ ignored.
    speeds = sorted([float(ship["SPEED"]) for ship in ships if float(ship["SPEED"]) >= 1])[1:-1]

    max_speed = max(speeds)
    min_speed = min(speeds)

    plt.hist(
        # histogram data
        speeds,

        # sequence for the x-value ranges
        bins=list(range(
            int(min_speed),

            # make the upper end of the range greater than the max value.
            ceil(max_speed / 10) * 10
        )),

        # visual settings
        edgecolor='black',
        alpha=0.7
    )

    plt.xlim(xmin=min_speed, xmax=ceil(max_speed / 10) * 10)

    plt.xlabel('Speed')
    plt.ylabel('Frequency')

    plt.savefig('histogram/speed_histogram.png')
    print("File has been save to histogram/speed_histogram.png")
