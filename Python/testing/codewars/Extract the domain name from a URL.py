import re

MATCHER = r"(?:http?s?:\/\/)?(?:www\.)?([\w|-]+)\.(?:\w{2,3})[\/\w+]*"

def main():
    url = "https://www.hyphen-site.org"
    matches = re.findall(MATCHER, url)
    print(matches)


if __name__ == "__main__":
    main()
