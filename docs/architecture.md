# Arquitetura

Este projeto representa uma arquitetura serverless para um assistente de delivery. A solução proposta usa AWS Step Functions como orquestrador do fluxo e Amazon Bedrock como camada de IA generativa para mensagens personalizadas ao cliente.

## Componentes principais

- **Entrada do pedido**: em uma arquitetura real, poderia ser recebida via API Gateway, chatbot, aplicativo mobile ou sistema de PDV.
- **AWS Step Functions**: coordena estados, escolhas, transições, falhas e encerramentos do fluxo.
- **Validação do pedido**: garante que dados mínimos existam antes de seguir para pagamento ou IA.
- **Pagamento**: simula os caminhos aprovado, recusado e pendente.
- **Amazon Bedrock**: gera mensagens amigáveis ao cliente com base no pedido e no status.
- **Atualização de status**: registra a evolução do pedido.

## Separação entre orquestração e IA

O Step Functions controla o fluxo determinístico: validar, decidir, rotear, tratar falhas e concluir. O Bedrock entra apenas onde há valor generativo, como redigir uma mensagem personalizada.

Essa separação é importante porque um modelo generativo não deve controlar sozinho regras críticas do negócio. Validação, pagamento, permissões e estados precisam ser previsíveis, auditáveis e testáveis.

## Por que Step Functions

Step Functions é adequado para fluxos com estados, escolhas e tratamento de erro. Ele torna explícito o caminho do pedido e facilita auditoria, observabilidade e manutenção.

## Por que Bedrock

Amazon Bedrock permite usar foundation models gerenciados para gerar texto. Neste projeto, ele é usado de forma controlada, recebendo um prompt claro e retornando uma mensagem para o cliente.

