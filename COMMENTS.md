## Decisão da arquitetura utilizada

A arquitetura escolhida para o projeto foi baseada em uma abordagem modular, separando as responsabilidades em diferentes serviços, como `AIService`, `IndexingService`, `FileService` e `JsonProcessingService`. Cada serviço é responsável por uma parte específica do fluxo de processamento, facilitando a manutenção, testes e escalabilidade do sistema. A comunicação entre os módulos é feita por meio de DTOs e métodos bem definidos, promovendo baixo acoplamento e alta coesão. Além disso, a integração com modelos de IA e serviços externos foi abstraída para permitir fácil substituição ou atualização de provedores.

Na arquitetura de inteligência artificial adotada neste projeto, optei por uma abordagem baseada em grafos, fundamentada nas melhores práticas e recomendações da LangGraph. Essa escolha permite estruturar o fluxo de processamento em nós (nodes) bem definidos, onde cada camada do sistema permanece isolada e responsável por uma função específica, promovendo alta coesão e baixo acoplamento entre os componentes. Dessa forma, a LLM (Large Language Model) atua como agente central de decisão, avaliando o contexto e determinando, de maneira dinâmica e inteligente, qual caminho seguir dentro do grafo de execução. Essa arquitetura facilita a extensibilidade, a manutenção e a escalabilidade do sistema, além de permitir a fácil integração de novos módulos ou fluxos de decisão conforme a evolução das necessidades do projeto.

O Pinecone é considerado um dos melhores bancos vetoriais do mercado devido à sua alta performance, escalabilidade e facilidade de integração com aplicações de inteligência artificial. Ele foi projetado especificamente para lidar com grandes volumes de embeddings, permitindo buscas semânticas extremamente rápidas e precisas, mesmo em bases de dados com milhões de vetores. Além disso, o Pinecone oferece gerenciamento automático de índices, balanceamento de carga, persistência de dados e alta disponibilidade, o que elimina a complexidade operacional normalmente associada à manutenção de bancos vetoriais próprios. Sua API simples e integração nativa com frameworks populares de IA, como o Langchain, tornam o desenvolvimento de soluções baseadas em busca semântica muito mais ágil e confiável.

O ecossistema formado pelo Langchain, Langgraph e Langsmith é altamente recomendado para projetos de IA porque oferece uma infraestrutura robusta, flexível e extensível para construção, orquestração e avaliação de fluxos de trabalho envolvendo LLMs (Large Language Models). O Langchain facilita a integração com múltiplos provedores de modelos, gerenciamento de memória, ferramentas e agentes, além de abstrair detalhes complexos do pipeline de IA. O Langgraph, por sua vez, permite estruturar o fluxo de execução em grafos, tornando o sistema mais modular, dinâmico e fácil de manter, além de possibilitar a criação de pipelines condicionais e ramificados. Já o Langsmith complementa o ambiente ao fornecer ferramentas avançadas de monitoramento, avaliação e depuração, essenciais para garantir a qualidade, rastreabilidade e evolução contínua das soluções de IA. Juntos, esses componentes promovem produtividade, segurança, escalabilidade e aceleram o ciclo de desenvolvimento de aplicações inteligentes.


## Lista de bibliotecas de terceiros utilizadas

- **langchain_groq**: Biblioteca que permite a integração com modelos Groq de linguagem natural, facilitando a utilização desses modelos em fluxos de processamento de IA. É especialmente útil para quem deseja explorar alternativas aos modelos tradicionais, trazendo flexibilidade e diversidade ao pipeline de IA.

- **langchain_openai**: Responsável por integrar os modelos da OpenAI (como GPT-4o) ao sistema, simplificando a chamada e o gerenciamento desses modelos em aplicações Python. Permite fácil alternância entre diferentes provedores de LLM, promovendo modularidade.

- **openai**: Biblioteca oficial da OpenAI, utilizada para acessar diretamente os serviços da empresa, como geração de texto, transcrição de áudio (Whisper) e síntese de voz (TTS). É fundamental para operações que exigem recursos avançados de IA fornecidos pela OpenAI.

- **langgraph**: Biblioteca desenvolvida para facilitar a construção de fluxos de trabalho baseados em grafos para aplicações de IA. Com o langgraph, é possível estruturar o processamento em nós (nodes) e arestas, permitindo a criação de pipelines dinâmicos, flexíveis e facilmente extensíveis. Essa abordagem é especialmente útil para cenários em que decisões condicionais e múltiplos caminhos de execução são necessários, promovendo maior organização e clareza no fluxo de dados e decisões dentro do sistema.

- **langsmith**: Plataforma e biblioteca que oferece ferramentas para avaliação, monitoramento e depuração de fluxos de IA, especialmente aqueles construídos com LangChain e LangGraph. O langsmith permite criar experimentos, rastrear execuções, analisar métricas de desempenho e identificar gargalos ou falhas nos pipelines de IA. Isso facilita o desenvolvimento iterativo, a validação de modelos e a melhoria contínua da qualidade das soluções de inteligência artificial implementadas.

