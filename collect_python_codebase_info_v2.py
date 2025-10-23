import os
from pathlib import Path
from dataclasses import dataclass, field

@dataclass
class FileDocumentation:
    """A data class to hold information for a single documented file."""
    path: Path
    comment: str = ""
    include_content: bool = True

def generate_tree(root_path: Path, prefix: str = "", max_depth: int = None, current_depth: int = 0):
    """Generates a directory tree structure using a generator."""
    if current_depth == 0:
        yield f"📁 {root_path.name}/"
    if max_depth is not None and current_depth >= max_depth:
        return

    # Filter out hidden files/dirs and sort dirs first, then files
    try:
        items = sorted(
            [p for p in root_path.iterdir() if not p.name.startswith('.')],
            key=lambda p: (not p.is_dir(), p.name.lower())
        )
    except PermissionError:
        return

    for i, item in enumerate(items):
        is_last = (i == len(items) - 1)
        connector = "└── " if is_last else "├── "
        
        if item.is_dir():
            yield f"{prefix}{connector}📁 {item.name}/"
            extension = "    " if is_last else "│   "
            yield from generate_tree(item, prefix + extension, max_depth, current_depth + 1)
        else:
            icon = "🐍" if item.suffix == '.py' else "📄"
            yield f"{prefix}{connector}{icon} {item.name}"

def get_user_feedback(filepath: Path) -> tuple[str, bool]:
    """Asks the user for a comment and whether to include the file's content."""
    print(f"\n{'='*60}\n📝 File: {filepath}\n{'='*60}")
    comment = input("Add a comment for this file (or press Enter to skip): ").strip()
    
    include_choice = input("Include this file's content in the doc? [Y/n]: ").strip().lower()
    include_content = include_choice != 'n'
    
    return comment, include_content

def create_codebase_documentation(
    root_dir: str = '.',
    output_file: str = 'codebase_documentation.md',
    ask_for_feedback: bool = True,
    include_tree: bool = True,
    tree_depth: int = None
):
    """
    Scans a Python codebase, optionally gathers human feedback, and generates
    comprehensive markdown documentation.
    """
    root_path = Path(root_dir).resolve()
    documented_files = []

    # 1. Find all Python files, skipping hidden directories
    all_py_files = [
        p for p in root_path.rglob('*.py')
        if not any(part.startswith('.') for part in p.parts)
    ]
    print(f"🔍 Found {len(all_py_files)} Python files.")

    # 2. Gather user feedback for each file if requested
    if ask_for_feedback and all_py_files:
        print("\n📋 Let's add some notes to your documentation!")
        for path in sorted(all_py_files):
            comment, include_content = get_user_feedback(path)
            documented_files.append(FileDocumentation(path, comment, include_content))
    else:
        documented_files = [FileDocumentation(path) for path in sorted(all_py_files)]

    # 3. Generate the markdown documentation
    with open(output_file, 'w', encoding='utf-8') as f:
        # --- Header ---
        f.write(f"# Python Codebase Documentation\n\n"
                f"**Root Directory:** `{root_path}`\n"
                f"**Total Python Files:** {len(documented_files)}\n\n---\n\n")

        # --- Project Structure Tree ---
        if include_tree:
            f.write("## 📂 Project Structure\n\n```\n")
            tree_lines = list(generate_tree(root_path, max_depth=tree_depth))
            f.write("\n".join(tree_lines))
            f.write("\n```\n\n---\n\n")

        # --- Table of Contents ---
        f.write("## 📑 Table of Contents\n\n")
        for i, doc in enumerate(documented_files, 1):
            relative_path = doc.path.relative_to(root_path.parent)
            anchor = str(relative_path).replace(os.sep, '-').replace('.', '-')
            f.write(f"{i}. [{relative_path}](#{anchor})\n")
        f.write("\n---\n\n")

        # --- Source Files Details ---
        f.write("## 📄 Source Files\n\n")
        for doc in documented_files:
            relative_path = doc.path.relative_to(root_path.parent)
            anchor = str(relative_path).replace(os.sep, '-').replace('.', '-')
            
            f.write(f"### <a name=\"{anchor}\"></a>{relative_path}\n\n")
            
            if doc.comment:
                f.write(f"> 💬 **Developer Note:** {doc.comment}\n\n")

            if not doc.include_content:
                f.write("*File content intentionally excluded by user.*\n\n---\n\n")
                continue

            try:
                f.write(f"**Size:** {doc.path.stat().st_size} bytes\n\n")
                f.write("```python\n")
                f.write(doc.path.read_text(encoding='utf-8'))
                f.write("\n```\n\n")
            except Exception as e:
                f.write(f"```\n# Could not read file: {e}\n```\n\n")
            
            f.write("---\n\n")

    print(f"\n✅ Documentation generated: {output_file}")
    print(f"📊 Documented {len(documented_files)} files.")
    comments_added = sum(1 for doc in documented_files if doc.comment)
    if comments_added:
        print(f"💬 Added {comments_added} developer comments.")

if __name__ == "__main__":
    create_codebase_documentation(
        root_dir='.',
        output_file='condensed_codebase_doc.md',
        ask_for_feedback=True,  # Set to False to skip all human input
        include_tree=True,      # Set to False to skip directory tree
        tree_depth=3            # Set to None for unlimited tree depth
    )