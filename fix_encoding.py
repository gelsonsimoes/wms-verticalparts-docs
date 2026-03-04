import os
import re

SIDEBAR_CONTENT = """
    <div class="group-title">Principal</div>
    <a href="../01-principal/dashboard.html">1.1 Dashboard Geral</a>
    <div class="group-title">Operar</div>
    <a href="../02-operar/cruzar-docas.html">2.1 Cruzar Docas</a>
    <a href="../02-operar/devolucoes.html">2.2 Processar Devoluções</a>
    <a href="../02-operar/pesar-cargas.html">2.3 Pesar Cargas</a>
    <a href="../02-operar/recebimento.html">2.4 Gerenciar Recebimento</a>
    <a href="../02-operar/conferir-recebimento.html">2.5 Conferir Recebimento</a>
    <a href="../02-operar/mapa-alocacao.html">2.6 Gerar Mapa de Alocação</a>
    <a href="../02-operar/conferencia-cega.html">2.7 Conferência Cega</a>
    <a href="../02-operar/alocar-estoque.html">2.8 Alocar Estoque</a>
    <a href="../02-operar/kanban.html">2.9 Kanban de Alocação</a>
    <a href="../02-operar/separar-pedidos.html">2.10 Separar Pedidos</a>
    <a href="../02-operar/embalar.html">2.11 Embalar Pedidos</a>
    <a href="../02-operar/saida.html">2.12 Monitorar Saída</a>
    <a href="../02-operar/checkin.html">2.13 Check-in Recebimento</a>
    <a href="../02-operar/kits.html">2.14 Estação de Kits</a>
    <a href="../02-operar/colmeia.html">2.15 Conferência Colmeia</a>
    <a href="../02-operar/mapa-visual.html">2.16 Mapa Visual Estoque</a>
    <a href="../02-operar/buffer1.html">2.17 Buffer 1</a>
    <a href="../02-operar/buffer2.html">2.18 Buffer 2</a>
    <a href="../02-operar/ordem-servico.html">2.19 Ordem de Serviço</a>
    <a href="../02-operar/seguros.html">2.20 Gestão de Seguros</a>
    <a href="../02-operar/pesagem-rodoviaria.html">2.21 Pesagem Rodoviária</a>
    <div class="group-title">Planejar</div>
    <a href="../03-planejar/ondas.html">3.1 Gerar Ondas de Separação</a>
    <a href="../03-planejar/sla.html">3.2 Monitorar Prazos (SLA)</a>
    <a href="../03-planejar/transportes.html">3.3 Agendar Transportes</a>
    <a href="../03-planejar/atividades.html">3.4 Monitorar Atividades</a>
    <a href="../03-planejar/manifestos.html">3.5 Gerenciar Manifestos</a>
    <a href="../03-planejar/expedir.html">3.6 Expedir Cargas</a>
    <a href="../03-planejar/portaria.html">3.7 Gerenciar Portaria</a>
    <a href="../03-planejar/docas.html">3.8 Atividades de Docas</a>
    <div class="group-title">Controlar</div>
    <a href="../04-controlar/inventario.html">4.1 Auditar Inventário</a>
    <a href="../04-controlar/kardex.html">4.2 Consultar Kardex</a>
    <a href="../04-controlar/analisar.html">4.3 Analisar Estoque</a>
    <a href="../04-controlar/remanejar.html">4.4 Remanejar Produtos</a>
    <a href="../04-controlar/lotes.html">4.5 Controlar Lotes e Validade</a>
    <a href="../04-controlar/avarias.html">4.6 Monitorar Avarias</a>
    <a href="../04-controlar/gestao-inventario.html">4.7 Gestão de Inventário</a>
    <div class="group-title">Fiscal</div>
    <a href="../05-fiscal/nfe.html">5.1 Gerenciar NF-e</a>
    <a href="../05-fiscal/cte.html">5.2 Gerenciar CT-e</a>
    <a href="../05-fiscal/cobertura.html">5.3 Emitir Cobertura Fiscal</a>
    <a href="../05-fiscal/armazem-geral.html">5.4 Armazém Geral</a>
    <div class="group-title">Financeiro</div>
    <a href="../06-financeiro/diarias.html">6.1 Calcular Diárias</a>
    <a href="../06-financeiro/contratos.html">6.2 Gerenciar Contratos</a>
    <div class="group-title">Cadastrar</div>
    <a href="../07-cadastrar/empresas.html">7.1 Gerenciar Empresas</a>
    <a href="../07-cadastrar/armazens.html">7.2 Configurar Armazéns</a>
    <a href="../07-cadastrar/enderecos.html">7.3 Cadastrar Endereços</a>
    <a href="../07-cadastrar/produtos.html">7.4 Catálogo de Produtos</a>
    <a href="../07-cadastrar/rotas.html">7.5 Rotas e Veículos</a>
    <a href="../07-cadastrar/areas.html">7.6 Configurar Áreas</a>
    <a href="../07-cadastrar/setores.html">7.7 Configurar Setores</a>
    <a href="../07-cadastrar/etiquetas.html">7.8 Gerenciar Etiquetas</a>
    <div class="group-title">Indicadores</div>
    <a href="../08-indicadores/financeiro.html">8.1 Dashboard Financeiro</a>
    <a href="../08-indicadores/ocupacao.html">8.2 Analisar Ocupação</a>
    <a href="../08-indicadores/produtividade.html">8.3 Medir Produtividade</a>
    <a href="../08-indicadores/auditoria.html">8.4 Auditar Logs</a>
    <a href="../08-indicadores/integracao.html">8.5 Resultados Integração</a>
    <div class="group-title">Integrar</div>
    <a href="../09-integrar/alertas.html">9.1 Alertas de Integração</a>
    <a href="../09-integrar/erp.html">9.2 Sincronizar Ordens ERP</a>
    <a href="../09-integrar/omie.html">9.3 Conectar Omie ERP</a>
    <a href="../09-integrar/arquivos.html">9.4 Mapear Arquivos</a>
    <a href="../09-integrar/apis.html">9.5 Configurar APIs REST</a>
    <a href="../09-integrar/ondas.html">9.6 Integrar Ondas</a>
    <div class="group-title">Configurar</div>
    <a href="../10-configurar/geral.html">10.1 Ajustar Configurações</a>
    <a href="../10-configurar/balancas.html">10.2 Integrar Balanças</a>
    <a href="../10-configurar/service-desk.html">10.3 Service Desk</a>
    <a href="../10-configurar/expurgo.html">10.4 Expurgar Dados</a>
    <a href="../10-configurar/certificados.html">10.5 Certificados SEFAZ</a>
    <div class="group-title">Segurança</div>
    <a href="../11-seguranca/usuarios.html">11.1 Gerenciar Usuários</a>
    <a href="../11-seguranca/grupos.html">11.2 Grupos de Acesso</a>
    <div class="group-title">Mobile</div>
    <a href="../mobile/login.html">Login</a>
    <a href="../mobile/menu.html">Menu Principal</a>
    <a href="../mobile/recebimento.html">Recebimento</a>
    <a href="../mobile/picking.html">Picking</a>
    <a href="../mobile/alocacao.html">Alocação</a>
    <a href="../mobile/inventario.html">Inventário Cego</a>
    <a href="../mobile/consulta.html">Consulta Rápida</a>
    <a href="../mobile/etiquetas.html">Imprimir Etiquetas</a>
    <a href="../mobile/remanejamento.html">Remanejamento</a>
"""

