# from .elliptic import make_keypair as get_point
from elliptic import get_pg, scalar_mult
from to_r1cs import code_to_r1cs_with_inputs
from qap import r1cs_to_qap
import random
import rsa
import numpy as np
(pubkey, privkey) = rsa.newkeys(2048)

#Choose s
def create_keys_for_voters(voters_list):
    voters_keys = []
    for elem in voters_list:
        crypto = rsa.encrypt(elem, pubkey)
        voters_keys.append(crypto)
    return voters_keys

fu = """
def qeval(x):
    y = x**3
    return y + x + 5
"""


def main():
    p, G = get_pg()
    # s = get_point()
    p1 = 3000
    k = 10
    alpa = random.randrange(1, p1)
    b = random.randrange(1, p1)

    r, A, B, C = code_to_r1cs_with_inputs(fu, [3])
    Ap, Bp, Cp, Z = r1cs_to_qap(A, B, C)

    crs = open("CRS", 'w')
    crs.write(f'{len(Ap)}\n')
    s = np.array([k**(len(Ap[0])-i-1) for i in range(len(Ap[0]))])
    Apx = np.dot(np.array(Ap), s)
    Bpx = np.dot(np.array(Bp), s)
    Cpx = np.dot(np.array(Cp), s)
    for i in range(len(Ap)):
        ai = Apx[i]
        bi = Bpx[i]
        ci = Cpx[i]
        crs.write(''.join('%s\n%s\n%s\n' % (ai, bi, ci)))
    ABCpx = np.dot(np.array(np.array(Ap) + np.array(Bp) + np.array(Cp)), s)
    for i in range(len(Ap)):
        abci = ABCpx[i]
        crs.write(''.join('%s\n' % abci))


if __name__ == '__main__':
    main()


