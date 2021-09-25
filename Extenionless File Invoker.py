import magic
import sys
import subprocess
import shlex
import winreg

#File Dictionary to get File extensions based on Magic library output
fileextdict = {
 "jpegimagedata": ".jpeg",
 "pngimagedata": ".png",
 "gifimagedata": ".gif",
 "utf-8unicode(withbom)text": ".csv",
 "excel":".xls",
 "microsoftword":".doc",
 "microsoftexcel2007+": ".xlsx",
 "microsoftword2007+": ".docx",
 "microsoftpowerpoint2007+":".ppt",
 "opendocumenttext": ".odt",
 "pdfdocument": ".pdf",
 "richtextformatdata": ".rtf",
 "pythonscript": ".py",
 "asciitext": ".txt",
 "7-ziparchivedata": ".7z",
 "ziparchivedata": ".zip",
 "rararchivedata": ".rar",
 "windowsimaging(wim)image": ".wim",
 "mpegadts": ".aac",
 "audiofilewithid3version2.3.0":".mp3",
 "audiofilewithid3version2.4.0":".mp3",
 "isomedia":".mp4",
 "matroskadata":".mkv",
 "mpegtransportstreamdata":".ts",
}

#To get the default application path based on the extension passed as suffix
# Code refrence https://stackoverflow.com/questions/48051864/how-to-get-the-default-application-mapped-to-a-file-extention-in-windows-using-p
def get_default_windows_app(suffix):
    class_root = winreg.QueryValue(winreg.HKEY_CLASSES_ROOT, suffix)
    with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r'{}\shell\open\command'.format(class_root)) as key:
        command = winreg.QueryValueEx(key, '')[0]
        return shlex.split(command)[0]

#To remove the white space of the Magic library output
def remove(string):
       return string.replace(" ", "").lower()

#To trim upto the "," that is to get the required word from the Magic library output
def trim(arg):
   filetype=""
   for element in range(0, len(arg)):
       if arg[element]!=",":
           filetype+=arg[element]
       else:
           break
   return filetype

#The function is invoked by main call, where the args contains the path
def main(args):
    path= args[1]
    #To decide which type the file is and which extension it has to be used.
    fileType = magic.from_file(path)
    var=remove(fileType)
    vartrim=trim(var)
    if vartrim=="compositedocumentfilev2document":
        if fileType.__contains__("Microsoft Excel"):
            programName = get_default_windows_app(fileextdict["excel"])
        elif fileType.__contains__("Microsoft Office Word"):
            programName = get_default_windows_app(fileextdict["microsoftword"])
        subprocess.Popen([programName, path], shell=True)
        exit()    
    if fileextdict[vartrim] == ".txt" or  fileextdict[vartrim] == ".py":
        programName = "notepad.exe"
    elif fileextdict[vartrim] == ".jpeg" or  fileextdict[vartrim] == ".jpg" or fileextdict[vartrim] == ".png":
        programName = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    else:    
        programName = get_default_windows_app(fileextdict[vartrim])
    #Open default application via command line execution
    #Code refrence https://blog.finxter.com/how-to-open-a-pdf-file-in-python/
    subprocess.Popen([programName, path], shell=True)
        

if __name__ == '__main__':
    main(sys.argv)