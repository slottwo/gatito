from json import load


def loadmap(map_id) -> list[list]:
    try:
        with open(f"gatito/assets/tilemaps/{map_id}.json") as f:
            j = load(f)
    except FileNotFoundError:
        print("Level not found.")
        exit(1)
    return [l['data'] for l in j['layers']]
