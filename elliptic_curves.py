def elliptic_add(P, Q, a, p):
    x1, y1 = P
    x2, y2 = Q
    lmbd = ((y2 - y1) * invmod(x2 - x1, p)) % p
    x3 = (lmbd**2 - x1 - x2) % p
    y3 = (-y1 + lmbd * (x1 - x3)) % p
    return (x3, y3)

def elliptic_multiply_by2(P, a, p):
    x1, y1 = P
    lmbd = (3 * x1**2 + a) * invmod(2 * y1, p) % p
    x3 = (lmbd**2 - 2 * x1) % p
    y3 = (-y1 + lmbd * (x1 - x3)) % p
    return (x3, y3)

def elliptic_multiply_byn(P, n, a, p):
    x1, y1 = P
    n_b = list(bin(n)[2:])
    cur_P = P
    for i in range(len(n_b)):
        if(n_b[i] == '1'):
            init_P = cur_P
            break
        cur_P = elliptic_multiply_by2(cur_P, a, p)
    next_init_P = init_P
    for j in range(i+1, len(n_b)):
        next_init_P = elliptic_multiply_by2(next_init_P, a, p)
        if(n_b[i] == '1'):
            init_P = elliptic_add(next_init_P, init_P, a, p)

    return init_P

def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

def xgcd(x,y):
    a0=1; b0=0
    a1=0; b1=1
    if x<0:
    	x *= -1
    	a0 = -1
    if y<0:
    	y *= -1
    	b1 = -1
    if x<y:
    	x,y,a0,b0,a1,b1 = y,x,a1,b1,a0,b0
    while 1:
    	times = int(x/y)
    	x -= times*y
    	a0 -= times*a1
    	b0 -= times*b1
    	if x==0:
    		break
    	x,y,a0,b0,a1,b1 = y,x,a1,b1,a0,b0
    return [y,a1,b1]

# Find multiplicative inverse
def invmod(x,p):
	[gcd,a,b] = xgcd(x,p)
	if gcd != 1:
		raise ValueError
	if a<0:
		a += p;
	return a