### Current progress: not done

A `torrent.pcap` was given, and the challenge seems to said that the flag will be the filename of the downloaded files.

Let's fire this up in wireshark:
We can see things like `ipv6.torrent.ubuntu.com` while following the UDP streams. 

However, none of these seemed to show up while using the `bittorrent` filter...

### TODO
- find ways to easily extract the data