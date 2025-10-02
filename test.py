import random

a = random.randrange(5, 10)
X = int(a * a * 0.2)

labirent = []

for i in range(a):
    sıra = []
    for j in range(a):
        sıra.append('0')
    labirent.append(sıra)

i = 0
while i < X:
    r = random.randrange(0, a)
    c = random.randrange(0, a)
    if labirent[r][c] == '0':
        labirent[r][c] = 'X'
        i += 1


while True:
    pr = random.randrange(0, a)
    pc = random.randrange(0, a)
    if labirent[pr][pc] == '0':
        labirent[pr][pc] = 'C'
        break


while True:
    fr = random.randrange(0, a)
    fc = random.randrange(0, a)
    if labirent[fr][fc] == '0':
        labirent[fr][fc] = 'M'
        break


for sıra in labirent:
    print(" ".join(sıra))


def konum(r, c):
    return f"{chr(ord('A') + c)}{r + 1}"


r, c = fr, fc
while (r, c) != (pr, pc):
    print(konum(r, c))
    yonler = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    random.shuffle(yonler)
    for dr, dc in yonler:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < a and 0 <= nc < a:
            if labirent[nr][nc] in ['0', 'C']:
                r, c = nr, nc
                break

print(konum(r, c))
print("mission complete...")  

