import pandas as pd
import numpy as np
import math
####################################################D_RTN Function
def D_RTN(new67,cusip):
    #获取index，price,shrout,divamt列
    led = new67[(new67["CUSIP"] == cusip)].index
    price=new67[(new67["CUSIP"]==cusip)]['PRC']
    share=new67[(new67["CUSIP"]==cusip)]['SHROUT']
    div=new67[(new67["CUSIP"]==cusip)]['DIVAMT']
    #f(t)
    f = share / (share.shift())
    #p(t-1)
    p=price.shift()
    #Daily Return r(t)
    rlist=[]
    for i in range(led[0],led[-1]+1):
        r=((price[i]*f[i]+div[i])/p[i])-1
        rlist.append(r)
    #去掉第一行的NAN,改成零
    del rlist[0]
    rlist.insert(0, 0)
    return rlist
####################################################D_RTN END
# fun1=D_RTN(new67,'00172320')
# print(len(fun1))
# print(fun1)

####################################################TURNOVER Function
#def turnover(new67,cusip):
def turnover(a):
    # 获取vol,shrout列
    #let=new67[(new67["CUSIP"] == cusip)].index
    #vo = new67[(new67["CUSIP"] == cusip)]['VOL']
    #sh = new67[(new67["CUSIP"] == cusip)]['SHROUT']   
    #Share Turnover list
    stlist = a.VOL / a.SHROUT
    return stlist
####################################################TURNOVER END
# fun2 = turnover(new67,'00172320')
# print(len(fun2))
# print(fun2)

# ####################################################SSD_T Function
# #获取两只股票的share turnover值 例子来自于'00080010','00172320'
# t1=[1.1699931176875431, 1.9270474879559532, 1.5141087405368203, 1.5829318651066759, 0.61940812112869925, 1.3076393668272539, 0.89470061940812118, 2.4088093599449416, 0.41293874741913283, 0.68823124569855476, 0.27529249827942187, 0.34411562284927738, 1.1011699931176875, 0.68823124569855476, 0.68823124569855476, 1.3076393668272539, 4.1293874741913283, 0.34411562284927738, 1.6517549896765313, 1.4452856159669649, 1.7205781142463867, 1.5829318651066759, 1.1699931176875431, 0.55058499655884374, 1.7894012388162424, 1.9270474879559532, 0.82587749483826567, 0.27529249827942187, 1.6517549896765313, 1.6517549896765313, 0.55058499655884374, 0.82587749483826567, 0.61940812112869925, 0.48176187198898829, 0.82587749483826567, 0.68823124569855476, 1.4452856159669649, 1.4452856159669649, 2.8905712319339298, 0.48176187198898829, 1.6517549896765313, 0.068823124569855468, 1.3764624913971095, 1.1699931176875431, 1.1699931176875431, 1.7205781142463867, 1.5829318651066759, 0.55058499655884374, 1.1011699931176875, 0.82587749483826567, 0.34411562284927738, 0.82587749483826567, 1.1699931176875431, 2.202339986235375, 1.5141087405368203, 1.5141087405368203, 2.6152787336545078, 1.1699931176875431, 0.82587749483826567, 0.61940812112869925, 0.82587749483826567, 0.48176187198898829, 1.0323468685478321, 1.1011699931176875, 2.3399862353750862, 1.3764624913971095, 0.20646937370956642, 1.5141087405368203, 0.27529249827942187, 1.1011699931176875, 2.8217481073640744, 0.96352374397797658, 0.34411562284927738, 1.1011699931176875, 1.1699931176875431, 0.61940812112869925, 0.48176187198898829, 1.7894012388162424, 1.3076393668272539, 0.96352374397797658, 0.55058499655884374, 1.7894012388162424, 0.89470061940812118, 1.5829318651066759, 3.097040605643496, 0.27529249827942187, 1.7205781142463867, 1.9958706125258088, 1.1011699931176875, 4.335856847900895, 0.68823124569855476, 0.96352374397797658, 1.0323468685478321, 2.202339986235375, 2.752924982794219, 0.82587749483826567, 1.9270474879559532, 0.89470061940812118, 1.0323468685478321, 1.4452856159669649, 10.461114934618031, 6.0564349621472813, 1.3764624913971095, 0.48176187198898829, 0.55058499655884374, 0.89470061940812118, 0.068823124569855468, 0.68823124569855476, 1.9958706125258088, 1.4452856159669649, 1.1699931176875431, 0.68823124569855476, 0.48176187198898829, 0.48176187198898829, 2.6152787336545078, 1.5141087405368203, 1.3764624913971095, 0.61940812112869925, 0.89470061940812118, 1.2388162422573985, 0.89470061940812118, 1.1699931176875431, 1.1011699931176875, 0.20646937370956642, 0.68823124569855476, 0.55058499655884374]
# t2=[0.85158150851581504, 1.7639902676399026, 1.5206812652068127, 1.1861313868613139, 0.74513381995133821, 1.4294403892944039, 1.2013381995133821, 1.2925790754257906, 0.62347931873479323, 0.6082725060827251, 0.36496350364963503, 0.57785888077858882, 1.1100973236009732, 0.66909975669099753, 0.74513381995133821, 0.57785888077858882, 0.77554744525547448, 0.72992700729927007, 0.57785888077858882, 0.51703163017031628, 2.6916058394160585, 1.3229927007299269, 1.2317518248175183, 0.6082725060827251, 1.2013381995133821, 1.1861313868613139, 1.079683698296837, 0.59306569343065696, 0.57785888077858882, 0.76034063260340634, 1.8400243309002433, 1.687956204379562, 0.47141119221411193, 0.48661800486618007, 0.6082725060827251, 0.57785888077858882, 0.79075425790754261, 1.9464720194647203, 1.1253041362530414, 1.4598540145985401, 0.39537712895377131, 0.95802919708029199, 0.57785888077858882, 0.63868613138686137, 0.95802919708029199, 0.66909975669099753, 1.3838199513381995, 1.2773722627737227, 0.85158150851581504, 0.30413625304136255, 0.45620437956204379, 0.85158150851581504, 0.86678832116788318, 0.57785888077858882, 1.687956204379562, 0.59306569343065696, 1.2925790754257906, 0.85158150851581504, 1.8856447688564477, 1.6119221411192215, 1.7031630170316301, 1.6271289537712896, 0.66909975669099753, 0.88199513381995132, 1.687956204379562, 0.76034063260340634, 1.1709245742092458, 1.3229927007299269, 0.74513381995133821, 0.80596107055961075, 1.2469586374695865, 1.9616788321167884, 1.079683698296837, 0.76034063260340634, 1.1100973236009732, 1.2013381995133821, 1.1861313868613139, 1.687956204379562, 2.2049878345498786, 1.7335766423357664, 1.8400243309002433, 0.86678832116788318, 0.86678832116788318, 1.1861313868613139, 1.809610705596107, 1.444647201946472, 1.444647201946472, 2.9805352798053528, 1.4598540145985401, 1.2925790754257906, 0.88199513381995132, 0.76034063260340634, 1.2773722627737227, 1.2165450121654502, 1.7791970802919708, 1.4598540145985401, 0.86678832116788318, 0.47141119221411193, 1.2469586374695865, 2.0529197080291972, 1.1861313868613139, 1.6727493917274938, 0.62347931873479323, 0.74513381995133821, 0.88199513381995132, 0.44099756690997566, 0.74513381995133821, 0.57785888077858882, 1.0340632603406326, 0.71472019464720193, 1.0036496350364963, 0.62347931873479323, 0.33454987834549876, 0.68430656934306566, 0.3497566909975669, 0.31934306569343068, 0.51703163017031628, 0.62347931873479323, 0.51703163017031628, 0.44099756690997566, 0.41058394160583944, 0.30413625304136255, 0.47141119221411193, 0.42579075425790752, 0.44099756690997566, 0.47141119221411193]
def ssd_t(t1, t2):
    #获取t1,t2长度
    les1=len(t1)
    les2=len(t2)
    #循环索引的范围来自于t1长度
    les = int(les1)
    ssd=0
    for i in range(les):
        ssd+=(t1[i]-t2[i])**2
    return ssd
