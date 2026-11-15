"""Audit the built public site for identity, review markers, and broken local links."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import json
import re


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
HOST = "tongfu0414.github.io"


class Document(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.errors = []
        self.review_count = 0
        self.h1_count = 0

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        ident = attrs.get("id")
        if ident:
            if ident in self.ids:
                self.errors.append(f"Duplicate id: {ident}")
            self.ids.add(ident)
        if tag == "h1":
            self.h1_count += 1
        if "needs-confirmation" in attrs.get("class", "").split():
            self.review_count += 1
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])
        if tag == "img" and "alt" not in attrs:
            self.errors.append("Image lacks alternative text")


def verify():
    if not (SITE / "index.html").is_file():
        raise SystemExit("Build the Jekyll site first.")
    problems = []
    documents = {}
    forbidden = re.compile(
        r"flagcounter|cloud\.umami\.is|github-contributions\.svg|"
        r"Evidence_Transcript|Paper Password",
        re.IGNORECASE,
    )
    for path in SITE.rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        if forbidden.search(text):
            problems.append(f"Inherited identity or private content: {path.relative_to(SITE)}")
        doc = Document()
        doc.feed(text)
        documents[path.resolve()] = doc
        problems.extend(f"{path.relative_to(SITE)}: {error}" for error in doc.errors)
    for path, doc in documents.items():
        relative = path.relative_to(SITE.resolve()).as_posix()
        page_url = "/" + relative
        if page_url.endswith("index.html"):
            page_url = page_url[: -len("index.html")]
        for link in doc.links:
            url = urlsplit(urljoin(f"https://{HOST}{page_url}", link))
            if url.scheme not in ("http", "https") or url.netloc.lower() != HOST:
                continue
            target = (SITE / unquote(url.path).lstrip("/")).resolve()
            if target.is_dir():
                target /= "index.html"
            if not target.is_file():
                problems.append(f"{relative}: missing local target {link}")
            elif url.fragment and target.suffix == ".html":
                target_doc = documents.get(target)
                if target_doc and unquote(url.fragment) not in target_doc.ids:
                    problems.append(f"{relative}: missing anchor {link}")
    for name in ("index.html", "zh/index.html"):
        doc = documents.get((SITE / name).resolve())
        if not doc or doc.h1_count != 1 or doc.review_count < 8:
            problems.append(f"{name}: missing heading or expected review highlights")
    for name in ("local", "docs", "scripts", "AGENTS.md", "Gemfile", "Gemfile.lock", "README.md"):
        if (SITE / name).exists():
            problems.append(f"Private or development material published: {name}")
    print(json.dumps({"html_pages": len(documents), "problems": problems}, ensure_ascii=False))
    if problems:
        raise SystemExit(1)


if __name__ == "__main__":
    verify()
