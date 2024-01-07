import argparse

from phoneutria.__main__ import Chelicera
from phoneutria.google_hacking import google_search


def main():
    parser = argparse.ArgumentParser(description="Script to test webservers with GET and POST requests.")
    parser.add_argument("-t", "--url", help="URL of the webservice")
    parser.add_argument("-w", nargs="+", help="Extract specific data from the response (only for GET requests)")
    parser.add_argument("--links", help="get links in html")
    parser.add_argument("-gh", nargs="+", help="google_hacking")

    args = parser.parse_args()

    if args.w:
        ch = Chelicera(args.url)
        ch.make_get_words(args.w)

    elif args.links:
        ch = Chelicera(args.url)
        ch.make_get_links()

    elif args.gh:
        text = str(args.gh)
        print(text)
        query = "intitle:\"Index of\" inurl:" + text
        google_search(query)


if __name__ == "__main__":
    main()