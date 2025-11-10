<p align="center">
  <img src="https://github.com/user-attachments/assets/b289ba16-01bc-4fa9-87b6-ddf8ad427aa9" width="342" height="345" alt="DelftBLUE GUI Logo">
</p>

<h1 align="center">
   DelftBlue GUI
</h1>


This repo aims to ease access to the DelftBlue supercomputer by introducing an asynchronous uplink/downlink strategy to synchronize working directory on the local machine with remote, using only a few clicks of a button.

To use, make sure your local machine has a ssh key corresponding to your account generated. You can generate it via:

    ssh-keygen -t ed25519 -C "username@login.delftblue.tudelft.nl"         
Once the ssh key is generated, the usage is very simple. In user.py specify your username:

    USER = <your_username>    

Then run main.py. Create jobs, then modify them to your needs (cmake, makefile, config etc)  Note that the interactive console for this patch is only supported for Arch based linux versions. Windows Powershell is not yet implemented. 

# *this is still work in progress and not all features may work properly*
