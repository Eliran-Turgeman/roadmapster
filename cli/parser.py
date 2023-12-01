import argparse


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='Roadmapster',
        description='Generate a roadmap towards any goal',
        epilog='Made by elt https://www.16elt.com'
    )
    parser.add_argument('-o', '--output', action='store', choices=['json'], default='json')
    return parser
