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

# preparations with plain maths
def convert_to_Montgomery_plain(x, R, m):
    x = x * R % m
    return x

def neg_inv(m, bit_width, base):
    phi_base = 2 ** (bit_width - 1)  # for powers of 2
    m_neginv = base - m ** (phi_base - 1) % base
    return m_neginv

# multiplication
def Montgomery_multiplication(x, y, base, m, m_neginv, length):
    accu = 0
    for i in range(length):
        u = accu % base + (x % base) * (y % base)
        v = u * m_neginv % base  # modulo base gives the last digit
        accu = (accu + (x % base) * y + v * m) // base
        x = x >> bit_width  # shiftig x so that modulo base we get th elast digit in the next round
    if accu > m:
        accu -= m
    return accu

# inverse conversion with plain maths
def reverse_from_Montgomery_plain(accu, R, m):
    phi_m = m - 1  # for prime numbers
    R_inv = R ** (phi_m - 1) % m
    accu  = accu * R_inv % m
    return accu

x = convert_to_Montgomery_plain(x, R, m)
y = convert_to_Montgomery_plain(y, R, m)
m_neginv = neg_inv(m, bit_width, base)
accu = Montgomery_multiplication(x, y, base, m, m_neginv, length)
accu = reverse_from_Montgomery_plain(accu, R, m)

print('Result with Montgomery:',accu)
