#chart and diagram generation
import matplotlib.pyplot as plt


#averages

labelsTotal = ['non-affected', 'misssense']
labelsOMiss = ['methionine', 'stop signal', 'size', 'amino']

fig1, axs=plt.subplots(1, 2, figsize=(10, 6))

average = [(10000000-7035707), 7035707]
totalAverage = [12.0471622, 27.6311912, 21.9600241, 38.3616224]

axs[0].pie(average, labels=labelsTotal, colors=['#66FF66', '#FF6666'], autopct='%1.0f%%')
axs[0].set_title('Proportion of misssense mutations')
axs[1].pie(totalAverage, labels=labelsOMiss, colors=['#FFB266', '#66B2FF', '#FF66B2', '#66FF66'], autopct='%1.0f%%')
axs[1].set_title('Proportion of all types of mutations')

#fig1.show()
fig1.savefig('/Users/j.alcaide/Desktop/figure_1.pdf')

#10*testevolution

fig2, axs=plt.subplots(1, 2, figsize=(10, 6))

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
misssenseEvo = [703188, 703473, 704233, 703102, 704122, 704163, 703709, 703599, 703777, 703141]
methionineEvo = [84939, 84185, 85074, 84845, 84325, 84995, 84776, 84577, 84979, 85125]
stopSignalEvo = [194649, 194343, 194198, 194059, 194880, 194256, 194088, 194277, 194747, 195050]
sizeEvo = [154151, 154719, 154477, 154778, 154110, 155180, 154565, 154216, 154622, 154622]
aminoEvo = [269449, 270226, 270484, 269420, 270807, 269732, 270280, 270529, 269429, 269346]

axs[0].plot(x, misssenseEvo, marker="^")
axs[0].set_ylim(600000, 800000)
axs[0].set_title('misssense mutations evolution')
axs[0].set_xlabel('testcases (1-10)')
axs[0].set_ylabel('numbers of misssense muatation')
axs[1].plot(x, methionineEvo, marker="2", label='methionine')
axs[1].plot(x, stopSignalEvo, marker="2", label='stop signal')
axs[1].plot(x, sizeEvo, marker="2", label='size')
axs[1].plot(x, aminoEvo, marker="2", label='amino')
axs[1].set_title('evolution of all mutations')
axs[1].set_xlabel('testcases (1-10)')
axs[1].set_ylabel('number of mutations')
axs[1].set_ylim(50000)
axs[1].legend(loc='lower left')

#fig2.show()
fig2.savefig('/Users/j.alcaide/Desktop/figure_2.pdf')


#margins

fig3, axs=plt.subplots(1, 2, figsize=(10, 6))

x = ['methionine', 'stop signal', 'size', 'amino']
anomaliesList = [methionineEvo, stopSignalEvo, sizeEvo, aminoEvo]
totalSum = [847820, 1944547, 1545438, 2699702]

#axs[0].boxplot(methionineEvo)
axs[0].boxplot(anomaliesList, labels=x)
axs[1].bar(x, totalSum)
fig3.show()
fig3.savefig('/Users/j.alcaide/Desktop/figure_3.pdf')
