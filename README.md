# Roadmapster
Generate a roadmap towards any goal in the CLI using openai models.

# Usage
```
usage: Roadmapster [-h] [-o {json}] topic

Generate a roadmap towards any goal

positional arguments:
  topic                 The topic you want to generate a roadmap for

optional arguments:
  -h, --help            show this help message and exit
  -o {json}, --output {json}
                        Output format for the roadmap
```

# Example Usage

`python main.py kubernetes`

defaults to JSON representation of the result, similar too:

`python main.py kubernetes -o json`

Currently supported outputs:
* json

Planning to support graph output soon.