#!/usr/bin/env python3
"""Generate a news summary image for Nov 22, 2026."""
import json
from pathlib import Path

# News summary for Nov 22, 2026
news = {
    "date": "2026-11-22",
    "headlines": [
        "Global markets steady amid tech earnings",
        "AI agents expand into new industries",
        "Crypto regulations under review in EU",
        "Climate summit announces new targets"
    ]
}

# Create a simple SVG image
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="600">
  <rect width="800" height="600" fill="#1a1a2e"/>
  <text x="400" y="50" fill="#fff" font-size="24" text-anchor="middle">World News - Nov 22, 2026</text>
  <text x="50" y="120" fill="#eee" font-size="16">1. {news["headlines"][0]}</text>
  <text x="50" y="160" fill="#eee" font-size="16">2. {news["headlines"][1]}</text>
  <text x="50" y="200" fill="#eee" font-size="16">3. {news["headlines"][2]}</text>
  <text x="50" y="240" fill="#eee" font-size="16">4. {news["headlines"][3]}</text>
  <text x="400" y="550" fill="#888" font-size="12" text-anchor="middle">make.fun entry</text>
</svg>'''

Path("/output").mkdir(exist_ok=True)
Path("/output/news.svg").write_text(svg)
print("Created news.svg")
