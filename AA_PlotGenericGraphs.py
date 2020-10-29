import numpy as np
import matplotlib.pyplot as plt
from cycler import cycler
import os
import argparse # Include standard modules

def ImshowPlot(Prof2D, Time1D, VariableName, title, Option_Save=0, FilenamePrefix='test'):
    # Prof2D = Te_arr
    # title = 'Te(r,t)'
    # VariableName = 'Te'
    # Option_Save = 1
    # FilenamePrefix = 'itera002'

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
        print("Save figure to : %s"%(Filename))
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
        plt.plot(Prof2D[:,Zonei], label=labeli)
        i += 1
    plt.xlabel('Time [ms]')
    ylabel = "%s(r, t)"%(VariableName)
    plt.ylabel(ylabel)
    plt.legend()
    if Option_Save == 1:
        print("Save figure to : %s" % (Filename))
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
    for timei in TimeList:
        index = np.where(Time1D<timei)[0][-1]
        # print(index)
        LowerTime = Time1D[index]
        labeli = "Time = %8.4e ms"%(LowerTime)
        plt.plot(Prof2D[index,:],label=labeli)

    plt.title(title)
    plt.xlabel('Zone')
    plt.ylabel(VariableName)
    plt.legend()
    if Option_Save == 1:
        print("Save figure to : %s" % (Filename))
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
    return string1

# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--device", "-d", help="Set device name, i.e. iter, jet, etc.")
parser.add_argument("--series", "-s", help="Set series code for running simulations, i.e. a001, a002, etc.")
parser.add_argument("--path", "-p", help="Set path to the data folder, default = .")

# Read arguments from the command line
args = parser.parse_args()

print("@ ================== BALDUR ANALYSIS SCRIPTS ======================= @")
print("@ PARAMETERS & OPTIONS: ")
if args.device:
    print("Device name             = %s"%(args.device))
    MachineName = args.device
else:
    print("Device name             = %s (default)" % ("iter"))
    MachineName = "iter"

if args.series:
    print("Name of series code     = %s"%(args.series))
    FolderCode = args.series
else:
    print("Name of series code     = %s (default)" % ("a002"))
    FolderCode = "a002"

if args.path:
    print("Path to the data folder = %s"%(args.path))
    PathToDataFolder = args.path
else:
    print("Path to the data folder = %s (default)"%("."))
    PathToDataFolder = "."

print("@ =================================================================== @")

# PathToDataFolder = "/Users/vitreloy/git2017/BALDUR_Analysis"
# PathToDataFolder = "./"
PathToJfile = "%s/%s"%(PathToDataFolder,FolderCode)
PathOfJfile = "%s/j%s%s"%(PathToJfile,MachineName,FolderCode)

print("This script is about to read data from: %s"%(PathOfJfile))

fileid1 = open(PathOfJfile, 'r')
lines1 = fileid1.readlines() # read on lines at once
# page #1
Page1Found = 0
HeaderTeFound = 0
# page #2
Page2Found = 0
HeaderDeuteriumFound = 0
# page #3
Page3Found = 0
HeaderEnergyLossesFound = 0
# 1d list
# page #1
Te_i = [0] * 52 # np.zeros(52, dtype=float)
Ti_i = [0] * 52 # np.zeros(52, dtype=float)
ne_i = [0] * 52 # np.zeros(52, dtype=float)
ni_i = [0] * 52 # np.zeros(52, dtype=float)
vloop_i = [0] * 52 # np.zeros(52, dtype=float)
jz_i = [0] * 52 #  np.zeros(52, dtype=float)
q_i = [0] * 52 # np.zeros(52, dtype=float)
beta_i = [0] * 52 # np.zeros(52, dtype=float)
# page #2
nD_i = [0] * 52 # np.zeros(52, dtype=float)
nT_i = [0] * 52 # np.zeros(52, dtype=float)
nImp1_i = [0] * 52 # np.zeros(52, dtype=float)
nImp2_i = [0] * 52 # np.zeros(52, dtype=float)
nImp3_i = [0] * 52 # np.zeros(52, dtype=float)
zeff_i = [0] * 52 # np.zeros(52, dtype=float)
# page #3
elec_conduct_i  = [0] * 52 # np.zeros(52, dtype=float)
elec_convect_i  = [0] * 52 # np.zeros(52, dtype=float)
ion_conduct_i  = [0] * 52 # np.zeros(52, dtype=float)
ion_convect_i  = [0] * 52 # np.zeros(52, dtype=float)
neu_loss_i  = [0] * 52 # np.zeros(52, dtype=float)
rad_loss_i  = [0] * 52 # np.zeros(52, dtype=float)
ohmic_heating_i  = [0] * 52 # np.zeros(52, dtype=float)
alpha_heating_i  = [0] * 52 # np.zeros(52, dtype=float)
other_heating_i  = [0] * 52 # np.zeros(52, dtype=float)
total_gain_i  = [0] * 52 # np.zeros(52, dtype=float)
ei_coupling_i  = [0] * 52 # np.zeros(52, dtype=float)

