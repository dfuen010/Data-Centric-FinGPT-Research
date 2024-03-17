## Setup Guide for Llama 2 

The following guide is for powershell usage, not recomended but the first approach I took in setting up Llama. 

#### Anaconda

+ Install Anaconda if you don't have it already.


#### PyTorch/CUDA Environment

+ In a powershell environment, create a conda environment
+ This can be done using the following commands
conda create --name pytorch python=3.11
conda activate pytorch
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
+ Then you can clone the Llama repo ( git clone URL )
+ Please Note: You have to go to the meta website and request access of the llama model which will give send you an email with what you need in order to successfully set up llama

#### After cloning
+ After you cloned the repo you have to run "pip install -e ." in the top directory
+ The next step is to run the download.sh file
+ Depending on your setup you may encounter multiple errors running the download.sh script
+ Once successfully running the script file, you will be prompted to paste the URL that you will have received in the email when requesting access to the Llama Model. 
+ Paste the link to download the model you requested.

#### Finish following the READ.ME provided by MEta


## Notes / Issues
I haven't got past the download.sh script running because of issues with my environments. Will try using juptyer notebook instead of linux powershell/ubuntu. 

I have just recently received access to llama (as of 3/15) and have spent the last two days trying to set it up locally. Cannot progress until Llama set up is complete. 