def fix_file(path):
    with open(path, 'rb') as f:
        content = f.read()
    try:
        text = content.decode('utf-8')
    except:
        text = content.decode('latin-1')

    # Replace header links and common icons
    text = re.sub(r'InÃ­cio', 'Início', text)
    text = re.sub(r'OperaÃ§Ã£o', 'Operação', text)
    
    # Replace sidebar entirely
    sidebar_pattern = r'<nav class="sidebar">.*?</nav>'
    new_sidebar = f'<nav class="sidebar">{SIDEBAR_CONTENT}</nav>'
    text = re.sub(sidebar_pattern, new_sidebar, text, flags=re.DOTALL)
    
    # Clean up mangled characters
    repls = {
        'Ã©': 'é', 'Ã¡': 'á', 'Ã­': 'í', 'Ã³': 'ó', 'Ãº': 'ú',
        'Ã ': 'à', 'Ã£': 'ã', 'Ãµ': 'õ', 'Ãª': 'ê', 'Ã¢': 'â',
        'Ã§': 'ç', 'â€”': '—', 'âœ“': '✓', 'ðŸ’¡': '💡',
        'versÃ£o': 'versão', 'Manual do UsuÃ¡rio': 'Manual do Usuário',
        'OperaÃ§Ã£o': 'Operação', 'mÃ³dulo': 'módulo', 'pÃ¡gina': 'página'
    }
    for old, new in repls.items():
        text = text.replace(old, new)
        
    # Replace GitHub link everywhere
    text = re.sub(r'https://github.com/[^"]*', 'https://www.wmsverticalparts.com.br', text)
    text = text.replace('GitHub', 'Site Oficial')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)

# Run for all html files
for root, dirs, files in os.walk('c:/Users/gelso/Projetos_Antigravity/wms_blog_verticalparts/wms-verticalparts-docs'):
    for file in files:
        if file.endswith('.html'):
            fix_file(os.path.join(root, file))
