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
        plt.plot(Prof2D[:,Zonei], label=labeli)
        i += 1
    plt.xlabel('Time [ms]')
    ylabel = "%s(r, t)"%(VariableName)
    plt.ylabel(ylabel)
    plt.legend()
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
# page #5 ( transport coefficients from theory)
Page5Found = 0
HeaderPage5Found = 0
# page #6 ( ion thermal diffusion coefficients)
Page6Found = 0
HeaderPage6Found = 0
# page #7
Page7Found = 0
HeaderPage7Found = 0
# page #8
Page8Found = 0
HeaderPage8Found = 0
# page #9
Page9Found = 0
HeaderPage9Found = 0
# page #13 (Growth rates and frequencies)
Page13Found = 0
HeaderGrowthRatesFound = 0

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
# page #5
rminor5_i = [0] * 52 # np.zeros(52, dtype=float)
chie_i  = [0] * 52 # np.zeros(52, dtype=float)
chii_i  = [0] * 52 # np.zeros(52, dtype=float)
zdifh_i  = [0] * 52 # np.zeros(52, dtype=float)
zdifz_i  = [0] * 52 # np.zeros(52, dtype=float)
# page #6
rminor6_i = [0] * 52 # np.zeros(52, dtype=float)
# MMM
thiig_i = [0] * 52 # np.zeros(52, dtype=float)
thirb_i = [0] * 52 # np.zeros(52, dtype=float)
thikb_i = [0] * 52 # np.zeros(52, dtype=float)
xithe_i = [0] * 52 # np.zeros(52, dtype=float)
neocl_i = [0] * 52 # np.zeros(52, dtype=float)
empirc_i = [0] * 52 # np.zeros(52, dtype=float)
xitot_i = [0] * 52 # np.zeros(52, dtype=float)
# Mixed B/gB
Xi_Bohm_i = [0] * 52 # np.zeros(52, dtype=float)
Xi_gBohm_i = [0] * 52 # np.zeros(52, dtype=float)
Xi_Mixed_i = [0] * 52 # np.zeros(52, dtype=float)
Xi_Neo_i = [0] * 52 # np.zeros(52, dtype=float)
Xi_Empirc_i = [0] * 52 # np.zeros(52, dtype=float)
Xi_Total_i = [0] * 52 # np.zeros(52, dtype=float)
# page #7
rminor7_i = [0] * 52 # np.zeros(52, dtype=float)
# MMM
theig_i = [0] * 52 # np.zeros(52, dtype=float)
therb_i = [0] * 52 # np.zeros(52, dtype=float)
thekb_i = [0] * 52 # np.zeros(52, dtype=float)
theeg_i = [0] * 52 # np.zeros(52, dtype=float)
thetb_i = [0] * 52 # np.zeros(52, dtype=float)
xethe_i = [0] * 52 # np.zeros(52, dtype=float)
neocle_i = [0] * 52 # np.zeros(52, dtype=float)
empirce_i = [0] * 52 # np.zeros(52, dtype=float)
xetot_i = [0] * 52 # np.zeros(52, dtype=float)
# Mixed B/gB
Xe_Bohm_i = [0] * 52 # np.zeros(52, dtype=float)
Xe_gBohm_i = [0] * 52 # np.zeros(52, dtype=float)
Xe_Mixed_i = [0] * 52 # np.zeros(52, dtype=float)
Xe_Neo_i = [0] * 52 # np.zeros(52, dtype=float)
Xe_Empirc_i = [0] * 52 # np.zeros(52, dtype=float)
Xe_Total_i = [0] * 52 # np.zeros(52, dtype=float)


# page #8
rminor8_i = [0] * 52 # np.zeros(52, dtype=float)
# MMM
thdig_i = [0] * 52 # np.zeros(52, dtype=float)
thdrb_i = [0] * 52 # np.zeros(52, dtype=float)
thdkb_i = [0] * 52 # np.zeros(52, dtype=float)
dhthe_i = [0] * 52 # np.zeros(52, dtype=float)
neocldh_i = [0] * 52 # np.zeros(52, dtype=float)
empircdh_i = [0] * 52 # np.zeros(52, dtype=float)
dhtot_i = [0] * 52 # np.zeros(52, dtype=float)
# Mixed B/gB
X_Particle_i = [0] * 52 # np.zeros(52, dtype=float)

