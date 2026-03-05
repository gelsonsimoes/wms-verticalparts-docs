import os
import re

# Directory paths
base_dir = r'c:\Users\gelso\Projetos_Antigravity\wms_blog_verticalparts\wms-verticalparts-docs'
screenshots_dir = os.path.join(base_dir, 'assets', 'img', 'screenshots')
paginas_dir = os.path.join(base_dir, 'paginas')

# List all screenshots
screenshots = os.listdir(screenshots_dir)

# Mapping of section names to numbers based on user's files
section_mapping = {
    "Principal": "1",
    "Operar": "1",
    "Planejar": "2",
    "Controlar": "3",
    "Fiscal": "4",
    "Financeiro": "5",
    "Cadastrar": "6",
    "Indicadores": "7",
    "Integrar": "8",
    "Configurar": "9",
    "Segurança": "10",
    "Mobile": "Mobile"
}

def clean_name(name):
    # Remove numbering and extension to get the module name
    name = re.sub(r'^\d+\.\d+\s+', '', name)
    name = os.path.splitext(name)[0]
    return name.strip().lower()

# Create a map of clean names to real screenshot paths
screenshot_map = {}
for s in screenshots:
    c_name = clean_name(s)
    screenshot_map[c_name] = s

print(f"Mapped {len(screenshot_map)} screenshots.")

def update_html_file(file_path):
    with open(file_path, 'rb') as f:
        content = f.read()
    try:
        text = content.decode('utf-8')
    except:
        text = content.decode('latin-1')

    modified = False
    
    # Extract the module name from the h3 tag
    h3_match = re.search(r'<h3>(.*?)\s*—\s*Manual do Usuário</h3>', text)
    if h3_match:
        full_title = h3_match.group(1)
        # Clean title to get module name
        module_name = re.sub(r'^\d+\.\d+\s+', '', full_title).strip().lower()
        
        # Look for a matching screenshot
        if module_name in screenshot_map:
            screenshot_file = screenshot_map[module_name]
            
            # Decide relative path based on file depth
            # Files in paginas/XX/YYY.html need ../../assets/...
            depth = file_path.replace(base_dir, '').count(os.sep)
            rel_prefix = '../' * (depth - 1)
            img_path = f"{rel_prefix}assets/img/screenshots/{screenshot_file}"
            
            # Find the placeholder div
            placeholder_pattern = r'<div style="background: #f8f9fa; height: 300px;.*?</div>\s*</div>'
            # Replacement image tag with zoom/hover effects or just nice styling
            replacement = f'''<img src="{img_path}" alt="{full_title}" style="width: 100%; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border: 1px solid #eee; transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
        </div>'''
            
            new_text = re.sub(placeholder_pattern, replacement, text, flags=re.DOTALL)
            if new_text != text:
                text = new_text
                modified = True
                print(f"Inserted image for {module_name} in {os.path.basename(file_path)}")

    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(text)

# Process all HTML files
for root, dirs, files in os.walk(paginas_dir):
    for file in files:
        if file.endswith('.html'):
            update_html_file(os.path.join(root, file))

# Also fix the numbering in sidebar and titles to match user's naming (Operar=1, etc)
# But only if it's strictly necessary. Let's see if we can do it safely.
# For now, let's just insert the images as requested.

print("Image insertion complete.")
