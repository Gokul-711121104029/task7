import os
import argparse
from PIL import Image

def process_image(in_path, out_path, size, out_format=None, pad=False, quality=85):
    with Image.open(in_path) as img:
        orig_mode = img.mode
        img_copy = img.copy()
        img_copy.thumbnail(size, Image.LANCZOS)  # preserves aspect ratio

        # If padding requested, create background and paste centered
        if pad:
            background = Image.new("RGBA", size, (255,255,255,255))
            x = (size[0] - img_copy.width) // 2
            y = (size[1] - img_copy.height) // 2
            background.paste(img_copy, (x, y), img_copy if img_copy.mode in ("RGBA","LA") else None)
            final = background
        else:
            final = img_copy

        # Decide output format
        fmt = out_format or img.format or "PNG"
        ext = fmt.lower()
        # Ensure RGB for JPEG
        if fmt.upper() in ("JPEG", "JPG") and final.mode in ("RGBA","LA"):
            final = final.convert("RGB")

        # Ensure output folder exists
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        save_kwargs = {}
        if fmt.upper() in ("JPEG","JPG"):
            save_kwargs["quality"] = quality
            save_kwargs["optimize"] = True

        final.save(out_path, fmt, **save_kwargs)

def main():
    parser = argparse.ArgumentParser(description="Batch resize images")
    parser.add_argument("--input", default="input_images", help="Input folder")
    parser.add_argument("--output", default="output_images", help="Output folder")
    parser.add_argument("--width", type=int, default=800, help="Target width")
    parser.add_argument("--height", type=int, default=800, help="Target height")
    parser.add_argument("--format", default=None, help="Output format (e.g. PNG, JPEG, WEBP). Leave empty to keep original format")
    parser.add_argument("--pad", action="store_true", help="Pad images to exact dimensions (adds white background)")
    parser.add_argument("--quality", type=int, default=85, help="JPEG quality (1-95)")
    args = parser.parse_args()

    size = (args.width, args.height)
    supported_ext = ('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.gif', '.tiff')

    total = 0
    errors = 0
    for fname in os.listdir(args.input):
        if not fname.lower().endswith(supported_ext):
            continue
        in_path = os.path.join(args.input, fname)
        base = os.path.splitext(fname)[0]
        out_fmt = args.format.upper() if args.format else None
        out_ext = (out_fmt.lower() if out_fmt else os.path.splitext(fname)[1].lstrip('.'))
        out_name = f"{base}.{out_ext}"
        out_path = os.path.join(args.output, out_name)
        try:
            process_image(in_path, out_path, size, out_format=out_fmt, pad=args.pad, quality=args.quality)
            print(f"Resized -> {out_path}")
            total += 1
        except Exception as e:
            print(f"Error processing {in_path}: {e}")
            errors += 1

    print(f"Done. Processed: {total}. Errors: {errors}")

if __name__ == '__main__':
    main()