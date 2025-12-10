<p align="center">
  <img src="https://github.com/user-attachments/assets/b289ba16-01bc-4fa9-87b6-ddf8ad427aa9" width="342" height="345" alt="DelftBLUE GUI Logo">
</p>

<h1 align="center">
   DelftBlue GUI
</h1>
This repo aims to provide a level-of-abstraction for interfacing with DelftBlue. Create, dispatch, terminate and monitor your jobs in a single GUI. 
<h2 align="center">
   Installation
</h1>


To use, make sure your local machine has a ssh key corresponding to your account generated. You can generate it via:

    ssh-keygen -t ed25519 -C "username@login.delftblue.tudelft.nl"         
You can view your SSH keys with (windows):
    
    cat $env:USERPROFILE\.ssh\id_ed25519.pub       
Once the ssh key is generated, transfer it to DelftBlue:

    ssh username@login.delftblue.tudelft.nl
    cd ./.ssh
    nano authorized_keys
And copy your local ssh key to this file.
Once ssh keys are setup, configure your username and the folder where you want to store jobs in user.txt:

     <your_username>    
     <path_to_your_folder>

Then run main. Alternatively, if you want to have a desktop shortcut, run the installer.

Running the executable should provide you with a menu screen (outside TUDelft you will need a VPN to access DelftBlue).
<p align="center">
 <img width="1497" height="828" alt="image" src="https://github.com/user-attachments/assets/1779695b-afa4-4a34-8bff-987f24760b52" />
</p>

The lower table shows all the subfolders you have in the remote folder. This is the space for your jobs. How you choose to build them is up to you - whether it is a raw excutable, a cmake or Make file. Everything in remote folder will be synced with your login node on DelftBLue.

Each job folder contains two bash scripts by default: 

<p align="left">
<img width="219" height="103" alt="image" src="https://github.com/user-attachments/assets/f2cfd349-76f4-4a09-9d14-b014e833e311" />
</p>


job.sh file is what is executed on the compute node; most of the time it is simply the executable you want to run (i.e., ./myprogram).
request.sh file specified the compute parameters you want to have - you can edit it on the fly via the GUI.

Once you have your request.sh file generated per your requirements, you can submit the job via the GUI:

<p align="left">
<img width="271" height="63" alt="image" src="https://github.com/user-attachments/assets/d27115fe-b7d9-45b4-8dae-cf89d388de8b" />
</p>


You should then see the status of your job, whether it is awaiting its turn:

<p align="left">
<img width="679" height="65" alt="image" src="https://github.com/user-attachments/assets/2ffd02df-db68-4651-ab00-d53b29501e86" />
</p>


Or whether it is running:

<p align="left">
<img width="679" height="65" alt="image" src="https://github.com/user-attachments/assets/86d2a66d-802a-41d6-8f04-3b91356359a0" />
</p>


You can now close the app and come back later to check the status of your jobs. 
Once the job is finished, it is automatically removed from the compute job queue. You can then downlink the data into your local machine.

You can terminate jobs by clicking on the Status icon:

<p align="left">
<img width="679" height="65" alt="image" src="https://github.com/user-attachments/assets/151fbd44-0d00-4ed9-92ac-21b90bd49742" />
</p>


