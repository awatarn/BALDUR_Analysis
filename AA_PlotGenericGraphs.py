import numpy as np
import os
import argparse # Include standard modules
from My_Function import *


# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--device", "-d", help="Set device name, i.e. iter, jet, etc.")
parser.add_argument("--series", "-s", help="Set series code for running simulations, i.e. a001, a002, etc.")
parser.add_argument("--path", "-p", help="Set path to the data folder, default = .")
parser.add_argument("--time0", "-t0", help="Set an initial time for plotting (round to an lower value), default = 1.0 ms")

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
    FolderCode = "b004"

if args.path:
    print("Path to the data folder = %s"%(args.path))
    PathToDataFolder = args.path
else:
    print("Path to the data folder = %s (default)"%("."))
    PathToDataFolder = "."

if args.time0:
    print("An initial time for plotting = %s"%(args.time0))
    time0 = float(args.time0)
else:
    print("An initial time for plotting = %s (default"%("1.0"))
    time0 = 1.0

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
# page #4
Page4Found = 0
HeaderPage4AFound = 0 # k-e totl
HeaderPage4BFound = 0 # NTV
HeaderPage4CFound = 0 # Er
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
# page #10
Page10Found = 0
HeaderPage10Found = 0
# page #12
Page12Found = 0
HeaderPage12Found = 0
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
# page #4
# k-e totl
zone4A_i  = [0] * 52 # np.zeros(52, dtype=float)
radius4A_i  = [0] * 52 # np.zeros(52, dtype=float)
ketotl_i  = [0] * 52 # np.zeros(52, dtype=float)
kitotl_i  = [0] * 52 # np.zeros(52, dtype=float)
vnware_i  = [0] * 52 # np.zeros(52, dtype=float)
veware_i  = [0] * 52 # np.zeros(52, dtype=float)
dhtotl_i  = [0] * 52 # np.zeros(52, dtype=float)
ditotl_i  = [0] * 52 # np.zeros(52, dtype=float)
# NTV
radius4B_i  = [0] * 52 # np.zeros(52, dtype=float)
wexba_i  = [0] * 52 # np.zeros(52, dtype=float)
Diamagn_i  = [0] * 52 # np.zeros(52, dtype=float)
vpolBt_NTV_i  = [0] * 52 # np.zeros(52, dtype=float)
vtorBp_NTV_i  = [0] * 52 # np.zeros(52, dtype=float)
sqpolfl_i  = [0] * 52 # np.zeros(52, dtype=float)
rho_i  = [0] * 52 # np.zeros(52, dtype=float)
# Er
radius4C_i  = [0] * 52 # np.zeros(52, dtype=float)
Er_i  = [0] * 52 # np.zeros(52, dtype=float)
gradP_i  = [0] * 52 # np.zeros(52, dtype=float)
vpolBt_Er_i  = [0] * 52 # np.zeros(52, dtype=float)
vtorBp_Er_i  = [0] * 52 # np.zeros(52, dtype=float)
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

# page #10
rminor10_i = [0] * 52 # np.zeros(52, dtype=float)
grdne_i = [0] * 52 # np.zeros(52, dtype=float)
grdni_i = [0] * 52 # np.zeros(52, dtype=float)
grdnh_i = [0] * 52 # np.zeros(52, dtype=float)
grdnz_i = [0] * 52 # np.zeros(52, dtype=float)
grdte_i = [0] * 52 # np.zeros(52, dtype=float)
grdti_i = [0] * 52 # np.zeros(52, dtype=float)
grdpr_i = [0] * 52 # np.zeros(52, dtype=float)
grdq_i = [0] * 52 # np.zeros(52, dtype=float)

