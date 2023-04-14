import matplotlib.pyplot as plt

#############################################################################

def plot_(values, error, labels,title,lim, color):
    x = [1,2,3,4]
    #for i in range(len(error)):
        #plt.text(x[i]+0.1, values[i]+0.1, "%.2f" % error[i])
    lim=[50,100]
    plt.errorbar( x,values, yerr=error, fmt='o', label=title, color=color)
    plt.plot( x,values,color=color)
    plt.ylim(lim)
    plt.ylabel('nm')
    plt.xticks(x, labels)
    plt.legend(fontsize=12)


def Liposome20C():
    lim=[60,80]
    title = "Liposome (20$^\circ$C)" # label of plot
    labels = ["0mM", "150mM", "300mM", "600mM"] #x-axis names
    values = [74.64166667,73.23166667,72.60833333,72.93333333] #Liposome
    error = [1.03058236, 0.2602562839, 2.263028944, 1.121843721] #Liposome
    color = "blue"
    plot_(values, error, labels, title, lim, color)
def Liposome37C():
    lim=[60,80]
    title = ("Liposome (37$^\circ$C)") # label of plot
    labels = ["0mM", "150mM", "300mM", "600mM"] #x-axis names
    values = [79.31333333,73.54166667,67.06333333,65.04666667] #Liposome
    error = [0.8200812968, 0.6757465008, 2.132260147, 0.6482540654] #Liposome
    color = "red"
    plot_(values, error, labels, title, lim, color)
def Indolicidin20C():
    lim=[60,80]
    title = ("Indolicidin (20$^\circ$C)") # label of plot
    labels = ["0mM", "150mM", "300mM", "600mM"] #x-axis names
    values = [77.115,74.295,74.32166667,72.07166667] #Liposome
    error = [2.18286509, 1.553447778, 0.4063249931, 0.7713840375] #Liposome
    color = "green"
    plot_(values, error, labels, title, lim, color)
def Indolicidin37C():
    lim=[60,80]
    title = ("Indolicidin (37$^\circ$C)") # label of plot
    labels = ["0mM", "150mM", "300mM", "600mM"] #x-axis names
    values = [70.86833333,72.39833333,71.77333333,68.685] #Liposome
    error = [0.3931072797, 0.7752633961, 0.4259499188, 1.945481945] #Liposome
    color = "orange"
    plot_(values, error, labels, title, lim, color)
def LL3720C():
    lim=[60,80]
    title = ("LL37 (20$^\circ$C)") # label of plot
    labels = ["0mM", "150mM", "300mM", "600mM"] #x-axis names
    values = [76.39833333,76.15833333,75.885,73.74833333] #Liposome
    error = [0.8292365967, 1.11540725, 0.6043453759, 1.812659188] #Liposome
    color = "purple"
    plot_(values, error, labels, title, lim, color)
def LL3737C():
    lim=[60,80]
    title = ("LL37 (37$^\circ$C)") # label of plot
    labels = ["0mM", "150mM", "300mM", "600mM"] #x-axis names
    values = [77.03,72.505,68.55533333,71.29333333] #Liposome
    error = [1.122808978, 0.5200320503, 0.7462573283, 1.00059982] #Liposome
    color = "black"
    plot_(values, error, labels, title, lim, color)


def plot_no_err(values, labels,title,lim, color):
    x = [1,2,3,4,5]
    lim=[80,120]
    #for i in range(len(error)):
        #plt.text(x[i]+0.1, values[i]+0.1, "%.2f" % error[i])
    error = [0,0,0,0,0]
    plt.errorbar( x,values, yerr=error, fmt='o', label=title, color=color)
    plt.plot( x,values,color=color)
    plt.ylim(lim)
    plt.ylabel('nm')
    plt.xticks(x, labels)
    plt.legend(fontsize=12)

def LipOld20C():
    lim=[120,80]
    title = "Liposome (20$^\circ$C)" # label of plot
    labels = ["0mM", "150mM", "300mM", "600mM", "1200mM"] #x-axis names
    values = [102.28,100.18,98.14,96.54,94.23] #Liposome
    color = "black"
    plot_no_err(values, labels, title, lim, color)

def GramOld20C():
    lim=[120,80]
    title = ("Gramicidin (20$^\circ$C)") # label of plot
    labels = ["0mM", "150mM", "300mM", "600mM", "1200mM"] #x-axis names
    values = [109.71, 107.33, 102.58, 100.82, 100.12] #Liposome
    color = "green"
    plot_no_err(values, labels, title, lim, color)

def IndoOld20C():
    lim=[120,80]
    title = ("Indolicidin (20$^\circ$C)") # label of plot
    labels = ["0mM", "150mM", "300mM", "600mM", "1200mM"] #x-axis names
    values = [102.82,100.84,99.13,97.59,94.76] #Liposome
    color = "blue"
    plot_no_err(values, labels, title, lim, color)

def LL37Old20C():
    lim=[120,80]
    title = ("LL37 (20$^\circ$C)") # label of plot
    labels = ["0mM", "150mM", "300mM", "600mM", "1200mM"] #x-axis names
    values = [110.14,100.68,99.25,96.86, 95.86] #Liposome
    color = "red"
    plot_no_err(values, labels, title, lim, color)

#############################################################################

def _20():
    Liposome20C()
    Indolicidin20C()
    LL3720C()
def _37():
    Liposome37C()
    Indolicidin37C()
    LL3737C()

def _Old():
    LipOld20C()
    GramOld20C()
    IndoOld20C()
    LL37Old20C()

for i in range(100):
    data = eval(input("Input: 0, 20 or 37\n"))
    if data == 20:
        _20()
        plt.show()
    elif data == 37:
        _37()
        plt.show()
    elif data == 0:
        _Old()
        plt.show()
    else:
        break
