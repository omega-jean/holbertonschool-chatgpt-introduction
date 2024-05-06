#!/usr/bin/python3
import sys

# Commence à parcourir les arguments à partir de sys.argv[1]
# sys.argv[0] contient le nom du script lui-même
for i in range(1, len(sys.argv)):
    print(sys.argv[i])
