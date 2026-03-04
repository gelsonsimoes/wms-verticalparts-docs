import os

def fix_file(path):
    try:
        with open(path, 'rb') as f:
            content = f.read()
        
        # Try to decode as utf-8, if it fails, it might be the culprit
        text = content.decode('utf-8')
    except UnicodeDecodeError:
        # If it fails, try latin-1 which always succeeds
        text = content.decode('latin-1')
    
    # Replace the GitHub links
    text = text.replace('https://github.com/gelsonsimoes/wms-verticalparts', 'https://www.wmsverticalparts.com.br')
    text = text.replace('GitHub Web', 'Site Oficial')
    text = text.replace('GitHub', 'Site Oficial')
    
    # Common mangled characters fix
    replacements = {
        'Ã­': 'í',
        'Ã§Ã£': 'çã',
        'Ãµ': 'õ',
        'Ãª': 'ê',
        'Ã¡': 'á',
        'Ã ': 'à',
        'Ã³': 'ó',
        'Ãº': 'ú',
        'Ã¢': 'â',
        'Ã': 'í', # Special case for InÃcio -> Início
        'â€”': '—',
        'Ã§': 'ç',
        'Ã£': 'ã',
        'ðŸ’¡': '💡',
        'âœ“': '✓'
    }
    
    # Instead of manual replacements, let's just make sure we are writing clean UTF-8
    # If the text was double encoded, this might be tricky.
    # The best way is to redefine the menu links in the script.
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Fixed: {path}")

# Run for index.html
fix_file('c:/Users/gelso/Projetos_Antigravity/wms_blog_verticalparts/wms-verticalparts-docs/index.html')

# Run for all html files in paginas
for root, dirs, files in os.walk('c:/Users/gelso/Projetos_Antigravity/wms_blog_verticalparts/wms-verticalparts-docs/paginas'):
    for file in files:
        if file.endswith('.html'):
            fix_file(os.path.join(root, file))
