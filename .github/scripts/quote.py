"""Puts today's line from .github/quotes.txt between the quote markers in README.md."""
import datetime
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

root = pathlib.Path(__file__).resolve().parents[2]
quotes = [q.strip() for q in (root / ".github" / "quotes.txt").read_text(encoding="utf8").splitlines() if q.strip()]
today = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7))).date()
line = quotes[today.toordinal() % len(quotes)]
readme = root / "README.md"
text = readme.read_text(encoding="utf8")
block = f"<!-- quote:start -->\n> 💬 **Câu nói hôm nay:** {line}\n<!-- quote:end -->"
new, n = re.subn(r"<!-- quote:start -->.*?<!-- quote:end -->", lambda _: block, text, flags=re.S)
if n != 1:
    raise SystemExit("quote markers not found in README.md")
if new != text:
    readme.write_text(new, encoding="utf8", newline="\n")
    print("updated:", line)
else:
    print("unchanged")
