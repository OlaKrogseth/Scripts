import numpy as np
import matplotlib.pyplot as plt
import os
import math
import scipy.optimize as sopt
import  tkinter as tk
from tkinter import filedialog



def readfile(fil): #Reads the data file, and returns an list of sublist, where each sublist is a line form the file
    liste=[]
    filename = fil
    file = open(filename, 'r')
    b = file.readline()
    while b!='':
        c = b.split()
        if len(c)!=0:
            liste.append(c)
        b = file.readline()
    file.close()
    return liste



def reshape_rawdata_list(data_list): #Takes in the file list from "Readfile" and returns an 3 arrays with Q, I, and  dI,
    length=len(data_list)
    Q_list=[0]*length
    I_list=[0]*length
    dI_list=[0]*length
    for i in range(len(data_list)):
        Q=float(data_list[i][0])*0.1 #To get resiprocal Å rathar than resiprocal nm
        I=float(data_list[i][1])*0.000802551 # Apropriate scaling of y axis
        dI=float(data_list[i][2])*0.000802551
        Q_list[i]=Q
        I_list[i]=I
        dI_list[i]=dI
    return Q_list,I_list,dI_list

def reshape_pros_list(data_list): #Takes in the file list from "Readfile" and returns an 3 arrays with Q, I, and  dI,
    length=len(data_list)
    Q_list=[0]*length
    I_list=[0]*length
    dI_list=[0]*length
    for i in range(len(data_list)):
        Q=float(data_list[i][0])
        I=float(data_list[i][1])
        dI=float(data_list[i][2])
        Q_list[i]=Q
        I_list[i]=I
        dI_list[i]=dI
    return Q_list,I_list,dI_list


main_path="M:\Documents\Master\Qtiprojects\ESRF240922\All"
dir_list=os.listdir(main_path)


def select_sample_code(sample_code,dir_list):
    samples=[]
    for sample in dir_list:
        if sample_code in sample:
            samples.append(sample)
    samples.sort()
    return samples

#selected_samples=select_sample_code("VKLP1_", dir_list)
#print(selected_samples)

def acsess_frames(sample_code):
    Path=os.path.join(main_path,sample_code)
    Path=os.path.join(Path,'frames')
    cons=os.listdir(Path)[0]
    if cons=='.DS_Store': # This is to deal with the automatically generated folder in mac
        cons=os.listdir(Path)[1]
    Path=os.path.join(Path,cons)
    #print(Path)
    frames=os.listdir(Path)
    #print(frames)
    return frames,Path

def sort_frames(frame_list):
    buffer=[]
    samples=[]
    for frame in frame_list:
        if "buffer" in frame:
            buffer.append(frame)
        elif "sample" in frame:
            samples.append(frame)
    buffer.sort()
    samples.sort()
    return [buffer,samples]

def read_multiple(Path,frames):
    data_list=[]
    for frame in frames:
        filename=os.path.join(Path,frame)
        frame_list=readfile(filename)
        Q,I,dI=reshape_rawdata_list(frame_list)
        data=[frame,Q,I,dI]
        data_list.append(data)
    return data_list



def plot_figure():
    plt.figure(figsize=(14,10))

def select_indexes(frames,list_of_indexes_to_remove):
    new_frames=[]
    for i in range(len(frames)):
        if i not in list_of_indexes_to_remove:
            new_frames.append(frames[i])
    return new_frames


def plot_multiple(data_matrix):
    plot_figure()
    for sample in data_matrix:
        title=sample[0]
        Q=sample[1]
        I=sample[2]
        dI=sample[3]
    #plt.errorbar(Q,I,dI)
        plt.scatter(Q,I,label=title)
    plt.semilogy()
    plt.semilogx()
    plt.legend()
    plt.show()

#new_frames=select_indexes(sorted_frames[1], [8,9])
#new_buffer=select_indexes(sorted_frames[0], [])
#loaded_data=read_multiple(Path, new_frames)
#loaded_buffer=read_multiple(Path, new_buffer)
#print(loaded_data[0][3])
#plot_multiple(loaded_data)

