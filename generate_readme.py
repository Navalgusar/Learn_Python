import os
import re

def extract_metadata(filepath):
    """Scans the first 20 lines of a file for Difficulty and Tags comments."""
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

    # Format difficulty with visual indicators matching the reference UI
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

def generate_table_for_directory(base_dir, is_nested=False):
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
        # os.walk handles deeply nested structures like HR's 'basic_data_types/Finding_the_Percentage/'
        for root, _, files in sorted(os.walk(cat_path)):
            py_files = sorted([f for f in files if f.endswith('.py')])
            for file in py_files:
                file_path = os.path.join(root, file).replace('\\', '/')
                
                # Use filename as problem name as requested
                problem_name = format_name(file)
                
                diff, tags = extract_metadata(file_path)
                
                output += f"| {count} | [{problem_name}]({file_path}) | {diff} | {tags} |\n"
                count += 1
                
        output += "\n</details>\n\n"
        
    return output

def update_readme():
    readme_path = 'README.md'
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Generate tables
    gfg_table = generate_table_for_directory("GfG_160")
    hr_table = generate_table_for_directory("HackerRank")
    
    # Inject GfG
    content = re.sub(
        r'(<!-- GFG_TABLE_START -->).*?(<!-- GFG_TABLE_END -->)',
        f"\\1\n\n{gfg_table}\\2",
        content,
        flags=re.DOTALL
    )
    
    # Inject HackerRank
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