# page #12
xbouni12_i = [0] * 52 # np.zeros(52, dtype=float)
zvrotxb_i = [0] * 52 # np.zeros(52, dtype=float)
zwexbxb_i = [0] * 52 # np.zeros(52, dtype=float)
zalpha_i = [0] * 52 # np.zeros(52, dtype=float)
zvtor_i = [0] * 52 # np.zeros(52, dtype=float)
zvpara_i = [0] * 52 # np.zeros(52, dtype=float)
zvperp_i = [0] * 52 # np.zeros(52, dtype=float)
zgradrsqrave_i = [0] * 52 # np.zeros(52, dtype=float)
zgradrave_i = [0] * 52 # np.zeros(52, dtype=float)


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
# page #4
# k-e totl
zone4A_list = []
radius4A_list = []
ketotl_list = []
kitotl_list = []
vnware_list = []
veware_list = []
dhtotl_list = []
ditotl_list = []
# NTV
radius4B_list = []
wexba_list = []
Diamagn_list = []
vpolBt_NTV_list = []
vtorBp_NTV_list = []
sqpolfl_list = []
rho_list = []
# Er
radius4C_list = []
Er_list = []
gradP_list = []
vpolBt_Er_list = []
vtorBp_Er_list = []
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

# page #10
rminor10_list = []
grdne_list = []
grdni_list = []
grdnh_list = []
grdnz_list = []
grdte_list = []
grdti_list = []
grdpr_list = []
grdq_list = []

