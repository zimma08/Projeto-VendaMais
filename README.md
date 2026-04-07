# VendaMais

## Visão Geral

O **VendaMais** é um projeto desenvolvido para a disciplina de **Design e Arquitetura de Software**, do curso de **Engenharia de Software**. A proposta do sistema é centralizar dados de vendas provenientes de diferentes fontes externas, como **ERPs** e **APIs de pagamento**, transformando essas informações em relatórios e dashboards que auxiliem a tomada de decisão gerencial.

A arquitetura foi construída com base nos **diagramas C4** e nos **ADRs (Architecture Decision Records)**, permitindo justificar as decisões técnicas adotadas e demonstrar de forma clara a estrutura do sistema.

---

## Arquitetura e Documentação

A solução foi modelada com foco em **organização, escalabilidade e manutenibilidade**, aplicando conceitos estudados na disciplina e aproximando o projeto de um cenário corporativo real.

A documentação arquitetural está fundamentada em dois pilares:

- **Diagramas C4**, para representar a estrutura do sistema em diferentes níveis
- **ADRs**, para registrar as decisões arquiteturais tomadas pela equipe

---

## Diagrama C4 – Contexto

No **diagrama de contexto**, o VendaMais aparece como o núcleo da solução, responsável por receber dados de sistemas externos e disponibilizá-los para análise.

O sistema se integra com um **ERP**, que fornece dados de vendas, e com uma **API de pagamentos**, responsável pelas informações transacionais. Após o processamento, esses dados são disponibilizados ao **Power BI**, que gera dashboards e relatórios.

O **gestor/analista** acessa a plataforma via navegador para acompanhar indicadores, métricas e relatórios estratégicos.

Esse diagrama apresenta a visão macro do ecossistema e evidencia a relação entre usuários, serviços externos e o sistema principal.

---

## Diagrama C4 – Containers

O **diagrama de containers** detalha a estrutura interna da aplicação.

A solução foi dividida em módulos principais para facilitar a separação de responsabilidades:

- **Frontend**: interface web para visualização dos dados
- **Backend**: regras de negócio e integração entre serviços
- **Azure Functions**: processamento assíncrono da ingestão
- **Azure Service Bus**: gerenciamento das filas de mensagens
- **Azure SQL Database**: armazenamento estruturado
- **Power BI**: geração de dashboards

Essa organização melhora a manutenção do sistema e favorece sua evolução futura.

---

## Decisões Arquiteturais (ADRs)

### ADR-001 — Estratégia de ingestão de dados

Foi adotado um modelo de **processamento assíncrono**, utilizando **Azure Functions** e **Azure Service Bus**.

Essa decisão foi tomada para permitir que o sistema lide melhor com **picos de volume**, sem impactar diretamente a experiência do usuário na aplicação principal.

A escolha prioriza **baixo acoplamento**, **resiliência** e **escalabilidade**.

### ADR-002 — Estratégia de armazenamento

Para o armazenamento dos dados, foi escolhido o **Azure SQL Database**.

A decisão se baseia na necessidade de trabalhar com **dados estruturados**, facilitar consultas analíticas e manter uma integração simples com ferramentas de BI, especialmente o **Power BI**.

Essa escolha atende bem ao contexto do projeto, considerando consistência e facilidade de consulta.

---

## Tecnologias Utilizadas

```text
Frontend: React
Backend: .NET / Node.js
Mensageria: Azure Service Bus
Processamento assíncrono: Azure Functions
Banco de dados: Azure SQL Database
BI: Power BI
Cloud: Microsoft Azure
Documentação: C4 Model + ADR
```

---

## Estrutura do Projeto

```text
vendamais/
├── frontend/
├── backend/
├── functions/
├── database/
├── docs/
│   ├── c4/
│   └── adr/
└── README.md
```

---

## Considerações Finais

O projeto demonstra a aplicação prática de conceitos importantes da disciplina, como **arquitetura em camadas**, **processamento assíncrono**, **documentação arquitetural com ADR** e **modelagem utilizando C4**.

A proposta busca representar uma solução próxima de um ambiente real de desenvolvimento, utilizando tecnologias modernas e decisões arquiteturais justificadas.

---

## Equipe

- Arthur
- Cauã
- Leandro
