import matplotlib.pyplot as plt
import numpy as np

def cm2inch(value):
    return value/2.54


# number of slides
nslides=9

# color of the ring; RGBA tuple
ring_color = (0.,94./255.,168./255.,1.)

# background color of the ring; RGBA tuple; A=0. -> transparent
ring_back_color = (1.,1.,1.,0.)

# color of the ring conture; RGBA tuple
ring_edge_color = ring_back_color

# background color of the number; RGBA tuple; A=0. -> transparent
numb_back_color = (1.,1.,1.,1.)

# color of the numbers, RGB tuple
numb_color = (0.,94./255.,168./255.)

# width of the ring; < 1.
size = 0.3

# filetyp; png or pdf, pdf looks better in ppt
of_type="png"


# nslides loop
for n in range(1,nslides+1):
    vals = np.array([nslides-n,n])

    snum=str(n)
    if n<10:
        snum='0'+str(n)

    # open fig
    fig, ax = plt.subplots(figsize=(cm2inch(2.),cm2inch(2.)))

    # define colors
    cmap = plt.get_cmap("bwr")
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list(name='mycmap',colors =[ring_back_color, ring_color], N=60)
    outer_colors = cmap(np.array([0, 59]))

    # plot ring chart
    ax.pie(vals, radius=1-size, colors=[numb_back_color])
    ax.pie(vals, radius=1, colors=outer_colors,
           wedgeprops=dict(width=size, edgecolor=ring_edge_color))

    # plot number
    x_pad = -.4
    if n > 99:
        x_pad = -.65
    plt.text(x_pad, -.25, snum, fontsize=12,color=numb_color)
    ax.set(aspect="equal")

    # save figure
    plt.savefig(str(n)+'.'+of_type, transparent=True)

    # close figure
    plt.close()

print('done')
