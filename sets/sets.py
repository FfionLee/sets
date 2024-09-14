studentid={12345,57345,43844,38645,12345}
print(studentid)
studentid.add(69472)
print(studentid)

ids=[3759,2096,7948]
studentid.update(ids)
print(studentid)

studentid.remove(57345)
print(studentid)

for i in studentid:
    print(i)

print(len(studentid))

num={7,4,6,2,8,3,9}
numz={8,3,6,2,0,4,1}
print(num.intersection(numz))
print(num.union(numz))
print(num.difference(numz))
print(num.symmetric_difference(numz))
print(num.symmetric_difference_update(numz))