# page #12
xbouni12_list = []
zvrotxb_list = []
zwexbxb_list = []
zalpha_list = []
zvtor_list = []
zvpara_list = []
zvperp_list = []
zgradrsqrave_list = []
zgradrave_list = []

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
Counter = 0
for linei in lines1: #[:54270]:
    i = i + 1 # count line number, the first line is line #1.
    # print("Line {}: {}".format(i, linei.strip()))
    # print("%5d %5d %5d %5d"%(Page1Found, Page2Found, Page3Found, Page13Found))
    # print("%5d %5d %5d %5d" % (HeaderTeFound, HeaderDeuteriumFound, HeaderEnergyLossesFound, HeaderGrowthRatesFound))
    # print("%5d"%(zonei))

    # print("linei = %d, [%d] :%s"%(i,len(linei),linei))
    if len(linei) <= 2:
        # Skip this line, maybe it is an empty line
        continue

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
    # ---------------------- Check the page at 0.000 ms------------------------ #
    if linei.find("*** time step    0 ***") != -1:
        # skip this time step
        continue

    # ---------------------- Check page #1 ------------------------------------ #
    if linei.find("- 1-  *** time") != -1:
        Page1Found = 1
        timei = float(linei[51:64])
        # time_list.append(timei)
        Counter += 1
        print("Record #%5d, time = %14f ms"%(Counter,timei))
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
    if linei.find("- 2-  *** time") != -1 and Page1Found == 1:
    # if Page1Found == 1 and HeaderTeFound == 1 and linei.find("BALDPN") != -1:
        # end of page#1 --> Reset variables
        Page1Found = 0
        HeaderTeFound = 0
        zonei = 0

        time_list.append(timei)

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
    if linei.find("- 2-  *** time") != -1:
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
    if linei.find("- 3-  *** time") != -1:
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
    if linei.find("- 3-  *** time") != -1:
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
    if linei.find("- 4-  *** time") != -1:
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

    # ---------------------- Check page #4 ------------------------------------ #
    if linei.find("- 4-  *** time") != -1:
        Page4Found = 1
        # timei = float(linei[51:64])
        # time_list.append(timei)
        # print("Page#%2d, time = %14f ms"%(6,timei))
        continue
    if Page4Found == 1 and linei.find("k-e totl    k-i totl      vnware") != -1:
        HeaderPage4AFound = 1
        continue
    if Page4Found == 1 and HeaderPage4AFound == 1 and zonei < 52:
        zonei += 1

        if zonei == 52:
            HeaderPage4AFound = 0
            zonei = 0
            continue
        # print('zonei = :',zonei,' :',linei)
        linei = CleanData(linei)
        temp1 = linei.split(' ')  # split string
        temp2 = [float(k) for k in temp1 if k != '']

        radius4A_i[zonei - 1] = temp2[1]
        ketotl_i[zonei - 1] = temp2[2]
        kitotl_i[zonei - 1] = temp2[3]
        vnware_i[zonei - 1] = temp2[4]
        veware_i[zonei - 1] = temp2[5]
        dhtotl_i[zonei - 1] = temp2[6]
        # print('temp2[6] = ',temp2[6])
        ditotl_i[zonei - 1] = temp2[7]
    if Page4Found == 1 and HeaderPage4AFound == 1 and linei.find("Predicted w_ExB by Kikuchi NTV model") != -1:
        HeaderPage4AFound = 0
        zonei = 0
        continue
    if Page4Found == 1 and linei.find("wexba     Dia.magn    vpol*Bt") != -1:
        HeaderPage4BFound = 1
        continue
    if Page4Found == 1 and linei.find("Er     gradP") != -1:
        # print("HeaderPage4CFound = 1")
        HeaderPage4BFound = 0
        HeaderPage4CFound = 1
        zonei = 0
        continue
    if Page4Found == 1 and HeaderPage4BFound == 1 and zonei < 52:

        zonei += 1

        if zonei == 52:
            HeaderPage4BFound = 0
            zonei = 0
            continue
        linei = CleanData(linei)
        temp1 = linei.split(' ')  # split string
        # print("4B :",temp1)
        temp2 = [float(k) for k in temp1 if k != '']

        radius4B_i[zonei - 1] = temp2[0]
        wexba_i[zonei - 1] = temp2[1]
        Diamagn_i[zonei - 1] = temp2[2]
        vpolBt_NTV_i[zonei - 1] = temp2[3]
        vtorBp_NTV_i[zonei - 1] = temp2[4]
        sqpolfl_i[zonei - 1] = temp2[5]
        rho_i[zonei - 1] = temp2[6]

    if Page4Found == 1 and HeaderPage4CFound == 1 and zonei < 52:

        zonei += 1

        if zonei == 52:
            HeaderPage4CFound = 0
            zonei = 0
            continue
        # print('Page4C(A) ',i,':',linei)
        linei = CleanData(linei)
        # print('Page4C(B) ', i, ':', linei)
        temp1 = linei.split(' ')  # split string
        # print("temp1 = ",temp1)
        temp2 = [float(k) for k in temp1 if k != '']
        # print(temp2)

        radius4C_i[zonei - 1] = temp2[0]
        Er_i[zonei - 1] = temp2[1]
        gradP_i[zonei - 1] = temp2[2]
        vpolBt_Er_i[zonei - 1] = temp2[3]
        vtorBp_Er_i[zonei - 1] = temp2[4]
    if Page4Found == 1 and linei.find("- 5-  *** time") != -1:
        Page4Found = 0
        HeaderPage4AFound = 0
        HeaderPage4BFound = 0
        HeaderPage4CFound = 0
        zonei = 0

        #append data
        radius4A_list.append(radius4A_i.copy())
        ketotl_list.append(ketotl_i.copy())
        kitotl_list.append(kitotl_i.copy())
        vnware_list.append(vnware_i.copy())
        veware_list.append(veware_i.copy())
        # print("dhtotl_i :",dhtotl_i)
        dhtotl_list.append(dhtotl_i.copy())
        # print("dhtot_list :",dhtotl_list)

        ditotl_list.append(ditotl_i.copy())
        # NTV
        radius4B_list.append(radius4B_i.copy())
        wexba_list.append(wexba_i.copy())
        Diamagn_list.append(Diamagn_i.copy())
        vpolBt_NTV_list.append(vpolBt_NTV_i.copy())
        vtorBp_NTV_list.append(vtorBp_NTV_i.copy())
        sqpolfl_list.append(sqpolfl_i.copy())
        rho_list.append(rho_i.copy())
        # Er
        radius4C_list.append(radius4C_i.copy())
        Er_list.append(Er_i.copy())
        gradP_list.append(gradP_i.copy())
        vpolBt_Er_list.append(vpolBt_Er_i.copy())
        vtorBp_Er_list.append(vtorBp_Er_i.copy())

        # print('Er_list = ',Er_list)
        # print('vtorBp_Er_i = ',vtorBp_Er_i)
        # exit(0)




    # ---------------------- Check page #5 ------------------------------------ #
    if linei.find("- 5-  *** time") != -1:
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
    if linei.find("- 6-  *** time") != -1:
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
    if linei.find("- 6-  *** time") != -1:
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



    if linei.find("- 7-  *** time") != -1:
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
    if linei.find("- 7-  *** time") != -1:
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

    if linei.find("- 8-  *** time") != -1:
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
    if linei.find("- 8-  *** time") != -1:
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
    if linei.find("- 9-  *** time") != -1:
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
    if linei.find("- 9-  *** time") != -1:
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
        # print("Page 9:",linei)
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
    if linei.find("-10-  *** time") != -1:
        Page9Found = 0
        HeaderPage9Found = 0
        zonei = 0
        # append data
        if lthery21 == 10: # MMM
            rminor9_list.append(rminor9_i.copy())
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

    # ---------------------- Check page #10 ------------------------------------ #
    if linei.find("-10-  *** time") != -1:
        Page10Found = 1
        # timei = float(linei[51:64])
        # time_list.append(timei)
        # print("Page#%2d, time = %14f ms"%(13,timei))
        continue
    if Page10Found == 1 and HeaderPage10Found == 1 and (linei.find(' grdne       grdni') != -1):
        continue
    if Page10Found == 1 and HeaderPage10Found == 1 and zonei < 52:
        zonei += 1

        if zonei == 52:
            continue

        linei = CleanData(linei)
        temp1 = linei.split(' ')  # split string
        temp2 = [float(k) for k in temp1 if k != '']

        rminor10_i[zonei - 1] = temp2[0]
        grdne_i[zonei - 1] = temp2[1]
        grdni_i[zonei - 1] = temp2[2]
        grdnh_i[zonei - 1] = temp2[3]
        grdnz_i[zonei - 1] = temp2[4]
        grdte_i[zonei - 1] = temp2[5]
        grdti_i[zonei - 1] = temp2[6]
        grdpr_i[zonei - 1] = temp2[7]
        grdq_i[zonei - 1] = temp2[8]
    if Page10Found == 1 and linei.find("Normalized gradients:") != -1:
        HeaderPage10Found = 1
        continue
    if linei.find("-11-  *** time") != -1:

        Page10Found = 0
        HeaderPage10Found = 0
        zonei = 0
        # append data
        rminor10_list.append(rminor10_i.copy())
        grdne_list.append(grdne_i.copy())
        grdni_list.append(grdni_i.copy())
        grdnh_list.append(grdnh_i.copy())
        grdnz_list.append(grdnz_i.copy())
        grdte_list.append(grdte_i.copy())
        grdti_list.append(grdti_i.copy())
        grdpr_list.append(grdpr_i.copy())
        grdq_list.append(grdq_i.copy())

    # ---------------------- Check page #12 ------------------------------------ #
    if linei.find("-12-  *** time") != -1:
        Page12Found = 1
        # timei = float(linei[51:64])
        # time_list.append(timei)
        # print("Page#%2d, time = %14f ms"%(13,timei))
        continue
    if Page12Found == 1 and HeaderPage12Found == 1 and (linei.find(' zvrotxb     zwexbxb') != -1):
        continue
    if Page12Found == 1 and HeaderPage12Found == 1 and zonei < 52:
        zonei += 1

        if zonei == 52:
            continue
        # print(linei)
        linei = CleanData(linei)
        # print(linei)
        temp1 = linei.split(' ')  # split string
        # print(temp1)
        temp2 = [float(k) for k in temp1 if k != '']
        # print(temp2)

        xbouni12_i[zonei - 1] = temp2[0]
        zvrotxb_i[zonei - 1] = temp2[1]
        zwexbxb_i[zonei - 1] = temp2[2]
        zalpha_i[zonei - 1] = temp2[3]
        zvtor_i[zonei - 1] = temp2[4]
        zvpara_i[zonei - 1] = temp2[5]
        zvperp_i[zonei - 1] = temp2[6]
        zgradrsqrave_i[zonei - 1] = temp2[7]
        zgradrave_i[zonei - 1] = temp2[8]

    if Page12Found == 1 and linei.find("Variables used by callglf2db:") != -1:
        HeaderPage12Found = 1
        continue
    if linei.find("-13-  *** time") != -1 and Page12Found == 1:
        # print(linei)
        Page12Found = 0
        HeaderPage12Found = 0
        zonei = 0
        # append data
        xbouni12_list.append(xbouni12_i.copy())
        zvrotxb_list.append(zvrotxb_i.copy())
        zwexbxb_list.append(zwexbxb_i.copy())
        zalpha_list.append(zalpha_i.copy())
        zvtor_list.append(zvtor_i.copy())
        zvpara_list.append(zvpara_i.copy())
        zvperp_list.append(zvperp_i.copy())
        zgradrsqrave_list.append(zgradrsqrave_i.copy())
        zgradrave_list.append(zgradrave_i.copy())

    # ---------------------- Check page #13 ------------------------------------ #
    if linei.find("-13-  *** time") != -1:
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
    if linei.find("-14-  *** time") != -1:
        Page13Found = 0
        HeaderGrowthRatesFound = 0
        zonei = 0
        # append data
        rminor13_list.append(rminor13_i.copy())
        gITG_list.append(gITG_i.copy())
        oITG_list.append(oITG_i.copy())
        gTEM_list.append(gTEM_i.copy())
        oTEM_list.append(oTEM_i.copy())

