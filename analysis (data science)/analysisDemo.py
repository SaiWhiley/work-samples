import pandas as pd

defaultsCsv = "Tanda Settings Info.csv"
orgSettingsCsv = "Tanda Organisation Settings.csv"

defaults = pd.read_csv(defaultsCsv)
orgSettings = pd.read_csv(orgSettingsCsv)

def getSettings():
    settingsDF = defaults['setting']
    settings = []
    for row in range(settingsDF.values.size):
        if(settingsDF.values[row] in settings):
            continue
        else:
            settings.append(settingsDF.values[row])
    return settings


def countPercentageSettingsChanged():
    settingsList = getSettings()
    for row in range(len(settingsList)):
        modifiers = 0
        currentSetting = settingsList[row]
        for user in range(len(orgSettings.index)):
            if(settingsList[row] in list(orgSettings)):
                print(settingsList[row])
                print(list(orgSettings)[row])
                if(defaults[' default'][row] == orgSettings[str(currentSetting)][user]):
                    print(defaults[' default'][row] + ' ' + orgSettings[str(currentSetting)][user])



def clean():
    settings = getSettings() # gets list of settings
    for col in range(len(list(orgSettings))):
        if(settings[col] in list(orgSettings)):
            continue
        else:
            defaults[defaults.setting != settings[col]]
            print('Missing setting:' + settings[col] + ' setting deleted from defaults dataframe')
            print(defaults)
    return defaults


print(len(list(orgSettings)))



    

