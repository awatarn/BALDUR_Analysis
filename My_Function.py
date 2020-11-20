import matplotlib.pyplot as plt
from cycler import cycler
import numpy as np
import csv

def ImshowPlot(Prof2D, Time1D, VariableName, title, Option_Save=0, FilenamePrefix='test', Time0Index=0):
    # Prof2D = Te_arr
    # title = 'Te(r,t)'
    # VariableName = 'Te'
    # Option_Save = 1
    # FilenamePrefix = 'itera002'

    # print(Prof2D)
    # exit(0)
    Prof2D = Prof2D[Time0Index:,:]
    Time1D = Time1D[Time0Index:]
    # print(Prof2D.shape)

    Filename = "Plot2D_Imshow_%s_%s.png"%(FilenamePrefix,VariableName)
    plt.figure()
    plt.imshow(Prof2D, extent=[0, 1, Time1D[-1], Time1D[0]], aspect='auto')
    plt.set_cmap('jet')
    # plt.imshow(Prof2D, aspect='auto')
    plt.gca().invert_yaxis()
    plt.colorbar()
    plt.xlabel('R/a')
    plt.title(title)
    plt.ylabel('Time [ms]')
    print("Function : ImshowPlot()")
    print("Variable : %s"%(VariableName))
    if Option_Save == 1:
        print("Save figure to : %s \n"%(Filename))
        plt.savefig(Filename, bbox_inches='tight')
    else:
        plt.show()
    plt.close()

def Plot1DTime_FixRad(Prof2D, Time1D, VariableName, Zone, title, Option_Save, FilenamePrefix):

    # Prof2D = Te_arr
    # title = 'Te(r,t)'
    # VariableName = 'Te'
    # Option_Save = 1
    # FilenamePrefix = 'itera002'
    # Zone = [0, 10,25]

    print("Function : Plot1DTime_FixRad()")
    print("Variable : %s" % (VariableName))

    Filename = "Plot1D_Time_%s_%s.png"%(FilenamePrefix,VariableName)
    i = 0
    plt.figure()
    plt.rc('axes', prop_cycle=(cycler('color', ['#9400D3', '#0000FF', '#00FF00', '#FF7F00', '#FF0000', '#8B0000']) +
                               cycler('linestyle', ['-', '-', '-', '-', '-', '-'])))
    for Zonei in Zone:
        labeli = "r = %2d/52"%(Zonei)
        plt.plot(Time1D, Prof2D[:,Zonei], label=labeli)
        i += 1
    plt.xlabel('Time [ms]')
    ylabel = "%s(r, t)"%(VariableName)
    plt.ylabel(ylabel)
    plt.legend()
    plt.title(title)
    if Option_Save == 1:
        print("Save figure to : %s \n" % (Filename))
        plt.savefig(Filename, bbox_inches='tight')
    else:
        plt.show()
    plt.close()
# Plot1DTime_FixTime(Te_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
def Plot1DTime_FixTime(Prof2D, Time1D, VariableName, TimeList,title,  Option_Save, FilenamePrefix):
    # Prof2D = Te_arr
    # title = 'Te(r,t)'
    # VariableName = 'Te'
    # Option_Save = 1
    # FilenamePrefix = 'itera002'
    # TimeList = [12000, 22000, 3000000]

    print("Function : Plot1DTime_FixTime()")
    print("Variable : %s" % (VariableName))

    Filename = "Plot1D_Rad_%s_%s.png"%(FilenamePrefix,VariableName)
    plt.figure()
    plt.rc('axes', prop_cycle=(cycler('color', ['#9400D3', '#0000FF', '#00FF00', '#FF7F00', '#FF0000', '#8B0000']) +
                               cycler('linestyle', ['-', '-', '-', '-', '-', '-'])))
    # print(TimeList)
    # print(Time1D)
    for timei in TimeList:
        # print('timei = ',timei)
        index = np.where(Time1D<=timei)[0][-1]
        # print(timei,' // ',index)
        LowerTime = Time1D[index]
        labeli = "Time = %8.4e ms"%(LowerTime)
        plt.plot(Prof2D[index,:],label=labeli)
        if Time1D.shape[0] != Prof2D.shape[0]:
            print("[ERROR] time records in Time1D and Prof2D are not consistent.")
            print('LowerTime = ',LowerTime,'timei = ',timei,' ',Time1D.shape,' // ',Prof2D.shape)
            print('index = ',index)
            print('      = ',Prof2D[index,:])

    plt.title(title)
    plt.xlabel('Zone')
    plt.ylabel(VariableName)
    plt.legend()
    if Option_Save == 1:
        print("Save figure to : %s \n" % (Filename))
        plt.savefig(Filename,  bbox_inches='tight')
    else:
        plt.show()
    plt.close()

def CleanData(string1):
    string1 = string1.replace('pc', '  ')
    string1 = string1.replace('nc', '  ')
    string1 = string1.replace('th', '  ')
    string1 = string1.replace('lm', '  ')
    string1 = string1.replace('o ', '  ')
    string1 = string1.replace('- ', '  ')
    string1 = string1.replace('-NaN', '  0')
    string1 = string1.replace(' NaN', '  0')
    string1 = string1.replace('\n', ' ')
    return string1

def writeCsvFile(fname, data, *args, **kwargs):
    """
    @param fname: string, name of file to write
    @param data: list of list of items

    Write data to file
    """
    mycsv = csv.writer(open(fname, 'w'), *args, **kwargs)
    for row in data:
        mycsv.writerow(row)

def SaveCsvFile(Time1D, VariableList, VariableNameList, Prefix='', SaveTimeOption=0):
    for i in range(0, len(VariableList)):
        zone_list = range(0, VariableList[i].shape[1])
        prof_list = np.vstack([zone_list,VariableList[i]]).T
        prof_list = prof_list.tolist()
        t_list = [0] + Time1D.tolist()
        t_list = [str(s) + ' ms' for s in t_list]
        combined_list = [t_list, *prof_list]
        csvfilename = Prefix + '_' + VariableNameList[i] + '.csv'
        print('Export %15s to %20s'%(VariableNameList[i], csvfilename))
        # writeCsvFile(csvfilename, combined_list)
        mycsv = csv.writer(open(csvfilename, 'w'))
        for row in combined_list:
            mycsv.writerow(row)
    if SaveTimeOption == 1:
        csvfilename = Prefix + '_' + 'TimeList.csv'
        mycsv = csv.writer(open(csvfilename, 'w'))
        t_list = [0] + Time1D.tolist()
        mycsv.writerow(t_list)
        # for row in t_list:
        #     mycsv.writerow(row)
        print('Export %15s to %20s' % ('Time1D', csvfilename))