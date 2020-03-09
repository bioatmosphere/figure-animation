import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FFMpegWriter, PillowWriter
from mpl_toolkits.axes_grid1 import make_axes_locatable



# data
cellulose     = pd.read_csv('data/cellulose.csv',index_col=0)
data_bacteria = pd.read_csv('data/bacteria.csv',index_col=0)
data_fungi    = pd.read_csv('data/fungi.csv',index_col=0)


# figure
fig,(ax1,ax2,ax3) = plt.subplots(1, 3,figsize=(10,5))

# bacterial taxon panel
im1 = ax1.imshow(data_bacteria.loc[:,str(10*0)].values.reshape(100,100), cmap='jet')
div1 = make_axes_locatable(ax1)                         # 
cax1 = div1.append_axes('bottom', size='7%', pad='4%')  #
cb1  = fig.colorbar(im1, cax=cax1, orientation="horizontal")
cb1.set_label('Bacterial Taxon (mg C cm$^-$$^3$)',size=12)
tx1 = ax1.set_title('Day 0')
ax1.tick_params(axis='both',left=False,bottom=False, labelleft=False, labelbottom=False)

# fungal taxon panel
im2 = ax2.imshow(data_fungi.loc[:,str(10*0)].values.reshape(100,100), cmap='jet')
div2 = make_axes_locatable(ax2)                
cax2 = div2.append_axes('bottom', size='7%', pad='4%')  
cb2  = fig.colorbar(im2, cax=cax2, orientation="horizontal")
cb2.set_label('Fungal Taxon (mg C cm$^-$$^3$)',size=12)
tx2 = ax2.set_title('Day 0')
ax2.tick_params(axis='both',left=False,bottom=False, labelleft=False, labelbottom=False)

# cellulose panel
im3 = ax3.imshow(cellulose.loc[:,str(10*0)].values.reshape(100,100), cmap='jet')
div3 = make_axes_locatable(ax3)                         # 
cax3 = div3.append_axes('bottom', size='7%', pad='4%')  #
cb3  = fig.colorbar(im3, cax=cax3, orientation="horizontal")
cb3.set_label('Cellulose (mg C cm$^-$$^3$)',size=12)
tx3 = ax3.set_title('Day 0')
ax3.tick_params(axis='both',left=False,bottom=False, labelleft=False, labelbottom=False)

# tweak margins of the final animation
fig.tight_layout()
#plt.subplots_adjust(left=0.05, right=0.95, bottom=0., top=1.0)

# animation
def animate(i):
    arr_bac = data_bacteria.loc[:,str(10*i)].values.reshape(100,100)
    im1.set_data(arr_bac)
    im1.set_clim(np.min(arr_bac), np.max(arr_bac))
    tx1.set_text('Day {0}'.format(10*i))

    arr_fun = data_fungi.loc[:,str(10*i)].values.reshape(100,100)
    im2.set_data(arr_fun)
    im2.set_clim(np.min(arr_fun), np.max(arr_fun))
    tx2.set_text('Day {0}'.format(10*i))

    arr = cellulose.loc[:,str(10*i)].values.reshape(100,100) 
    im3.set_data(arr)
    im3.set_clim(np.min(arr), np.max(arr))
    tx3.set_text('Day {0}'.format(10*i))


ani = animation.FuncAnimation(fig, animate, frames=74)

# writer for gif
writer = PillowWriter(fps=3)

# save as gif file
ani.save('DEMENTpy_animation.gif', writer = writer, dpi=1000)