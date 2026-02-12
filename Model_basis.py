#!/usr/bin/env python3
"""

- Represent a polymer on a 2D square lattice using coordinates.

- Define bonds implicitly (i bonded to i+1).

- Validate a conformation:
    (1) Self-avoiding: no two monomers occupy the same lattice site
    (2) Connected: each bond has Manhattan distance = 1


"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple
import argparse

Pos2D = Tuple[int, int]


def manhattan(a: Pos2D, b: Pos2D) -> int:
    """Manhattan distance on a square lattice."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def neighbors_2d(p: Pos2D) -> List[Pos2D]:
    """4-neighbor moves on a 2D square lattice."""
    x, y = p
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


@dataclass
class Polymer2D:
    """2D lattice polymer represented by coordinates (x,y) for each monomer."""
    coords: List[Pos2D]

    @property
    def N(self) -> int:
        return len(self.coords)

    def validate(self) -> None:
        """Check SAW validity: self-avoidance + connectivity."""
        # 1) Self-avoidance (no overlaps)
        if len(set(self.coords)) != self.N:
            raise ValueError("Invalid polymer: overlap detected (not self-avoiding).")

        # 2) Connectivity: each adjacent pair (i, i+1) must be nearest neighbors
        for i in range(self.N - 1):
            if manhattan(self.coords[i], self.coords[i + 1]) != 1:
                raise ValueError(
                    f"Invalid polymer: broken bond at ({i},{i+1}). "
                    f"{self.coords[i]} -> {self.coords[i+1]} (must be Manhattan distance 1)"
                )

    def bonds(self) -> List[Tuple[int, int]]:
        """Return bonded index pairs (i, i+1)."""
        return [(i, i + 1) for i in range(self.N - 1)]

    def summary(self) -> str:
        """Small summary useful for debugging."""
        xs = [p[0] for p in self.coords]
        ys = [p[1] for p in self.coords]
        return (
            f"N = {self.N}\n"
            f"First monomer: {self.coords[0]}\n"
            f"Last monomer : {self.coords[-1]}\n"
            f"x range: [{min(xs)}, {max(xs)}]\n"
            f"y range: [{min(ys)}, {max(ys)}]\n"
        )


def straight_chain(N: int) -> Polymer2D:
    """initialization: a straight chain along +x."""
    coords = [(i, 0) for i in range(N)]
    poly = Polymer2D(coords)
    poly.validate()
    return poly


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=20, help="Number of monomers (chain length)")
    args = ap.parse_args()

    poly = straight_chain(args.N)

    print("WEEK 1 — 2D lattice polymer representation")
    print(poly.summary())
    print("Bonds (index pairs):", poly.bonds()[:10], "..." if poly.N > 11 else "")
    print("Validation: OK ")


if __name__ == "__main__":
    main()