# page #9
rminor9_i = [0] * 52 # np.zeros(52, dtype=float)
# MMM
tzdig_i = [0] * 52 # np.zeros(52, dtype=float)
tzdrb_i = [0] * 52 # np.zeros(52, dtype=float)
thzkb_i = [0] * 52 # np.zeros(52, dtype=float)
dzthe_i = [0] * 52 # np.zeros(52, dtype=float)
neoclz_i = [0] * 52 # np.zeros(52, dtype=float)
empircz_i = [0] * 52 # np.zeros(52, dtype=float)
dztot_i = [0] * 52 # np.zeros(52, dtype=float)
# Mixed B/gB
X_Impuirity_i = [0] * 52 # np.zeros(52, dtype=float)

# page #13
rminor13_i  = [0] * 52 # np.zeros(52, dtype=float)
gITG_i  = [0] * 52 # np.zeros(52, dtype=float)
oITG_i  = [0] * 52 # np.zeros(52, dtype=float)
gTEM_i  = [0] * 52 # np.zeros(52, dtype=float)
oTEM_i  = [0] * 52 # np.zeros(52, dtype=float)

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
# page #5
rminor5_list = []
chie_list = []
chii_list = []
zdifh_list = []
zdifz_list = []
# page #6
rminor6_list = []
# MMM
thiig_list = []
thirb_list = []
thikb_list = []
xithe_list = []
neocl_list = []
empirc_list = []
xitot_list = []
# Mixed B/gB
Xi_Bohm_list = []
Xi_gBohm_list = []
Xi_Mixed_list = []
Xi_Neo_list = []
Xi_Empirc_list = []
Xi_Total_list = []
# page #7
rminor7_list = []
# MMM
theig_list = []
therb_list = []
thekb_list = []
theeg_list = []
thetb_list = []
xethe_list = []
neocle_list = []
empirce_list = []
xetot_list = []
# Mixed B/gB
Xe_Bohm_list = []
Xe_gBohm_list = []
Xe_Mixed_list = []
Xe_Neo_list = []
Xe_Empirc_list = []
Xe_Total_list = []

# page #8
rminor8_list = []
# MMM
thdig_list = []
thdrb_list = []
thdkb_list = []
dhthe_list = []
neocldh_list = []
empircdh_list = []
dhtot_list = []
# Mixed B/gB
X_Particle_list = []

# page #9
rminor9_list = []
# MMM
tzdig_list = []
tzdrb_list = []
thzkb_list = []
dzthe_list = []
neoclz_list = []
empircz_list = []
dztot_list = []
# Mixed B/gB
X_Impuirity_list = []

# page #13
rminor13_list = []
gITG_list = []
oITG_list = []
gTEM_list = []
oTEM_list = []

lthery21 = 0 # 8 for mixed b/gb, 10 for multimode, 23 for glf23

NoOfImp = 0

