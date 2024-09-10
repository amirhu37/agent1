import numpy as np
from agent01 import Agent, TimeStamp
# import agent01
# print(agent01.__dict__)


ag = Agent()

def func1(x):
    return x**2

def func2(x):
    return x**2


ag.add_belif(func2)
ag.add_action(func2, np.array([3,4,5]), TimeStamp.Next)


ag.add_belif(func1)
ag.add_action(func1, np.array([2,3,3]), TimeStamp.Now)




print(ag)
print(ag.actions)
# print(ag.belifs)


print(TimeStamp.Now==TimeStamp.Next)
ag.action = sorted(ag.actions, key=lambda x: x[2])

print(ag.actions)

for f, arg,t in ag.actions:
    print(t)
    if t == TimeStamp.Now:
        s = f(arg)
        print(s)

