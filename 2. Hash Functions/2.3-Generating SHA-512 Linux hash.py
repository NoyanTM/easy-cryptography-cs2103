#(env) root@UbuntuNoyan:~# sudo tail -n 1 /etc/shadow
#noyan:$y$j9T$O6M1OnKXN6KBbSePzqW5v/$4c5qscKaGTe7gtcWxZucEQKR40kJgfuzpsTXZ/kFRk6:19450:0:99999:7:::

import hashlib
from passlib.hash import sha512_crypt # pip install passlib
print(sha512_crypt.using(salt="qIo0foX5", rounds=5000).hash("P0sw0rd"))