i = 0
zonei = 0
for linei in lines1: #[:54270]:
    i = i + 1 # count line number, the first line is line #1.
    # print("Line {}: {}".format(i, linei.strip()))
    # print("%5d %5d %5d %5d"%(Page1Found, Page2Found, Page3Found, Page13Found))
    # print("%5d %5d %5d %5d" % (HeaderTeFound, HeaderDeuteriumFound, HeaderEnergyLossesFound, HeaderGrowthRatesFound))
    # print("%5d"%(zonei))

    # --------------------- Check lthery(21) ---------------------------------- #
    if linei.find("lthery(21)") != -1:
        exclamationMark = linei.find("!")
        lthery = linei.find("lthery")
        # print(linei)
        # print(exclamationMark)
        # print(lthery)
        if lthery < exclamationMark:
            EqualMark = linei.find("=")
            CommaMark = linei.find(",")
            lthery21 = int(linei[(EqualMark+1):CommaMark])
            print("\nTransport model: %d = " % (lthery21),end='')
            if lthery21 == 8:
                print("Mixed B/gB")
            elif lthery21 == 10:
                print("Multimode")
            elif lthery21 == 23:
                print("glf23")
            print("\n")


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
        temp1 = linei.split(' ') # split string
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
        temp1 = linei.split(' ')  # split string
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
    if Page3Found == 1 and HeaderEnergyLossesFound == 1 and linei.find("j    cm    conduct  convect.") != -1:
        continue
    if Page3Found == 1 and HeaderEnergyLossesFound == 1 and zonei < 52:
        zonei += 1
        if zonei == 1:
            # zonei += 1
            continue
        if zonei == 51 or zonei == 52:
            continue

        linei = CleanData(linei)
        temp1 = linei.split(' ')  # split string
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

    # if Page3Found == 1 and HeaderEnergyLossesFound == 1 and linei.find('particles') != -1:
    if linei.find("- 4-") != -1:
        # end of page#1 --> Reset variables
        Page3Found = 0
        HeaderEnergyLossesFound = 0
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

    # ---------------------- Check page #5 ------------------------------------ #
    if linei.find("- 5-") != -1:
        Page5Found = 1
        # timei = float(linei[51:64])
        # time_list.append(timei)
        # print("Page#%2d, time = %14f ms"%(13,timei))
        continue
    if Page5Found == 1 and linei.find(" transport coefficients from theory") != -1:
        HeaderPage5Found = 1
        continue
    if Page5Found == 1 and HeaderPage5Found == 1 and (linei == '\n' or linei.find("m*m/s") != -1 ):
        continue
    if Page5Found == 1 and HeaderPage5Found == 1 and linei.find('chi-elc        chi-ion') != -1:
        continue
    if Page5Found == 1 and HeaderPage5Found == 1 and zonei < 52:
        zonei += 1

        if zonei == 1:
            zonei += 1
        if zonei == 52:
            continue

        linei = CleanData(linei)
        temp1 = linei.split(' ')  # split string
        # print(temp1)
        temp2 = [float(k) for k in temp1 if k != '']

        rminor5_i[zonei - 1] = temp2[1]
        chie_i[zonei - 1] = temp2[2]
        chii_i[zonei - 1] = temp2[3]
        zdifh_i[zonei - 1] = temp2[5]
        zdifz_i[zonei - 1] = temp2[6]
    if linei.find("- 6-") != -1:
        Page5Found = 0
        HeaderPage5Found = 0
        zonei = 0
        #append data
        rminor5_list.append(rminor5_i.copy())
        chie_list.append(chie_i.copy())
        chii_list.append(chii_i.copy())
        zdifh_list.append(zdifh_i.copy())
        zdifz_list.append(zdifz_i.copy())

    # ---------------------- Check page #6 ------------------------------------ #
    if linei.find("- 6-") != -1:
        Page6Found = 1
        # timei = float(linei[51:64])
        # time_list.append(timei)
        # print("Page#%2d, time = %14f ms"%(6,timei))
        continue
    if Page6Found == 1 and linei.find("ion thermal diffusion coefficients") != -1:
        HeaderPage6Found = 1
        continue
    if Page6Found == 1 and HeaderPage6Found == 1 and \
        (linei.find("------------") != -1 or linei.find("m2/s") != -1
         or linei.find("thiig") != -1 or linei.find("Xi_Bohm") != -1):
        continue
    if Page6Found == 1 and HeaderPage6Found == 1 and zonei < 52:
        zonei += 1

        if zonei == 52:
            continue
        linei = CleanData(linei)
        temp1 = linei.split(' ')  # split string
        temp2 = [float(k) for k in temp1 if k != '']

        if lthery21 == 10: # MMM
            rminor6_i[zonei - 1] = temp2[0]
            thiig_i[zonei - 1] = temp2[1]
            thirb_i[zonei - 1] = temp2[2]
            thikb_i[zonei - 1] = temp2[3]
            xithe_i[zonei - 1] = temp2[4]
            neocl_i[zonei - 1] = temp2[5]
            empirc_i[zonei - 1] = temp2[6]
            xitot_i[zonei - 1] = temp2[7]
        elif lthery21 == 8: # Mixed B/gB
            rminor6_i[zonei - 1] = temp2[0]
            Xi_Bohm_i[zonei - 1] = temp2[1]
            Xi_gBohm_i[zonei - 1] = temp2[2]
            Xi_Mixed_i[zonei - 1] = temp2[3]
            Xi_Neo_i[zonei - 1] = temp2[4]
            Xi_Empirc_i[zonei - 1] = temp2[5]
            Xi_Total_i[zonei - 1] = temp2[6]



    if linei.find("- 7-") != -1:
        Page6Found = 0
        HeaderPage6Found = 0
        zonei = 0
        # append data
        if lthery21 == 10:  # MMM
            rminor6_list.append(rminor6_i.copy())
            thiig_list.append(thiig_i.copy())
            thirb_list.append(thirb_i.copy())
            thikb_list.append(thikb_i.copy())
            xithe_list.append(xithe_i.copy())
            neocl_list.append(neocl_i.copy())
            empirc_list.append(empirc_i.copy())
            xitot_list.append(xitot_i.copy())
        elif lthery21 == 8:  # Mixed B/gB
            rminor6_list.append(rminor6_i.copy())
            Xi_Bohm_list.append(Xi_Bohm_i.copy())
            Xi_gBohm_list.append(Xi_gBohm_i.copy())
            Xi_Mixed_list.append(Xi_Mixed_i.copy())
            Xi_Neo_list.append(Xi_Neo_i.copy())
            Xi_Empirc_list.append(Xi_Empirc_i.copy())
            Xi_Total_list.append(Xi_Total_i.copy())

    # ---------------------- Check page #7 ------------------------------------ #
    if linei.find("- 7-") != -1:
        Page7Found = 1
        # timei = float(linei[51:64])
        # time_list.append(timei)
        # print("Page#%2d, time = %14f ms"%(6,timei))
        continue
    if Page7Found == 1 and linei.find("electron thermal diffusion coefficients") != -1:
        HeaderPage7Found = 1
        continue
    if Page7Found == 1 and HeaderPage7Found == 1 and (linei.find('---------------') != -1 or \
            linei.find('m2/s        m2/s') != -1 or \
            linei.find('theig       therb') != -1 or linei.find("Xe_Bohm") != -1):
        continue
    if Page7Found == 1 and HeaderPage7Found == 1 and zonei < 52:
        zonei += 1

        if zonei == 52:
            continue

        linei = CleanData(linei)
        temp1 = linei.split(' ')  # split string
        temp2 = [float(k) for k in temp1 if k != '']

        if lthery21 == 10: # MMM
            rminor7_i[zonei - 1] = temp2[0]
            theig_i[zonei - 1] = temp2[1]
            therb_i[zonei - 1] = temp2[2]
            thekb_i[zonei - 1] = temp2[3]
            theeg_i[zonei - 1] = temp2[4]
            thetb_i[zonei - 1] = temp2[5]
            xethe_i[zonei - 1] = temp2[6]
            neocle_i[zonei - 1] = temp2[7]
            empirce_i[zonei - 1] = temp2[8]
            xetot_i[zonei - 1] = temp2[9]
        elif lthery21 == 8: # Mixed B/gB
            rminor7_i[zonei - 1] = temp2[0]
            Xe_Bohm_i[zonei - 1] = temp2[1]
            Xe_gBohm_i[zonei - 1] = temp2[2]
            Xe_Mixed_i[zonei - 1] = temp2[3]
            Xe_Neo_i[zonei - 1] = temp2[4]
            Xe_Empirc_i[zonei - 1] = temp2[5]
            Xe_Total_i[zonei - 1] = temp2[6]

    if linei.find("- 8-") != -1:
        Page7Found = 0
        HeaderPage7Found = 0
        zonei = 0
        # append data
        if lthery21 == 10: # MMM
            rminor7_list.append(rminor7_i.copy())
            theig_list.append(theig_i.copy())
            therb_list.append(therb_i.copy())
            thekb_list.append(thekb_i.copy())
            theeg_list.append(theeg_i.copy())
            thetb_list.append(thetb_i.copy())
            xethe_list.append(xethe_i.copy())
            neocle_list.append(neocle_i.copy())
            empirce_list.append(empirce_i.copy())
            xetot_list.append(xetot_i.copy())
        elif lthery21 == 8:
            Xe_Bohm_list.append(Xe_Bohm_i.copy())
            Xe_gBohm_list.append(Xe_gBohm_i.copy())
            Xe_Mixed_list.append(Xe_Mixed_i.copy())
            Xe_Neo_list.append(Xe_Neo_i.copy())
            Xe_Empirc_list.append(Xe_Empirc_i.copy())
            Xe_Total_list.append(Xe_Total_i.copy())

    # ---------------------- Check page #8 ------------------------------------ #
    if linei.find("- 8-") != -1:
        Page8Found = 1
        # timei = float(linei[51:64])
        # time_list.append(timei)
        # print("Page#%2d, time = %14f ms"%(13,timei))
        continue
    if Page8Found == 1 and linei.find("hydrogenic particle diffusion coefficients") != -1:
        HeaderPage8Found = 1
        continue
    if Page8Found == 1 and HeaderPage8Found == 1 and (linei.find('---------------') != -1 or \
            linei.find('m2/s        m2/s') != -1 or \
            linei.find('thdig       thdrb') != -1 or linei.find("X_Particle") != -1):
        continue
    if Page8Found == 1 and HeaderPage8Found == 1 and zonei < 52:
        zonei += 1

        if zonei == 52:
            continue

        linei = CleanData(linei)
        temp1 = linei.split(' ')  # split string
        temp2 = [float(k) for k in temp1 if k != '']

        if lthery21 == 10: # MMM
            rminor8_i[zonei - 1] = temp2[0]
            thdig_i[zonei - 1] = temp2[1]
            thdrb_i[zonei - 1] = temp2[2]
            thdkb_i[zonei - 1] = temp2[3]
            dhthe_i[zonei - 1] = temp2[4]
        elif lthery21 == 8: # Mixed B/gB
            rminor8_i[zonei - 1] = temp2[0]
            X_Particle_i[zonei - 1] = temp2[1]
    if linei.find("- 9-") != -1:
        Page8Found = 0
        HeaderPage8Found = 0
        zonei = 0
        # append data
        if lthery21 == 10: # MMM
            rminor8_list.append(rminor8_i.copy())
            thdig_list.append(thdig_i.copy())
            thdrb_list.append(thdrb_i.copy())
            thdkb_list.append(thdkb_i.copy())
            dhthe_list.append(dhthe_i.copy())
        elif lthery21 == 8: # Mixed B/gB
            rminor8_list.append(rminor8_i.copy())
            X_Particle_list.append(X_Particle_i.copy())

    # ---------------------- Check page #9 ------------------------------------ #
    if linei.find("- 9-") != -1:
        Page9Found = 1
        # timei = float(linei[51:64])
        # time_list.append(timei)
        # print("Page#%2d, time = %14f ms"%(13,timei))
        continue
    if Page9Found == 1 and linei.find("impurity particle diffusion coefficients") != -1:
        HeaderPage9Found = 1
        continue
    if Page9Found == 1 and HeaderPage9Found == 1 and (linei.find('---------------') != -1 or \
                                                      linei.find('m2/s        m2/s') != -1 or \
                                                      linei.find('tzdig') != -1 or \
                                                      linei.find("X_Impuirity") != -1):
        continue
    if Page9Found == 1 and HeaderPage9Found == 1 and zonei < 52:
        zonei += 1

        if zonei == 52:
            continue

        linei = CleanData(linei)
        temp1 = linei.split(' ')  # split string
        temp2 = [float(k) for k in temp1 if k != '']
        if len(temp2) < 8: # fill with zeros if data are only partially available
            temp2.extend([0] * (8 - len(temp2)))

        if lthery21 == 10: # MMM
            rminor9_i[zonei - 1] = temp2[0]
            tzdig_i[zonei - 1] = temp2[1]
            tzdrb_i[zonei - 1] = temp2[2]
            thzkb_i[zonei - 1] = temp2[3]
            dzthe_i[zonei - 1] = temp2[4]
            neoclz_i[zonei - 1] = temp2[5]
            empircz_i[zonei - 1] = temp2[6]
            dztot_i[zonei - 1] = temp2[7]
        elif lthery21 == 8: # Mixed B/gB
            rminor9_i[zonei - 1] = temp2[0]
            X_Impuirity_i[zonei - 1] = temp2[1]
    if linei.find("-10-") != -1:
        Page9Found = 0
        HeaderPage9Found = 0
        zonei = 0
        # append data
        if lthery21 == 10: # MMM
            rminor9_list.append(rminor8_i.copy())
            tzdig_list.append(tzdig_i.copy())
            tzdrb_list.append(tzdrb_i.copy())
            thzkb_list.append(thzkb_i.copy())
            dzthe_list.append(dzthe_i.copy())
            neoclz_list.append(neoclz_i.copy())
            empircz_list.append(empircz_i.copy())
            dztot_list.append(dztot_i.copy())

        elif lthery21 == 8: # Mixed B/gB
            rminor9_list.append(rminor8_i.copy())
            X_Impuirity_list.append(X_Impuirity_i.copy())


    # ---------------------- Check page #13 ------------------------------------ #
    if linei.find("-13-") != -1:
        Page13Found = 1
        # timei = float(linei[51:64])
        # time_list.append(timei)
        # print("Page#%2d, time = %14f ms"%(13,timei))
        continue
    if Page13Found == 1 and linei.find("Growth rates and frequencies:") != -1:
        HeaderGrowthRatesFound = 1
        continue
    if Page13Found == 1 and HeaderGrowthRatesFound == 1 and linei.find('gamma_ITG') != -1:
        continue
    if Page13Found == 1 and HeaderGrowthRatesFound == 1 and zonei < 52:
        zonei += 1

        linei = CleanData(linei)
        temp1 = linei.split(' ')  # split string
        temp2 = [float(k) for k in temp1 if k != '']

        rminor13_i[zonei - 1] = temp2[0]
        gITG_i[zonei - 1] = temp2[1]
        oITG_i[zonei - 1] = temp2[2]
        gTEM_i[zonei - 1] = temp2[3]
        oTEM_i[zonei - 1] = temp2[4]
    if linei.find("-14-") != -1:
        Page13Found = 0
        HeaderGrowthRatesFound = 0
        zonei = 0
        # append data
        rminor13_list.append(rminor13_i.copy())
        gITG_list.append(gITG_i.copy())
        oITG_list.append(oITG_i.copy())
        gTEM_list.append(gTEM_i.copy())
        oTEM_list.append(oTEM_i.copy())

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
rminor5_arr = np.array(rminor5_list)
chie_arr = np.array(chie_list)
chii_arr = np.array(chii_list)
zdifh_arr = np.array(zdifh_list)
zdifz_arr = np.array(zdifz_list)
rminor6_arr = np.array(rminor6_list)
if lthery21 == 10: # MMM
    thiig_arr = np.array(thiig_list)
    thirb_arr = np.array(thirb_list)
    thikb_arr = np.array(thikb_list)
    xithe_arr = np.array(xithe_list)
    neocl_arr = np.array(neocl_list)
    empirc_arr = np.array(empirc_list)
    xitot_arr = np.array(xitot_list)
