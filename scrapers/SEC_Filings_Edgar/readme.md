# How to set up the SEC Filings Edgar scraper

## Environment Setup

### Installation

1. Install Python 3.12 from the microsoft store/official website
2. Install Miniconda (https://docs.anaconda.com/free/miniconda/index.html)
   1. Start up the installer
   2. Check off Add Miniconda3 to my PATH environment variable
   3. Leave everything else as default
3. Check if conda is installed by running the following command in your terminal:

```bash
conda --version
#Latest version as of 3/7/2024 is 24.1.2
```


### Quick Conda Guide

V1. Create a new conda environment using the following command in your terminal:

```bash
conda create -n sec_filings_edgar python=3.12
```

V2. Create a new conda environment using the environment.yml file:
1. CD into the same directory where the environment.yml file is located
2. Run the following command in your terminal:

```bash
conda env create -f environment.yml
```

Activate/Deactivate the environment using the following command in your terminal:

```bash
conda activate sec_filings_edgar
deactivate
```

If nothing happens when you run the activate command, you may need to run the following command in your terminal:

```bash
conda init
conda activate sec_filings_edgar
(sec_filings_edgar) PS C:\Users\TestUser> # Your terminal should look like this
```

Conda other useful commands:

```bash
conda env list # List all conda environments
conda env remove --name sec_filings_edgar # Remove the conda environment
conda env export > environment.yml # Export the current conda environment to a file
```
