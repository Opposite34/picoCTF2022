The prompts tells us the following:

```
Alice and Bob wanted to exchange information secretly. 
The two of them agreed to use the Diffie-Hellman key exchange algorithm, using p = 13 and g = 5. 
They both chose numbers secretly where Alice chose 7 and Bob chose 3. 
Then, Alice sent Bob some encoded text (with both letters and digits) 
using the generated key as the shift amount for a Caesar cipher over the alphabet and the decimal digits. 
Can you figure out the contents of the message?
```

Using the given p and g value, we are able to decode the secret message which is `5` 

Then we use the value as a the shift value and perform caeser shift and we receive `C4354R_C1PH3R_15_4_817_0U7D473D_E657DA5D`

Flag: `picoCTF{C4354R_C1PH3R_15_4_817_0U7D473D_E657DA5D}`