# print("time_list = ",time_list)
print("@ === Total time slices = %5d"%(len(time_list)))
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

radius4A_arr = np.array(radius4A_list)
ketotl_arr = np.array(ketotl_list)
kitotl_arr = np.array(kitotl_list)
vnware_arr = np.array(vnware_list)
veware_arr = np.array(veware_list)
dhtotl_arr = np.array(dhtotl_list)
ditotl_arr = np.array(ditotl_list)
# NTV
radius4B_arr = np.array(radius4B_list)
wexba_arr = np.array(wexba_list)
Diamagn_arr = np.array(Diamagn_list)
vpolBt_NTV_arr = np.array(vpolBt_NTV_list)
vtorBp_NTV_arr = np.array(vtorBp_NTV_list)
sqpolfl_arr = np.array(sqpolfl_list)
rho_arr = np.array(rho_list)
# Er
radius4C_arr = np.array(radius4C_list)
Er_arr = np.array(Er_list)
gradP_arr = np.array(gradP_list)
vpolBt_Er_arr = np.array(vpolBt_Er_list)
vtorBp_Er_arr = np.array(vtorBp_Er_list)

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

rminor10_arr = np.array(rminor10_list)
grdne_arr = np.array(grdne_list)
grdni_arr = np.array(grdni_list)
grdnh_arr = np.array(grdnh_list)
grdnz_arr = np.array(grdnz_list)
grdte_arr = np.array(grdte_list)
grdti_arr = np.array(grdti_list)
grdpr_arr = np.array(grdpr_list)
grdq_arr = np.array(grdq_list)

