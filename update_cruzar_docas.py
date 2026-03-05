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
            ("cruzar-docas.html", "2.1 Cruzar Docas", "paginas/02-operar/"),
            ("devolucoes.html", "2.2 Processar Devoluções", "paginas/02-operar/"),
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
    },
    {
        "name": "Planejar",
        "prefix": "3",
        "items": [
            ("ondas.html", "3.1 Gerar Ondas de Separação", "paginas/03-planejar/"),
            ("sla.html", "3.2 Monitorar Prazos (SLA)", "paginas/03-planejar/"),
            ("transportes.html", "3.3 Agendar Transportes", "paginas/03-planejar/"),
            ("atividades.html", "3.4 Monitorar Atividades", "paginas/03-planejar/"),
            ("manifestos.html", "3.5 Gerenciar Manifestos", "paginas/03-planejar/"),
            ("expedir.html", "3.6 Expedir Cargas", "paginas/03-planejar/"),
            ("portaria.html", "3.7 Gerenciar Portaria", "paginas/03-planejar/"),
            ("docas.html", "3.8 Atividades de Docas", "paginas/03-planejar/"),
        ]
    },
    {
        "name": "Controlar",
        "prefix": "4",
        "items": [
            ("inventario.html", "4.1 Auditar Inventário", "paginas/04-controlar/"),
            ("kardex.html", "4.2 Consultar Kardex", "paginas/04-controlar/"),
            ("analisar.html", "4.3 Analisar Estoque", "paginas/04-controlar/"),
            ("remanejar.html", "4.4 Remanejar Produtos", "paginas/04-controlar/"),
            ("lotes.html", "4.5 Controlar Lotes e Validade", "paginas/04-controlar/"),
            ("avarias.html", "4.6 Monitorar Avarias", "paginas/04-controlar/"),
            ("gestao-inventario.html", "4.7 Gestão de Inventário", "paginas/04-controlar/"),
        ]
    },
    {
        "name": "Fiscal",
        "prefix": "5",
        "items": [
            ("nfe.html", "5.1 Gerenciar NF-e", "paginas/05-fiscal/"),
            ("cte.html", "5.2 Gerenciar CT-e", "paginas/05-fiscal/"),
            ("cobertura.html", "5.3 Emitir Cobertura Fiscal", "paginas/05-fiscal/"),
            ("armazem-geral.html", "5.4 Armazém Geral", "paginas/05-fiscal/"),
        ]
    },
    {
        "name": "Financeiro",
        "prefix": "6",
        "items": [
            ("diarias.html", "6.1 Calcular Diárias", "paginas/06-financeiro/"),
            ("contratos.html", "6.2 Gerenciar Contratos", "paginas/06-financeiro/"),
        ]
    },
    {
        "name": "Cadastrar",
        "prefix": "7",
        "items": [
            ("empresas.html", "7.1 Gerenciar Empresas", "paginas/07-cadastrar/"),
            ("armazens.html", "7.2 Configurar Armazéns", "paginas/07-cadastrar/"),
            ("enderecos.html", "7.3 Cadastrar Endereços", "paginas/07-cadastrar/"),
            ("produtos.html", "7.4 Catálogo de Produtos", "paginas/07-cadastrar/"),
            ("rotas.html", "7.5 Rotas e Veículos", "paginas/07-cadastrar/"),
            ("areas.html", "7.6 Configurar Áreas", "paginas/07-cadastrar/"),
            ("setores.html", "7.7 Configurar Setores", "paginas/07-cadastrar/"),
            ("etiquetas.html", "7.8 Gerenciar Etiquetas", "paginas/07-cadastrar/"),
        ]
    }
]

# Sidebar helper
def get_sidebar_html(rel):
    sb = ""
    for sec in sections:
        sb += f'    <div class="group-title">{sec["name"]}</div>\n'
        for f, t, p in sec["items"]:
            sb += f'    <a href="{rel}{p}{f}">{t}</a>\n'
    return sb

# Update index.html
index_nav = ""
for sec in sections:
    for f, t, p in sec["items"][:1]: # Show first of each section as card
        # Map icon
        icon = "📦"
        if sec["name"] == "Operar": icon = "📥"
        elif sec["name"] == "Planejar": icon = "📋"
        elif sec["name"] == "Controlar": icon = "📊"
        elif sec["name"] == "Fiscal": icon = "🧾"
        elif sec["name"] == "Financeiro": icon = "💰"
        elif sec["name"] == "Cadastrar": icon = "🗂️"
        
        index_nav += f'''      <a class="nav-card" href="{p}{f}">
        <div class="icon">{icon}</div>
        <h4>{sec["name"]}</h4>
        <p>Acesse os tutoriais do módulo {sec["name"].lower()}.</p>
      </a>\n'''