def error_average(Ldata):
    num_of_Qs=len(Ldata[0][1])
    num_of_frames=len(Ldata)
    average_Is=[]
    combined_errors=[]
    for i in range(num_of_Qs):
        dI_list=[] # List of the dI values at a single Q from all the frames
        I_list=[] # List of the dI values at a single Q from all the frames
        for j in range(num_of_frames):
            dI=Ldata[j][3][i]
            I=Ldata[j][2][i]
            dI_list.append(dI)
            I_list.append(I)
        dI_list=np.array(dI_list)
        I_list=np.array(I_list)
        weights=1/(dI_list*dI_list) #Computes list of weights, correspeonding to the weight of the I of each frame at a given Q
        weighted_I=np.dot(I_list,weights) # Multipies each I with the corresponding weight and computes the sum if weighted Is
        weights_sum=np.sum(weights) # Sums up the weights
        average_I=weighted_I/weights_sum #Computes the error weigthed average I
        average_Is.append(average_I)
        w_sdt=np.sqrt(1/(np.sum(1/(dI_list**2))))
        combined_errors.append(w_sdt)
    Qs=Ldata[0][1]
    return [Qs,average_Is,combined_errors]


def error_average_2(Ldata): #This is with standard diviation, we are using standard error.
    num_of_Qs=len(Ldata[0][1])
    num_of_frames=len(Ldata)
    average_Is=[]
    combined_errors=[]
    for i in range(num_of_Qs):
        dI_list=[] # List of the dI values at a single Q from all the frames
        I_list=[] # List of the dI values at a single Q from all the frames
        for j in range(num_of_frames):
            dI=Ldata[j][3][i]
            I=Ldata[j][2][i]
            dI_list.append(dI)
            I_list.append(I)
        dI_list=np.array(dI_list)
        I_list=np.array(I_list)
        weights=1/(dI_list*dI_list) #Computes list of weights, correspeonding to the weight of the I of each frame at a given Q
        weighted_I=np.dot(I_list,weights) # Multipies each I with the corresponding weight and computes the sum if weighted Is
        weights_sum=np.sum(weights) # Sums up the weights
        average_I=weighted_I/weights_sum #Computes the error weigthed average I
        average_Is.append(average_I)
        var_diff=(I_list-average_I)**2
        weighted_var_diff=np.dot(var_diff,weights)
        var=weighted_var_diff/weights_sum
        std=np.sqrt(var)
        combined_errors.append(std)
    Qs=Ldata[0][1]
    return [Qs,average_Is,combined_errors]

def simple_average_std(Ldata):
    num_of_Qs=len(Ldata[0][1])
    num_of_frames=len(Ldata)
    average_Is=[]
    stds=[]
    for i in range(num_of_Qs):
        #dI_list=[] # List of the dI values at a single Q from all the frames
        I_list=[]
        for j in range(num_of_frames):
            #dI=Ldata[j][3][i]
            I=Ldata[j][2][i]
            #dI_list.append(dI)
            I_list.append(I)
        avrI=np.average(I_list)
        std=np.std(I_list)
        average_Is.append(avrI)
        stds.append(std)
    Qs=Ldata[0][1]
    return [Qs,average_Is,stds]



#averaged_data=error_average(loaded_data)
#averaged_buffer=error_average(loaded_buffer)
#print(averaged_data[2][0])


def plot_average(sampleName,averaged_data):
    plot_figure()
    Q=averaged_data[0]
    I=averaged_data[1]
    dI=averaged_data[2]
    plt.errorbar(Q,I,dI,label=sampleName)
    plt.semilogy()
    plt.semilogx()
    plt.legend()
    plt.show()

def get_frame_number(filename,current_highest_frame,has_been_0):
    a=int(filename[-8:-4])
    if a==0:
        if has_been_0==1:
            frame_number = a+current_highest_frame+1
            has_been_0=1
        else: frame_number = a
    elif a > current_highest_frame:
        frame_number=a
        current_highest_frame=a
    elif a <= current_highest_frame:
        frame_number=a+current_highest_frame+1
    return frame_number,current_highest_frame,has_been_0

