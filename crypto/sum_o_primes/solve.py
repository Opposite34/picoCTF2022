x = 0x1c0e127fe9274dcd9830ecf0af5cf1c75e7c24106247495f3756d013d939ea66befa038012844379905cb0281cd4009f1bd6102680b8a029d69a51dbbfc1ddf77b21eeee42b0e4897cd2a541b99d41523e5cd44799cd209eeae33db029937aad6c5bb3f359dad8b780e1b07d73ac1d0cef6d5517ab78ec19d8dbe31d5322c6382
n = 0xc4bf129f0b86c18115b8eabfc5399e366e75d703f191f993b56d433d86c2a7c85ff1304c9d9068893232ced732e769114873a6dfdc61949388a0bc8a1f4ef0332888e714c9deadb2439c532aa1c8210f8a90409f6e7776239eebf649149f02e005683c86e677ebf17506ed076eddf593696dbc58340dde1c3a7da443f0b27d3ba8e8f04e7139e199ef34cb88e26e3794b319a4018a6627203c479edd50cb9c5b2cdc8a8de14c6c0294e6ad13c95c98fe8e8f1b9587dc7f2ddbba1233a14ed831321323c1e68b525f8fb8a93bd7081e702606c7174d1534af66858c25c5b19304accde3a0659cd29c3c7cb411e015422b5a8fd0d403470553bc5f870b3506709d
c = 0x2c628ae700a75caf1be3e354599249dd9ae80f38c1ac8fdcd53167e918f53b1a1cbd42a5e57951d634c3f88b7e96787c8b19682a0ab5e78eb97dc87cf51e3099b0b2b105183ae524d170bdf4a3cd5fbccd021315a94e6a99220a876b970bee15b40c39794d5063c0fe9da2b728e641d3a488fc198363785224717985b5b8e0ee055f03d6b165ad6b9e0bf99dc50a371629ed012836c0cfa7073d708650bc4e7b8277a5ddab3aa5d6d7e0deea2266792898d8ef603850eab52c3d06cf8a93b7e91321b310035f867c32fea4238ba725a165ba972dd0aa543b41be82f67325fb9a2bfddcec9ae9a4f95f0981de531f4442ba6ee9d95e4ae11212137900ee0938ab
e = 65537

def sum_o_prime_decrypt(sum, n, c, e):
    #(p-1)(q-1) = pq - p - q + 1
    #(p-1)(q-1) = pq - (p+q) + 1
    #(p-1)(q-1) = n - sum + 1
    m = n - sum + 1
    d = pow(e, -1, m)

    plaintext = pow(c, d, n)
    # int -> hex -> bytes -> text
    return(bytes.fromhex(hex(plaintext)[2:]).decode('utf-8'))

with open("flag.txt", 'w') as f:
    f.write(sum_o_prime_decrypt(x,n,c,e))