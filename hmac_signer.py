import hmac
import base64
import hashlib
import os

prehash = os.getenv('PREHASH')
secret_key = os.getenv('SECRET_KEY')

if prehash and secret_key:
    signature = base64.b64encode(hmac.new(secret_key.encode(), prehash.encode(), hashlib.sha256).digest()).decode()
    print(f"Signature: {signature}")
else:
    print("Error: Missing inputs")