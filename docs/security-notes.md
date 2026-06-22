# Segurança e boas práticas

Este projeto foi preparado para GitHub público e não contém credenciais.

## Recomendações

- Não versionar `.env` real.
- Não versionar chaves AWS, tokens, certificados, arquivos `.pem` ou `.key`.
- Não subir a pasta `.aws/`.
- Não usar dados reais de clientes em exemplos ou testes.
- Validar entrada antes de chamar qualquer modelo.
- Evitar enviar dados sensíveis ao LLM.
- Revisar custos antes de um deploy real.

## IAM

O arquivo `infrastructure/iam-policy-example.json` é didático e usa `Resource: "*"` para simplificar o estudo. Em produção, aplique least privilege com ARNs específicos para state machines, modelos, logs e demais recursos.

## Bedrock

Antes de usar Bedrock em produção, revise o modelo escolhido, a região, o formato do payload, os limites de tokens, as políticas de retenção de dados e possíveis guardrails.

