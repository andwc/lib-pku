def c(a):
    m=a.count('@')
    if m !=1:
        return False
    b,d=a.split('@')
    if b.startswith('.') or d.startswith('.') or b.endswith('.') or d.endswith('.'):
        return False
    if '.' not in d:
        return False
    return True
import sys
for line in sys.stdin:
    a = line.strip()
    if c(a):
        print('YES')
    else:
        print('NO')