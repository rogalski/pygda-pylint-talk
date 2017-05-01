import sys

if len(sys.argv) <= 1:
    raise RuntimeError

print('\n'.join(sys.argv[1:]))
