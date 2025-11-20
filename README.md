# OKX HMAC Signer

GitHub Action para generar firmas HMAC SHA256 para OKX API V5. Integra con Make.com via webhook.

## Uso
1. Agrega secret `OKX_SECRET_KEY` en repo Settings > Secrets.
2. Trigger desde Make: POST a `/dispatches` con `{"event_type": "generate-signature", "client_payload": {"prehash": "tu_prehash"}}`.
3. Fetch output de la run para la sign.

## Ejemplo Prehash
`2025-11-20T13:45:22.789ZPOST/api/v5/trade/order{"instId":"BTC-USDT","tdMode":"cash","side":"buy","ordType":"market","sz":"0.001"}`

## Dependencias
Python 3.12 con hmac, base64, hashlib (nativas).
