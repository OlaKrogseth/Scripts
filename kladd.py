import matplotlib.pyplot as plt

#############################################################################

def plot_(values, error, labels,title,lim, color):
    x = [1,2,3,4]
    #for i in range(len(error)):
        #plt.text(x[i]+0.1, values[i]+0.1, "%.2f" % error[i])
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
    values = [75.37,73.39333333,72.6,72.54666667] #Liposome
    error = [0.5950070028,0.1502590356,1.30656037,0.647696774] #Liposome
    color = "blue"
    plot_(values, error, labels, title, lim, color)
def Liposome37C():
    lim=[60,80]
    title = ("Liposome (37$^\circ$C)") # label of plot
    labels = ["0mM", "150mM", "300mM", "600mM"] #x-axis names
    values = [79.31333333,71.83666667,66.54666667,64.39666667] #Liposome
    error = [0.4734741575,0.3901424241,1.23106097,0.3742696592] #Liposome
    color = "red"
    plot_(values, error, labels, title, lim, color)
def Indolicidin20C():
    lim=[60,80]
    title = ("Indolicidin (20$^\circ$C)") # label of plot
    labels = ["0mM", "150mM", "300mM", "600mM"] #x-axis names
    values = [75.7,74.98,73.95,71.60333333] #Liposome
    error = [1.260277747,0.896883493,0.2345918441,0.4453587817] #Liposome
    color = "green"
    plot_(values, error, labels, title, lim, color)
def Indolicidin37C():
    lim=[60,80]
    title = ("Indolicidin (37$^\circ$C)") # label of plot
    labels = ["0mM", "150mM", "300mM", "600mM"] #x-axis names
    values = [72.27333333,72.58333333,69.41333333,66.93] #Liposome
    error = [0.2269605937,0.4475985304,0.2459223003,1.123224525] #Liposome
    color = "orange"
    plot_(values, error, labels, title, lim, color)
def LL3720C():
    lim=[60,80]
    title = ("LL37 (20$^\circ$C)") # label of plot
    labels = ["0mM", "150mM", "300mM", "600mM"] #x-axis names
    values = [75.00666667,75.78666667,74.97666667,73.14666667] #Liposome
    error = [0.4787599723,0.643980676,0.3489189654,1.04653927] #Liposome
    color = "purple"
    plot_(values, error, labels, title, lim, color)
def LL3737C():
    lim=[60,80]
    title = ("LL37 (37$^\circ$C)") # label of plot
    labels = ["0mM", "150mM", "300mM", "600mM"] #x-axis names
    values = [77.03,71.35333333,68.2,71.41] #Liposome
    error = [0.6482540654,0.3002406442,0.4308518694,0.5776965755] #Liposome
    color = "black"
    plot_(values, error, labels, title, lim, color)

#############################################################################

#Liposome20C()
Liposome37C()

#Indolicidin20C()
Indolicidin37C()

#LL3720C()
LL3737C()

plt.show()