# We won't regenerate everything if it exists and has custom content, 
# but for now let's just create the specialized Cruzar Docas page.

# Special page Cruzar Docas
cruzar_docas_content = """<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>2.1 Cruzar Docas — WMS VerticalParts Docs</title>
  <link rel="stylesheet" href="../../assets/css/style.css">
</head>
<body>
<header class="site-header">
  <div class="logo">VerticalParts <span>WMS Docs</span></div>
  <nav>
    <a href="../../index.html">Início</a>
    <a href="../02-operar/recebimento.html">Operação</a>
    <a href="../mobile/login.html">Mobile</a>
    <a href="https://www.wmsverticalparts.com.br" target="_blank">Site Oficial</a>
  </nav>
</header>
<div class="layout">
  <nav class="sidebar">
""" + get_sidebar_html("../../") + """
  </nav>
  <main class="content">
    <div class="tutorial-card">
      <div class="breadcrumb">Operação > Transbordo Móvel</div>
      <h3>2.1 Cruzar Docas — Manual do Usuário</h3>
      <p>O módulo de <strong>Cruzar Docas (Cross-Docking)</strong> permite o monitoramento em tempo real do fluxo de transbordo, onde mercadorias recém-recebidas são enviadas diretamente para a expedição sem passar pela armazenagem convencional.</p>
      
      <div class="demo-wrap">
        <div class="demo-label">Demonstração Visual</div>
        <img src="../../assets/img/screenshots/2.1 Cruzar Docas .png" alt="Tela de Cruzar Docas" style="width: 100%; border-radius: 20px; box-shadow: 0 20px 50px rgba(0,0,0,0.15); border: 1px solid #ddd;">
      </div>

      <div class="features-grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 30px;">
        <div class="f-item" style="background: #fff8e1; p: 20px; border-radius: 15px; border-left: 5px solid #ffb300; padding: 15px;">
           <strong style="color: #ffb300;">📺 Modo TV (Mirroring)</strong>
           <p style="font-size: 13px; margin: 5px 0;">Painel otimizado para monitores de galpão com KPIs de SLA Crítico e notas processadas.</p>
        </div>
        <div class="f-item" style="background: #e8f5e9; p: 20px; border-radius: 15px; border-left: 5px solid #43a047; padding: 15px;">
           <strong style="color: #43a047;">⚡ Rota Expressa</strong>
           <p style="font-size: 13px; margin: 5px 0;">Validação inteligente de transbordo direto para o cliente final.</p>
        </div>
      </div>

      <h2>Como Operar este Módulo</h2>
      <ul class="steps">
        <li><strong>Filtragem de Status:</strong> Utilize os botões no topo para alternar entre notas <em>Pendentes</em>, <em>Processadas</em> ou <em>Canceladas</em>.</li>
        <li><strong>Monitoramento de Alocação:</strong> Acompanhe a barra <strong>Alocada</strong> (黄) para saber quanto do volume já foi separado para transbordo.</li>
        <li><strong>Acompanhamento de Expedição:</strong> A barra <strong>Expedida</strong> (绿) indica o que já foi efetivamente carregado no veículo.</li>
        <li><strong>Detalhamento da NF:</strong> Clique em uma linha para abrir o painel inferior. Lá você verá o SKU, EAN e a conferência de itens (Solicitado vs Atendido).</li>
        <li><strong>Validação de Rota:</strong> No painel de detalhes, confirme se a carga seguirá via <strong>Rota Expressa</strong> para entrega direta.</li>
        <li><strong>Manifesto:</strong> Após a conferência total, utilize o botão <strong>Imprimir Manifesto</strong> para liberar o veículo.</li>
      </ul>

      <div class="tip">
        <strong>💡 Insight Logístico:</strong> Fique atento ao KPI de "SLA Crítico" no Modo TV. Ele indica NFs pendentes com alocação incompleta que precisam de atenção imediata.
      </div>

      <div class="result">
        <strong>✓ Conclusão:</strong> Uma NF é considerada "Processada" quando as barras de Alocação e Expedição atingem 100% e o fluxo operacional é validado.
      </div>
    </div>
  </main>
</div>
<footer>
  <p>WMS VerticalParts Docs — Atualizado a cada versão — <a href="https://www.wmsverticalparts.com.br" target="_blank">wmsverticalparts.com.br</a></p>
</footer>
<script src="../../assets/js/main.js"></script>
</body>
</html>
"""

# Write the special page
with open(os.path.join(base_dir, "paginas/02-operar/cruzar-docas.html"), "w", encoding="utf-8") as f:
    f.write(cruzar_docas_content)

print("Specialized Cruzar Docas page created.")