xbouni12_arr = np.array(xbouni12_list)
zvrotxb_arr = np.array(zvrotxb_list)
zwexbxb_arr = np.array(zwexbxb_list)
zalpha_arr = np.array(zalpha_list)
zvtor_arr = np.array(zvtor_list)
zvpara_arr = np.array(zvpara_list)
zvperp_arr = np.array(zvperp_list)
zgradrsqrave_arr = np.array(zgradrsqrave_list)
zgradrave_arr = np.array(zgradrave_list)

rminor13_arr = np.array(rminor13_list)
gITG_arr = np.array(gITG_list)
oITG_arr = np.array(oITG_list)
gTEM_arr = np.array(gTEM_list)
oTEM_arr = np.array(oTEM_list)


RadList = [0, 10, 20, 30, 40]

Option_Save = 1
FilenamePrefix = "%s%s"%(MachineName, FolderCode)
os.chdir(PathToJfile)

# https://stackoverflow.com/questions/9542738/python-find-in-list
# time0upper = next((x for x in Time1D if time0 < x),None)
# time0upper_idx = Time1D.index(time0upper)
time0lower = np.where(Time1D<time0)
time0lower_index = time0lower[0][-1]

idx = np.round(np.linspace(time0lower_index,len(Time1D)-2, 5)).astype(int)
TimeList = Time1D[idx]

print("TimeList = ",TimeList)
print("\n")

# Visualization ----------------------------------------------------------------
# Page #1
VariableList1 = [Te_arr, Ti_arr, ne_arr, ni_arr, q_arr, beta_arr]
VariableNameList1 = ['Te', 'Ti', 'ne', 'ni', 'q', 'beta']
TitleList1 = [str(s) + '(r,t)' for s in VariableNameList1]

