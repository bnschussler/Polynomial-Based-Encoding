This project "encrypts" data by locking it under a secure key. However, unlike SHA and other normal encryption methods, the entire decryption algorithm consists of a single multiplication by a constant*! It may be that there is an obvious way to break the encoding, but I haven't found one yet (though admittedly I made this very recently and haven't been looking for very long). The entire decryption program is less than 40 lines long.

This isn't exactly an encryption algorithm, in that it locks specific strings under passcodes, but doesn't have a decryptable encoding for every string. It doesn't have many uses as far as I can tell. However, it's simplicity made it interesting to me, and so I decided to make it.

*Technically, the input string is converted into an odd integer first, but the bulk of the math consists of a single multiplication.
