import os, csv
import pandas
# ==============================================================
todays_date = '20220809'


# =============================================================

pNotes = '../../R/dataAFMrm/csv/NotesForRM20220701GL0XXSeries.csv'

data = pandas.read_csv(pNotes)
print(data.loc[:, "Sample"])

pRAW = os.listdir('RAW')


print(pRAW)