def get_datapoint_marker(frame_number):
    marker_codes=["o","s","v","p","D","P"]
    marker_index=frame_number//10
    marker=marker_codes[marker_index]
    return marker



def plot_average_with_samples(loaded_data):
    averaged_data=error_average(loaded_data)
    plot_figure()
    current_highest=0
    for sample in loaded_data:
        frame_numb,current_highest,has_been_0=get_frame_number(sample[0],current_highest,0)
        title="Frame:"+str(frame_numb)+"  "+sample[0]
        marker=get_datapoint_marker(frame_numb)
        Q=sample[1]
        I=sample[2]
        dI=sample[3]
        #plt.errorbar(Q,I,dI,label=title)
        plt.scatter(Q,I,marker=marker,label=title)
    avQ=averaged_data[0]
    avI=averaged_data[1]
    avdI=averaged_data[2]
    plt.errorbar(avQ,avI,avdI,label='Averaged')
    plt.xlabel(r'$\mathrm{Q\  [\AA^{-1}]}$',fontsize=13)
    plt.ylabel(r'$\mathrm{I(Q)\  [cm^{-1}]}$',fontsize=13)
    plt.tick_params(top=True,right=True,which='both')
    plt.semilogy()
    plt.semilogx()
    plt.legend()
    plt.show()

#plot_average_with_samples(loaded_buffer)

#"{:e}".format(12300000)


def write_to_file(path,filename,data):
    fpath=os.path.join(path,filename)
    f=open(fpath,'w')
    for i in range(len(data[0])):
        Q_sci="{:.18e}".format(data[0][i])
        Q_str=str(Q_sci)
        I_sci="{:.18e}".format(data[1][i])
        I_str=str(I_sci)
        dI_sci="{:.18e}".format(data[2][i])
        dI_str=str(dI_sci)
        line=Q_str+" "+I_str+" "+dI_str+"\n"
        f.write(line)
    f.close()

def subtract_background(sample,background):
    I_sub_list=[]
    dI_sub_list=[]
    for i in range(len(sample[0])):
        Q=sample[0][i]
        I_sample=np.array(sample[1][i])
        dI_sample=np.array(sample[2][i])
        I_background=np.array(background[1][i])
        dI_background=np.array(background[2][i])
        I_sub=I_sample-I_background
        dI_sub=dI_sample+dI_background
        I_sub_list.append(I_sub)
        dI_sub_list.append(dI_sub)
    return [sample[0],I_sub_list,dI_sub_list]


#subbed_data=subtract_background(averaged_data, averaged_buffer)

def print_list(liste):
    for element in liste:
        print(element)


def plot_subbed(sampleName,averaged_data):
    plot_figure()
    Q=averaged_data[0]
    I=averaged_data[1]
    dI=averaged_data[2]
    #plt.errorbar(Q,I,dI,label=sampleName)
    plt.scatter(Q,I,label=sampleName+'_Subtracted')
    plt.xlabel(r'$\mathrm{Q\  [\AA^{-1}]}$',fontsize=13)
    plt.ylabel(r'$\mathrm{I(Q)\  [cm^{-1}]}$',fontsize=13)
    #plt.tick_params(top=True,right=True,which='both')
    plt.semilogy()
    plt.semilogx()
    plt.ylim(1e-5,10)
    plt.legend()
    plt.show()


def plot_subbed_for_loop(sampleName,averaged_data):
    Q=averaged_data[0]
    I=averaged_data[1]
    dI=averaged_data[2]
    #plt.errorbar(Q,I,dI,label=sampleName)
    plt.scatter(Q,I,label=sampleName)


def load_data(sample_name,frames_to_remove_sample,frames_to_remove_buffer):
    frames,Path=acsess_frames(sample_name)
    sorted_frames=sort_frames(frames)
    sample=select_indexes(sorted_frames[1], frames_to_remove_sample)
    buffer=select_indexes(sorted_frames[0], frames_to_remove_buffer)
    loaded_sample=read_multiple(Path, sample)
    loaded_buffer=read_multiple(Path, buffer)
    return loaded_sample,loaded_buffer

