from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Iterable, List, Set, Tuple

# simple class to hold router info
# frozen=True means once created, it can't be changed
@dataclass(frozen=True)
class Router:
    id: int
    location_id: int
    links: Tuple[int, ...]   # store linked router ids as a tuple


def parse_input(data: dict) -> Tuple[Dict[int, str], Dict[int, Router]]:
    # make sure the input has both locations and routers
    if "locations" not in data or "routers" not in data:
        raise ValueError("input must contain 'locations' and 'routers'")

    # build a dictionary of location id → location name
    locations = {loc["id"]: loc["name"] for loc in data["locations"]}

    # build a dictionary of router id → Router object
    # handles both snake_case and camelCase in the input
    routers: Dict[int, Router] = {}
    for r in data["routers"]:
        rid = r.get("id")
        lid = r.get("location_id") or r.get("locationId")
        links = r.get("router_links") or r.get("links", [])
        routers[rid] = Router(id=rid, location_id=lid, links=tuple(links))

    return locations, routers


def location_pairs(locations: Dict[int, str], routers: Dict[int, Router]) -> Set[Tuple[str, str]]:
    # compute unique location-to-location pairs
    pairs: Set[Tuple[str, str]] = set()
    for r in routers.values():
        loc_a = locations.get(r.location_id)
        if not loc_a:
            continue  # skip if router has no valid location

        for lid in r.links:
            other = routers.get(lid)
            if not other:
                continue  # skip if linked router is missing

            loc_b = locations.get(other.location_id)
            if not loc_b or loc_b == loc_a:
                continue  # skip if no location or same location

            # sort so (a, b) and (b, a) count as the same pair
            pairs.add(tuple(sorted((loc_a, loc_b))))

    return pairs


def format_pairs(pairs: Iterable[Tuple[str, str]]) -> List[str]:
    # turn pairs into human-readable strings like "A <-> B"
    return [f"{a} <-> {b}" for a, b in sorted(pairs)]
