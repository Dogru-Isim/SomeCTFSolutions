flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x5c) + chr(0x01) \
 + chr(0x57) + chr(0x2a) + chr(0x17) + chr(0x5e) + chr(0x5f) + chr(0x0d) + chr(0x3b) + chr(0x19) + chr(0x56) + chr(0x5b) + chr(0x5e) \
 + chr(0x36) + chr(0x53) + chr(0x07) + chr(0x51) + chr(0x18) + chr(0x58) + chr(0x05) + chr(0x57) + chr(0x11) + chr(0x3a) + chr(0x0f) \
 + chr(0x0a) + chr(0x5b) + chr(0x57) + chr(0x41) + chr(0x55) + chr(0x0c) + chr(0x59) + chr(0x14)

secret = flag_enc
key = "enkidu"

new_key = key
i = 0
while len(new_key) < len(secret):
    new_key = new_key + key[i]
    i = (i + 1) % len(key)
    
print("".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)]))
