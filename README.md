# Luigi Amorfini My Library Functions "la_functions"
Luigi Amorfini - Library My Functions

# open powershell in d:\ or X:

cd D:\

mkdir python

cd python

mkdir prove

cd prove

python -m venv venv

venv\Scripts\activate.ps1

python -m pip --no-cache-dir install -U pip ; pip --no-cache-dir install setuptools --upgrade ; pip --no-cache-dir install wheel

pip --no-cache-dir install pillow requests numpy sounddevice soundfile


git clone https://github.com/luigi-amorfini/la_functions.git

cd la_functions/

mv libs ../

Remove-Item -Recurse -Force .git

rm .gitignore

mv calcola_iva.py ../

cd ..

Remove-Item -Recurse -Force la_functions

cd libs/la_functions

python setup.py build

python setup.py sdist

pip install .\dist\la_functions-0.1.0.tar.gz

cd .. ; cd ..

cls

py .\calcola_iva.py

# The End Powershell Terminal

code .
# Visual studio code
