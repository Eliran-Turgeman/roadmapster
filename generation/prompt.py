TOPIC_PLACEHOLDER = "ROADMAPSTER_TOPIC_PLACEHOLDER"
PROMPT = f"""
I require a JSON representation of a directed acyclic graph tailored as a study roadmap for {TOPIC_PLACEHOLDER}. 
Within this graph, each node should correspond to a crucial learning milestone. The nodes must encapsulate:

A succinct description of the learning objective. A curated list of resources, each accompanied by a direct link. A 
designation of whether the step is 'required' or 'optional' for foundational Kubernetes knowledge. Dependencies 
between nodes must clearly indicate which steps are prerequisites for others, allowing for the identification of 
learning paths that can be pursued in parallel. This clarity will enable the flexible sequencing of study topics 
where possible, as well as an understanding of the critical path for sequential learning. The JSON structure should 
prioritize the representation of study steps and their dependencies, omitting extraneous narrative details

Ensure that the JSON structure consistently uses these fields for each node, and that the relationships between nodes 
are clearly defined through the "prerequisites" field. The representation should facilitate the identification of 
parallel and sequential learning paths without including any unnecessary details.

- "id": A unique identifier for the learning milestone.
- "title": A brief title summarizing the learning objective.
- "description": A succinct explanation of the learning objective.
- "resources": An array of objects, each containing:
  - "name": The title of the resource.
  - "url": A direct link to the resource.
- "status": A string indicating if the step is "required" or "optional".
- "prerequisites": An array of "id" values indicating dependencies on other learning milestones."""
