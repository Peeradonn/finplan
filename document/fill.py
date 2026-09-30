"""
Fill {{key}} placeholders with the model's numbers (figures/numbers.json, written by model/make_charts.py).

    python fill.py manuscript.md          -> manuscript.filled.md (for reading)
    import fill; fill.fill_text(text)     -> used by render.py before printing HTML

Every model number in the documents is a placeholder, so a model change reaches the text on the next render.
Unknown keys stop the build: a missing number must never print as "{{...}}" or as a stale value.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
NUMBERS = os.path.join(os.path.dirname(HERE), "figures", "numbers.json")
PATTERN = re.compile(r"\{\{\s*([a-z0-9_]+)\s*\}\}")

def load():
    with open(NUMBERS, encoding="utf-8") as f:
        return json.load(f)

def fill_text(text, numbers=None):
    numbers = numbers or load()
    missing = sorted({k for k in PATTERN.findall(text) if k not in numbers})
    if missing:
        raise KeyError(f"No value in numbers.json for: {', '.join(missing)}")
    return PATTERN.sub(lambda m: numbers[m.group(1)], text)

if __name__ == "__main__":
    for path in sys.argv[1:]:
        with open(path, encoding="utf-8") as f:
            text = f.read()
        root, ext = os.path.splitext(path)
        out = f"{root}.filled{ext}"
        with open(out, "w", encoding="utf-8") as f:
            f.write(fill_text(text))
        print(f"{path} -> {out} ({len(PATTERN.findall(text))} placeholders filled)")
