# Nothing much, I just want to keep a note of 1 thing:
# ***************************************************
# Why python3 instead of python in mac?
# In mac, the default python version is 2.7, and you have to use "python3" to run python 3 code. 
# In windows, you can just use "python" to run python 3 code. 
# So if you are using mac, remember to use "python3" instead of "python" when running your code.

# Also, if you want to use pip to install packages, you should use "pip3" instead of "pip" in mac. 
# In windows, you can just use "pip". 
# So if you are using mac, remember to use "pip3" instead of "pip" when installing packages.

# This is all becoz of same reason as above, the default python version in mac is 2.7, and pip is associated with that version. 
# So if you want to install packages for python 3, you have to use "pip3" to install them.
#****************************************************

#****************************************************
# How to run Python code in terminal?
# If u wanna run python in terminal, u can just type "python" or "python3" (depending on your system) and then you will enter the python interactive shell, where you can type python code and see the results immediately. 
# This is a great way to test out small pieces of code and see how they work.
#****************************************************

# I am writing a test program to see how do we run a python code.
import sys
print(sys.version)

#****************************************************
# Creating Virtual Environment
# A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages. 
# It allows you to have different versions of Python and different packages installed on the same system without conflicts.

# Creating a virtual environment:
#               python3 -m venv myenv
# This will create a virtual environment named "myenv" in the current directory. 
# You can replace "myenv" with any name you want for your virtual environment.

# Activating the virtual environment:
#               source myenv/bin/activate
# This will activate the virtual environment and you will see the name of the virtual environment in your terminal prompt. 
# Now, any packages you install using pip will be installed in this virtual environment and will not affect your global Python installation.

# Deactivating the virtual environment:
#                   deactivate
# This will deactivate the virtual environment and return you to your global Python installation.
#****************************************************

#****************************************************
# Installing packages in virtual environment
# In order to install 3rd party packages in your virtual environment, you can use pip. For example, if you want to install the "requests" package, you can use the following command:
#               pip install requests
# This will install the "requests" package in your virtual environment. You can then import and use the "requests" package in your Python code without affecting your global Python installation.

# but if you want to install a specific version of a package, you can use the following command:
#               pip install requests==2.25.1
# This will install version 2.25.1 of the "requests" package in your virtual environment. You can replace "2.25.1" with any version number you want to install.

# If u want to install multiple packages at once, you can create a requirements.txt file that lists all the packages you want to install, one per line. For example, your requirements.txt file might look like this:
# requests==2.25.1
# numpy==1.19.5
# pandas==1.2.4
# Then, you can use the following command to install all the packages listed in the requirements.txt
#               pip install -r requirements.txt
# This will install all the packages listed in the requirements.txt file in your virtual environment. This is a convenient way to manage your project dependencies and ensure that everyone working on the project has the same packages installed.

# We can give the requirements.txt file to other people working on the same project, and they can use the same command to install all the packages needed for the project. This helps to ensure that everyone is using the same versions of the packages and reduces the chances of compatibility issues.
# Generally, we dont share whole virtual environment with other people, we just share the requirements.txt file and let them create their own virtual environment and install the packages using the requirements.txt file. This way, everyone can have their own isolated environment and avoid conflicts between different projects.
#****************************************************

#****************************************************
# Do u know why we write pip instead of pip3 inside virtual environment?
# Inside a virtual environment, pip automatically points to correct PYTHON version : the one that is used to create the virtual environment.
# when we ran: 
#               python3 -m venv myVirtualEnv
# The venv will contain its own isolated Python3 installation.
# When we activate the virtual environment, this modifies our PATH so that pip now refers to the venv's pip, which is linked to Python3.  
#****************************************************

#****************************************************
# Alternatives of venv and pip
# uv is the newest and fastest alternative to venv and pip. 
# It is a tool that combines the functionality of both venv and pip, allowing you to create virtual environments and manage packages in a more efficient way. 
# It is designed to be faster and more user-friendly than traditional tools, making it a great choice for Python developers who want to streamline their workflow.
#****************************************************

#****************************************************
# File Nomenclature/Organiztion:
# Any file which has .py extension is called MODULE.
# Any file which has .py extension and contains a main function is called SCRIPT.
# Any folder which contains __init__.py file is called PACKAGE.

# script vs module:
# A script is a file that is intended to be executed directly, while a module is a file that is intended to be imported and used by other code. 
# A script typically contains a main function that serves as the entry point for the program, while a module may contain functions, classes, and variables that can be used by other code. 
# In Python, you can use the __name__ variable to determine whether a file is being run as a script or imported as a module. 
# If __name__ == "__main__", it means the file is being run as a script, and you can include code that should only be executed in that case.
# #****************************************************

# #****************************************************
# PEP8
# PEP8 is the style guide for Python code. 
# It provides guidelines and best practices for writing Python code in a consistent and readable way. 
# Following PEP8 can help improve the readability and maintainability of your code, making it easier for others (and yourself) to understand and work with it in the future. 
# Some of the key recommendations in PEP8 include using 4 spaces for indentation, limiting lines to 79 characters, and using descriptive variable names.
# You can use tools like flake8 or pylint to check your code against PEP8 guidelines and ensure that it adheres to the recommended style. 
#******************************************************

# ****************************************************
# Zen of Python
# The Zen of Python is a collection of 19 guiding principles for writing Python code, written by Tim Peters. 
# It is often cited as a set of aphorisms that capture the philosophy of Python and the design decisions that have been made in the language. 
# The Zen of Python can be accessed by importing the "this" module in Python. 
# Some of the key principles in the Zen of Python include "Beautiful is better than ugly", "Explicit is better than implicit", and "Simple is better than complex". 
# The Zen of Python serves as a reminder to Python developers to write code that is clear, concise, and easy to understand, while also adhering to the principles of good software design.
# ****************************************************