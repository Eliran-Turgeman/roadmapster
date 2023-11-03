from generation.roadmap_generator_ai import RoadmapGenerator
from graph_creation.roadmap_graph_creator import RoadmapGraphCreator

if __name__ == '__main__':
    roadmap = RoadmapGenerator().generate('mock')
    graph_creator = RoadmapGraphCreator()
    graph_creator.create(roadmap)
    graph_creator.show()
