I have been searching up how to install and run the fingpt models on huggingface and github. There were problems concerning the fact that the models were gated on huggingface. In other words, I had to get huggingface's and meta's permission to be able to install the model and its usable datasets. To be able to do that, I had to send a join request to the fingpt group's organization on huggingface.
![image](https://github.com/dfuen010/Data-Centric-FinGPT-Research/assets/46663757/9cccbe1e-2fd0-451d-87dd-6045a2956ea8)

However, we have to wait until the organization accepts me which can take a long time. Until then, we wouldn't be able to use the huggingface models. So, I have tried it another way with huggingface's un-gated features. Primarily, this method involves "peft" and installing peft-models. However, this model cannot be used without GPU's so unless you have a GPU API installed, we have to use kaggle's free resources or google colab.

3/23/2024
-Update to the peft models idea:
  The problem with the second part of the peft models implementation was that we needed to make and designate a offload folder in our automodel options. After identifying that problem, we simply needed to change the pretrained options. However, we run now into a new problem, the RAM for a regular session runs out if we use a google colab notebook. We have to figure out how to save memory a little more to make a functioning notebook.


4/12/2024
I found a method of using the models online without being limited to peft's fixed model parameters. However, the method requires running on kaggle with GPU to use kaggle's free access to hugging face's tokens and wandb api. It cannot be used any place else. This means that we can't do this on our own internet or on colab. As this is an obvious issue, I am attempting many methods in order to find a workaround.
