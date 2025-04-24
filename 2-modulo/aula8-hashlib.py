import hashlib
#print(hashlib.algorithms_available)
#print(hashlib.algorithms_guaranteed)

algoritimo = hashlib.sha256()
print(algoritimo.digest())
frase = "Melhor forma de prever o futuro é crialo!".encode()
algoritimo.update(frase)
print(algoritimo.hexdigest())

md5 = hashlib.md5()
md5.update(frase)
print(md5.hexdigest())