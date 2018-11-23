from Tkinter import Tk

def MakeIss(MyAppConfig, BuildNum, FileSource):

    ApptoIss = open(FileSource + "//" + MyAppConfig + ".iss", 'a')
    ApptoIss.write('#define MyAppName "Maintenance Installer" \n')
    ApptoIss.write('#define MyAppPublisher "Inovatech Engineering Corporation"\n')
    ApptoIss.write('#define MyAppPublisher "Inovatech Engineering Corporation"\n')
    ApptoIss.write('#define MyAppURL "https://inovatechengineering.com/"\n')
    ApptoIss.write('#define MyAppExeName "SPM.exe"\n')
    ApptoIss.write('#define MyAppConfig "' + MyAppConfig + '"\n')
    ApptoIss.write('#define BuildNum "'+ str(BuildNum) + '"\n')
    ApptoIss.write('\n')

    ApptoIss.write('\n')
    ApptoIss.write('\n')

    ApptoIss.write('[Setup]\n')
    ApptoIss.write('AppId={{CA91F52A-8196-45DF-8675-23B9FEBE3EBD}\n')
    ApptoIss.write('AppName={#MyAppName}\n')
    ApptoIss.write('AppVersion={#BuildNum}\n')
    ApptoIss.write('AppVerName={#MyAppName} {#BuildNum}\n')
    ApptoIss.write('AppPublisher={#MyAppPublisher}\n')
    ApptoIss.write('AppPublisherURL={#MyAppURL}\n')
    ApptoIss.write('AppSupportURL={#MyAppURL}\n')
    ApptoIss.write('AppUpdatesURL={#MyAppURL}\n')
    ApptoIss.write('CreateAppDir=no\n')
    ApptoIss.write('OutputDir="' + FileSource + '"\n')
    ApptoIss.write('OutputBaseFilename=SPM{#MyAppConfig}_R{#BuildNum}\n')
    ApptoIss.write('Compression=lzma\n')
    ApptoIss.write('SolidCompression=yes\n')

    ApptoIss.write('\n')
    ApptoIss.write('\n')

    ApptoIss.write('[Languages]\n')
    ApptoIss.write('Name: "english"; MessagesFile: "compiler:Default.isl"\n')
    ApptoIss.write('\n')
    ApptoIss.write('\n')


    ApptoIss.write('[InstallDelete]\n')
    ApptoIss.write(r'Type: filesandordirs; Name: "C:\ProgramData\Inovatech Engineering Corp\SteelPRO Director\Documentation\Maintenance\en-US";')
    ApptoIss.write('\n')
    ApptoIss.write(r'Type: files; Name: "C:\ProgramData\Inovatech Engineering Corp\SteelPRO Director\Settings\Maintenance\Maintenance.xml"')
    ApptoIss.write('\n')
    ApptoIss.write(r'Type: files; Name: "C:\ProgramData\Inovatech Engineering Corp\SteelPRO Director\Settings\Maintenance\Scheduled.xml"')
    ApptoIss.write('\n')


    ApptoIss.write('\n')
    ApptoIss.write('\n')

    ApptoIss.write('[Files]\n')
    ApptoIss.write('Source: "'+ FileSource +'//en-US//*"; DestDir: "C://ProgramData//Inovatech Engineering Corp//SteelPRO Director//Documentation//Maintenance//en-US"; Flags: ignoreversion recursesubdirs createallsubdirs\n')
    ApptoIss.write('Source: "'+ FileSource +'//Maintenance.xml"; DestDir: "C://ProgramData//Inovatech Engineering Corp//SteelPRO Director//Settings//Maintenance"; Flags: ignoreversion\n')
    ApptoIss.write('\n')