def concatinate_samps_bufs(sample_list,buffer_list):
    new_list=sample_list+buffer_list
    return new_list


#plot_subbed('Subtracted_data', subbed_data)

def create_dir(path,dirname):
    current_dirs=os.listdir(path)
    if dirname not in current_dirs:
        dPath=os.path.join(path, dirname)
        os.makedirs(dPath)
    else: dPath=os.path.join(path, dirname)
    return dPath

def save_files(main_path,sample_name,avrSamp,avrBuff,subbed):
    Path=os.path.join(main_path,sample_name)
    dPath=create_dir(Path,'Processed')
    filename_buffer='Average_buffer_'+sample_name+'.dat'
    filename_sample='Average_sample_'+sample_name+'.dat'
    filename_subtracted='Subtracted_'+sample_name+'.dat'
    write_to_file(dPath,filename_buffer, avrBuff)
    write_to_file(dPath,filename_sample, avrSamp)
    write_to_file(dPath,filename_subtracted, subbed)

def save_subed(path,dirname,sample_name,subbed):
    dPath=create_dir(path,dirname)
    filename='Subtracted_'+sample_name+'.dat'
    write_to_file(dPath, filename, subbed)




def do_save(ans):
    if ans=='y':
        save_files(main_path, sample_name, avr_sample, avr_buffer, subbed_sample)
        save_subed(main_path,'All_processed',sample_name,subbed_sample)
        print('Files are saved')


###### START HERE ######

def getfile_path(): #get file from directory
    root = tkinter.tk()
    root.withdraw()
    dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')


filepath = str(getfile_path())
newname = str(filepath) #Creating new file name and directory path
last_position = newname.rfind("/")
newname = newname[newname.rfind("/"):]
newname_start = newname.replace("/", "")

main_path="M:\Documents\Master\Qtiprojects\ESRF240922\All" # Write the path to the folder containing the data
directory_list=os.listdir(main_path)
#print_list(directory_list) # To print out the elements in the directory of main path


### Select a name string to only show the samples with that in the name

samples_of_choice=select_sample_code(samplefilename, directory_list)
print_list(samples_of_choice) #To print out the elements in main dir corresponding to the sample code name


# Give the hole name to the spesific sample you want to subtract
sample_name=samplefilename
save='y' # Saving: 'y' for yes, and 'n' for no
plot='y' # Plotting: 'y' for yes, and 'n' for no
samples,buffers=load_data(sample_name, [0,1,2,3], []) #Fill in the indecies to be removed, first is for the samples, second for the buffers

avr_sample=simple_average_std(samples)
avr_buffer=simple_average_std(buffers)
subbed_sample=subtract_background(avr_sample, avr_buffer)

if plot=='y':
    plot_average_with_samples(samples)
    plot_average_with_samples(buffers)
    plot_subbed(sample_name, subbed_sample)

do_save(save)


#### THis is code to plot multiple files that have already been processed #####

def plot_multiple_processed(path,sample_name_list):
    pros_dir=os.listdir(path)
    plot_figure()
    for sample in sample_name_list:
        for file in pros_dir:
            if sample in file:
                filename=os.path.join(path, file)
                sample_data=readfile(filename)
                Q,I,dI=reshape_pros_list(sample_data)
                avr_data=[Q,I,dI]
                filename_split=file.split('_')
                sampname=filename_split[1]
                plot_subbed_for_loop(sampname, avr_data)
    plt.xlabel(r'$\mathrm{Q\  [\AA^{-1}]}$',fontsize=13)
    plt.ylabel(r'$\mathrm{I(Q)\  [cm^{-1}]}$',fontsize=13)
    plt.tick_params(top=True,right=True,which='both')
    plt.semilogy()
    plt.semilogx()
    plt.legend()
    plt.show()

