import pandas as pd
from analysisFuncs import *

defaultsCsv = "Tanda Settings Info.csv"
orgSettingsCsv = "Tanda Organisation Settings.csv"

defaults = pd.read_csv(defaultsCsv)
orgSettings = pd.read_csv(orgSettingsCsv)

defaults = clean(defaults, orgSettings)

percentageSettingsChanged(defaults, orgSettings)






    

