from pathlib import Path

import yaml

settings = {}
with open(Path(__file__).parent / "../../settings.yaml", "r") as stream:
    try:
        settings = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
