import os

base_dir = os.getcwd()

# Data structure matching user's numbering (Principal=1, Operar=2, Planejar=3...)
sections = [
    {
        "name": "Principal",
        "prefix": "1",
        "items": [
            ("dashboard.html", "1.1 Dashboard Geral", "paginas/01-principal/"),
        ]
    },
    {
        "name": "Operar",
        "prefix": "2",
        "items": [
            ("cruzar-docas-interativo.html", "2.1 Cruzar Docas Interativo", "paginas/02-operar/"),
            ("devolucoes-interativo.html", "2.2 Processar Devoluções Interativo", "paginas/02-operar/"),
            ("pesar-cargas.html", "2.3 Pesar Cargas", "paginas/02-operar/"),
            ("recebimento.html", "2.4 Gerenciar Recebimento", "paginas/02-operar/"),
            ("conferir-recebimento.html", "2.5 Conferir Recebimento", "paginas/02-operar/"),
            ("mapa-alocacao.html", "2.6 Gerar Mapa de Alocação", "paginas/02-operar/"),
            ("conferencia-cega.html", "2.7 Conferência Cega", "paginas/02-operar/"),
            ("alocar-estoque.html", "2.8 Alocar Estoque", "paginas/02-operar/"),
            ("kanban.html", "2.9 Kanban de Alocação", "paginas/02-operar/"),
            ("separar-pedidos.html", "2.10 Separar Pedidos", "paginas/02-operar/"),
            ("embalar.html", "2.11 Embalar Pedidos", "paginas/02-operar/"),
            ("saida.html", "2.12 Monitorar Saída", "paginas/02-operar/"),
            ("checkin.html", "2.13 Check-in Recebimento", "paginas/02-operar/"),
            ("kits.html", "2.14 Estação de Kits", "paginas/02-operar/"),
            ("colmeia.html", "2.15 Conferência Colmeia", "paginas/02-operar/"),
            ("mapa-visual.html", "2.16 Mapa Visual Estoque", "paginas/02-operar/"),
            ("buffer1.html", "2.17 Buffer 1", "paginas/02-operar/"),
            ("buffer2.html", "2.18 Buffer 2", "paginas/02-operar/"),
            ("ordem-servico.html", "2.19 Ordem de Serviço", "paginas/02-operar/"),
            ("seguros.html", "2.20 Gestão de Seguros", "paginas/02-operar/"),
            ("pesagem-rodoviaria.html", "2.21 Pesagem Rodoviária", "paginas/02-operar/"),
        ]
    }
]

# We will generate the index.html as well to include the interactive tutorials.

def get_sidebar_html(rel):
    sb = ""
    for sec in sections:
        sb += f'    <div class="group-title">{sec["name"]}</div>\n'
        for f, t, p in sec["items"]:
            # Correct path construction
            path = f"{rel}{p}{f}"
            sb += f'    <a href="{path}">{t}</a>\n'
    return sb

def get_html(title, depth=2):
    rel = "../../" if depth == 2 else ""
    # Special theme for Interactive pages
    is_interactive = "Interativo" in title
    bg_style = 'style="background: #0f172a; color: white;"' if is_interactive else ""
    card_style = 'style="background: #1e293b; border-color: #334155; color: #e2e8f0;"' if is_interactive else ""
    title_style = 'style="color: #fbbf24; border-left-color: #fbbf24;"' if is_interactive else ""
    
    return f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — WMS VerticalParts Docs</title>
  <link rel="stylesheet" href="{rel}assets/css/style.css">
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;900&display=swap" rel="stylesheet">
</head>
<body {bg_style}>
<header class="site-header" {'style="background:#0f172a; border-bottom:1px solid #1e293b;"' if is_interactive else ""}>
  <div class="logo">VerticalParts <span>WMS Docs</span></div>
  <nav>
    <a href="{rel}index.html">Início</a>
    <a href="{rel}paginas/02-operar/cruzar-docas-interativo.html">Operação</a>
    <a href="{rel}paginas/mobile/login.html">Mobile</a>
    <a href="https://www.wmsverticalparts.com.br" target="_blank">Site Oficial</a>
  </nav>
</header>
<div class="layout">
  <nav class="sidebar" {'style="background:#0f172a; border-right:1px solid #1e293b;"' if is_interactive else ""}>
{get_sidebar_html(rel)}
  </nav>
  <main class="content" {'style="background:#0f172a;"' if is_interactive else ""}>
    <div class="tutorial-card" {card_style}>
      <h3 {title_style}>{title} — Manual do Usuário</h3>
      <p>Esta página descreve as funcionalidades e o fluxo de operação do módulo <strong>{title}</strong>.</p>
      
      <div class="demo-wrap" style="background: #0d1117; border-radius: 10px; padding: 20px; text-align: center; margin: 20px 0;">
        <div class="demo-label" style="background:#fbbf24; color:#000; font-size:10px; font-weight:700; padding:4px 12px; border-radius:4px; display:inline-block; margin-bottom:15px; letter-spacing:1px;">DEMONSTRAÇÃO VISUAL</div>
        <div style="background: #f8f9fa; height: 300px; border-radius: 20px; display: flex; align-items: center; justify-content: center; color: #adb5bd; font-family: 'Poppins', sans-serif; font-size: 14px; font-weight: 700; text-transform: uppercase;">
           Aguardando Imagem/GIF
        </div>
      </div>

      <h2>Fluxo de Trabalho</h2>
      <ul class="steps">
        <li>Acesse o menu lateral e clique em <strong>{title}</strong>.</li>
        <li>Utilize os filtros de pesquisa para localizar os registros desejados.</li>
        <li>Realize a operação conforme as regras de negócio da VerticalParts.</li>
        <li>Confirme as alterações para sincronizar com o WMS Central.</li>
      </ul>
    </div>
  </main>
</div>
<footer {'style="background:#0f172a; border-top:1px solid #1e293b;"' if is_interactive else ""}>
  <p>WMS VerticalParts Docs — Atualizado a cada versão — <a href="https://www.wmsverticalparts.com.br" target="_blank">wmsverticalparts.com.br</a></p>
</footer>
<script src="{rel}assets/js/main.js"></script>
</body>
</html>
"""

# Regenerate regular pages (skip the ones we manually built custom)
custom_files = ["cruzar-docas-interativo.html", "devolucoes-interativo.html", "demo.html"]

for section in sections:
    for item_file, item_title, folder in section["items"]:
        if item_file in custom_files: continue
        
        full_path = os.path.join(base_dir, folder, item_file)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(get_html(item_title))

print("Pages updated. Running image insertion...")
# Skip image insertion for interactive pages as they handle their own images.
