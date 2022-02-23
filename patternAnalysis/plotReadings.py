#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np 

# Backup in another file
with open("consumption.csv") as fileToRead:
    with open("test.csv", "w") as fileToWrite:
        for line in fileToRead:
            fileToWrite.write(line)
fileToRead.close()
fileToWrite.close()


# In[2]:


# change the slash to dot for naming the files
def slash2dot(str):
    dateSplit = str.split('/')
    return(".".join(dateSplit))

# Line counter
i = 0
# Define a variable to check the date of data
startDate = ''
# Ignore the first row as it is an header
counterStart = 1
# List array variable to capture field
list = []
# List of csv files that will be created
files = []

with open("consumption.csv") as fileToRead:
    for line in fileToRead:
        i +=1
        
        # Capture the field data in the csv file 
        # split by comma
        list = line.split(',')
        
        # Create a new file as the data for preceeding date is over
        if (list[0] != startDate) & (i > counterStart):
            # First field is the date variable
            startDate = list[0]
            # New csv file with the date created
            newFile = slash2dot(startDate + '.csv')
            # Save the file name
            files.append(newFile)

        # Write the data to the file
        if i > counterStart:
            fileToWrite = open(newFile, "a")
            fileToWrite.write(line)
            fileToWrite.close()
    
    fileToRead.close()
    
print(files)


# In[3]:


# Change from time format seperator ':' to '.'
# The last time is 00:00, this has to be 
# changed to 24.00
def colons2dot(str):
    timeSplit = str.split(':')
    if ".".join(timeSplit) != '00.00':
        return(".".join(timeSplit))
    else:
        return("24.00")


# In[4]:


timeOfReading_26 = []
import110_26 = []
export110_26 = []
import33_26 = []
export33_26 = []
import25_26 = []
export25_26 = []

with open("26.11.19.csv") as fileToRead:
    for line in fileToRead:
        list = line.split(',')
        timeOfReading_26.append(float(colons2dot(list[1])))
        import110_26.append(float(list[2]))
        export110_26.append(float(list[3]))
        import33_26.append(float(list[4]))
        export33_26.append(float(list[5]))
        import25_26.append(float(list[6]))
        export25_26.append(float(list[7]))


# In[5]:


timeOfReading_27 = []
import110_27 = []
export110_27 = []
import33_27 = []
export33_27 = []
import25_27 = []
export25_27 = []

with open("27.11.19.csv") as fileToRead:
    for line in fileToRead:
        list = line.split(',')
        timeOfReading_27.append(float(colons2dot(list[1])))
        import110_27.append(float(list[2]))
        export110_27.append(float(list[3]))
        import33_27.append(float(list[4]))
        export33_27.append(float(list[5]))
        import25_27.append(float(list[6]))
        export25_27.append(float(list[7]))
        


# In[6]:


timeOfReading_28 = []
import110_28 = []
export110_28 = []
import33_28 = []
export33_28 = []
import25_28 = []
export25_28 = []

with open("28.11.19.csv") as fileToRead:
    for line in fileToRead:
        list = line.split(',')
        timeOfReading_28.append(float(colons2dot(list[1])))
        import110_28.append(float(list[2]))
        export110_28.append(float(list[3]))
        import33_28.append(float(list[4]))
        export33_28.append(float(list[5]))
        import25_28.append(float(list[6]))
        export25_28.append(float(list[7]))


# In[7]:


timeOfReading_29 = []
import110_29 = []
export110_29 = []
import33_29 = []
export33_29 = []
import25_29 = []
export25_29 = []

with open("29.11.19.csv") as fileToRead:
    for line in fileToRead:
        list = line.split(',')
        timeOfReading_29.append(float(colons2dot(list[1])))
        import110_29.append(float(list[2]))
        export110_29.append(float(list[3]))
        import33_29.append(float(list[4]))
        export33_29.append(float(list[5]))
        import25_29.append(float(list[6]))
        export25_29.append(float(list[7]))


# In[16]:


fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2, figsize=(20,50))

ax1.plot(timeOfReading_26,import110_26, label = '110 KV import')
ax1.plot(timeOfReading_26,import33_26, label = '33 KV import')
ax1.plot(timeOfReading_26,import25_26, label = '25 KV import')

ax1.grid(True)
ax1.legend(loc="upper left")
ax1.set_xticks(np.arange(0,25,2))
ax1.title.set_text('Imports on 26.11.19')
bbox = ax1.get_tightbbox(fig.canvas.get_renderer())
fig.savefig("26.import.png", bbox_inches=bbox.transformed(fig.dpi_scale_trans.inverted()))

ax2.plot(timeOfReading_26,export110_26, label = '110 KV export')
ax2.plot(timeOfReading_26,export33_26, label = '33 KV export')
ax2.plot(timeOfReading_26,export25_26, label = '25 KV export')

ax2.grid(True)
ax2.legend(loc="upper left")
ax2.set_xticks(np.arange(0,25,2))
ax2.title.set_text('Exports on 26.11.19')
bbox = ax2.get_tightbbox(fig.canvas.get_renderer())
fig.savefig("26.export.png", bbox_inches=bbox.transformed(fig.dpi_scale_trans.inverted()))

ax3.plot(timeOfReading_27,import110_27, label = '110 KV import')
ax3.plot(timeOfReading_27,import33_27, label = '33 KV import')
ax3.plot(timeOfReading_27,import25_27, label = '25 KV import')

