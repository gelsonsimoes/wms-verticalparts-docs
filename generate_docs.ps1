# ═══════════════════════════════════════════════════════════════
#  SCRIPT DE GERAÇÃO AUTOMÁTICA DE PÁGINAS DO BLOG WMS
#  VerticalParts - Documentação e Tutoriais
# ═══════════════════════════════════════════════════════════════

$baseDir = Get-Location
$templateFile = "$baseDir\index.html" # Usaremos a index como base de nav/sidebar

$paginas = @(
    # Módulo 1
    @{ path="paginas/01-principal/dashboard.html"; title="1.1 Dashboard Geral" },

    # Módulo 2
    @{ path="paginas/02-operar/cruzar-docas.html"; title="2.1 Cruzar Docas" },
    @{ path="paginas/02-operar/devolucoes.html"; title="2.2 Processar Devoluções" },
    @{ path="paginas/02-operar/pesar-cargas.html"; title="2.3 Pesar Cargas" },
    @{ path="paginas/02-operar/recebimento.html"; title="2.4 Gerenciar Recebimento" },
    @{ path="paginas/02-operar/conferir-recebimento.html"; title="2.5 Conferir Recebimento" },
    @{ path="paginas/02-operar/mapa-alocacao.html"; title="2.6 Gerar Mapa de Alocação" },
    @{ path="paginas/02-operar/conferencia-cega.html"; title="2.7 Conferência Cega" },
    @{ path="paginas/02-operar/alocar-estoque.html"; title="2.8 Alocar Estoque" },
    @{ path="paginas/02-operar/kanban.html"; title="2.9 Kanban de Alocação" },
    @{ path="paginas/02-operar/separar-pedidos.html"; title="2.10 Separar Pedidos" },
    @{ path="paginas/02-operar/embalar.html"; title="2.11 Embalar Pedidos" },
    @{ path="paginas/02-operar/saida.html"; title="2.12 Monitorar Saída" },
    @{ path="paginas/02-operar/checkin.html"; title="2.13 Check-in Recebimento" },
    @{ path="paginas/02-operar/kits.html"; title="2.14 Estação de Kits" },
    @{ path="paginas/02-operar/colmeia.html"; title="2.15 Conferência Colmeia" },
    @{ path="paginas/02-operar/mapa-visual.html"; title="2.16 Mapa Visual Estoque" },
    @{ path="paginas/02-operar/buffer1.html"; title="2.17 Buffer 1" },
    @{ path="paginas/02-operar/buffer2.html"; title="2.18 Buffer 2" },
    @{ path="paginas/02-operar/ordem-servico.html"; title="2.19 Ordem de Serviço" },
    @{ path="paginas/02-operar/seguros.html"; title="2.20 Gestão de Seguros" },
    @{ path="paginas/02-operar/pesagem-rodoviaria.html"; title="2.21 Pesagem Rodoviária" },

    # Módulo 3
    @{ path="paginas/03-planejar/ondas.html"; title="3.1 Gerar Ondas de Separação" },
    @{ path="paginas/03-planejar/sla.html"; title="3.2 Monitorar Prazos (SLA)" },
    @{ path="paginas/03-planejar/transportes.html"; title="3.3 Agendar Transportes" },
    @{ path="paginas/03-planejar/atividades.html"; title="3.4 Monitorar Atividades" },
    @{ path="paginas/03-planejar/manifestos.html"; title="3.5 Gerenciar Manifestos" },
    @{ path="paginas/03-planejar/expedir.html"; title="3.6 Expedir Cargas" },
    @{ path="paginas/03-planejar/portaria.html"; title="3.7 Gerenciar Portaria" },
    @{ path="paginas/03-planejar/docas.html"; title="3.8 Atividades de Docas" },

    # Módulo 4
    @{ path="paginas/04-controlar/inventario.html"; title="4.1 Auditar Inventário" },
    @{ path="paginas/04-controlar/kardex.html"; title="4.2 Consultar Kardex" },
    @{ path="paginas/04-controlar/analisar.html"; title="4.3 Analisar Estoque" },
    @{ path="paginas/04-controlar/remanejar.html"; title="4.4 Remanejar Produtos" },
    @{ path="paginas/04-controlar/lotes.html"; title="4.5 Controlar Lotes e Validade" },
    @{ path="paginas/04-controlar/avarias.html"; title="4.6 Monitorar Avarias" },
    @{ path="paginas/04-controlar/gestao-inventario.html"; title="4.7 Gestão de Inventário" },

    # Módulo 5
    @{ path="paginas/05-fiscal/nfe.html"; title="5.1 Gerenciar NF-e" },
    @{ path="paginas/05-fiscal/cte.html"; title="5.2 Gerenciar CT-e" },
    @{ path="paginas/05-fiscal/cobertura.html"; title="5.3 Emitir Cobertura Fiscal" },
    @{ path="paginas/05-fiscal/armazem-geral.html"; title="5.4 Armazém Geral" },

    # Módulo 6
    @{ path="paginas/06-financeiro/diarias.html"; title="6.1 Calcular Diárias" },
    @{ path="paginas/06-financeiro/contratos.html"; title="6.2 Gerenciar Contratos" },

    # Módulo 7
    @{ path="paginas/07-cadastrar/empresas.html"; title="7.1 Gerenciar Empresas" },
    @{ path="paginas/07-cadastrar/armazens.html"; title="7.2 Configurar Armazéns" },
    @{ path="paginas/07-cadastrar/enderecos.html"; title="7.3 Cadastrar Endereços" },
    @{ path="paginas/07-cadastrar/produtos.html"; title="7.4 Catálogo de Produtos" },
    @{ path="paginas/07-cadastrar/rotas.html"; title="7.5 Rotas e Veículos" },
    @{ path="paginas/07-cadastrar/areas.html"; title="7.6 Configurar Áreas" },
    @{ path="paginas/07-cadastrar/setores.html"; title="7.7 Configurar Setores" },
    @{ path="paginas/07-cadastrar/etiquetas.html"; title="7.8 Gerenciar Etiquetas" },

    # Módulo 8
    @{ path="paginas/08-indicadores/financeiro.html"; title="8.1 Dashboard Financeiro" },
    @{ path="paginas/08-indicadores/ocupacao.html"; title="8.2 Analisar Ocupação" },
    @{ path="paginas/08-indicadores/produtividade.html"; title="8.3 Medir Produtividade" },
    @{ path="paginas/08-indicadores/auditoria.html"; title="8.4 Auditar Logs" },
    @{ path="paginas/08-indicadores/integracao.html"; title="8.5 Resultados Integração" },

    # Módulo 9
    @{ path="paginas/09-integrar/alertas.html"; title="9.1 Alertas de Integração" },
    @{ path="paginas/09-integrar/erp.html"; title="9.2 Sincronizar Ordens ERP" },
    @{ path="paginas/09-integrar/omie.html"; title="9.3 Conectar Omie ERP" },
    @{ path="paginas/09-integrar/arquivos.html"; title="9.4 Mapear Arquivos" },
    @{ path="paginas/09-integrar/apis.html"; title="9.5 Configurar APIs REST" },
    @{ path="paginas/09-integrar/ondas.html"; title="9.6 Integrar Ondas" },

    # Módulo 10
    @{ path="paginas/10-configurar/geral.html"; title="10.1 Ajustar Configurações" },
    @{ path="paginas/10-configurar/balancas.html"; title="10.2 Integrar Balanças" },
    @{ path="paginas/10-configurar/service-desk.html"; title="10.3 Service Desk" },
    @{ path="paginas/10-configurar/expurgo.html"; title="10.4 Expurgar Dados" },
    @{ path="paginas/10-configurar/certificados.html"; title="10.5 Certificados SEFAZ" },

    # Módulo 11
    @{ path="paginas/11-seguranca/usuarios.html"; title="11.1 Gerenciar Usuários" },
    @{ path="paginas/11-seguranca/grupos.html"; title="11.2 Grupos de Acesso" },

    # Mobile
    @{ path="paginas/mobile/login.html"; title="Mobile: Login" },
    @{ path="paginas/mobile/menu.html"; title="Mobile: Menu Principal" },
    @{ path="paginas/mobile/recebimento.html"; title="Mobile: Recebimento" },
    @{ path="paginas/mobile/picking.html"; title="Mobile: Picking" },
    @{ path="paginas/mobile/alocacao.html"; title="Mobile: Alocação" },
    @{ path="paginas/mobile/inventario.html"; title="Mobile: Inventário Cego" },
    @{ path="paginas/mobile/consulta.html"; title="Mobile: Consulta Rápida" },
    @{ path="paginas/mobile/etiquetas.html"; title="Mobile: Imprimir Etiquetas" },
    @{ path="paginas/mobile/remanejamento.html"; title="Mobile: Remanejamento" }
)

