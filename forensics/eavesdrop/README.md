### Current progress: not done

A `capture.flag.pcap` packet capture file is given.

We opened this file up in wireshark and follow the TCP stream.
There are 3 streams - two of which seems to be important for us.

Stream 0 looks like the following:
![stream0](stream0.jpg)

And Stream 2:
![stream2](stream2.jpg)

Stream 0 tells us that the flag could potentially be encrypted in a `DES3` encryption.
We can potentially decrypt this with: `openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123`

Stream 2 is actually this flag file mentioned above, seeing as it is being transferred via port `9002`.

We extracted the stream 2 value to python using the "c array" format in wireshark. We placed this into [enc_arr.py](enc_arr.py)

However, it seems to show a `bad decrypt` error when running the command...

### TODO
- Clean out the value for `file.des3` from the .pcap