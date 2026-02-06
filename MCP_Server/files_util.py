import os
from typing import Dict, List
from dotenv import load_dotenv

load_dotenv()

def read_lines(path: str) -> List[str]:
    """
    Reads and returns all lines from a file at the given absolute path
    
    :param path: Path to the file to read lines from
    :type path: str
    :return: List of lines read from the file
    :rtype: List[str]
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []


def load_config() -> Dict[str, str]:
    return {
        "notes_dir_path": os.getenv("NOTES_DIR_PATH", "."),
    }

  
def normalize_rel_path(path: str) -> str:
    """
    Expands and normalizes a relative path within the notes directory
    
    :param path: Potentially relative path as a string
    :type path: str
    :return: Expanded absolute path within the notes directory
    :rtype: str
    """
    path = (path or "").strip().replace("\\", "/")
    if ".." in path:
        raise ValueError(f"Path escapes notes directory: {path}")
    
    if not path.endswith((".md", ".markdown")):
        path += ".md"
    
    if path.startswith("/"):
        return path
    else:
        cfg = load_config()
        notes_dir_path = cfg.get("notes_dir_path", ".")
        return os.path.join(notes_dir_path, path)

class TextHeader:
    def __init__(self, level: int, header: str, line_number: int):
        self.level = level
        self.header = header
        self.line_number = line_number

def extract_headers(full_path: str) -> list[TextHeader]:
    """
    Extract headers from a markdown file.
    """
    lines = read_lines(full_path)
    headers: list[TextHeader] = []
    in_code_block = False

    for i, line in enumerate(lines):
        line = line.strip()
        if line.startswith("```"):
            in_code_block = not in_code_block
            continue

        if in_code_block or not line.startswith("#"):
            continue

        hashes = len(line) - len(line.lstrip("#"))
        headers.append(TextHeader(hashes, line[hashes:].strip(), i))

    return headers