def plot_multiple_processed_labeled(path,sample_name_list,legend_name_list,title,savefig,figpath):
    pros_dir=os.listdir(path)
    plot_figure()
    for i in range(len(sample_name_list)):
        sample=sample_name_list[i]
        legend_name=legend_name_list[i]
        for file in pros_dir:
            if sample in file:
                filename=os.path.join(path, file)
                sample_data=readfile(filename)
                Q,I,dI=reshape_pros_list(sample_data)
                avr_data=[Q,I,dI]
                filename_split=file.split('_')
                sampname=filename_split[1]
                plot_subbed_for_loop(legend_name, avr_data)
    plt.title(title,fontsize=17)
    plt.xlabel(r'$\mathrm{Q\  [\AA^{-1}]}$',fontsize=17)
    plt.ylabel(r'$\mathrm{I(Q)\  [cm^{-1}]}$',fontsize=17)
    plt.tick_params(top=True,right=True,which='both')
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.semilogy()
    plt.semilogx()
    plt.legend(fontsize=16)
    if savefig:
        figure_name_and_path=os.path.join(figpath,title)
        plt.savefig(figure_name_and_path)
    plt.show()


def load_multiple(path,sample_name_list):
    outmatrix=[]
    pros_dir=os.listdir(path)
    for sample in sample_name_list:
        for file in pros_dir:
            if sample in file:
                filename=os.path.join(path, file)
                sample_data=readfile(filename)
                Q,I,dI=reshape_rawdata_list(sample_data)
                avr_data=[Q,I,dI]
                filename_split=file.split('_')
                sampname=filename_split[1]
                out_list=[sampname,avr_data]
                outmatrix.append(out_list)
    return outmatrix


### Write path to the folder containing the processed files ###
#pros_path="/Users/vladimir/Tidligere_OneDrive/BM26FEB22/Resulteter_april_22/VK_colistin/All_processed"

### This is the path tho where the plot will be saved, if you want
#figure_path="/Users/vladimir/Tidligere_OneDrive/BM26FEB22/figures/Colistin"


# Here you write the names of the samples, what they are called (for the legend), title of the plot, 'True' if you want to save the plot and the path to save it.

#plot_multiple_processed_labeled(pros_path,['VKCOL53_','VKCOL54_','VKCOL55_','VKCOL56_'],['Col 10mg/ml, Piperazine, 0.10M MgCl2','Col 5mg/ml, Piperazine, 0.10M MgCl2','Col 2.5mg/ml, Piperazine, 0.10M MgCl2','Col 1mg/ml, Piperazine, 0.10M MgCl2'],'Colistin in Piperazine, 0_10M MgCl2',True,figure_path)


"""
def add_lists_elementwhise(list1,list2):
    narr1=np.array(list1)
    narr2=np.array(list2)
    added=narr1+narr2
    return added


### ADDING AND PLOTTING INTENSITIES ###

Q=pros_samp_lists[0][1][0]
pep_40_I=pros_samp_lists[0][1][1]
hep_60_I=pros_samp_lists[1][1][1]

pep_40_dI=pros_samp_lists[0][1][2]
hep_60_dI=pros_samp_lists[1][1][2]


added_I=add_lists_elementwhise(pep_40_I, hep_60_I)
added_dI=add_lists_elementwhise(pep_40_dI, hep_60_dI)

added_data=[Q,added_I,added_dI]
mix_I=pros_samp_lists[2][1][1]
mix_dI=pros_samp_lists[2][1][2]
mix_data=[Q,mix_I,mix_dI]
plot_figure()
plot_subbed_for_loop('Sum of peptide and heparin scattering', added_data)
plot_subbed_for_loop('Scattering of mixture', mix_data)
plt.xlabel(r'$\mathrm{Q\  [\AA^{-1}]}$',fontsize=13)
plt.ylabel(r'$\mathrm{I(Q)\  [cm^{-1}]}$',fontsize=13)
plt.title('Peptide:4mg/ml Hep:2mg/ml (6/1 molar ratio pep/hep)',fontsize=15)
plt.tick_params(top=True,right=True,which='both')
plt.semilogy()
plt.semilogx()
plt.legend()
plt.show()
"""
