# Roadmapster
Generate a roadmap towards any goal in the CLI using openai models.

# Install
Currently only via `git clone`

# Usage
Generate an openai api key following https://platform.openai.com/api-keys and create a `.env` file with the following env variable `OPENAI_API_KEY`

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

defaults to JSON representation of the result, similar to `python main.py kubernetes -o json`

Currently supported outputs:
* json

Planning to support graph output soon.