# page #1
time_list = []
Te_list = []
Ti_list = []
ne_list = []
ni_list = []
vloop_list = []
jz_list = []
q_list = []
beta_list = []
# page #2
nD_list = []
nT_list = []
nImp1_list = []
nImp2_list = []
nImp3_list = []
zeff_list = []
# page #3
elec_conduct_list = []
elec_convect_list = []
ion_conduct_list = []
ion_convect_list = []
neu_loss_list = []
rad_loss_list = []
ohmic_heating_list = []
alpha_heating_list = []
other_heating_list = []
total_gain_list = []
ei_coupling_list = []

NoOfImp = 0

i = 0
zonei = 0
for linei in lines1: # [:11400]:
    i = i + 1 # count line number, the first line is line #1.
    # print("Line {}: {}".format(i, linei.strip()))


    # ---------------------- Check page #1 ------------------------------------ #
    if linei.find("- 1-") != -1:
        Page1Found = 1
        timei = float(linei[51:64])
        time_list.append(timei)
        print("Page#%2d, time = %14f ms"%(1,timei))
        continue
    if Page1Found == 1 and linei.find("te    reg      ti    reg") != -1:
        # print("Line of header Te is found.")
        HeaderTeFound = 1
        continue
    if Page1Found == 1 and HeaderTeFound == 1 and linei.find("cm      kev") != -1:
        # print("skip")
        continue
    if Page1Found == 1 and HeaderTeFound == 1 and zonei < 52:
        zonei += 1

        linei = CleanData(linei)
        temp1 = linei.split('  ') # split string
        temp2 = [float(k) for k in temp1 if k!='']
        temp_Te = temp2[2]
        temp_Ti = temp2[3]
        temp_ne = temp2[4]
        temp_ni = temp2[5]
        temp_vloop = temp2[6]
        temp_jz = temp2[7]
        temp_q = temp2[8]
        temp_beta = temp2[9]

        Te_i[zonei - 1] = float(temp_Te)
        Ti_i[zonei - 1] = float(temp_Ti)
        ne_i[zonei - 1] = float(temp_ne)
        ni_i[zonei - 1] = float(temp_ni)
        vloop_i[zonei - 1] = float(temp_vloop)
        jz_i[zonei - 1] = float(temp_jz)
        q_i[zonei - 1] = float(temp_q)
        beta_i[zonei - 1] = float(temp_beta)
    if linei.find("- 2-") != -1:
    # if Page1Found == 1 and HeaderTeFound == 1 and linei.find("BALDPN") != -1:
        # end of page#1 --> Reset variables
        Page1Found = 0
        HeaderTeFound = 0
        zonei = 0
        # append data
        Te_list.append(Te_i.copy())
        Ti_list.append(Ti_i.copy())
        ne_list.append(ne_i.copy())
        ni_list.append(ni_i.copy())
        vloop_list.append(vloop_i.copy())
        jz_list.append(jz_i.copy())
        q_list.append(q_i.copy())
        beta_list.append(beta_i.copy())

    # ---------------------- Check page #2 ------------------------------------ #
    if linei.find("- 2-") != -1:
        Page2Found = 1
        # timei = float(linei[51:64])
        # time_list.append(timei)
        # print("Page#%2d, time = %14f ms"%(2,timei))
        continue
    if Page2Found == 1 and linei.find("nu-el          nu-h      deuterium") != -1:
        # print("Line of header Te is found.")
        HeaderDeuteriumFound = 1
        continue
    if Page2Found == 1 and HeaderDeuteriumFound == 1 and \
            linei.find("part/cu cm") != -1:
        continue
    if Page2Found == 1 and HeaderDeuteriumFound == 1 and zonei < 52:
        zonei += 1
        # print(linei)

        if zonei == 1:
            # Data in the first zone is not available, so skip it
            continue
        if zonei == 52:
            # Data in the last zone is not available, so skip it
            continue

        linei = CleanData(linei)
        temp1 = linei.split('  ')  # split string
        temp2 = [float(k) for k in temp1 if k != '']

        if NoOfImp == 0:
            if len(temp2) == 9:
                NoOfImp = 2
            elif len(temp2) == 10:
                NoOfImp = 3

        temp_deuterium = temp2[4]
        temp_tritium = temp2[5]
        temp_imp1 = temp2[6]
        temp_imp2 = temp2[7]
        if NoOfImp == 2:
            temp_zeff = temp2[8]
        elif NoOfImp == 3:
            temp_imp3 = temp2[8]
            temp_zeff = temp2[9]

        nD_i[zonei-1] = float(temp_deuterium)
        nT_i[zonei-1] = float(temp_tritium)
        nImp1_i[zonei-1] = float(temp_imp1)
        nImp2_i[zonei-1] = float(temp_imp2)
        if NoOfImp == 3:
            nImp3_i[zonei-1] = float(temp_imp3)
        zeff_i[zonei-1] = float(temp_zeff)
    if linei.find("- 3-") != -1:
        # end of page#1 --> Reset variables
        Page2Found = 0
        HeaderDeuteriumFound = 0
        zonei = 0
        # append data
        nD_list.append(nD_i.copy())
        nT_list.append(nT_i.copy())
        nImp1_list.append(nImp1_i.copy())
        nImp2_list.append(nImp2_i.copy())
        if NoOfImp == 3:
            nImp3_list.append(nImp3_i.copy())
        zeff_list.append(zeff_i.copy())

    # ---------------------- Check page #3 ------------------------------------ #
    if linei.find("- 3-") != -1:
        Page3Found = 1
        # timei = float(linei[51:64])
        # time_list.append(timei)
        # print("Page#%2d, time = %14f ms"%(2,timei))
        continue
    if Page3Found == 1 and linei.find("energy losses from plasma") != -1:
        # print("Line of header Te is found.")
        HeaderEnergyLossesFound = 1
        continue
    if Page3Found == 1 and HeaderEnergyLossesFound == 1 and linei.find("j    cm    conduct  convect."):
        continue
    if Page3Found == 1 and HeaderEnergyLossesFound == 1 and zonei < 52:
        zonei += 1
        if zonei == 1:
            continue
        if zonei == 51 or zonei == 52:
            continue

        linei = CleanData(linei)
        temp1 = linei.split('  ')  # split string
        temp2 = [float(k) for k in temp1 if k != '']

        temp_elec_conduct = temp2[2]
        temp_elec_convect = temp2[3]
        temp_ion_conduct = temp2[4]
        temp_ion_convect = temp2[5]
        temp_neu_loss = temp2[6]
        temp_rad_loss = temp2[7]
        temp_ohmic_heating = temp2[8]
        temp_alpha_heating = temp2[9]
        temp_other_heating = temp2[10]
        temp_total_gain = temp2[11]
        temp_ei_coupling = temp2[12]

    if linei.find("- 4-") != -1:
        # end of page#1 --> Reset variables
        Page2Found = 0
        HeaderDeuteriumFound = 0
        zonei = 0
        # append data
        elec_conduct_list.append(elec_conduct_i.copy())
        elec_convect_list.append(elec_convect_i.copy())
        ion_conduct_list.append(ion_conduct_i.copy())
        ion_convect_list.append(ion_convect_i.copy())
        neu_loss_list.append(neu_loss_i.copy())
        rad_loss_list.append(rad_loss_i.copy())
        ohmic_heating_list.append(ohmic_heating_i.copy())
        alpha_heating_list.append(alpha_heating_i.copy())
        other_heating_list.append(other_heating_i.copy())
        total_gain_list.append(total_gain_i.copy())
        ei_coupling_list.append(ei_coupling_i.copy())

