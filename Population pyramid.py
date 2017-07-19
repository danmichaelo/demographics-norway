#encoding=utf8
import csv
import matplotlib
from matplotlib import rc
matplotlib.use('svg')
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

YEAR = 2017


def prepare_canvas(width=350.0, fontsize=12, fontsize_small=10, lw=0.5):
    """
    Prepares a figure with specified width <width> and height
    calculated according to the golden mean ratio.

    Arguments:
       - width : float specifying the width in points, or string holding a value and its unit separated by space.
                 Valid units are 'cm', 'pt', 'in'

    Example:
        prepare_canvas(width='7.2 cm')
    """
    try:
        width = width.split()
        width_value = float(width[0])
        width_units = width[1]
    except AttributeError:
        width_value = float(width)
        width_units = 'pt'  # assume points

    inches_per_pt = 1.0/72.27 # According to TeX
    inches_per_cm = 1.0/2.54  #
    if width_units == 'pt':
        fig_width = width_value * inches_per_pt
    elif width_units == 'cm':
        fig_width = width_value * inches_per_cm
    elif width_units == 'in':
        fig_width = width_value

    golden_mean = (np.sqrt(5)-1.0)/2.0      # Aesthetic ratio
    fig_height = 0.9*fig_width      # height in inches
    fig_size = [fig_width,fig_height]

    rc('figure', figsize=fig_size)
    rc('lines', linewidth=lw)
    rc('font', family='sans-serif', serif=['Latin Modern Roman','Palatino'], size=fontsize)
    rc('text', usetex=False)
    rc('legend', fontsize=fontsize)
    rc('axes', labelsize=fontsize)
    rc('xtick', labelsize=fontsize_small)
    rc('ytick', labelsize=fontsize_small)


def read_tsv(filename):
    tmp = []
    with open(filename,'rb') as f:
        reader = csv.reader(f, delimiter='\t')
        header = reader.next()  # skip header
        dataset = []
        for row in reader:
            age = int(row[0].split(' ')[0])
            sex = 'F' if row[1] == 'Females' else 'M'
            for i in range(2, len(row)):
                npersons = int(row[i])
                year = int(header[i])
                tmp.append({
                    'age': age,
                    'sex': sex,
                    'year': year,
                    'npersons': npersons
                })

    tmp = pd.DataFrame(tmp)
    return tmp


# Prep
prepare_canvas(width = '10 cm')
ax = plt.gca()

# Get data
df = read_tsv('data/table10211.tsv')
df = df[df.year == YEAR]
women = df[df.sex == 'F']
men = df[df.sex == 'M']

# Plot
ax.barh(women.age.values, -women.npersons.values, color='#490A3D', linewidth=0, height=1.2)
ax.barh(men.age.values, men.npersons.values, color='#BD1550', linewidth=0, height=1.2)

# Style
ax.set_ylabel(u'Age in years')
ax.set_xlabel(u'Population in thousands')
plt.grid('on', linestyle='-', color='#8A9B0F', alpha=0.5)
plt.legend(('Women', 'Men'), frameon=False, loc='upper left', ncol=2, mode='expand', borderaxespad=0.)
plt.yticks(np.arange(0,105,10))
plt.xlim(-40000,40000)
plt.ylim(0,105)
plt.xticks(np.arange(-40000,40000,10000), np.abs(np.arange(-40,40,10)))
plt.subplots_adjust(left=0.16)
plt.subplots_adjust(bottom=0.15)

# Save
plt.savefig('plots/Population pyramid Norway %d.svg' % YEAR)
