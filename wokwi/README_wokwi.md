# Coleta de Dados – Wokwi (Fase 2 / Cap 1)

Este projeto simula um sistema de irrigação inteligente usando ESP32 na plataforma Wokwi.

## Sensores simulados
- 3 botões → N, P, K (nutrientes)
- LDR → pH do solo (simulado)
- DHT22 → umidade e temperatura
- Relé → liga/desliga a bomba de irrigação
- LED verde → indica irrigação ligada

## Geração dos dados
Durante a simulação, o código enviou para o **Serial Monitor** registros no formato JSON:

```json
{"umid":13.5,"ph":6.34,"N":true,"P":true,"K":true,"chuva":false,"bomba":true}
{"umid":45.6,"ph":6.34,"N":true,"P":true,"K":true,"chuva":true,"bomba":false}