# Page #2
VariableList2 = [nD_arr, nT_arr, nImp1_arr, nImp2_arr, zeff_arr]
VariableNameList2 = ['nD', 'nT', 'nImp1', 'nImp2', 'Zeff']
TitleList2 = [str(s) + '(r,t)' for s in VariableNameList2]
if NoOfImp == 3:
    # Page #2: imp3 density
    VariableList2 += [nImp3_arr]
    VariableNameList2 += ['nImp3']

# Page #4:
VariableList4A = [ketotl_arr, kitotl_arr, vnware_arr, veware_arr, dhtotl_arr, ditotl_arr]
VariableNameList4A = ['ketotl', 'kitotl', 'vnware', 'veware', 'dhtotl', 'ditotl']
TitleList4A = [str(s) + '(r,t)' for s in VariableNameList4A]

VariableList4B = [radius4B_arr, wexba_arr, Diamagn_arr, vpolBt_NTV_arr, vtorBp_NTV_arr, sqpolfl_arr,]
VariableNameList4B = ['radius4B', 'wexba', 'Diamagn', 'vpolBt_NTV', 'vtorBp_NTV', 'sqpolfl']
TitleList4B = [str(s) + '(r,t)' for s in VariableNameList4B]

VariableList4C = [radius4C_arr, Er_arr, gradP_arr, vpolBt_Er_arr, vtorBp_Er_arr]
VariableNameList4C = ['radius4C', 'Er', 'gradP', 'vpolBt_Er', 'vtorBp_Er']
TitleList4C = [str(s) + '(r,t)' for s in VariableNameList4C]

# Page #5:
VariableList5 = [chie_arr, chii_arr, zdifh_arr, zdifz_arr]
VariableNameList5 = ['chi-e', 'chi-i', 'zdifh', 'zdifz']
TitleList5 = [str(s) + '(r,t)' for s in VariableNameList5]

# Page #6
if lthery21 == 10:
    VariableList6 = [thiig_arr, thirb_arr, thikb_arr, xithe_arr, neocl_arr, empirc_arr, xitot_arr]
    VariableNameList6 = ['thiig', 'thirb', 'thikb', 'xithe', 'neocl', 'empirc', 'xitot']
    TitleList6 = [str(s) + '(r,t)' for s in VariableNameList6]
elif lthery21 == 8:
    VariableList6 = [Xi_Bohm_arr, Xi_gBohm_arr, Xi_Mixed_arr, Xi_Neo_arr, Xi_Empirc_arr, Xi_Total_arr]
    VariableNameList6 = ['Xi_Bohm', 'Xi_gBohm', 'Xi_Mixed', 'Xi_Neo', 'Xi_Empirc', 'Xi_Total']
    TitleList6 = [str(s) + '(r,t)' for s in VariableNameList6]

# Page #7
if lthery21 == 10: # MMM
    VariableList7 =     [theig_arr   , therb_arr   , thekb_arr   , theeg_arr, thetb_arr,
                         xethe_arr   , neocle_arr  , empirce_arr , xetot_arr]
    TitleList7 =        ['theig(r,t)'   , 'therb(r,t)'   , 'thekb(r,t)'   , 'theeg(r,t)', 'thetb(r,t)',
                         'xethe(r,t)'   , 'neocle(r,t)'  , 'empirce(r,t)' , 'xetot(r,t)']
    VariableNameList7 = ['theig'   , 'therb'   , 'thekb'   , 'theeg', 'thetb',
                         'xethe'   , 'neocle'  , 'empirce' , 'xetot']
elif lthery21 == 8: # Mixed B/gB
    VariableList7 =     [Xe_Bohm_arr   , Xe_gBohm_arr   , Xe_Mixed_arr   , Xe_Neo_arr   , Xe_Empirc_arr   , Xe_Total_arr]
    TitleList7 =        ['Xe_Bohm(r,t)', 'Xe_gBohm(r,t)', 'Xe_Mixed(r,t)', 'Xe_Neo(r,t)', 'Xe_Empirc(r,t)', 'Xe_Total(r,t)']
    VariableNameList7 = ['Xe_Bohm'     , 'Xe_gBohm'     , 'Xe_Mixed'     , 'Xe_Neo'     , 'Xe_Empirc'     , 'Xe_Total']

