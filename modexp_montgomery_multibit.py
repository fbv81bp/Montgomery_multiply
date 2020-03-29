# Based on Handbook of Applied Cryptography
# by A. Menezes, P. van Oorschot, and S. Vanstone
# CRC Press, 1996. 
# Chapter 14., 14.36 Algorithm Montgomery multiplication, page 603.


# working parameters of the algorithm
m = 16381  # modulus
bit_width = 4  # bit_width of calculation (hexadecimal)
#bit_width = 8  # bytewise calculation
base = 2**bit_width #number system base (hexadecimal)
length = 4  # in hexadecimal
#length = 2  # bytes
R = base**length
x  = 0x16A0  # 5792 in decimal
y  = 0x04CD  # 1229 in decimal


print('Expected result:',x * y % m)


# preparations
x = x * R % m
y = y * R % m
phi_base = 2 ** (bit_width - 1)  # for powers of 2
m_neginv = base - m ** (phi_base - 1) % base


# multiplication
accu = 0
for i in range(length):
    u = (accu % base + (x % base) * (y % base)) * m_neginv % base  # modulo base gives the last digit
    accu = (accu + (x % base) * y + u * m) // base
    x = x >> bit_width  # shiftig x so that modulo base we get th elast digit in the next round
if accu > m:
    accu -= m


# inverse conversion
phi_m = m - 1  # for prime numbers
R_inv = R ** (phi_m - 1) % m
accu  = accu * R_inv % m


print('Result with Montgomery:',accu)