elif lthery21 == 8: # Mixed
    Xi_Bohm_arr = np.array(Xi_Bohm_list)
    Xi_gBohm_arr = np.array(Xi_gBohm_list)
    Xi_Mixed_arr = np.array(Xi_Mixed_list)
    Xi_Neo_arr = np.array(Xi_Neo_list)
    Xi_Empirc_arr = np.array(Xi_Empirc_list)
    Xi_Total_arr = np.array(Xi_Total_list)

rminor7_arr = np.array(rminor7_list)
if lthery21 == 10: # MMM
    theig_arr = np.array(theig_list)
    therb_arr = np.array(therb_list)
    thekb_arr = np.array(thekb_list)
    theeg_arr = np.array(theeg_list)
    thetb_arr = np.array(thetb_list)
    xethe_arr = np.array(xethe_list)
    neocle_arr = np.array(neocle_list)
    empirce_arr = np.array(empirce_list)
    xetot_arr = np.array(xetot_list)
elif lthery21 == 8: # Mixed B/gB
    Xe_Bohm_arr = np.array(Xe_Bohm_list)
    Xe_gBohm_arr = np.array(Xe_gBohm_list)
    Xe_Mixed_arr = np.array(Xe_Mixed_list)
    Xe_Neo_arr = np.array(Xe_Neo_list)
    Xe_Empirc_arr = np.array(Xe_Empirc_list)
    Xe_Total_arr = np.array(Xe_Total_list)

