import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FFMpegWriter, PillowWriter
from mpl_toolkits.axes_grid1 import make_axes_locatable


# data
data_bacteria = pd.read_csv('data/bacteria.csv',index_col=0)
data_fungi    = pd.read_csv('data/fungi.csv',index_col=0)


# figure
fig,(ax1,ax2) = plt.subplots(1, 2,figsize=(10,5))

im1 = ax1.imshow(data_bacteria.loc[:,str(10*0)].values.reshape(100,100), cmap='jet')
div1 = make_axes_locatable(ax1)                         # https://matplotlib.org/3.1.1/gallery/axes_grid1/demo_colorbar_with_axes_divider.html
cax1 = div1.append_axes('bottom', size='7%', pad='4%')  #
cb1  = fig.colorbar(im1, cax=cax1, orientation="horizontal")
cb1.set_label('Bacterial Taxon (mg C cm$^-$$^3$)',size=12)
tx1 = ax1.set_title('Day 0')
ax1.tick_params(axis='both',left=False,bottom=False, labelleft=False, labelbottom=False)


im2 = ax2.imshow(data_fungi.loc[:,str(10*0)].values.reshape(100,100), cmap='jet')
div2 = make_axes_locatable(ax2)                # https://matplotlib.org/3.1.1/gallery/axes_grid1/demo_colorbar_with_axes_divider.html
cax2 = div2.append_axes('bottom', size='7%', pad='4%')  #
cb2  = fig.colorbar(im2, cax=cax2, orientation="horizontal")
cb2.set_label('Fungal Taxon (mg C cm$^-$$^3$)',size=12)
tx2 = ax2.set_title('Day 0')
ax2.tick_params(axis='both',left=False,bottom=False, labelleft=False, labelbottom=False)

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

    # In this version you don't have to do anything to the colorbar,
    # it updates itself when the mappable it watches (im) changes

ani = animation.FuncAnimation(fig, animate, frames=74)


# writer for .mp4
#writer = FFMpegWriter(fps=20, metadata=dict(artist='Me'), bitrate=1800)

# writer for gif
writer = PillowWriter(fps=3)

# save as gif file
ani.save('microbes.gif', writer = writer, dpi=1000)