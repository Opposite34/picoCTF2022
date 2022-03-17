"""
char peer0_0[] = { /* Packet 57 */
0x53, 0x61, 0x6c, 0x74, 0x65, 0x64, 0x5f, 0x5f, 
0x03, 0xa9, 0x15, 0xe7, 0x2c, 0x0f, 0xb7, 0x5f, 
0x35, 0x2a, 0xda, 0x1e, 0x07, 0x31, 0x57, 0x0d, 
0x63, 0x6c, 0xaf, 0x9b, 0x67, 0xac, 0x26, 0x48, 
0x02, 0x62, 0x5a, 0x94, 0x48, 0xb6, 0x54, 0xd1, 
0xce, 0x8a, 0xfb, 0xa4, 0xdc, 0xae, 0x87, 0x07 };
"""

des_enc_arr = [
0x53, 0x61, 0x6c, 0x74, 0x65, 0x64, 0x5f, 0x5f, 
0x03, 0xa9, 0x15, 0xe7, 0x2c, 0x0f, 0xb7, 0x5f, 
0x35, 0x2a, 0xda, 0x1e, 0x07, 0x31, 0x57, 0x0d, 
0x63, 0x6c, 0xaf, 0x9b, 0x67, 0xac, 0x26, 0x48, 
0x02, 0x62, 0x5a, 0x94, 0x48, 0xb6, 0x54, 0xd1, 
0xce, 0x8a, 0xfb, 0xa4, 0xdc, 0xae, 0x87, 0x07 ]

text = "".join(chr(val) for val in des_enc_arr)

with open("file.des3", 'w') as f:
    f.write(text)
