import re


def is_valid_slug(slug: str) -> bool:
    pattern = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
    return bool(pattern.match(slug))
