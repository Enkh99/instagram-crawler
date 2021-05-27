import argparse

def parser():
        
    parser = argparse.ArgumentParser(
        description = "Get Link"
    )

    parser.add_argument("link", help="Getting link")

    args = parser.parse_args()
    print(args)