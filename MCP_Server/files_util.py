import os
from typing import Dict, List, Optional
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


def write_lines(path: str, content: List[str]) -> None:
    """
    Writes lines to a file at the given absolute path
    
    :param path: Path to the file to write lines to
    :type path: str
    :param content: List of lines to write to the file
    :type content: List[str]
    """
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(content)


def insert_lines_at(path: str, line_number: int, content: List[str]) -> None:
    """
    Inserts lines at a specific line number in a file
    
    :param path: Path to the file to modify
    :type path: str
    :param line_number: Line number where to insert content (0-indexed)
    :type line_number: int
    :param content: List of lines to insert
    :type content: List[str]
    """
    existing_lines = read_lines(path)
    write_lines(path, existing_lines[:line_number] + content + existing_lines[line_number:])

def append_lines(path: str, content: List[str]) -> None:
    existing_lines = read_lines(path)
    write_lines(path, existing_lines + content)

def load_config() -> Dict[str, str]:
    return {
        "notes_dir_path": os.getenv("NOTES_DIR_PATH", "./FakeNotes/"),
        "tasks_file_path": os.getenv("TASKS_FILE_PATH", "./FakeNotes/tasks.md"),
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
    
    if path == ".":
        path = "./"
    
    if path.startswith("/"):
        return path
    else:
        cfg = load_config()
        notes_dir_path = cfg.get("notes_dir_path", "./FakeNotes/")
        return os.path.join(notes_dir_path, path)

class TextHeader:
    def __init__(self, level: int, header: str, line_number: int):
        self.level = level
        self.header = header
        self.line_number = line_number

def extract_header(full_path: str, header_name: str) -> TextHeader | None:
    lines = read_lines(full_path)
    headers: list[TextHeader] = []
    in_code_block = False
    header_name = header_name.strip().lower()

    for i, line in enumerate(lines):
        line = line.strip()
        if line.startswith("```"):
            in_code_block = not in_code_block
            continue

        if in_code_block or not line.startswith("#"):
            continue

        hashes = len(line) - len(line.lstrip("#"))
        if line[hashes:].strip().lower() == header_name:
            return TextHeader(hashes, line[hashes:].strip(), i)

    return None

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

def format_task_lines(task_header: str, subtasks: Optional[List[str]]) -> List[str]:
    lines: List[str] = [f"- [ ] {task_header}\n"]
    if not subtasks:
        return lines
    for s in subtasks:
        s_clean = s.strip()
        lines.append(f"    - [ ] {s_clean}\n")
    return lines

def get_note_property(full_path: str, property_name: str) -> Optional[str]:
    """
    Extract a property value from the front matter of a markdown file.
    Assumes front matter is in YAML format and delimited by '---' lines.
    """
    lines = read_lines(full_path)
    in_front_matter = False
    property_name = property_name.strip().lower()

    for line in lines:
        line = line.strip()
        if line == "---":
            in_front_matter = not in_front_matter
            continue

        if not in_front_matter:
            continue

        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        if key.strip().lower() == property_name:
            return value.strip()

    return None