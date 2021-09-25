It's a Simple Prototype to Protect Data against Ransomware. 

The Prototype designes, simply removes the Extensions of All the Files of the specified Folder (including subfolder) and will be in contunious loop, even if a new file added to
the folder, it will remove the extension of that file.

So whenever a Ransomware attack happens, if it is a Crypto Ransomware, it will encrypt the files based on Extensions, so this method will protect them from getting encrypted
and keeping data safe.

So What happens when we remove an Extension of the Files, how the Windows will get to Know which File it is? and how to open it?

Ans: So to make it simple and tell windows which program needs to be invoked, a code is written (Extensionless File Invoker.py), which takes the Extensionless File name and 
     Checks it's header using a library called "Python-Magic", Python-magic gives output --> whether it is PDF, DOCUMENT, IMAGE, EXCEL etc...based on this output
     a seprate File Dictionary is written to get the extensions of the files and then it is passed to Query the registry to get the default program for that File and as a Final 
     step, the Extenionless File path and the default program to Invoke it is passed to a "Subprocess" to open it.
     
     
When an Extension of a File removed, How you going to get the path of that File and How "Extensionless File Invoker.py" will get the path?

Ans: There is a default commands in Windows to associate a "No Extension" Files to open with a particular program and below are those commands.

           assoc .="No Extension" && ftype "No Extension"="C:\EPAR\Extenionless File Invoker.exe" "%1"
           
By running the above commands in Command Window(Run as Administrator), we can associate "No Extension" Files to our program "Extensionless File Invoker.exe"

# Model of the Prototype

![Model](https://user-images.githubusercontent.com/23623577/134751755-39d41179-87a1-4829-8c66-f9d63576a78c.JPG)

## Execution of File Extenion Remover and intergrating them with Extensionless File Invoker

![Capture](https://user-images.githubusercontent.com/23623577/134751908-295ab932-af9f-4ac7-a215-ec18dc883e5c.JPG)



     
