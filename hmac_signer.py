import hmac
import base64
import hashlib
import os

# Input from GitHub env
prehash = os.getenv('PREHASH')
secret_key = os.getenv('SECRET_KEY')

if prehash and secret_key:
    # HMAC SHA256 del prehash con secret como key
    signature_bytes = hmac.new(
        secret_key.encode('utf-8'),
        prehash.encode('utf-8'),
        hashlib.sha256
    ).digest()
    # Base64 encode
    signature = base64.b64encode(signature_bytes).decode('utf-8')
    # Output a archivo para GitHub leer
    with open('signature.txt', 'w') as f:
        f.write(signature)
    print(f"Signature generated: {signature[:20]}...")  # Log parcial por seguridad
else:
    print("Error: Missing PREHASH or SECRET_KEY")
    exit(1)
