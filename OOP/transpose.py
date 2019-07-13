m = [(1,2,3),(4,5,6)]
for row in m:
    print(row)

tm = zip(*m)
for row in tm:
    print(row)

m = [7,8,9]
tm =[10,11,12]
for i,j in zip(m,tm):
    print(i," ",j)