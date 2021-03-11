import json
from pathlib import Path

# movies = [
#     {"id": 1, "title": "Terminator", "year": 1989},
#     {"id": 2, "title": "Cop", "year": 1989},
#     {"id": 3, "title": "Borhter thei", "year": 1989},
# ]

# # stringify
# data = json.dumps(movies)
# print(data)
# write json

# parse json
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
