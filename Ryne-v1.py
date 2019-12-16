#!/usr/bin/env python
# coding: utf-8

# In[105]:


import numpy as np
import matplotlib.pyplot as plt
import os
import glob
get_ipython().run_line_magic('matplotlib', 'inline')

from readTRC import *


# In[106]:


cd /Users/xryne/Desktop/Python/time_constant_waveforms


# In[107]:


Folders=os.listdir()
if '.DS_Store' in Folders: Folders.remove('.DS_Store')
Folders


# In[108]:


files = glob.glob(Folders[0]+'/*.trc')
files.sort()
files[0]


# In[109]:


files1 = glob.glob(Folders[1]+'/*.trc')
files1.sort()
files1[0]


# In[110]:


files2 = glob.glob(Folders[2]+'/*.trc')
files2.sort()
files2[0]


# In[112]:


files3 = glob.glob(Folders[3]+'/*.trc')
files3.sort()
files3[0]


# In[113]:


files4 = glob.glob(Folders[4]+'/*.trc')
files4.sort()
files4[0]


# In[ ]:





# In[114]:


datX, datY, info = readTrc(files[0])


# In[115]:


datX1, datY1, info1 = readTrc(files1[0])


# In[116]:


datX2, datY2, info2 = readTrc(files2[0])


# In[117]:


datX3, datY3, info3 = readTrc(files3[0])


# In[118]:


datX4, datY4, info4 = readTrc(files4[0])


# In[119]:


plt.plot(datX,datY)


# In[120]:


plt.plot(datX1,datY1)


# In[121]:


plt.plot(datX2,datY2)


# In[122]:


plt.plot(datX3,datY3)


# In[123]:


plt.plot(datX4,datY4)


# In[124]:


len(datY)


# In[125]:


Length = len(files)
Xavg = np.zeros(2502)
Yavg = np.zeros(2502)
for Q in range(0,Length):
    datX, datY, info = readTrc(files[Q])
    Xavg += datX
    Yavg += datY
Xavg = Xavg/Length
Yavg = Yavg/Length


# In[126]:


Length1 = len(files1)
Xavg1 = np.zeros(2502)
Yavg1 = np.zeros(2502)
for Q in range(0,Length1):
    datX1, datY1, info1 = readTrc(files[Q])
    Xavg1 += datX1
    Yavg1 += datY1
Xavg1 = Xavg1/Length1
Yavg1 = Yavg1/Length1


# In[127]:


Length2 = len(files2)
Xavg2 = np.zeros(2502)
Yavg2 = np.zeros(2502)
for Q in range(0,Length2):
    datX2, datY2, info2 = readTrc(files2[Q])
    Xavg2 += datX2
    Yavg2 += datY2
Xavg2 = Xavg2/Length2
Yavg2 = Yavg2/Length2


# In[128]:


Length3 = len(files3)
Xavg3 = np.zeros(2502)
Yavg3 = np.zeros(2502)
for Q in range(0,Length3):
    datX3, datY3, info3 = readTrc(files3[Q])
    Xavg3 += datX3
    Yavg3 += datY3
Xavg3 = Xavg3/Length3
Yavg3 = Yavg3/Length3


# In[129]:


Length4 = len(files4)
Xavg4 = np.zeros(2502)
Yavg4 = np.zeros(2502)
for Q in range(0,Length4):
    datX4, datY4, info4 = readTrc(files4[Q])
    Xavg4 += datX4
    Yavg4 += datY4
Xavg4 = Xavg4/Length4
Yavg4 = Yavg4/Length4


# In[163]:


plt.figure(figsize=(10,7))

f, ax = plt.subplots(1)

ax.plot(Xavg*1e6,Yavg*1e3,color='k',linewidth=1,alpha=0.5)
ax.plot(Xavg1*1e6,Yavg1*1e3,color='b',linewidth=2,alpha=0.5)
ax.plot(Xavg2*1e6,Yavg2*1e3,color='r',linewidth=3,alpha=0.5)
ax.plot(Xavg3*1e6,Yavg3*1e3,color='g',linewidth=1,alpha=0.5)
ax.plot(Xavg4*1e6,Yavg4*1e3,color='c',linewidth=1,alpha=0.5)


plt.title('Average Waveforms', fontsize=20)

plt.xlabel('Time ($\mu$s)',fontsize=10)
plt.ylabel('Voltage (mV)',fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.ylim(-22,2)
plt.xlim(-1,2)

ax.legend(('Ar 1.0 - 10psi', 'Ar 1.0 - 20psi', 'Ar 0.97 Xe 0.03 - 10psi', 'Ar 0.97 Xe 0.03 - 20psi', 'Vacuum'), loc= 'lower right')

plt.savefig('Waveforms.pdf')

plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[32]:


# for looking at later

dataX=[]
dataY=[]
XTraces=dict()
YTraces=dict()
volt = dict()
time = dict()
for z in range(0,len(files)):
    dataX=[]
    dataY=[]
    Files = os.listdir(files[z])
    for x in range(0,len(Files)):
        datX, datY, info = readTrc(paths[z]+"/"+Files[x])
        NTraces     =   info['SUBARRAY_COUNT']
        TotalPoints =   info[ 'WAVE_ARRAY_COUNT']
        dx          =   info['HORIZ_INTERVAL']
        PPT         =   TotalPoints/NTraces
        YTraces[x]   =   np.split(datY, NTraces)
        XTraces[x]   =   np.split(datX, NTraces)
        for y in range(0,len(YTraces[x])):
            dataX.append(XTraces[x][y])
            dataY.append(YTraces[x][y])
    volt[z] = np.array(dataY)
    time[z] = np.array(dataX)


# In[ ]:





# In[29]:


mu = 1e6
ml = 1e3
unit=  r"$\frac{V}{cm}$"
plt.figure(figsize=(15,9))
for x in range(0,len(files)):
    plt.plot(Time[x]*ml,Volt[x]*ml,label=str(Efield[x]) + unit,color=cm.afmhot((x+2)/17))

#plt.text(325, -10, r'750 Torr', fontsize=30)
#plt.text(25, 10, r'RC=10$\mu$s', fontsize=30)
plt.title('BTX ION drift 5-24-17 ',fontsize=30)
plt.xlim(0,170)
plt.ylim(-0.8,0)
plt.xlabel(r'Time / ms',fontsize=26)
plt.ylabel('Voltaeg / mV',fontsize=26)
plt.xticks(fontsize=24)
plt.yticks(fontsize=24)
#plt.xticks(np.arange(0, 400, 50.0))
plt.grid()
plt.legend(loc='upper right',fontsize=25)
plt.tight_layout()
plt.savefig('Ar100%_10psi.pdf')

plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




