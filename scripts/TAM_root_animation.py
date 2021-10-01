import numpy as np
#import pandas as pd
from netCDF4 import Dataset

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FFMpegWriter, PillowWriter
#from mpl_toolkits.axes_grid1 import make_axes_locatable

# data
df_3R_ovr = Dataset('3R_default_output.nc','r') #3-pool TAM structure with vertically resolved root mass(_ovr)

# figure
fig,(ax1,ax2) = plt.subplots(1, 2,figsize=(15,8))
plt.subplots_adjust(wspace=0.3)


frootc_pft_df_ovr_m_t1 = df_3R_ovr.variables['frootctam_pft_vr'][0].squeeze()[0,:,0]
frootc_pft_df_ovr_a_t1 = df_3R_ovr.variables['frootctam_pft_vr'][0].squeeze()[1,:,0]
frootc_pft_df_ovr_t_t1 = df_3R_ovr.variables['frootctam_pft_vr'][0].squeeze()[2,:,0]


ax1.set_title('Evergreen (Day 0)',size=14)
ax1.grid()
ax1.set_xlabel('Biomass',size=14,weight='heavy')
ax1.xaxis.set_label_position('top')
ax1.tick_params('both',labelsize=14,top=True,labeltop=True,bottom=False,labelbottom=False,grid_linestyle='--')
ax1.set_xlim(0,30)

ax1.set_ylabel('Layer',size=14,weight='heavy')
ax1.set_ylim(-9,0)
ax1.yaxis.set_ticks(np.arange(0,-10,-1))
labels=[item.get_text() for item in ax1.get_yticklabels()]
labels= [i for i in range(1,11)]
ax1.set_yticklabels(labels)

ax1.plot(frootc_pft_df_ovr_m_t1, np.arange(0,-10,-1),color='blue')
ax1.plot(frootc_pft_df_ovr_a_t1, np.arange(0,-10,-1),color='orange')
ax1.plot(frootc_pft_df_ovr_t_t1, np.arange(0,-10,-1),color='red')


frootc_pft_df_ovr_m_t2 = df_3R_ovr.variables['frootctam_pft_vr'][1].squeeze()[0,:,0]
frootc_pft_df_ovr_a_t2 = df_3R_ovr.variables['frootctam_pft_vr'][1].squeeze()[1,:,0]
frootc_pft_df_ovr_t_t2 = df_3R_ovr.variables['frootctam_pft_vr'][1].squeeze()[2,:,0]

ax2.set_title('Deciduous (Day 0)',size=14)
ax2.grid()
ax2.set_xlabel('Biomass',size=14,weight='heavy')
ax2.xaxis.set_label_position('top')
ax2.tick_params('both',labelsize=14,top=True,labeltop=True,bottom=False,labelbottom=False,grid_linestyle='--')
ax2.set_xlim(0,15)

ax2.set_ylabel('Layer',size=14,weight='heavy')
ax2.set_ylim(-9,0)
ax2.yaxis.set_ticks(np.arange(0,-10,-1))
labels=[item.get_text() for item in ax2.get_yticklabels()]
labels= [i for i in range(1,11)]
ax2.set_yticklabels(labels)

ax2.plot(frootc_pft_df_ovr_m_t2, np.arange(0,-10,-1),color='blue')
ax2.plot(frootc_pft_df_ovr_a_t2, np.arange(0,-10,-1),color='orange')
ax2.plot(frootc_pft_df_ovr_t_t2, np.arange(0,-10,-1),color='red')

def animate(i):
    frootc_pft_df_ovr_m_t1 = df_3R_ovr.variables['frootctam_pft_vr'][0].squeeze()[0,:,i*1]
    frootc_pft_df_ovr_a_t1 = df_3R_ovr.variables['frootctam_pft_vr'][0].squeeze()[1,:,i*1]
    frootc_pft_df_ovr_t_t1 = df_3R_ovr.variables['frootctam_pft_vr'][0].squeeze()[2,:,i*1]
    
    ax1.clear()

    ax1.set_title('Evergreen (Day {0})'.format(1*i))
    ax1.grid()
    ax1.set_xlabel('Biomass',size=14,weight='heavy')
    ax1.xaxis.set_label_position('top')
    ax1.tick_params('both',labelsize=14,top=True,labeltop=True,bottom=False,labelbottom=False,grid_linestyle='--')
    ax1.set_xlim(0,30)

    ax1.set_ylabel('Layer',size=14,weight='heavy')
    ax1.set_ylim(-9,0)
    ax1.yaxis.set_ticks(np.arange(0,-10,-1))
    labels=[item.get_text() for item in ax1.get_yticklabels()]
    labels= [i for i in range(1,11)]
    ax1.set_yticklabels(labels)

    ax1.plot(frootc_pft_df_ovr_m_t1, np.arange(0,-10,-1),color='blue')
    ax1.plot(frootc_pft_df_ovr_a_t1, np.arange(0,-10,-1),color='orange')
    ax1.plot(frootc_pft_df_ovr_t_t1, np.arange(0,-10,-1),color='red')
    
    ################################################################

    frootc_pft_df_ovr_m_t2 = df_3R_ovr.variables['frootctam_pft_vr'][1].squeeze()[0,:,i*1]
    frootc_pft_df_ovr_a_t2 = df_3R_ovr.variables['frootctam_pft_vr'][1].squeeze()[1,:,i*1]
    frootc_pft_df_ovr_t_t2 = df_3R_ovr.variables['frootctam_pft_vr'][1].squeeze()[2,:,i*1]

    ax2.clear()

    ax2.set_title('Deciduous (Day {0})'.format(1*i))
    ax2.grid()
    ax2.set_xlabel('Biomass',size=14,weight='heavy')
    ax2.xaxis.set_label_position('top')
    ax2.tick_params('both',labelsize=14,top=True,labeltop=True,bottom=False,labelbottom=False,grid_linestyle='--')
    ax2.set_xlim(0,15)

    ax2.set_ylabel('Layer',size=14,weight='heavy')
    ax2.set_ylim(-9,0)
    ax2.yaxis.set_ticks(np.arange(0,-10,-1))
    labels=[item.get_text() for item in ax2.get_yticklabels()]
    labels= [i for i in range(1,11)]
    ax2.set_yticklabels(labels)
    ax2.plot(frootc_pft_df_ovr_m_t2, np.arange(0,-10,-1),color='blue')
    ax2.plot(frootc_pft_df_ovr_a_t2, np.arange(0,-10,-1),color='orange')
    ax2.plot(frootc_pft_df_ovr_t_t2, np.arange(0,-10,-1),color='red')
    

ani = animation.FuncAnimation(fig, animate, frames=365,repeat=False)


writer = PillowWriter(fps=8)

ani.save('TAM_root.gif',writer=writer)