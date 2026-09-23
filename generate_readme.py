import os
import re
import urllib.parse

def extract_metadata(filepath):
    """Scans the first 20 lines of a file for Difficulty and explicit Tags."""
    difficulty = ""
    tags = ""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for _ in range(20):
                line = f.readline()
                if not line:
                    break
                
                diff_match = re.search(r'#\s*Difficulty:\s*(.*)', line, re.IGNORECASE)
                tags_match = re.search(r'#\s*Tags:\s*(.*)', line, re.IGNORECASE)
                
                if diff_match: difficulty = diff_match.group(1).strip()
                if tags_match: tags = tags_match.group(1).strip()
    except Exception:
        pass

    if difficulty.lower() == 'easy':
        difficulty = '🟢 Easy'
    elif difficulty.lower() == 'medium':
        difficulty = '🟠 Medium'
    elif difficulty.lower() == 'hard':
        difficulty = '🔴 Hard'
        
    return difficulty, tags

def format_name(filename):
    """Cleans up the file name for display."""
    name = filename.replace('.py', '')
    name = name.replace('_', ' ')
    name = name.replace('-', ' ')
    return name.title()

def generate_folder_tags(root_path, base_dir):
    """Generates a list of tags by cleaning up the parent folder names."""
    rel_path = os.path.relpath(root_path, base_dir)
    if rel_path == '.':
        return []
        
    folders = rel_path.split(os.sep)
    tags = []
    
    for folder in folders:
        clean_folder = re.sub(r'^\d+_', '', folder)
        clean_folder = clean_folder.replace('_', ' ').title()
        tags.append(clean_folder)
        
    return tags

def get_problem_count(base_dir):
    """Counts the total number of .py files in the directory."""
    if not os.path.exists(base_dir):
        return 0
    
    count = 0
    for root, _, files in os.walk(base_dir):
        count += len([f for f in files if f.endswith('.py')])
    return count

def generate_progress_bar(solved, total=160, bar_length=10):
    """Generates a visual markdown progress bar."""
    filled_length = int(bar_length * solved // total)
    bar = '🟩' * filled_length + '⬜' * (bar_length - filled_length)
    percentage = round((solved / total) * 100, 1)
    
    return f"**Challenge Progress:** {bar} **[ {solved} / {total} ]** ({percentage}%)"

def generate_table_for_directory(base_dir):
    if not os.path.exists(base_dir):
        return ""
    
    output = ""
    categories = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))])
    
    for category in categories:
        cat_path = os.path.join(base_dir, category)
        clean_cat_name = category.split('_', 1)[-1] if '_' in category and base_dir == 'GfG_160' else category.replace('_', ' ').title()
        
        output += f"<details>\n<summary><b>{clean_cat_name}</b></summary>\n\n"
        output += "| # | Problem | Difficulty | Tags |\n|---|---|---|---|\n"
        
        count = 1
        for root, _, files in sorted(os.walk(cat_path)):
            py_files = sorted([f for f in files if f.endswith('.py')])
            for file in py_files:
                file_path = os.path.join(root, file).replace('\\', '/')
                
                target_link = file_path
                for readme_name in ['README.md', 'readme.md', 'Readme.md']:
                    potential_readme = os.path.join(root, readme_name)
                    if os.path.exists(potential_readme):
                        target_link = potential_readme.replace('\\', '/')
                        break
                
                # Encode the URL to safely handle spaces and parentheses
                target_link = urllib.parse.quote(target_link, safe='/')
                
                problem_name = format_name(file)
                diff, explicit_tags = extract_metadata(os.path.join(root, file))
                folder_tags = generate_folder_tags(root, base_dir)
                
                all_tags = []
                if explicit_tags:
                    all_tags.extend([t.strip() for t in explicit_tags.split(',')])
                
                for ft in folder_tags:
                    if ft not in all_tags and ft.lower() != problem_name.lower():
                        all_tags.append(ft)
                        
                final_tags = ", ".join(all_tags) if all_tags else "-"
                final_diff = diff if diff else "⚪ Unrated"
                
                output += f"| {count} | [{problem_name}]({target_link}) | {final_diff} | {final_tags} |\n"
                count += 1
                
        output += "\n</details>\n\n"
        
    return output

def update_readme():
    readme_path = 'README.md'
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Generate content
    gfg_table = generate_table_for_directory("GfG_160")
    hr_table = generate_table_for_directory("HackerRank")
    
    gfg_count = get_problem_count("GfG_160")
    gfg_progress_text = generate_progress_bar(gfg_count, total=160)
    
    # Inject Progress Bar
    content = re.sub(
        r'(<!-- GFG_PROGRESS_START -->).*?(<!-- GFG_PROGRESS_END -->)',
        f"\\1\n{gfg_progress_text}\n\\2",
        content,
        flags=re.DOTALL
    )

    # Inject Tables
    content = re.sub(
        r'(<!-- GFG_TABLE_START -->).*?(<!-- GFG_TABLE_END -->)',
        f"\\1\n\n{gfg_table}\\2",
        content,
        flags=re.DOTALL
    )
    
    content = re.sub(
        r'(<!-- HR_TABLE_START -->).*?(<!-- HR_TABLE_END -->)',
        f"\\1\n\n{hr_table}\\2",
        content,
        flags=re.DOTALL
    )
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    update_readme()