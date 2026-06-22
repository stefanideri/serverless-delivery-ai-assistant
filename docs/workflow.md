# Fluxo do pedido

## 1. Recepção do pedido

O fluxo começa quando o cliente envia um pedido com identificador, dados do cliente, lista de itens e status de pagamento.

## 2. Validação

A validação confirma se o cliente possui nome e endereço, se o pedido tem pelo menos um item e se cada item possui quantidade maior que zero.

## 3. Pagamento

O campo `payment_status` aceita `approved`, `declined` ou `pending`.

- `approved`: o fluxo segue para geração de mensagem.
- `declined`: o pedido é recusado.
- `pending`: o fluxo aguarda confirmação futura.

## 4. Geração de mensagem

Quando o pagamento é aprovado, a aplicação monta um prompt para o Amazon Bedrock gerar uma mensagem curta, clara e amigável.

## 5. Atualização de status

O pedido aprovado passa para o próximo status operacional, como `preparing`.

## 6. Finalização

Na simulação local, o fluxo retorna um JSON com status, mensagem, prompt demonstrativo e próximo passo.

## 7. Tratamento de erro

Pedidos inválidos não chamam Bedrock. Isso reduz custo, evita mensagens incorretas e impede o envio de dados incompletos para a camada generativa.

