from hardware import *
from steam_read import *



print("\nSystem Hardware:")
print("-"*30)
for i in hardware:
    print(i, ":" ,hardware[i])


url = input("\nEnter steam game url: ")
steam_specs = read_specs(url)
if steam_specs[2] > 6:
    print("\nMinimum Hardware to Run:")
    print("-"*30)
    for i in steam_specs[0]:
        print(i, steam_specs[0][i])


    print("\nRecommended Hardware to Run:")
    print("-" * 30)
    for i in steam_specs[1]:
        print(i, steam_specs[1][i])
else:
    print("\nMinimum Hardware to Run:")
    print("-"*30)
    for i in steam_specs[0]:
        print(i, steam_specs[0][i])

