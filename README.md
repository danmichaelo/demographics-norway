# Demographics of Norway

Python scripts for generating a few plots using data from Statistics Norway.

## Population graph and annual growth

- Run `python 'Population graphs.py'` to generate `plots/Population graph for Norway.svg`
  and `plots/Annual population growth of Norway.svg`.
- Data source: [SSB table 05803](https://www.ssb.no/statistikkbanken/selectvarval/Define.asp?subjectcode=&ProductId=&MainTable=FolkHistorie&nvl=&PLanguage=1&nyTmpVar=true&CMSSubjectArea=befolkning&KortNavnWeb=folkemengde&StatVariant=&checked=true) "Population 1 January and population changes during the calendar year".
	- Contents: Select the fields "Population", "Livebirths, total", "Death, total", "In-migration", "Emigration" and "Population increase, absolute figures".
	- Year: Select all.
	- Export as "semi-colon delimited" and save as `table05803.csv`


## Population pyramid

- Run `python 'Population pyramid.py'` to generate `plots/Population pyramid Norway.svg`.
- Data source: [SSB table 10211](https://www.ssb.no/statistikkbanken/SelectVarVal/Define.asp?subjectcode=al&ProductId=al&MainTable=FolkemEttAarig&SubTable=1&PLanguage=0&nvl=True&Qid=2026663&gruppe1=Hele&gruppe2=Hele&gruppe3=Hele&VS1=AlleAldre00B&VS2=Kjonn3&VS3=&mt=0&KortNavnWeb=folkemengde&CMSSubjectArea=befolkning&StatVariant=&checked=true) "Population, by sex and age".
	- "Age": select all
	- "Sex": select "Males" and "Females"
	- "Year": select all years (or just the latest)
	- Export as "Matrix (.TSV)" and save as `data/table10211.tsv`

