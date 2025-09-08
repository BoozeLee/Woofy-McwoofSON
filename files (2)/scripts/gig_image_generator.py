#!/usr/bin/env python3
"""
Woofy Gig Image Generator 🐶
Combines badge SVGs and service titles into a gig-ready PNG image.
Requires: cairosvg, pillow
Usage: python gig_image_generator.py --title "AI Bug Fix" --badges woofy-badge.svg perplexity-certified.svg fast-delivery.svg
"""
import sys, argparse
from PIL import Image, ImageDraw, ImageFont
import cairosvg
import io

def svg_to_png(svg_path):
    png_bytes = cairosvg.svg2png(url=svg_path)
    return Image.open(io.BytesIO(png_bytes))

def create_gig_image(title, badge_paths, output="gig-image.png"):
    # Prepare base image
    width, height = 720, 360
    img = Image.new("RGBA", (width, height), (244, 240, 230, 255))
    draw = ImageDraw.Draw(img)
    # Title
    font = ImageFont.truetype("arial.ttf", 48)
    draw.text((40, 40), f"🐶 {title}", fill="#b67a1c", font=font)
    # Badges
    x, y = 40, 120
    for badge in badge_paths:
        badge_img = svg_to_png(badge).resize((180, 60))
        img.paste(badge_img, (x, y), badge_img)
        x += 200
    img.save(output)
    print(f"Saved {output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--badges", nargs="+", required=True)
    parser.add_argument("--output", default="gig-image.png")
    args = parser.parse_args()
    create_gig_image(args.title, args.badges, args.output)