import random
sms = "hi thsis tx_dt12"
print(sms)

encycption_lol = 128 // 8
chr_pool = ''
for i in range(0x00, 0x255):
    chr_pool += chr(i)
#print(chr_pool)
key=''
for i in range(encycption_lol):
    key += random.choice(chr_pool)
#print(key)
key_index = 0
max_key_index = encycption_lol-1


# encryption
enc_msm=""
for char in sms:
    encrypted_chr = ord(char) ^ ord(key[key_index])
    enc_msm += chr(encrypted_chr)
    if key_index >= max_key_index:
        key_index = 0
    else:
        key_index += 1
print(enc_msm)

key_index = 0
dec_sms =''
for char_dec in enc_msm:
    dec_char = ord(char_dec) ^ ord(key[key_index])
    dec_sms += chr(dec_char)

    if key_index >= max_key_index:
        key_index = 0
    else:
        key_index += 1

print(dec_sms)
