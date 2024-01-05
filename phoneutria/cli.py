import argparse

from phoneutria.__main__ import Chelicera
from phoneutria.google_hacking import google_search

def main():
    parser = argparse.ArgumentParser(description="Script to test webservers with GET and POST requests.")
    parser.add_argument("-t", "--url", help="URL of the webservice")  # Corrected argument name
    parser.add_argument("--post", help="Data for POST request (format: key1=value1&key2=value2)")
    parser.add_argument("--get", nargs="+", help="Extract specific data from the response (only for GET requests)")
    parser.add_argument("--google_hacking", nargs="+", help="Extract specific data from the response (only for GET requests)")

    args = parser.parse_args()

    if args.post:
        post_data = dict(item.split("=") for item in args.post.split("&"))
        # Verificação de CSRF para requisições POST
        if "csrf_token" not in post_data:
            print("CSRF token not found in POST data. Possible CSRF vulnerability.")
        make_post(args.url, post_data)  # Corrected function call

    elif args.google_hacking:
        text = str(args.google_hacking)
        print(text)
        query = "intitle:\"Index of\" inurl:" + text
        google_search(query)

    else:
        make_get(args.url, args.get)
    


def make_get(url, extract):
    ch = Chelicera(url)
    ch.make_get_request(extract)

def make_post(url, post_data):
    ch = Chelicera(url)
    ch.make_post_request(post_data)


if __name__ == "__main__":
    main()