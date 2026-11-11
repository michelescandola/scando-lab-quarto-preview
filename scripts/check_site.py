"""Check rendered pages and local links using only Python's standard library.

Run `quarto render` first, then `python3 scripts/check_site.py`.
The same check runs in GitHub Actions after each contribution.
"""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys


class PageParser(HTMLParser):
    """Collect identifiers, local references and page heading counts."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.duplicates = []
        self.references = []
        self.accessible_references = []
        self.heading_count = 0

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        identifier = attributes.get("id")
        if identifier:
            if identifier in self.ids:
                self.duplicates.append(identifier)
            self.ids.add(identifier)
        if tag == "h1":
            self.heading_count += 1
        for attribute in ("href", "src"):
            if attribute in attributes:
                self.references.append(attributes[attribute])
        for attribute in ("aria-controls", "aria-labelledby", "aria-describedby"):
            self.accessible_references.extend(attributes.get(attribute, "").split())


def main():
    site = Path(__file__).resolve().parents[1] / "_site"
    paths = sorted(site.rglob("*.html"))
    if not paths:
        print("No rendered pages found. Run quarto render first.")
        return 1

    pages = {}
    errors = []
    for path in paths:
        parser = PageParser()
        parser.feed(path.read_text(encoding="utf-8"))
        pages[path.resolve()] = parser
        label = str(path.relative_to(site))
        if parser.heading_count != 1:
            errors.append(f"{label}: expected one h1, found {parser.heading_count}")
        for identifier in parser.duplicates:
            errors.append(f"{label}: duplicate ID {identifier}")
        for identifier in parser.accessible_references:
            if identifier not in parser.ids:
                errors.append(f"{label}: missing accessible target {identifier}")

    for path, parser in pages.items():
        label = str(path.relative_to(site))
        for reference in parser.references:
            if not reference:
                errors.append(f"{label}: empty link or asset reference")
                continue
            parts = urlsplit(reference)
            if parts.scheme or parts.netloc:
                continue  # Remote links are intentionally outside this local check.
            local_path = unquote(parts.path)
            if not local_path:
                target = path
            elif local_path.startswith("/"):
                target = (site / local_path.lstrip("/")).resolve()
            else:
                target = (path.parent / local_path).resolve()
            if not target.exists():
                errors.append(f"{label}: missing local target {reference}")
            elif parts.fragment and target in pages:
                identifier = unquote(parts.fragment)
                if identifier not in pages[target].ids:
                    errors.append(f"{label}: missing fragment {reference}")

    if errors:
        print("Site validation failed:")
        for error in errors:
            print("- " + error)
        return 1
    print(f"Checked {len(pages)} pages: local links, assets, heading counts and IDs are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