print("time_list = ",time_list)
print("Total time slices = %5d"%(len(time_list)))
# print(Te_list)
# print(len(Te_list))

# Visualization
Time1D = np.array(time_list)

Te_arr = np.array(Te_list)
Ti_arr = np.array(Ti_list)
ne_arr = np.array(ne_list)
ni_arr = np.array(ni_list)
vloop_arr = np.array(vloop_list)
jz_arr = np.array(jz_list)
q_arr = np.array(q_list)
beta_arr = np.array(beta_list)
nD_arr = np.array(nD_list)
nT_arr = np.array(nT_list)
nImp1_arr = np.array(nImp1_list)
nImp2_arr = np.array(nImp2_list)
nImp3_arr = np.array(nImp3_list)
zeff_arr = np.array(zeff_list)


RadList = [0, 10, 20, 30, 40]

Option_Save = 1
FilenamePrefix = "%s%s"%(MachineName, FolderCode)
os.chdir(PathToJfile)

idx = np.round(np.linspace(1,len(Time1D)-1, 5)).astype(int)
TimeList = Time1D[idx]


# Page #1: TE
title = 'Te(r,t)'
VariableName = 'Te'
Plot1DTime_FixRad(Te_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
Plot1DTime_FixTime(Te_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
ImshowPlot(Te_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)

# Page #1: TI
title = 'Ti(r,t)'
VariableName = 'Ti'
Plot1DTime_FixRad(Ti_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
Plot1DTime_FixTime(Ti_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
ImshowPlot(Ti_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)

# Page #1: NE
title = 'ne(r,t)'
VariableName = 'ne'
Plot1DTime_FixRad(ne_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
Plot1DTime_FixTime(ne_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
ImshowPlot(ne_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)

# Page #1: NI
title = 'ni(r,t)'
VariableName = 'ni'
Plot1DTime_FixRad(ni_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
Plot1DTime_FixTime(ni_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
ImshowPlot(ni_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)

# Page #1: q
title = 'q(r,t)'
VariableName = 'q'
Plot1DTime_FixRad(q_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
Plot1DTime_FixTime(q_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
ImshowPlot(q_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)

# Page #1: beta
title = 'beta(r,t)'
VariableName = 'beta'
Plot1DTime_FixRad(beta_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
Plot1DTime_FixTime(beta_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
ImshowPlot(beta_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)

# Page #2: Deuterium density
title = 'nD(r,t)'
VariableName = 'nD'
Plot1DTime_FixRad(nD_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
Plot1DTime_FixTime(nD_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
ImshowPlot(nD_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)

# Page #2: Tritium density
title = 'nT(r,t)'
VariableName = 'nT'
Plot1DTime_FixRad(nT_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
Plot1DTime_FixTime(nT_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
ImshowPlot(nT_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)

# Page #2: imp1 density
title = 'nImp1(r,t)'
VariableName = 'nImp1'
Plot1DTime_FixRad(nImp1_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
Plot1DTime_FixTime(nImp1_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
ImshowPlot(nImp1_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)

# Page #2: imp2 density
title = 'nImp2(r,t)'
VariableName = 'nImp2'
Plot1DTime_FixRad(nImp2_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
Plot1DTime_FixTime(nImp2_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
ImshowPlot(nImp2_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)

if NoOfImp == 3:
    # Page #2: imp3 density
    title = 'nImp3(r,t)'
    VariableName = 'nImp3'
    Plot1DTime_FixRad(nImp3_arr, Time1D, VariableName, RadList, title, Option_Save, FilenamePrefix)
    Plot1DTime_FixTime(nImp3_arr, Time1D, VariableName, TimeList, title, Option_Save, FilenamePrefix)
    ImshowPlot(nImp3_arr, Time1D, VariableName, title, Option_Save, FilenamePrefix)

# Page #2: Zeff density
title = 'Zeff(r,t)'
VariableName = 'Zeff'
Plot1DTime_FixRad(zeff_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
Plot1DTime_FixTime(zeff_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
ImshowPlot(zeff_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)







# print(Ti_i)
# print(ne_i)
# print(ni_i)
# print(vloop_i)
# print(jz_i)
# print(q_i)
# print(beta_i)
