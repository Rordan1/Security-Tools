
#Choose file encryption / password hashing / key gen

##file encryption

0. tool
*   openssl
*   gpg

1.   Algorithm

*   md5
*   sha256


2.   Salt




*   hmac


3.  Pepper


*   pbkdf2

4. File Compression


*   gzip
*   tar


## hashing passwords


1.   hashing algorithm
, , or

*   bcrypt
*   Argon2
*   Scrypt




##key gen


1.   assymetric
*   ssh-keygen

2.   symetric
openssl

3. password or not


*   asym: -N "your_password_here": Sets the password for the private key
*  sym: -k "your_password_here": Sets the password for the key.





-p option to add or change a passphrase for an existing SSH private key
-t: Specifies the key type (in this case, RSA). \
-b: Specifies the key length (4096 bits is a common choice for RSA).\
-f: Specifies the filename for the key pair.







