p = 97  # prime 1
q = 101  # prime 2
m = p * q  # modulus
e = 19  # encrypting exponent
phi = (p - 1) * (q - 1)  # Euler's totient
d = e ** (phi - 1) % phi  # decrypting exponent
x = 8  # plain text
y = x ** e % m  # cipher text
print(x == y ** d % m)
