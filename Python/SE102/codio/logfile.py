import re

LOG_FILE_CONTENT = """
*.amazon.co.uk    89
*.doubleclick.net    139
*.fbcdn.net    212
*.in-addr.arpa    384
*.l.google.com    317
1.client-channel.google.com    110
6.client-channel.google.com    45
a.root-servers.net    1059
apis.google.com    43
clients4.google.com    71
clients6.google.com    81
connect.facebook.net    68
edge-mqtt.facebook.com    56
graph.facebook.com    150
mail.google.com    128
mqtt-mini.facebook.com    47
ssl.google-analytics.com    398
star-mini.c10r.facebook.com    46
staticxx.facebook.com    48
www.facebook.com    178
www.google.com    162
www.google-analytics.com    127
www.googleapis.com    87
"""

MATCHER = r"\.([a-z-]+)\.(com|net|co.uk|arpa)\s+(\d+)"


def count_domains(log_file, min_hits=0):
    """
    Filters the logfile and returns for each unique domain the times it has been logged.
    :param log_file: The logfile to analyse.
    :param min_hits: The minimum times a domain has to be logged to be displayed.
    :return: Print-ready string with sorted domains by times logged.
    """
    # Fetch all domains with regex including the times logged.
    domains = re.findall(MATCHER, log_file)

    # Get a unique list of domains
    domain_list_unique = set(f"{host}.{ending}" for host, ending, count in domains)

    # sort, filter and count for each unique domain the number of logs in the log_file.
    # Only return domains with times logged > min_hits.
    domain_list_counted_filtered_sorted = list(
        sorted(
            filter(
                lambda d: d[1] > min_hits,
                {
                    domain_name: sum(
                        [
                            int(count)
                            for host, ending, count in domains
                            if domain_name == f"{host}.{ending}"
                        ]
                    )
                    for domain_name in domain_list_unique
                }.items()
            ),
            # sort by count, then alphabetically.
            key=lambda d: (-d[1], d[0]),
            reverse=False
        )
    )

    return "\n".join([
        f'{domain}: ({count})'
        for domain, count in domain_list_counted_filtered_sorted
    ])


def main():
    print(count_domains(LOG_FILE_CONTENT, 0))


if __name__ == "__main__":
    main()
