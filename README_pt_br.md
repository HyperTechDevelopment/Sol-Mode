# Sol Mode

Um jeito de trabalhar para agentes que precisam levar a tarefa até o fim: do pedido ao resultado verificado, com progresso que dá pra acompanhar e evidência de verdade por trás de cada afirmação.

## O que muda

Na prática, a maioria das falhas de agente não é falta de conhecimento. É processo quebrado. Sabe como é: o trabalho para no meio porque o agente pede uma permissão que você já deu, ele diz "pronto" sem ter testado nada de fato, ninguém definiu o que conta como prova naquele tipo de tarefa, ou a conversa compacta e ele recomeça do zero como se nada tivesse acontecido.

O Sol Mode arruma o comportamento em volta do trabalho:

- **Escopo antes da cerimônia.** Coisa trivial — um arquivo, umas dez linhas, sem comportamento novo — resolve direto, sem processo pesado. E antes de mergulhar, localiza onde a resposta mora: dá pra abrir e conferir, precisa pesquisar primeiro, ou é só palpite? Cada caso recebe o tratamento certo.
- **Permissão proporcional ao risco.** O que dá pra desfazer anda sem pedir. O que não dá — deploy, publish, mandar mensagem pra alguém — é terminado primeiro como resultado concreto, pra sua aprovação cair sobre algo revisável em vez de um plano vago.
- **Progresso que dá pra seguir.** Notas curtas enquanto o trabalho anda: o que assumiu, o que achou, pra onde vai. E uma resposta final que se sustenta sozinha, porque as notas somem depois.
- **Evidência por domínio.** Cada tipo de trabalho tem seu bloco de regras dizendo o que precisa ser aberto antes de agir: design, dados, DevOps, finanças, jurídico, marketing, operações, pesquisa. Design foi exercitado em demo real (`references/examples.md`); os outros sete são experimentais e aceitam demos.
- **Verificação por observação.** Rodou, renderizou, contou. Reler o próprio código e dizer "parece certo" não conta.
- **Relato que admite o limite.** O que não deu pra verificar aparece rotulado como não verificado. Sem insinuação.

## Por que testar

A internet tá cheia de skill de método que entrega dica: seja simples, seja cirúrgico, verifique. Dica é bom, mas ninguém segue dica sob pressão. O Sol Mode entrega um loop com ordem — oito fases que rodam a cada turno — mais as regras de evidência pra cada tipo de trabalho. Essa é a diferença.

- **É um loop, não uma lista.** Enquadrar a intenção, checar autoridade, reconhecer o terreno em paralelo (olhando o que existe antes de sair lendo arquivo), planejar o turno em voz alta, executar, verificar por observação e parar, relatar, persistir através da compactação. E quando aparece algo que contradiz o esperado, a surpresa vira o assunto principal: se muda o que é "pronto", o plano atualiza; se muda o pedido, a intenção é reenquadrada. Nada de desvio silencioso.
- **Permissão sem atrito.** Reversível anda sem perguntar. Autorização dada uma vez vale pros turnos seguintes — ninguém merece responder "pode continuar?" três vezes na mesma tarefa.
- **Evidência obrigatória por domínio.** Oito blocos dizem o que tem que ser aberto antes de agir, quem vence quando as fontes discordam e quais situações significam "isso não tá pronto". Código continua sendo o padrão, sem bloco. Trabalho médico fica de fora de propósito: aquilo precisa de revisão humana qualificada, não de checklist.
- **Verificação com freio de mão.** Teste só quando faz sentido e é necessário — nunca teste que espelha a implementação. E depois de três ciclos de corrigir-e-verificar no mesmo problema, o trabalho para e devolve a saída real mais uma hipótese, em vez de rodar em círculo pra sempre.
- **Relato feito pra contexto que colapsa.** As notas de progresso somem quando a resposta final chega, então nada essencial mora só nelas. Resultado primeiro, evidência e ressalvas junto, parte não verificada com nome e sobrenome.
- **Funciona em qualquer modelo e harness.** Uma tabelinha traduz conceitos genéricos pro ambiente em uso, e a maquinaria do próprio harness não conta como delegação. Nenhum nome de modelo, nenhuma ferramenta proprietária presa nas regras.
- **Vem com verificador, não só promessa.** `scripts/verify.py` confere estrutura, referências, codificação e um inventário de regras — regressão silenciosa quebra o check em vez de passar batida. Pouca skill de método entrega isso.
- **Limites declarados.** O `provenance-and-limits.md` fala abertamente o que nenhuma skill garante: hierarquia de instruções, compactação, ferramentas disponíveis, parâmetros do modelo, ajuste, medição. Tá lá pra ninguém adotar o método de olhos fechados.

Quando vale o teste? Quando seus agentes vivem pedindo permissão à toa, dizendo "pronto" sem mostrar prova, pulando estados de tela (loading, erro, vazio) ou recomeçando depois que a conversa compacta. Começa com `sol-mode plan <tarefa>`: você vê a classificação, o que provaria o "pronto" e uma recomendação antes de encostar em qualquer arquivo. E dá uma olhada no `references/examples.md`, que passa a mesma página de login pelos três métodos lado a lado — fica fácil sentir a diferença.

## Como usar

```
sol-mode <tarefa>          roda o método completo na tarefa
sol-mode plan <tarefa>     entrega o plano e para, sem tocar em nada
sol-mode audit             avalia o trabalho concluído mais recente contra as regras
sol-mode ui <tarefa>       constrói interface com as regras de design obrigatórias
sol-mode off               desativa pelo resto da sessão
```

Ele também entra sozinho quando começa um trabalho além do portão trivial e nenhuma skill específica cobre o caso. O pedido que vem na mesma mensagem já é a tarefa — sem etapa separada de ativação, sem "posso começar?".

## Conteúdo

```
SKILL.md                      o método: postura, escopo, loop, regras de decisão, comunicação, escrita
references/
  operating-protocol.md       permissão, ambiguidade, escopo, pronto, verificação, edição, skills, delegação
  communication-style.md      notas de progresso, resposta final, formatação, visuais
  tooling-and-research.md     loteamento, segurança de shell, fronteira de pesquisa, citações, limites de citação
  modes.md                    Plan, Audit, UI
  examples.md                 comparativo de página de login entre três métodos
  provenance-and-limits.md    de onde o método veio e o que nenhuma skill pode garantir
  domains/                    blocos de namespace: design (exercitado), dados, DevOps, finanças, jurídico, marketing, operações, pesquisa (experimentais)
scripts/
  verify.py                   checagens de estrutura, referências, codificação e cobertura de regras
```

Só o `SKILL.md` (cerca de 2.600 palavras) carrega por padrão; tudo em `references/` carrega sob demanda.

## Como verificar

```
python scripts/verify.py
```

Sai com 0 quando tudo passa. Só precisa de Python 3, mais nada.

## Licença

MIT. Veja `LICENSE`.

## Proveniência

As regras nasceram como adaptação de um system prompt que circula por aí, de um agente de código de ponta. Mas cada linha aqui foi reescrita do zero: nada copiado, nada citado, sem mapeamento linha a linha. Os blocos de domínio, os modos e o verificador são criação original desta skill.
