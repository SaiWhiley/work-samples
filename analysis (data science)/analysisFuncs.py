# takes a dataframe direct from csv, returns list of settings.
# made for Settings Info.csv, looks at column headers
def getSettings(inputDF):  
    settingsDF = inputDF['setting']
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


#checks for data present in defaults not included in orgSettings, removes culpabale variable 
def clean(defaultsDF, orgSettingsDF):
    listOfSettings = getSettings(defaultsDF)
    for setting in range(len(listOfSettings)):
        if(listOfSettings[setting] in list(orgSettingsDF)):
            continue
        else:
            print("Setting missing in orgSettings:" + listOfSettings[setting] + ", row dropped from defaults")
            defaultsDF = defaultsDF[defaultsDF.setting != listOfSettings[setting]]