#encoding=utf8

import matplotlib
matplotlib.use('svg')

from matplotlib import rc
rc('lines', linewidth=0.5)
rc('font', family='sans-serif', size=12)
rc('axes', labelsize=12)
rc('xtick', labelsize=10)
rc('ytick', labelsize=10)

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import csv

golden_mean = (np.sqrt(5)-1.0)/2.0
inches_per_cm = 1.0/2.54
fig_width = 10 * inches_per_cm
fig_height = golden_mean * fig_width

###############################################################################
# Read data
csvfile = open('data/table05803.csv', 'rb')
dialect = csv.Sniffer().sniff(csvfile.read(1024))
csvfile.seek(0)
reader = csv.reader(csvfile, dialect)

data = {}

for row in reader:
    if len(row) > 3:
        header = 'Year' if row[0] == ' ' else row[0]
        data[header] = []
        for col in row[1:]:
            try:
                data[header].append(int(col))
            except:
                data[header].append(None)

df = pd.DataFrame(data)

###############################################################################
# Plot: Population graph for Norway.svg

fig = plt.figure(figsize = [fig_width, fig_height])
ax = fig.add_subplot(111)
ax.plot(df['Year'], df['Population'] / 1.e6, '-', linewidth=1.4, color='r')
ax.set_xlim(1734, 2020)
ax.set_ylim(0.4, 5.5)
ax.minorticks_on()
ax.grid('on', linestyle='-', color='#dddddd', which='both')
ax.set_yticks(np.arange(0.5, 5.6, 0.5))
ax.set_yticks(np.arange(0.5, 5.6, 0.25), minor=True)
ax.set_axisbelow(True)
fig.subplots_adjust(left=0.1, bottom=0.1, right=0.95, top=0.93)

fig.savefig('plots/Population graph for Norway.svg')

###############################################################################
# Plot: Annual population growth of Norway.svg

start_x = 1951 - 1735
end_x = df.Year.max()
df_sel = df[np.logical_and(df.Year >= start_x, df.Year < end_x)]

year = df_sel['Year']
nat_growth = (df_sel['Livebirths, total'] - df_sel['Death, total']) / 1.e3
immi_growth = (df_sel['In-migration'] - df_sel['Emigration']) / 1.e3

fig = plt.figure(figsize = [fig_width, fig_height])
ax = fig.add_subplot(111)
ax.fill_between(np.array(year.values, dtype=np.int64), 0.0, nat_growth.values, color='#FFA500', alpha=0.5)
ax.plot(year, nat_growth, color='#FFA500', linewidth=2.0)
ax.fill_between(year, nat_growth, nat_growth + immi_growth, color='#4DBD33', alpha=0.5)
ax.plot(year, nat_growth + immi_growth, color='#4DBD33', linewidth=2.0)
ax.grid('on',linestyle='-', color='#dddddd',which='both')
ax.set_xlim(1951, 2013)
ax.set_ylim(0, 70)

fig.savefig(u'plots/Annual population growth of Norway.svg')

