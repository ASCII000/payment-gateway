<p align="center">

### ⚠️ Foi utilizado inteligência artificial para elaboração da arquitetura e definição dos padrões aplicados neste projeto? ⚠️

Gostaria de deixar claro desde o início que nenhuma inteligência artificial foi utilizada para a elaboração da arquitetura ou definição dos padrões aplicados neste projeto. Todas as decisões relacionadas à arquitetura, aplicação dos princípios SOLID, CQRS, DDD e demais padrões de projeto foram resultado de minha análise e auditoria completa.

As ferramentas de inteligência artificial foram utilizadas exclusivamente para compreensão de contextos, revisão arquitetural e sugestões, sem interferir na autoria das decisões técnicas.

Para o desenvolvimento do código, utilizei os ambientes Windsurf e VSCode.

Esta declaração visa garantir transparência quanto à origem das escolhas técnicas e ao esforço dedicado ao projeto.

</p>


---


# API Payment Gateways

Esta é uma API de demonstração para a orquestração de gateways de pagamento, com foco em seguir as boas práticas de arquitetura de microserviços como SOLID, DDD, CQRS, etc.

## Ferramentas utilizadas

![Python](https://img.shields.io/badge/-Python-333333?style=flat&logo=python)
![FastAPI](https://img.shields.io/badge/-FastAPI-333333?style=flat&logo=fastapi)
![SQLModel](https://img.shields.io/badge/-SQLModel-333333?style=flat&logo=sqlmodel)
![Poetry](https://img.shields.io/badge/-Poetry-333333?style=flat&logo=poetry)

### Arquitetura
Este projeto utiliza:
- **SOLID**: classes com responsabilidade única e injeção de dependência clara.
- **DDD**: organização de domínios como providers e transactions, com entities, repositories e services.
- **CQRS**: separação de comandos (writes) e queries (reads) em camadas distintas.

Essa estrutura facilita manutenção, testes unitários e evolução do projeto em produção.

### Execução local
Para executar esse projeto e necessario o [Python 3.13](https://www.python.org/downloads/) e o [Poetry](https://python-poetry.org/).
Realize o clone desse projeto:

```bash
git clone https://github.com/ASCII000/payment-gateway.git
```

Logo após em um terminal bash execute:

```bash
cd payment-gateway
bash scripts/run_api.bash
```
- **OBS**: O script já esta encarregado de criar o ambiente virutal e instalar as dependências, (APENAS) se necessario.


Por padão a API deve executar na porta 8000 e voce pode acessar ela na url http://localhost:8000/docs

## Storymap
![Linkedin](https://img.shields.io/badge/-Linkedin-333333?style=flat&logo=linkedin)
![Clickup](https://img.shields.io/badge/-Clickup-333333?style=flat&logo=clickup)
![Drawsql](https://img.shields.io/badge/-Drawsql-333333?style=flat&logo=drawsql)

Olá 👋
Essa é uma área mais reservada onde quero compartilhar um pouco sobre esse projeto e te ajudar a entender melhor o que ele é, como foi pensado e desenvolvido.

Antes de tudo, quero dizer que esse projeto foi criado para mostrar as melhores práticas de arquitetura de microserviços, com foco em seguir princípios como SOLID, DDD e CQRS — tudo para garantir um código organizado, escalável e fácil de manter.

Se você quiser acompanhar o andamento do projeto, aqui estão alguns links que vão te dar uma boa visão geral:

Caso queira ter uma visão sobre como esta sendo desenvolvimento projeto recomendo esses links
- [Clickup](https://sharing.clickup.com/90131910902/b/h/6-901316707674-2/7901915786528da) Visualize o quadro Kanban do projeto.
- [Drawsql](https://drawsql.app/teams/outleep/diagrams/dev-gateway-payments) Visualize o diagrama do banco de dados.
- [Linkdin](https://www.linkedin.com/in/emerson-silva-361048266) Entre em contato comigo 🤗.