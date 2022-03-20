### Current progress: not done

A `disk.img` image file is given.

We have tried the command below to grep all potential PRIVATE KEY files

```bash
strings -t d disk.img | grep -iE "BEGIN (.*) PRIVATE KEY"
```

These are output into [potential_priv_keylist](potential_priv_keylist.txt)
However, we cannot use any of these key to login to the server...