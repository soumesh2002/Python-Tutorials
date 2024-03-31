## Setup Instructions 🧑‍💻

- System requirments

    - Python 3.x 🐍
    - Ram: &#x2265; 16 GB
    - Storage: &#x2265; 200 GB
    - OS: Windows 🪟, Linux 🐧

- Required software
    - [Miniconda](https://docs.anaconda.com/free/miniconda/index.html)
    - [Visual Studio Code](https://code.visualstudio.com/)

## Setting up __conda__  
![alt text](images_for_readme/image-15.png)

![alt text](images_for_readme/image-14.png)

👉 Install __miniconda__ by following the on-screen instructions

❗ __make sure to add miniconda to path__  

![alt text](images_for_readme/miniconda_to_path.png)

👉 Open Anaconda Prompt  

![alt text](images_for_readme/image.png) 

![alt text](images_for_readme/image-1.png)  

✅ __Creating a separete python development environment streamline your package management__  

    conda create -n pyenv python=3.11  

![alt text](images_for_readme/image-2.png)  

⌛ wait for some time to finish the intital setup  

👉 after completion, time to activate your conda env 😇  

👉 you can activate conda env: __pyenv__ by using: 

    conda activate pyenv  

![alt text](images_for_readme/image-3.png)  

👉 you can see __(base)__ has changed to __(pyenv)__  

👉 Let's install required packages:  

    conda install numpy pandas matplotlib seaborn jupyter ipykernel

![alt text](images_for_readme/image-4.png)  

✅ Proceed with the installation  

🚀 Your conda env: __pyenv__ is ready to use with the requried packages  

⚠️ Make sure to activate __pyenv__ using the command given above before using it.

## Setting up __Visual Studio Code__  

![alt text](images_for_readme/image-5.png)


 👉 [Installing Visual Studio Code in Windows 🪟](https://code.visualstudio.com/docs/setup/windows)  

⚠️ For Linux based distributions (Ubuntu) 🐧 

    sudo snap install code --classic  

After installation, we need to install few __extension__ required for working with python. For installing extension in __Visual Studio Code__  

👉 Open VS Code  

👉 Click this icon on the left activity bar to search __Extensions Marketplace__  

![alt text](images_for_readme/image-6.png)

Search for __Python__ and install the extension  

![alt text](images_for_readme/image-8.png)  

Search for __Jupyter__ and install the extension  

![alt text](images_for_readme/image-9.png)  

__Optional Extensions__

![alt text](images_for_readme/image-10.png)

![alt text](images_for_readme/image-11.png)

![alt text](images_for_readme/image-12.png)

![alt text](images_for_readme/image-13.png)

- After installing all the required extensions, let us create __.ipynb()__ file for working with python code

![alt-text](images_for_readme/create_new_folder.png)

![alt text](images_for_readme/image-16.png)

![alt text](images_for_readme/image-17.png)  

⚠️ Change __kernel__ to __pyenv__

![alt text](images_for_readme/image-18.png)  

👉 Choose __pyenv__ from the list

![alt text](images_for_readme/image-19.png)  

🚀 There you go, you successfully activated your __conda env__ in VS Code

![alt text](images_for_readme/image-20.png)  

🧑‍💻 __Let's Test__  

![alt text](images_for_readme/image-21.png)

🤘 __It's working ✅✅✅__


If any issue persists, please [Create a New Issue](https://github.com/soumesh2002/Python-Tutorials/issues)  

I'll Surely help 😇  

