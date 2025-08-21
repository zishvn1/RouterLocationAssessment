from src.router_links import parse_input, location_pairs, format_pairs
import json

def test_pairs_basic():
    # simple test with fake data (two routers in two different locations)
    # router 1 is in location A, router 2 is in location B
    # they link to each other, so the output should be "A <-> B"
    data = {
        "routers": [
            {"id": 1, "location_id": 1, "router_links": [2]},
            {"id": 2, "location_id": 2, "router_links": [1]}
        ],
        "locations": [
            {"id": 1, "name": "A"},
            {"id": 2, "name": "B"}
        ]
    }
    locs, routers = parse_input(data)
    pairs = location_pairs(locs, routers)

    # make sure the pair is found
    assert ("A", "B") in pairs

    # also check that the formatting looks right
    lines = format_pairs(pairs)
    assert lines == ["A <-> B"]


def test_sample_json():
    # load the full dataset from data.json
    with open("data.json") as f:
        data = json.load(f)

    # parse it like usual
    locations, routers = parse_input(data)
    pairs = location_pairs(locations, routers)

    # check some known expected links are there
    assert ("Birmingham Hippodrome", "Williamson Park") in pairs
    assert ("Lancaster Brewery", "Lancaster University") in pairs
    assert ("Lancaster Brewery", "Loughborough University") in pairs
    assert ("Lancaster Castle", "Loughborough University") in pairs

    # make sure no location links to itself (a != b)
    for a, b in pairs:
        assert a != b
