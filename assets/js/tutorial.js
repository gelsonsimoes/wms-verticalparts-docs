/* assets/js/tutorial.js */
const tutorialData = {
    "que-e": { x: "50%", y: "50%", title: "O que é Cruzar Docas?", desc: "O Cross-Docking é uma estratégica logística onde as mercadorias chegam na doca de entrada e vão direto para a doca de saída, sem passar pelo estoque da prateleira (armazenagem)." },
    "modo-tv": { x: "77%", y: "30%", title: "Alternar Modo TV", desc: "Otimiza a interface para grandes monitores de galpão. Aumenta fontes, remove distrações e foca nos KPIs de SLA Crítico para visibilidade à distância." },
    "filtros": { x: "56%", y: "30%", title: "Filtros de Status", desc: "Alterne rapidamente entre notas 'Pendentes' (em operação), 'Processadas' (concluídas) ou 'Canceladas' para organizar sua fila de trabalho." },
    "tabela": { x: "50%", y: "55%", title: "Lista de Notas Fiscais", desc: "Exibe todas as NFs do fluxo. Mostra o progresso de Alocação (Amarelo) e Expedição (Verde) em tempo real. Clique em uma linha para ver detalhes." },
    "rota-sim": { x: "75%", y: "81%", title: "Rota Expressa: SIM", desc: "Confirma que o item seguirá fluxo direto para o cliente final. O sistema valida os dados e gera o manifesto de transbordo imediato." },
    "rota-nao": { x: "83%", y: "81%", title: "Rota Expressa: NÃO", desc: "Se o item precisar de armazenamento temporário ou seguir fluxo normal de expedição futura, utilize esta opção para direcionar ao buffer." },
    "imprimir": { x: "89%", y: "94%", title: "Imprimir Manifesto", desc: "Gera o documento físico necessário para o motorista. Só deve ser acionado após a conclusão da conferência física do transbordo." },
    "detalhes": { x: "96%", y: "65%", title: "Fechar Detalhes", desc: "Recolhe o painel inferior para dar mais espaço à lista principal de monitoramento de docas." }
};

function initTutorial() {
    const cursor = document.getElementById('ghost-cursor');
    const items = document.querySelectorAll('.accordion-item');

    items.forEach(item => {
        item.addEventListener('mouseenter', () => {
            const id = item.getAttribute('data-id');
            const pos = tutorialData[id];
            
            if (pos) {
                // Move cursor
                cursor.style.left = pos.x;
                cursor.style.top = pos.y;
                
                // Active state
                items.forEach(i => i.classList.remove('active'));
                item.classList.add('active');
                
                // Click animation
                cursor.classList.add('clicking');
                setTimeout(() => cursor.classList.remove('clicking'), 300);
            }
        });
    });
}

document.addEventListener('DOMContentLoaded', initTutorial);
