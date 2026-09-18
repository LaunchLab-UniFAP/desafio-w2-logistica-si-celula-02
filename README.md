## 🚀 LaunchLab UniFAP — Guia de Execução do Desafio Semanal
Este é um repositório corporativo e pedagógico de alto desempenho. A sua célula deve seguir rigorosamente as diretrizes contidas neste documento para validar as competências e conquistar a certificação da semana.


## 🛠️ 1. Instruções Iniciais de Configuração (Proibido dar FORK)
O ecossistema do LaunchLab simula o ambiente de engenharia de software do mercado real. Por questões de governança de TI e compliance corporativo, o fluxo de clonagem do projeto deve seguir regras estritas:

1. NÃO DEIXE UM FORK: É terminantemente proibido utilizar o botão Fork do GitHub neste repositório. O fork vincula seu código publicamente ao perfil do professor, quebrando o isolamento das equipes.
2. USE O TEMPLATE: O integrante líder da célula deve clicar exclusivamente no botão verde "Use this template" ➔ "Create a new repository".
3. ALTERE O OWNER: Na tela de criação do novo repositório, mude obrigatoriamente o campo Owner (Dono) do seu perfil pessoal para a organização oficial do programa: LaunchLab-UniFAP.
4. NOMENCLATURA PADRÃO: Nomeie o repositório utilizando estritamente a tag da sua bancada: desafio-w[NUMERO_DA_SEMANA]-[CURSO]-celula[NUMERO_DA_BANCADA]. (Exemplo: desafio-w2-ads-celula04).
5. CONVITE AO PARCEIRO E MONITOR: Vá em Settings ➔ Collaborators ➔ Add people e convide o outro membro da sua dupla e o usuário do GitHub do seu Embaixador.


## 👥 2. Matriz de Papéis e Responsabilidades na Célula
As células operam como equipes autônomas focadas na identidade e no orgulho de cada curso. Ninguém trabalha isolado.
## 🚀 O Papel do Desenvolvedor de ADS

* Missão: Construir o motor operacional, a mecânica lógica e a estabilidade das funções do software.
* Responsabilidade: Implementar algoritmos limpos, garantir o tratamento completo de exceções em tempo de execução e assegurar o sucesso nos testes de integração automatizados do sistema.

## 💼 O Papel do Desenvolvedor de SI

* Missão: Desenvolver a arquitetura estrutural de dados, governança de TI e regras estratégicas de negócio do projeto.
* Responsabilidade: Estruturar os metadados corporativos, implementar funções de validação de viabilidade econômica/processos e redigir as seções de conformidade, compliance legal e impacto do sistema.

## 🛡️ O Papel do Aluno Embaixador

* Missão: Atuar como Líder Técnico e monitor preventivo de ritmo ao longo da semana.
* Responsabilidade: Auditar os gráficos de commits, remover impedimentos de versionamento de código e responder às Issues abertas pelas células utilizando exclusivamente o método socrático.


## ⚠️ 3. Política de Compliance e Uso de Inteligência Artificial (IA)
O uso de ferramentas de IA (como ChatGPT, GitHub Copilot ou Claude) no LaunchLab UniFAP é regulado por normas estritas de ética profissional:

* 🟢 O que é PERMITIDO (Uso como Assistente): Utilizar a IA para explicar mensagens de erro retornadas pelo console do terminal, sugerir conceitos de sintaxe estruturada ou auxiliar na formatação de arquivos markdown.
* 🔴 O que é PROIBIDO (Sujeito a Retenção de Medalha - ND): Gerar o código-fonte por completo via prompts, copiar e colar funções inteiras sem compreender a mecânica, ou utilizar robôs para redigir as análises textuais do relatório.
* A Auditoria Docente: O professor pode realizar inspeções e arguições orais surpresa. Se um aluno for questionado em sala e não souber explicar a arquitetura ou o funcionamento do código assinado por ele, a competência será marcada imediatamente como Não Desenvolvida (ND) para toda a célula, acionando o Contrato de Convivência.


## 📑 4. Relatório de Entrega da Célula (Preenchimento Obrigatório)
Instrução: Edite as seções abaixo preenchendo as evidências críticas da dupla até o prazo limite estipulado no ciclo semanal.
## 📂 Identificação

* Curso: [Sistemas de Informação]
* Membro 1 (Nome & GitHub): @[Kaishote] - [Italo Brito da Costa]
* Membro 2 (Nome & GitHub): @[LucasPierreAraujo] - [Pedro Lucas Araujo Pinho pierre]
* Embaixador Vinculado: @[Lucas-d-Barbosa] - [Francisco Lucas dos Santos Barbosa]

## 🌍 Seção de Análise Crítica (Formação Geral)

Com base no cenário proposto da semana, descreva qual o impacto humano, social, ético ou ambiental da tecnologia que sua célula colocou em produção. Como as decisões de código impactam o mundo físico e a vida do cidadão/empresa?
💬 RESPOSTA DA CÉLULA:  O sistema antigo usava rotas fixas, então o caminhão passava sempre nos mesmos bairros, independentemente de ter lixo para recolher. Nas cooperativas com menos volume, ele voltava quase vazio. Isso emite CO₂ e ocupa o motorista sem necessidade, enquanto outras centrais ficam sobrecarregadas esperando atendimento.
A nossa solução define um limite mínimo de ocupação e avisa quando a carga fica abaixo dele. Assim o desperdício vira um número, e não uma impressão de quem está na operação.

## 💻 Seção de Engenharia e Governança de TI

Justifique a decisão de arquitetura técnica adotada pela célula nesta entrega. Como as regras de negócio de ADS e as estruturas de dados de SI foram construidas para garantir que a solução seja escalável e de fácil manutenção?
💬 RESPOSTA DA CÉLULA: Separamos as regras de negócio do código que as executa. Os parâmetros ficam no dicionário METADADOS_COMPLIANCE, e a função apenas os consulta.

Por isso o limite de 15 m³ não aparece escrito direto na função. Ele é calculado a partir da capacidade da frota vezes o percentual mínimo. Se a prefeitura mudar a meta, ou se a frota for trocada por caminhões maiores, basta alterar um número no dicionário e o resto do sistema se ajusta sozinho.

Isso facilita a manutenção, porque existe um único lugar para mexer. E ajuda a governança, porque o Git guarda o histórico de quem mudou o parâmetro e quando.

## 🛠️ Diário de Bordo da Bancada

* Maior travamento técnico superado pela dupla durante a semana: O maior problema que tivemos foi organizar as regras de negócio dentro do código de uma forma que os dados pudessem ser analisados corretamente. Tivemos algumas dúvidas sobre como definir os limites de ocupação da frota e como fazer o sistema identificar quando havia muita ociosidade. Depois de testar algumas possibilidades, conseguimos ajustar a lógica e fazer a função apresentar os resultados esperados.
* Como a intervenção ou a Issue aberta para o Embaixador ajudou a destravar a célula: A intervenção ajudou principalmente a tirar algumas dúvidas sobre como deveríamos estruturar essa parte do projeto e quais informações seriam importantes para a análise. Com as orientações recebidas, conseguimos entender melhor o que precisava ser feito e dar continuidade ao desenvolvimento sem precisar mudar a ideia principal que já tínhamos definido.



## Lembrete de Fechamento: Garanta que todo o projeto esteja commitado na branch principal ('main') e responda ao Micro Simulado individual no AVA antes do prazo limite.