# Page #8:
if lthery21 == 10: # MMM
    VariableList8 =     [thdig_arr   , thdrb_arr   , thdkb_arr   , dhthe_arr]
    TitleList8 =        ['thdig(r,t)', 'thdrb(r,t)', 'thdkb(r,t)', 'dhthe(r,t)']
    VariableNameList8 = ['thdig'     , 'thdrb'     , 'thdkb'     , 'dhthe']
elif lthery21 == 8: # Mixed B/gB
    VariableList8 = [X_Particle_arr]
    TitleList8 = ['X_Particle(r,t)']
    VariableNameList8 = ['X_Particle']

# Page #9:
if lthery21 == 10: # MMM
    VariableList9 = [tzdig_arr, tzdrb_arr, thzkb_arr, dzthe_arr, neoclz_arr, empircz_arr, dztot_arr]
    VariableNameList9 = ['tzdig', 'tzdrb', 'thzkb', 'dzthe', 'neoclz', 'empircz', 'dztot']
    TitleList9 = [str(s) + '(r,t)' for s in VariableNameList9]

elif lthery21 == 8: # Mixed B/gB
    VariableList9 = [X_Impuirity_arr]
    VariableNameList9 = ['X_Impurity']
    TitleList9 = [str(s) + '(r,t)' for s in VariableNameList9]

# Page #10:
VariableList10 = [grdne_arr, grdni_arr, grdnh_arr,  grdnz_arr, grdte_arr, grdti_arr, grdpr_arr, grdq_arr]
VariableNameList10 = ['grdne', 'grdni', 'grdnh', 'grdnz', 'grdte', 'grdti', 'grdpr', 'grdq']
TitleList10 = [str(s) + '(r,t)' for s in VariableNameList10]

# Page #12:
VariableList12 = [xbouni12_arr, zvrotxb_arr, zwexbxb_arr, zalpha_arr, zvtor_arr, zvpara_arr, zvperp_arr, zgradrsqrave_arr, zgradrave_arr]
VariableNameList12 = ['xbouni', 'zvrotxb', 'zwexbxb', 'zalpha', 'zvtor', 'zvpara', 'zvperp', 'zgradrsqrave', 'zgradrave']
TitleList12 = [str(s) + '(r,t)' for s in VariableNameList12]

# Page #13:
VariableList13 = [gITG_arr, gTEM_arr]
VariableNameList13 = ['gamma_ITG', 'gamma_TEM']
TitleList13 = [str(s) + '(r,t)' for s in VariableNameList13]

# All pages
VariableList = VariableList1 + VariableList2 \
               + VariableList4A + VariableList4B + VariableList4C \
               + VariableList5 + VariableList6 + VariableList7 + VariableList8 \
               + VariableList9 + VariableList10 + VariableList12 + VariableList13
VariableNameList = VariableNameList1 + VariableNameList2 \
                   + VariableNameList4A + VariableNameList4B + VariableNameList4C \
                   + VariableNameList5 + VariableNameList6 + VariableNameList7 + VariableNameList8 \
                   + VariableNameList9 + VariableNameList10 + VariableNameList12 + VariableNameList13
TitleList = [str(s) + '(r,t)' for s in VariableNameList]

# Validation of lists
if (len(VariableList) != len(VariableNameList)) or (len(VariableList) != len(TitleList)):
    print("[Error] Lengths of lists are not correct!")
    print("        %3d, %3d, %3d"%(len(VariableList),len(VariableNameList), len(TitleList)))
    exit(0)

# Plot data from lists
for i in range(0, len(VariableList)):
    print("Plot #%3d from %3d"%(i+1, len(VariableList)))
    Plot1DTime_FixRad(VariableList[i], Time1D, VariableNameList[i], RadList, TitleList[i], Option_Save, FilenamePrefix)
    Plot1DTime_FixTime(VariableList[i], Time1D, VariableNameList[i], TimeList, TitleList[i], Option_Save, FilenamePrefix)
    ImshowPlot(VariableList[i], Time1D, VariableNameList[i], TitleList[i], Option_Save, FilenamePrefix, Time0Index=time0lower_index)

# Export to CSV files
SaveCsvFile(Time1D, VariableList, VariableNameList, FolderCode, SaveTimeOption=1)
