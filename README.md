# Demographics of Norway

Python scripts for generating a few plots for https://commons.wikimedia.org/wiki/Category:Demographics_of_Norway using data from Statistics Norway.

## Population graph and annual growth

- Run `python 'Population graphs.py'` to generate `plots/Population graph for Norway.svg`
  and `plots/Annual population growth of Norway.svg`.
- Data source: [SSB table 05803](https://www.ssb.no/en/table/05803) "Population 1 January and population changes during the calendar year".
	- Contents: Select the fields "Population", "Livebirths, total", "Death, total", "In-migration", "Emigration" and "Population increase, absolute figures".
	- Year: Select all.
	- Export as "semi-colon delimited" and save as `table05803.csv`


## Population pyramid

- Run `python 'Population pyramid.py'` to generate `plots/Population pyramid Norway.svg`.
- Data source: [SSB table 10211](https://www.ssb.no/en/table/01222) "Population, by sex and age".
	- "Age": select all
	- "Sex": select "Males" and "Females"
	- "Year": select all years (or just the latest)
	- Export as "Matrix (.TSV)" and save as `data/table10211.tsv`