- **pinecone**: O Pinecone é um serviço e biblioteca especializada em indexação e busca vetorial de dados. Ele permite armazenar, gerenciar e consultar grandes volumes de vetores (como embeddings gerados por modelos de linguagem), tornando possível realizar buscas semânticas rápidas e eficientes. No contexto deste projeto, o Pinecone é fundamental para recuperar informações relevantes a partir de textos ou embeddings, viabilizando funcionalidades como busca semântica, recomendação de conteúdos e recuperação de contexto para modelos de IA. Sua integração facilita a escalabilidade e a performance do sistema, principalmente em cenários com grandes quantidades de dados não estruturados.

- **logging**: Módulo padrão do Python para registro de logs, fundamental para monitoramento, depuração e auditoria do sistema. Permite acompanhar o funcionamento da aplicação e identificar rapidamente possíveis falhas.

- **uuid**: Utilizado para geração de identificadores únicos universais, garantindo unicidade em registros, arquivos ou entidades manipuladas pelo sistema.

- **re**: Biblioteca padrão para manipulação de expressões regulares, muito útil para limpeza, validação e extração de padrões em strings, como remoção de tags HTML ou validação de formatos específicos.

- **os** e **pathlib**: Bibliotecas essenciais para manipulação de arquivos e diretórios no sistema operacional. `os` oferece funções para interação com o ambiente do sistema, enquanto `pathlib` fornece uma interface orientada a objetos para manipulação de caminhos de arquivos.

- **base64**: Utilizada para codificação e decodificação de dados em base64, especialmente útil para converter imagens ou arquivos binários em strings, facilitando o transporte e armazenamento desses dados em formatos textuais.

- **json**: Biblioteca padrão para manipulação de dados no formato JSON, permitindo leitura, escrita e transformação de dados estruturados, amplamente utilizada em APIs e persistência de informações.

## O que você melhoraria se tivesse mais tempo

- Implementaria testes automatizados (unitários e de integração) para garantir maior robustez e facilitar futuras manutenções.
- Melhoraria o tratamento de erros, adicionando mensagens mais detalhadas e integração com sistemas de monitoramento passadas via JSON.
- Implementaria cache para respostas de IA e buscas no Pinecone, otimizando performance.
- Implementaria um banco de rápido acesso como o Redis para as mensagens do Chat por um determinado período.
- Criaria uma documentação mais detalhada, com alguns exemplos.
- Distinção de memória de curto prazo e de longo prazo via Langgraph.
- Um melhor tratamento no processamento das imagens.
- A criação de avaliadores via Langsmith para poder testar os modelos.
- Realizaria mais testes nos métodos que dependiam de modelos de LLM, visando aperfoiçar a pessoa.

## Quais requisitos obrigatórios que não foram entregues

- O único requisito obrigatório que não foi entregue, foi a geração de vídeo.

## Como utilizar o projeto

Para utilizar este projeto de inteligência artificial, siga os passos abaixo:

1. **Pré-requisitos**  
   - Certifique-se de ter o Python 3.10+ instalado em sua máquina.
   - Instale todas as dependências necessárias executando o comando:
     ```
     pip install -r requirements.txt
     ```
   - Configure as variáveis de ambiente necessárias (por exemplo, chaves de API da OpenAI, Pinecone, etc.) em um arquivo `.env` na raiz do projeto.

2. **Configuração e Inicialização do Postgres com LangGraph**  
   - Para inicializar o banco de dados, utilize:
     ```
     docker-compose up
     ```
   - O LangGraph utiliza o Postgres para persistência dos estados do grafo, garantindo robustez e rastreabilidade das execuções.
   - **Atenção:** Na primeira vez que for rodar o projeto, é necessário executar o método `checkpointer.setup()` para criar as tabelas e estruturas necessárias no banco de dados. Esse procedimento só precisa ser feito uma vez; nas execuções seguintes, não é mais necessário rodar o `setup()`.

3. **Inicialização do Backend**  
   - Execute o arquivo `main.py` e inicie o servidor FastAPI com:
     ```
     uvicorn main:app --reload
     ```
   - O backend ficará disponível em `http://localhost:8000`.

4. **Inicialização do Frontend**  
   - Em outro terminal, navegue até a pasta `app/frontend` e execute:
     ```
     streamlit run chat.py
     ```
   - A interface web estará disponível em `http://localhost:8501`.

5. **Utilização da Interface**  
   - Acesse a interface web pelo navegador.
   - Informe o ID do usuário e envie mensagens pelo chat.
   - O sistema irá processar suas mensagens, utilizando modelos de linguagem e recursos de IA para responder, extrair informações e gerar conteúdos personalizados.
   - Sempre que você extrair uma mensagem final, a memória da conversa é limpa se baseando no ID.

6. **Upload e Processamento de Arquivos**  
   - A aplicação possui endpoints bem estruturados para lidar com o processamento dos arquivos.
   - Existem 2 namespaces no Pinecone: um chamado de 'dev', caso você queira testar os endpoints e visualizar os dados diretamente no Pinecone, e outro chamado 'prod', que será utilizado pelo chat para melhorar a resposta.

7. **Atenção às Configurações**  
   - Preste atenção nas variáveis de ambiente e demais configurações solicitadas para garantir o funcionamento correto do sistema.
