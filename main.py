from cli.parser import create_parser
from generation.roadmap_generator_ai import RoadmapGenerator
from output.json import JsonOutput

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    roadmap = RoadmapGenerator().generate(args.topic)

    if args.output == 'json':
        output = JsonOutput(roadmap).show()

