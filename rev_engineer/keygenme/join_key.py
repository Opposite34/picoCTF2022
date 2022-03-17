local_98 = "7b4654436f636970"
local_90 = "30795f676e317262"
local_88 = "6b5f6e77305f7275"
local_80 = "5f7933"
local_ba = "7d"

join_arr = [local_ba, local_80, local_88, local_90, local_98]

def decode_hex(hexval):
    return bytes.fromhex(hexval).decode('utf-8')

print("".join([decode_hex(val) for val in join_arr])[::-1])