####################################################SSD_T END
# fun3=ssd_t()
# print(fun3)

# ####################################################SMD_T  Function
# #获取两只股票的share turnover值 例子来自于'00080010','00172320'
# t1=[1.1699931176875431, 1.9270474879559532, 1.5141087405368203, 1.5829318651066759, 0.61940812112869925, 1.3076393668272539, 0.89470061940812118, 2.4088093599449416, 0.41293874741913283, 0.68823124569855476, 0.27529249827942187, 0.34411562284927738, 1.1011699931176875, 0.68823124569855476, 0.68823124569855476, 1.3076393668272539, 4.1293874741913283, 0.34411562284927738, 1.6517549896765313, 1.4452856159669649, 1.7205781142463867, 1.5829318651066759, 1.1699931176875431, 0.55058499655884374, 1.7894012388162424, 1.9270474879559532, 0.82587749483826567, 0.27529249827942187, 1.6517549896765313, 1.6517549896765313, 0.55058499655884374, 0.82587749483826567, 0.61940812112869925, 0.48176187198898829, 0.82587749483826567, 0.68823124569855476, 1.4452856159669649, 1.4452856159669649, 2.8905712319339298, 0.48176187198898829, 1.6517549896765313, 0.068823124569855468, 1.3764624913971095, 1.1699931176875431, 1.1699931176875431, 1.7205781142463867, 1.5829318651066759, 0.55058499655884374, 1.1011699931176875, 0.82587749483826567, 0.34411562284927738, 0.82587749483826567, 1.1699931176875431, 2.202339986235375, 1.5141087405368203, 1.5141087405368203, 2.6152787336545078, 1.1699931176875431, 0.82587749483826567, 0.61940812112869925, 0.82587749483826567, 0.48176187198898829, 1.0323468685478321, 1.1011699931176875, 2.3399862353750862, 1.3764624913971095, 0.20646937370956642, 1.5141087405368203, 0.27529249827942187, 1.1011699931176875, 2.8217481073640744, 0.96352374397797658, 0.34411562284927738, 1.1011699931176875, 1.1699931176875431, 0.61940812112869925, 0.48176187198898829, 1.7894012388162424, 1.3076393668272539, 0.96352374397797658, 0.55058499655884374, 1.7894012388162424, 0.89470061940812118, 1.5829318651066759, 3.097040605643496, 0.27529249827942187, 1.7205781142463867, 1.9958706125258088, 1.1011699931176875, 4.335856847900895, 0.68823124569855476, 0.96352374397797658, 1.0323468685478321, 2.202339986235375, 2.752924982794219, 0.82587749483826567, 1.9270474879559532, 0.89470061940812118, 1.0323468685478321, 1.4452856159669649, 10.461114934618031, 6.0564349621472813, 1.3764624913971095, 0.48176187198898829, 0.55058499655884374, 0.89470061940812118, 0.068823124569855468, 0.68823124569855476, 1.9958706125258088, 1.4452856159669649, 1.1699931176875431, 0.68823124569855476, 0.48176187198898829, 0.48176187198898829, 2.6152787336545078, 1.5141087405368203, 1.3764624913971095, 0.61940812112869925, 0.89470061940812118, 1.2388162422573985, 0.89470061940812118, 1.1699931176875431, 1.1011699931176875, 0.20646937370956642, 0.68823124569855476, 0.55058499655884374]
# t2=[0.85158150851581504, 1.7639902676399026, 1.5206812652068127, 1.1861313868613139, 0.74513381995133821, 1.4294403892944039, 1.2013381995133821, 1.2925790754257906, 0.62347931873479323, 0.6082725060827251, 0.36496350364963503, 0.57785888077858882, 1.1100973236009732, 0.66909975669099753, 0.74513381995133821, 0.57785888077858882, 0.77554744525547448, 0.72992700729927007, 0.57785888077858882, 0.51703163017031628, 2.6916058394160585, 1.3229927007299269, 1.2317518248175183, 0.6082725060827251, 1.2013381995133821, 1.1861313868613139, 1.079683698296837, 0.59306569343065696, 0.57785888077858882, 0.76034063260340634, 1.8400243309002433, 1.687956204379562, 0.47141119221411193, 0.48661800486618007, 0.6082725060827251, 0.57785888077858882, 0.79075425790754261, 1.9464720194647203, 1.1253041362530414, 1.4598540145985401, 0.39537712895377131, 0.95802919708029199, 0.57785888077858882, 0.63868613138686137, 0.95802919708029199, 0.66909975669099753, 1.3838199513381995, 1.2773722627737227, 0.85158150851581504, 0.30413625304136255, 0.45620437956204379, 0.85158150851581504, 0.86678832116788318, 0.57785888077858882, 1.687956204379562, 0.59306569343065696, 1.2925790754257906, 0.85158150851581504, 1.8856447688564477, 1.6119221411192215, 1.7031630170316301, 1.6271289537712896, 0.66909975669099753, 0.88199513381995132, 1.687956204379562, 0.76034063260340634, 1.1709245742092458, 1.3229927007299269, 0.74513381995133821, 0.80596107055961075, 1.2469586374695865, 1.9616788321167884, 1.079683698296837, 0.76034063260340634, 1.1100973236009732, 1.2013381995133821, 1.1861313868613139, 1.687956204379562, 2.2049878345498786, 1.7335766423357664, 1.8400243309002433, 0.86678832116788318, 0.86678832116788318, 1.1861313868613139, 1.809610705596107, 1.444647201946472, 1.444647201946472, 2.9805352798053528, 1.4598540145985401, 1.2925790754257906, 0.88199513381995132, 0.76034063260340634, 1.2773722627737227, 1.2165450121654502, 1.7791970802919708, 1.4598540145985401, 0.86678832116788318, 0.47141119221411193, 1.2469586374695865, 2.0529197080291972, 1.1861313868613139, 1.6727493917274938, 0.62347931873479323, 0.74513381995133821, 0.88199513381995132, 0.44099756690997566, 0.74513381995133821, 0.57785888077858882, 1.0340632603406326, 0.71472019464720193, 1.0036496350364963, 0.62347931873479323, 0.33454987834549876, 0.68430656934306566, 0.3497566909975669, 0.31934306569343068, 0.51703163017031628, 0.62347931873479323, 0.51703163017031628, 0.44099756690997566, 0.41058394160583944, 0.30413625304136255, 0.47141119221411193, 0.42579075425790752, 0.44099756690997566, 0.47141119221411193]
def smd_t(t1, t2):
    #将两个list合并
    npvec1, npvec2 = np.array(t1), np.array(t2)
    npvec = np.array([npvec1, npvec2])
    inv_sub = np.linalg.inv(np.cov(t1, t2))
    #计算马氏距离并累加求和
    maha=0
    for i in range(len(npvec.T)):
        sub = npvec.T[i]
        maha += math.sqrt(np.dot(inv_sub, sub).dot(sub.T))
    return maha
####################################################SMD_T  END
# fun4=smd_t()
# print(fun4)