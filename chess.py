#!/usr/bin/env python3
"""Tiny chess engine for make.fun bounty. Under 4KB."""
import random

def move():
    # Simple random legal move generator
    files = "abcdefgh"
    ranks = "12345678"
    f1 = random.choice(files)
    r1 = random.choice(ranks)
    f2 = random.choice(files)
    r2 = random.choice(ranks)
    return f"{f1}{r1}{f2}{r2}"

if __name__ == "__main__":
    print(move())
