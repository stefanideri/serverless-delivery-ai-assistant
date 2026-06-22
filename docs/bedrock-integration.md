# Integração com Amazon Bedrock

O Amazon Bedrock aparece no fluxo como a camada responsável por gerar mensagens personalizadas para o cliente.

## O que seria enviado ao modelo

Em uma implementação real, a aplicação enviaria um prompt com dados mínimos do pedido, como nome do cliente, identificador do pedido, status e contexto da mensagem desejada.

Exemplo de intenção:

```text
Gere uma mensagem curta, clara e amigável para o cliente Thiago informando que o pedido PED-1001 foi confirmado e está em preparação.
```

## O que o modelo retorna

O modelo retornaria uma mensagem em linguagem natural, adequada para ser enviada ao cliente por app, WhatsApp, SMS, e-mail ou chatbot.

## Clareza do prompt

Prompts claros reduzem respostas ambíguas. É importante orientar tom, tamanho, idioma, objetivo e restrições.

## Cuidados com dados sensíveis

Evite enviar dados sensíveis ao LLM, como documentos, cartões, tokens, endereços completos quando não forem necessários ou qualquer informação confidencial.

## Variação por modelo

O request body varia conforme o foundation model escolhido. O `modelId` também precisa estar disponível na região AWS selecionada e habilitado na conta.

Este repositório não chama a API real do Bedrock.