rminor8_arr = np.array(rminor8_list)
if lthery21 == 10: # MMM
    thdig_arr = np.array(thdig_list)
    thdrb_arr = np.array(thdrb_list)
    thdkb_arr = np.array(thdkb_list)
    dhthe_arr = np.array(dhthe_list)
elif lthery21 == 8: # Mixed B/gB
    X_Particle_arr = np.array(X_Particle_list)

rminor9_arr = np.array(rminor9_list)
if lthery21 == 10: # MMM
    tzdig_arr = np.array(tzdig_list)
    tzdrb_arr = np.array(tzdrb_list)
    thzkb_arr = np.array(thzkb_list)
    dzthe_arr = np.array(dzthe_list)
    neoclz_arr = np.array(neoclz_list)
    empircz_arr = np.array(empircz_list)
    dztot_arr = np.array(dztot_list)
elif lthery21 == 8: # Mixed B/gB
    X_Impuirity_arr = np.array(X_Impuirity_list)

rminor13_arr = np.array(rminor13_list)
gITG_arr = np.array(gITG_list)
oITG_arr = np.array(oITG_list)
gTEM_arr = np.array(gTEM_list)
oTEM_arr = np.array(oTEM_list)


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

# Page #5: chi-elec
title = 'chi-e(r,t)'
VariableName = 'chi-e'
Plot1DTime_FixRad(chie_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
Plot1DTime_FixTime(chie_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
ImshowPlot(chie_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)

# Page #5: chi-i
title = 'chi-i(r,t)'
VariableName = 'chi-i'
Plot1DTime_FixRad(chii_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
Plot1DTime_FixTime(chii_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
ImshowPlot(chii_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)

# Page #5: zdifh
title = 'zdifh(r,t)'
VariableName = 'zdifh'
Plot1DTime_FixRad(zdifh_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
Plot1DTime_FixTime(zdifh_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
ImshowPlot(zdifh_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)

# Page #5: zdifz
title = 'zdifz(r,t)'
VariableName = 'zdifz'
Plot1DTime_FixRad(zdifz_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
Plot1DTime_FixTime(zdifz_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
ImshowPlot(zdifz_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)

if lthery21 == 10:

    # Page #6: thiig
    title = 'thiig(r,t)'
    VariableName = 'thiig'
    Plot1DTime_FixRad(thiig_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
    Plot1DTime_FixTime(thiig_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
    ImshowPlot(thiig_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)

    # Page #6: thirb
    title = 'thirb(r,t)'
    VariableName = 'thirb'
    Plot1DTime_FixRad(thirb_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
    Plot1DTime_FixTime(thirb_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
    ImshowPlot(thirb_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)

    # Page #6: thikb
    title = 'thikb(r,t)'
    VariableName = 'thikb'
    Plot1DTime_FixRad(thikb_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
    Plot1DTime_FixTime(thikb_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
    ImshowPlot(thikb_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)

    # Page #6: xithe
    title = 'xithe(r,t)'
    VariableName = 'xithe'
    Plot1DTime_FixRad(xithe_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
    Plot1DTime_FixTime(xithe_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
    ImshowPlot(xithe_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)

    # Page #6: neocl
    title = 'neocl(r,t)'
    VariableName = 'neocl'
    Plot1DTime_FixRad(neocl_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
    Plot1DTime_FixTime(neocl_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
    ImshowPlot(neocl_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)

    # Page #6: empirc
    title = 'empirc(r,t)'
    VariableName = 'empirc'
    Plot1DTime_FixRad(empirc_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
    Plot1DTime_FixTime(empirc_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
    ImshowPlot(empirc_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)

    # Page #6: xitot
    title = 'xitot(r,t)'
    VariableName = 'xitot'
    Plot1DTime_FixRad(xitot_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
    Plot1DTime_FixTime(xitot_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
    ImshowPlot(xitot_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)
elif lthery21 == 8: # Mixed B/gB
    VariableList = [Xi_Bohm_arr, Xi_gBohm_arr, Xi_Mixed_arr, Xi_Neo_arr, Xi_Empirc_arr, Xi_Total_arr]
    TitleList = ['Xi_Bohm(r,t)', 'Xi_gBohm(r,t)', 'Xi_Mixed(r,t)', 'Xi_Neo(r,t)', 'Xi_Empirc(r,t)', 'Xi_Total(r,t)']
    VariableNameList = ['Xi_Bohm', 'Xi_gBohm', 'Xi_Mixed', 'Xi_Neo', 'Xi_Empirc', 'Xi_Total']

    for i in range(0, len(VariableList)):
        Plot1DTime_FixRad(VariableList[i], Time1D, VariableNameList[i], RadList, TitleList[i], Option_Save,
                          FilenamePrefix)
        Plot1DTime_FixTime(VariableList[i], Time1D, VariableNameList[i], TimeList, TitleList[i], Option_Save,
                           FilenamePrefix)
        ImshowPlot(VariableList[i], Time1D, VariableNameList[i], TitleList[i], Option_Save, FilenamePrefix)

# Page #7:
if lthery21 == 10: # MMM
    VariableList = [theig_arr, therb_arr, thekb_arr, theeg_arr, thetb_arr,
                    xethe_arr, neocle_arr, empirce_arr, xetot_arr]
    TitleList = ['theig(r,t)', 'therb(r,t)', 'thekb(r,t)', 'theeg(r,t)', 'thetb(r,t)',
                        'xethe(r,t)', 'neocle(r,t)', 'empirce(r,t)', 'xetot(r,t)']
    VariableNameList = ['theig', 'therb', 'thekb', 'theeg', 'thetb',
                        'xethe', 'neocle', 'empirce', 'xetot']
elif lthery21 == 8: # Mixed B/gB
    VariableList = [Xe_Bohm_arr, Xe_gBohm_arr, Xe_Mixed_arr, Xe_Neo_arr, Xe_Empirc_arr, Xe_Total_arr]
    TitleList = ['Xe_Bohm(r,t)', 'Xe_gBohm(r,t)', 'Xe_Mixed(r,t)', 'Xe_Neo(r,t)', 'Xe_Empirc(r,t)', 'Xe_Total(r,t)']
    VariableNameList = ['Xe_Bohm', 'Xe_gBohm', 'Xe_Mixed', 'Xe_Neo', 'Xe_Empirc', 'Xe_Total']

for i in range(0, len(VariableList)):
    Plot1DTime_FixRad(VariableList[i], Time1D, VariableNameList[i], RadList, TitleList[i], Option_Save,
                      FilenamePrefix)
    Plot1DTime_FixTime(VariableList[i], Time1D, VariableNameList[i], TimeList, TitleList[i], Option_Save,
                       FilenamePrefix)
    ImshowPlot(VariableList[i], Time1D, VariableNameList[i], TitleList[i], Option_Save, FilenamePrefix)


# Page #8:
if lthery21 == 10: # MMM
    VariableList =     [thdig_arr   , thdrb_arr   , thdkb_arr   , dhthe_arr]
    TitleList =        ['thdig(r,t)', 'thdrb(r,t)', 'thdkb(r,t)', 'dhthe(r,t)']
    VariableNameList = ['thdig'     , 'thdrb'     , 'thdkb'     , 'dhthe']
elif lthery21 == 8: # Mixed B/gB
    VariableList = [X_Particle_arr]
    TitleList = ['X_Particle(r,t)']
    VariableNameList = ['X_Particle']

for i in range(0, len(VariableList)):
    Plot1DTime_FixRad(VariableList[i], Time1D, VariableNameList[i], RadList, TitleList[i], Option_Save, FilenamePrefix)
    Plot1DTime_FixTime(VariableList[i], Time1D, VariableNameList[i], TimeList, TitleList[i], Option_Save, FilenamePrefix)
    ImshowPlot(VariableList[i], Time1D, VariableNameList[i], TitleList[i], Option_Save, FilenamePrefix)

# Page #9:
if lthery21 == 10: # MMM
    VariableList = [tzdig_arr, tzdrb_arr, thzkb_arr, dzthe_arr, neoclz_arr, empircz_arr, dztot_arr]
    TitleList = ['tzdig(r,t)', 'tzdrb(r,t)', 'thzkb(r,t)', 'dzthe(r,t)', 'neoclz(r,t)', 'empircz(r,t)', 'dztot(r,t)']
    VariableNameList = ['tzdig', 'tzdrb', 'thzkb', 'dzthe', 'neoclz', 'empircz', 'dztot']

elif lthery21 == 8: # Mixed B/gB
    VariableList = [X_Impuirity_arr]
    TitleList = ['X_Impurity(r,t)']
    VariableNameList = ['X_Impurity']

for i in range(0, len(VariableList)):
    Plot1DTime_FixRad(VariableList[i], Time1D, VariableNameList[i], RadList, TitleList[i], Option_Save,
                      FilenamePrefix)
    Plot1DTime_FixTime(VariableList[i], Time1D, VariableNameList[i], TimeList, TitleList[i], Option_Save,
                       FilenamePrefix)
    ImshowPlot(VariableList[i], Time1D, VariableNameList[i], TitleList[i], Option_Save, FilenamePrefix)

# Page #13: gamma_ITG
title = 'gamma_ITG(r,t)'
VariableName = 'gamma_ITG'
Plot1DTime_FixRad(gITG_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
Plot1DTime_FixTime(gITG_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
ImshowPlot(gITG_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)

# Page #13: gamma_TEM
title = 'gamma_TEM(r,t)'
VariableName = 'gamma_TEM'
Plot1DTime_FixRad(gTEM_arr, Time1D, VariableName, RadList, title, Option_Save,FilenamePrefix)
Plot1DTime_FixTime(gTEM_arr, Time1D, VariableName, TimeList, title, Option_Save,FilenamePrefix)
ImshowPlot(gTEM_arr, Time1D, VariableName, title, Option_Save,FilenamePrefix)





# print(Ti_i)
# print(ne_i)
# print(ni_i)
# print(vloop_i)
# print(jz_i)
# print(q_i)
# print(beta_i)
