#!/usr/bin/env python
import fileinput
ff = fileinput.input(files=("/etc/fstab"), inplace=True, backup='.bak')
for line in ff:


    if "cifs" in line:
        s = line.split()
        ops = s[3]
        ops_s = ops.split(',')
        c = 0
        for o in ops_s:
            if "vers" in o:
                ops_s.pop(c)
            if "cache" in o:
                ops_s.pop(c)
            c += 1
        ops_s.append("vers=3.0")
        ops_s.append("cache=strict")
        s[3] = ",".join(ops_s)

        line2 = " ".join(s)
        print(line2)
    else:
        print(line),
ff.close()
