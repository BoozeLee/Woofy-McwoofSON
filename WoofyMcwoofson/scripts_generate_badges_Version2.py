import os

def make_coverage_badge(coverage_pct, dest="branding/coverage-badge.svg"):
    color = "#4c1" if coverage_pct >= 90 else "#dfb317" if coverage_pct >= 75 else "#e05d44"
    badge = f'''<svg xmlns="http://www.w3.org/2000/svg" width="120" height="20">
  <rect width="120" height="20" fill="#555"/>
  <rect x="60" width="60" height="20" fill="{color}"/>
  <text x="30" y="14" fill="#fff" font-family="Verdana" font-size="11">coverage</text>
  <text x="90" y="14" fill="#fff" font-family="Verdana" font-size="11">{coverage_pct:.0f}%</text>
</svg>'''
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w") as f:
        f.write(badge)
    print(f"Badge generated at {dest}")

if __name__ == "__main__":
    # Example: parse coverage from XML or env, here we mock 100%
    make_coverage_badge(100)