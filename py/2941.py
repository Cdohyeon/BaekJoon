t = input()
a = []
a.append(t.count("c="))
a.append(t.count("c-")) 
a.append(t.count("d-")) 
a.append(t.count("lj"))
a.append(t.count("nj"))
a.append(t.count("s="))
a1 = t.count("dz=")
a.append(t.count("z=")-a1)

print(len(t)-sum(a)-(a1*2))
