#!/usr/bin/env python3
"""GTA 6 meme generator for make.fun bounty."""
from pathlib import Path

# Simple GTA 6 meme SVG
svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600">
  <rect width="800" height="600" fill="#000"/>
  <text x="400" y="200" fill="#fff" font-size="48" text-anchor="middle" font-family="Impact">GTA 6</text>
  <text x="400" y="280" fill="#ff0" font-size="24" text-anchor="middle">Coming soon...</text>
  <text x="400" y="350" fill="#0f0" font-size="20" text-anchor="middle">make.fun</text>
  <text x="400" y="500" fill="#888" font-size="14" text-anchor="middle">@makefunai</text>
</svg>'''

Path("/output").mkdir(exist_ok=True)
Path("/output/gta6_meme.svg").write_text(svg)
print("Created gta6_meme.svg")
