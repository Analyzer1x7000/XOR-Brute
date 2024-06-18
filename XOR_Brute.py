# Function to attempt XOR decryption with all possible single-byte keys
def xor_decrypt(data, key):
    decoded = ""
    for i in range(0, len(data), 2):
        byte = data[i:i+2]
        if len(byte) == 2:
            decoded += chr(int(byte, 16) ^ key)
    return decoded

# Try all keys from 0 to 255 and check for readable outputs
possible_decryptions = []
for key in range(256):
    decrypted = xor_decrypt(encoded_data, key)
    if all(32 <= ord(c) < 127 for c in decrypted):  # Check if the output is mostly printable ASCII
        possible_decryptions.append((key, decrypted))

possible_decryptions
