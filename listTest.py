
import matplotlib.pyplot as plt
def makegraph(list):
    plt.bar(range(len(list)),list)
    plt.show()

a1=[1,2,3,54,65,76]
for x in range(5):
    a1.append(x)
    makegraph(a1)
