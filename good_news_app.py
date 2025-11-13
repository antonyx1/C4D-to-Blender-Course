"""Simple CLI application that shares only good news stories.

The script loads a curated list of positive stories from ``data/good_news.json``
and can either display a random item or list multiple entries filtered by
category or text search.
"""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from typing import Iterable, List, Sequence


DATA_PATH = Path(__file__).with_name("data") / "good_news.json"


def load_news() -> List[dict]:
    """Load the curated list of good news stories from disk."""

    with DATA_PATH.open("r", encoding="utf-8") as source:
        return json.load(source)


def normalize(text: str) -> str:
    return text.strip().lower()


def filter_by_category(news: Sequence[dict], category: str | None) -> List[dict]:
    if not category:
        return list(news)

    target = normalize(category)
    return [
        story
        for story in news
        if any(normalize(cat) == target for cat in story.get("categories", []))
    ]


def filter_by_search(news: Iterable[dict], query: str | None) -> List[dict]:
    if not query:
        return list(news)

    target = normalize(query)
    return [
        story
        for story in news
        if target in normalize(story.get("title", ""))
        or target in normalize(story.get("summary", ""))
    ]


def format_story(story: dict) -> str:
    categories = ", ".join(story.get("categories", [])) or "good vibes"
    source = story.get("source", "")
    details = [story["title"], f"Categorie: {categories}"]
    details.append(story.get("summary", ""))
    if source:
        details.append(f"Fonte: {source}")
    return "\n".join(details)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Condividi solo buone notizie direttamente dal tuo terminale."
    )
    parser.add_argument(
        "--category",
        help="Mostra solo notizie appartenenti alla categoria indicata (es. natura, scienza).",
    )
    parser.add_argument(
        "--search",
        help="Filtra le notizie che contengono il testo indicato nel titolo o nel riassunto.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="Elenca tutte le notizie filtrate invece di mostrarne una casuale.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=5,
        help="Numero massimo di notizie da mostrare quando si usa --list (default: 5).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    news = filter_by_search(filter_by_category(load_news(), args.category), args.search)

    if not news:
        print("Nessuna buona notizia corrisponde ai filtri scelti, riprova!")
        return

    if args.list:
        for story in news[: max(args.limit, 1)]:
            print(format_story(story))
            print("-" * 60)
    else:
        story = random.choice(news)
        print(format_story(story))


if __name__ == "__main__":
    main()
