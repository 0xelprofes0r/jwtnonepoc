# JWT Vulnerability Testing Tool

A lightweight, native Python script designed to test local lab environments and CTF challenges for common JSON Web Token (JWT) implementation flaws. It generates forged tokens using two well-known logical bypass techniques without relying on external dependencies.

## Key Features

- **'None' Algorithm Exploration:** Generates signature-less tokens by setting the `alg` header to `none`.
- **Key Confusion (RS256 to HS256):** Misuses the server's public key as a symmetric HMAC-SHA256 secret key to sign custom payloads.
- **Dynamic Payload Handling:** Accepts custom user metadata (e.g., username, roles) directly via standard input.
- **Multi-line Input Support:** Seamlessly handles multiline PEM-formatted public keys using system input streams.

## Technical Details

The script automatically handles JWT structural requirements:
- Converts Python dictionaries to minified JSON strings.
- Encodes data into URL-Safe Base64 format.
- Trims trailing padding characters (`=`) according to RFC 7519 standards.

## Usage

Ensure you have Python 3.x installed. Run the script from your terminal:

```bash
python poc.py
```

### Flow
1. Enter your target payload data (e.g., target username and privileged role).
2. Choose the exploitation vector (`1` for None Algorithm, `2` for Key Confusion).
3. If Key Confusion is selected, paste the target server's Public Key into the prompt, hit `Enter`, and signal the end of input (`Ctrl+D` on Linux/macOS or `Ctrl+Z` on Windows).
4. Copy the generated token for your testing environment.

## Disclaimer

This tool is created strictly for educational purposes, authorized security audits, and CTF competitions. Do not use this script against production environments or unauthorized systems.