Write-Host "🚀 Iniciando geração de documentação..." -ForegroundColor Cyan

foreach ($pag in $paginas) {
    $fullPath = Join-Path $baseDir $pag.path
    $dir = Split-Path $fullPath
    
    # Criar diretório se não existir
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }

    # Só gera se o arquivo não existir (para não sobrescrever os manuais)
    if (-not (Test-Path $fullPath)) {
        Write-Host "📄 Gerando: $($pag.title)" -ForegroundColor Yellow
        
        $html = @"
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>$($pag.title) — WMS VerticalParts Docs</title>
  <link rel="stylesheet" href="../../assets/css/style.css">
</head>
<body>

<header class="site-header">
  <div class="logo">VerticalParts <span>WMS Docs</span></div>
  <nav>
    <a href="../../index.html">Início</a>
    <a href="../02-operar/recebimento.html">Operação</a>
    <a href="../mobile/login.html">Mobile</a>
    <a href="https://github.com/gelsonsimoes/wms-verticalparts" target="_blank">GitHub</a>
  </nav>
</header>

<div class="layout">
  <nav class="sidebar">
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
  </nav>

  <main class="content">
    <div class="tutorial-card">
      <h3>$($pag.title) — Manual do Usuário</h3>
      <p>Esta página descreve as funcionalidades e o fluxo de operação do módulo <strong>$($pag.title)</strong>.</p>

      <div class="demo-wrap">
        <div class="demo-label">Demonstração Visual</div>
        <div style="background: #f8f9fa; height: 300px; border-radius: 20px; display: flex; items-center; justify-content: center; color: #adb5bd; font-family: 'Inter', sans-serif; font-size: 14px; font-weight: 700; text-transform: uppercase; letter-spacing: 2px;">
           Aguardando GIF Demonstrativo
        </div>
      </div>

      <h2>Fluxo de Trabalho</h2>
      <ul class="steps">
        <li>Acesse o menu lateral e clique em <strong>$($pag.title)</strong>.</li>
        <li>Utilize os filtros de pesquisa para localizar os registros desejados.</li>
        <li>Realize a operação conforme as regras de negócio da VerticalParts.</li>
        <li>Confirme as alterações para sincronizar com o WMS Central.</li>
      </ul>

      <div class="tip">
        <strong>💡 Dica:</strong> Todas as alterações nesta tela são auditadas e registradas no log de atividades do sistema.
      </div>

      <div class="result">
        <strong>✓ Próximo Passo:</strong> Consulte o módulo relacionado para dar continuidade ao fluxo logístico.
      </div>
    </div>
  </main>
</div>

<footer>
  <p>WMS VerticalParts Docs &mdash; Atualizado a cada versão</p>
</footer>
<script src="../../assets/js/main.js"></script>
</body>
</html>
"@
        $html | Out-File -FilePath $fullPath -Encoding utf8
    } else {
        Write-Host "✅ Já existe: $($pag.title)" -ForegroundColor Gray
    }
}

Write-Host "✨ Todas as páginas foram geradas com sucesso!" -ForegroundColor Green
Write-Host "👉 Agora você pode substituir os placeholders pelos tutoriais específicos." -ForegroundColor Cyan
