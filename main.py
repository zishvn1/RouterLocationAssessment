import argparse
import json
import sys
from pathlib import Path
import requests

from src.router_links import parse_input, location_pairs, format_pairs


def load_from_url(url: str) -> dict:
    # grab json data from a url
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()
    return resp.json()


def load_from_file(path: str) -> dict:
    # read json data from a local file
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    # handle command line args (either file or url, not both)
    parser = argparse.ArgumentParser(description="compute unique location links from router data")
    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument("--url", help="url of json api")
    src.add_argument("--file", help="path to local json file")
    args = parser.parse_args()

    try:
        # load the data from whichever source was given
        data = load_from_url(args.url) if args.url else load_from_file(args.file)

        # parse json into locations and routers
        locations, routers = parse_input(data)

        # compute location pairs
        pairs = location_pairs(locations, routers)

        # print them in a readable format
        for line in format_pairs(pairs):
            print(line)

    except Exception as e:
        # if anything goes wrong, show the error and exit
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()  # run it if script is executed directly
