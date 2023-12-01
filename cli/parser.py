import argparse


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='Roadmapster',
        description='Generate a roadmap towards any goal',
        epilog='Made by elt https://www.16elt.com'
    )
    parser.add_argument('topic', action='store',
                        help='The topic you want to generate a roadmap for')
    parser.add_argument('-o', '--output', action='store', choices=['json'], default='json',
                        help='Output format for the roadmap')
    return parser