ax3.grid(True)
ax3.legend(loc="upper left")
ax3.set_xticks(np.arange(0,25,2))
ax3.title.set_text('Imports on 27.11.19')
bbox = ax3.get_tightbbox(fig.canvas.get_renderer())
fig.savefig("27.import.png", bbox_inches=bbox.transformed(fig.dpi_scale_trans.inverted()))

ax4.plot(timeOfReading_27,export110_27, label = '110 KV export')
ax4.plot(timeOfReading_27,export33_27, label = '33 KV export')
ax4.plot(timeOfReading_27,export25_27, label = '25 KV export')

ax4.grid(True)
ax4.legend(loc="upper left")
ax4.set_xticks(np.arange(0,25,2))
ax4.title.set_text('Exports on 27.11.19')
bbox = ax4.get_tightbbox(fig.canvas.get_renderer())
fig.savefig("27.export.png", bbox_inches=bbox.transformed(fig.dpi_scale_trans.inverted()))

ax5.plot(timeOfReading_28,import110_28, label = '110 KV import')
ax5.plot(timeOfReading_28,import33_28, label = '33 KV import')
ax5.plot(timeOfReading_28,import25_28, label = '25 KV import')

ax5.grid(True)
ax5.legend(loc="upper left")
ax5.set_xticks(np.arange(0,25,2))
ax5.title.set_text('Imports on 28.11.19')
bbox = ax5.get_tightbbox(fig.canvas.get_renderer())
fig.savefig("28.import.png", bbox_inches=bbox.transformed(fig.dpi_scale_trans.inverted()))

ax6.plot(timeOfReading_28,export110_28, label = '110 KV export')
ax6.plot(timeOfReading_28,export33_28, label = '33 KV export')
ax6.plot(timeOfReading_28,export25_28, label = '25 KV export')
ax6.title.set_text('Exports on 28.11.19')

ax6.grid(True)
ax6.legend(loc="upper left")
ax6.set_xticks(np.arange(0,25,2))
bbox = ax6.get_tightbbox(fig.canvas.get_renderer())
fig.savefig("28.export.png", bbox_inches=bbox.transformed(fig.dpi_scale_trans.inverted()))

ax7.plot(timeOfReading_29,import110_29, label = '110 KV import')
ax7.plot(timeOfReading_29,import33_29, label = '33 KV import')
ax7.plot(timeOfReading_29,import25_29, label = '25 KV import')

ax7.grid(True)
ax7.legend(loc="upper left")
ax7.set_xticks(np.arange(0,25,2))
ax7.title.set_text('Imports on 29.11.19')
bbox = ax7.get_tightbbox(fig.canvas.get_renderer())
fig.savefig("29.import.png", bbox_inches=bbox.transformed(fig.dpi_scale_trans.inverted()))

ax8.plot(timeOfReading_29,export110_29, label = '110 KV export')
ax8.plot(timeOfReading_29,export33_29, label = '33 KV export')
ax8.plot(timeOfReading_29,export25_29, label = '25 KV export')

ax8.grid(True)
ax8.legend(loc="upper left")
ax8.set_xticks(np.arange(0,25,2))
ax8.title.set_text('Exports on 29.11.19')
bbox = ax8.get_tightbbox(fig.canvas.get_renderer())
fig.savefig("29.export.png", bbox_inches=bbox.transformed(fig.dpi_scale_trans.inverted()))

plt.show()


# In[28]:


fig, (ax1, ax3, ax5) = plt.subplots(3,1, figsize=(20,20))
fig.subplots_adjust(right=0.75)

ax2 = ax1.twinx()

ax1.plot(timeOfReading_26,import110_26, color='r', label = '110 KV import')

ax2.plot(timeOfReading_26,export110_26, label = '110 KV export')


ax1.grid(True)
ax1.legend(loc="upper center")
ax2.legend(loc="upper left")
ax1.set_xticks(np.arange(0,25,2))
ax1.title.set_text('110 KV Import/Export on 26.11.19')
bbox = ax1.get_tightbbox(fig.canvas.get_renderer())
fig.savefig("26.110.import.export.png", bbox_inches=bbox.transformed(fig.dpi_scale_trans.inverted()))

ax4 = ax3.twinx()

ax3.plot(timeOfReading_26,import33_26, color='r', label = '33 KV import')

ax4.plot(timeOfReading_26,export33_26, label = '33 KV export')


ax3.grid(True)
ax3.legend(loc="upper center")
ax4.legend(loc="upper left")
ax3.set_xticks(np.arange(0,25,2))
ax3.title.set_text('33 KV Import/Export on 26.11.19')
bbox = ax3.get_tightbbox(fig.canvas.get_renderer())
fig.savefig("26.33.import.export.png", bbox_inches=bbox.transformed(fig.dpi_scale_trans.inverted()))

ax6 = ax5.twinx()

ax5.plot(timeOfReading_26,import25_26, color='r', label = '25 KV import')

ax6.plot(timeOfReading_26,export25_26, label = '25 KV export')


ax5.grid(True)
ax5.legend(loc="upper center")
ax6.legend(loc="upper left")
ax5.set_xticks(np.arange(0,25,2))
ax5.title.set_text('25 KV Import/Export on 26.11.19')
bbox = ax5.get_tightbbox(fig.canvas.get_renderer())
fig.savefig("26.25.import.export.png", bbox_inches=bbox.transformed(fig.dpi_scale_trans.inverted()))


# In[ ]:




