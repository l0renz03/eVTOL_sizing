import numpy as np
import scipy.optimize as sp
import matplotlib.pyplot as plt
from wingpowerloading import wingloadinglanding2, rho, CLmax, Vcruise
from wingsizing import MTOWcruise, b, AR

wingloading = wingloadinglanding2[0]
speedpos = np.arange(0,200, 0.1)
speedneg = np.arange(0,100,0.1)
nposmax = 3.8
nnegmax = -0.4 *nposmax
VD = 1.4 * Vcruise
Vstall = np.sqrt(wingloading*2/rho/CLmax)
gustcruise = 50*0.3048
gustVD = 25*0.3048
gustVB = 66*0.3048
CLalpha = 4.885 #https://watermark.silverchair.com/100026_1_5.0191632.pdf?token=AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAABYQwggWABgkqhkiG9w0BBwagggVxMIIFbQIBADCCBWYGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMdiwIoz4E5mhURtiGAgEQgIIFN20gUfVf1sHrpy9vr-j_IFUobb0RepzTZ2ZV4E3mpJMSyUQR3beqE1qjicGHuXtxXCALwA04Kh6oO7zD5cVYt55LGGgZjze9qWNC8U1GGoyrF0pNi5KsABsH2NmojLmVRgoFDc8g5zsf5HVpTG7bQBeJx59bg9BNtikb4BSiFqsh_GdiAi2Wo0d4rgPcSlk5GVVeBc9N7utoRnISkPZsvUUnGt0bD1R83A1jJoViGHII17mR3xv3zv37NNnpxGsqAmiDhUoG25aj3zKmjGUyUYod3aCxAIt8v2-XcoRmF8NjszRZVsrYVz6--tGM3mS37NYNEGHiA_1LTX3pvk0bnfLeDvIYhe_KlM2Behf6h43FwIQEUiCBNcqDtQybovZqYt_ehsT2iqKOZqeG7XHm0zoWMNSUtACo71ThAoIu8c-tjJ0GqfV4-OCVmu7JXXL5I_IDU3vCUCsTshEatAqRfKjvPw5aglMi2cZIE7pL4S999gp5b6sAahZNRUhBSLoHS3zpiRklBvpktn6046FOPFmOc4369fg0cRpP1GuUI-ywCBrjESf_zIZCZJvI9upq8D6W76z28-KCH9yekV3xUnyTdVPeJ6gY7RPoTNdtqEUgd7KUCXypRyf0_iYaZaBtrTkaaNqVsekx37GU1uk-wtKUtQ2ud734XQYNduC9DaE4o4kdb5gtzUs29XfTyHUesHO__CfLHDtMxI72CYwihP4hPVaJHVnw7CvqcBaFbJ1itNerHWa5FQcPMzReP0rpc82C2QTqV1JBnKC7zYPeCy6k1lTEjovK7Z8GqoGAK_E3IGCDO8XMh8LP4MekwHzsW8NmyN-TXVWi1I4W9qP3v9M__w8Fela9KRELvFUPkQGbTjNjVVj6baDV3g_B9_GNp2uDKFe2StIGgCSmvMImghZaSd9ImVWZJeLzOo3yAPSExmnEzxpjliJCWAIv-nKt2oipXs-nl1WmE-FKnT8E9Ui32wPrY3ztyuMIdPL27vzQGYtdnkFFU7ZHJjHoSoQsse0A3g0gOhrmgMteFq9xzpjXykizEFrEhr_Xnf0r7jmZ8fDThkosMRGjOc3bHHBqZeSzYg1uKJnds_9fE1QROUvngOBwHqVLAr2dfo6aNVB7dbCKYu7JbGwuzD-4Rc7Tc-sgtmZioErjvaVU3oCZkjERyMAV3d0HbZ3UdRTIQFMC3VrVh4cmsJvtK6KxFFAz5x8CyEm3lRaJUsP--I3_I003Kt-6oFV5HDVClEn2K0EGT9Pgn_juzxtKnTs5IgqXOtIX8Zz-K1ERZkAm_H-1rURN5e3F3nVd2e-PuEqs-GoJ76T-w7vs8OBXkcNMN2KjU9U0SG7vZZyeDo8NozodVPMC34-jpKHlfm_hW_nK5M_cx6e6luvexMkR7tDeuVHhLeJBHCWJr5mcDKg4z_xYzHHy6Pnaid15G6PFLEc0k-gVLPaCMB_sYeYjAEQV8CGI1q4PP0ZBf3rLFMLYkvqqPTzB8NNimWeG50FS26E67yBhTAXwft7-F8aWtg5uTqBLC6Pl_qqEfCdjOHuZAZ1FNPjCSLx8JxVesMotssNy4FzVTBpqLeNzytY3kLyBtNeUWcjz1TGbYU1-kjJRUsDDlwlkeXfTlfxf1yhP0T6_cwLhx76U8WV6FeWCPxiLif8VWgEbBTPfmEqKvCyfiSvB1fAYLnx94WvAOdXCgaTiwUi7iJRplei7Ge0FsCPtwTUvhufEx3Z4ewhrX_KoYWhsXMcFRVHdi6x8VCDVfyPviBJlINxnyxrT3Q ROSKAM
chord = b/AR
g=9.81


nposlist=[]
VA = []
for i in range(len(speedpos)):
    if 0.5*rho*speedpos[i]**2*CLmax/wingloading <= nposmax:
        nposlist.append(0.5*rho*speedpos[i]**2*CLmax/wingloading)
    elif all(speedpos[i] < value for value in VA):
        VA.append(speedpos[i])
VA = VA[0]
nneglist=[]
Vnegn = []
for i in range(len(speedneg)):
    if -0.5*rho*speedneg[i]**2*CLmax/wingloading >= nnegmax:
        nneglist.append(-0.5*rho*speedneg[i]**2*CLmax/wingloading)
    elif all(speedneg[i] < value for value in Vnegn):
        Vnegn.append(speedneg[i])
Vnegn=Vnegn[0]

speednposmax = np.arange(VA,VD,0.1)
speednnegmax = np.arange(Vnegn,Vcruise,0.1)
nposmaxlist = nposmax * np.ones(len(speednposmax))
nnegmaxlist = nnegmax * np.ones(len(speednnegmax))
speednnegdive = np.arange(Vcruise,VD,0.1)
speedmaxlist = VD*np.ones(10)
nspeedmaxlist = np.linspace(0,nposmax,len(speedmaxlist))
nnegdivelist = []
for i in range(len(speednnegdive)):
    nnegdivelist.append(nnegmax-nnegmax*i/len(speednnegdive))
mug = 2*wingloading/(rho*chord*CLalpha*g)
kg = 0.88*mug/(5.3+mug)
deltancruise = kg*rho*Vcruise*CLalpha*gustcruise/2/wingloading
ngustcruisepos = 1 + deltancruise
ngustcruiseneg = 1 - deltancruise
deltanVD = kg*rho*VD*CLalpha*gustVD/2/wingloading
ngustVDpos = 1 + deltanVD
ngustVDneg = 1 - deltanVD

def eq(VB):
    return CLmax*rho/2/wingloading*VB**2 - kg*rho*CLalpha*gustVB/2/wingloading*VB-1

VB=sp.fsolve(eq,Vcruise)[0]
deltanVB = kg*rho*VB*CLalpha*gustVB/2/wingloading
ngustVBpos = 1 + deltanVB
ngustVBneg = 1 - deltanVB



plt.plot(speedpos[0:len(nposlist)],nposlist)
plt.plot(speedneg[0:len(nneglist)],nneglist)
plt.plot(speednposmax,nposmaxlist)
plt.plot(speednnegmax,nnegmaxlist)
plt.plot(speednnegdive,nnegdivelist)
plt.plot(speedmaxlist,nspeedmaxlist)
plt.plot([0, VD], [1, 1], linestyle='--', color='black', linewidth = 1, label='Horizontal Line')
plt.plot([Vstall,Vstall],[0,1],linestyle='--', color='black',linewidth=1)
plt.plot([VA,VA],[0,nposmax],linestyle='--', color='black',linewidth=1)
plt.plot([Vcruise,Vcruise],[0,nnegmax],linestyle='--', color='black',linewidth=1)
plt.plot([0,VB],[1,ngustVBpos])
plt.plot([0,VB],[1,ngustVBneg])
plt.plot([0,Vcruise],[1,ngustcruisepos])
plt.plot([0,Vcruise],[1,ngustcruiseneg])
plt.plot([0,VD],[1,ngustVDpos])
plt.plot([0,VD],[1,ngustVDneg])
plt.axhline(0, linewidth=0.5,color='black')
plt.xlim(0)
plt.show()
