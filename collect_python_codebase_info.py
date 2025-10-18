import os
from pathlib import Path

def generate_tree_structure(root_dir, prefix="", is_last=True, max_depth=None, current_depth=0):
    """
    Generate a visual tree structure of the directory.
    Like drawing a family tree, but for your project files.
    """
    lines = []
    root_path = Path(root_dir)
    
    if current_depth == 0:
        lines.append(f"📁 {root_path.name}/\n")
    
    if max_depth and current_depth >= max_depth:
        return lines
    
    try:
        items = sorted(root_path.iterdir(), key=lambda x: (not x.is_dir(), x.name))
        items = [item for item in items if not item.name.startswith('.')]
        
        for i, item in enumerate(items):
            is_last_item = (i == len(items) - 1)
            connector = "└── " if is_last_item else "├── "
            
            if item.is_dir():
                lines.append(f"{prefix}{connector}📁 {item.name}/\n")
                extension = "    " if is_last_item else "│   "
                lines.extend(generate_tree_structure(
                    item, 
                    prefix + extension, 
                    is_last_item,
                    max_depth,
                    current_depth + 1
                ))
            else:
                icon = "🐍" if item.suffix == '.py' else "📄"
                lines.append(f"{prefix}{connector}{icon} {item.name}\n")
    
    except PermissionError:
        pass
    
    return lines

def get_human_comment(filepath):
    """
    Pause and ask the human for their insights.
    Like a tour guide asking 'Any questions about this exhibit?'
    """
    print(f"\n{'='*60}")
    print(f"📝 File: {filepath}")
    print(f"{'='*60}")
    comment = input("Add a comment for this file (press Enter to skip): ").strip()
    return comment

def collect_python_codebase_info(
    root_dir='.', 
    output_file='codebase_documentation.md',
    ask_for_comments=True,
    include_tree=True,
    tree_depth=None
):
    """
    Collect Python codebase information and generate markdown documentation.
    
    Parameters:
    - root_dir: Starting directory to scan
    - output_file: Output markdown file name
    - ask_for_comments: Whether to ask for human input for each file
    - include_tree: Whether to include directory tree structure
    - tree_depth: Maximum depth for tree structure (None = unlimited)
    """
    python_files = []
    file_comments = {}
    
    # First pass: collect all Python files
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip hidden directories
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        
        py_files = [f for f in filenames if f.endswith('.py')]
        for filename in py_files:
            filepath = os.path.join(dirpath, filename)
            python_files.append(filepath)
    
    print(f"\n🔍 Found {len(python_files)} Python files")
    
    # Get human comments if requested
    if ask_for_comments and python_files:
        print("\n📋 Let's add some developer notes to your documentation!")
        print("(You can skip any file by pressing Enter)\n")
        
        for filepath in python_files:
            comment = get_human_comment(filepath)
            if comment:
                file_comments[filepath] = comment
    
    # Generate markdown documentation
    with open(output_file, 'w', encoding='utf-8') as f:
        # Header
        f.write("# Python Codebase Documentation\n\n")
        f.write(f"**Root Directory:** `{os.path.abspath(root_dir)}`\n\n")
        f.write(f"**Total Python Files:** {len(python_files)}\n\n")
        f.write("---\n\n")
        
        # Directory Tree
        if include_tree:
            f.write("## 📂 Project Structure\n\n")
            f.write("```\n")
            tree_lines = generate_tree_structure(root_dir, max_depth=tree_depth)
            f.writelines(tree_lines)
            f.write("```\n\n")
            f.write("---\n\n")
        
        # Table of Contents
        f.write("## 📑 Table of Contents\n\n")
        for i, filepath in enumerate(python_files, 1):
            # Create anchor-friendly link
            anchor = filepath.replace(os.sep, '-').replace('.', '-')
            f.write(f"{i}. [{filepath}](#{anchor})\n")
        f.write("\n---\n\n")
        
        # File Contents
        f.write("## 📄 Source Files\n\n")
        
        for filepath in python_files:
            # Create anchor for TOC linking
            anchor = filepath.replace(os.sep, '-').replace('.', '-')
            
            f.write(f"### {filepath}\n\n")
            
            # Add developer comment if exists
            if filepath in file_comments:
                f.write(f"> 💬 **Developer Note:** {file_comments[filepath]}\n\n")
            
            # File metadata
            try:
                file_size = os.path.getsize(filepath)
                f.write(f"**Size:** {file_size} bytes\n\n")
            except:
                pass
            
            # Source code
            f.write("```python\n")
            try:
                with open(filepath, 'r', encoding='utf-8') as file_content:
                    f.write(file_content.read())
            except Exception as e:
                f.write(f"# Could not read file: {e}\n")
            f.write("\n```\n\n")
            f.write("---\n\n")
    
    print(f"\n✅ Documentation generated: {output_file}")
    print(f"📊 Documented {len(python_files)} files")
    if file_comments:
        print(f"💬 Added {len(file_comments)} developer comments")

if __name__ == "__main__":
    # Example usage with customization options
    collect_python_codebase_info(
        root_dir='.',
        output_file='codebase_documentation.md',
        ask_for_comments=True,  # Set to False to skip human input
        include_tree=True,       # Set to False to skip directory tree
        tree_depth=3            # Limit tree depth (None for unlimited)
    )
