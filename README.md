# Luigi Amorfini My Library Functions "la_functions"
>> Guida per thonny ide

# Strumenti->Apri shell di sistema

python -m pip --no-cache-dir install -U pip && pip --no-cache-dir install setuptools --upgrade && pip --no-cache-dir install wheel

pip --no-cache-dir install pillow requests numpy


git clone https://github.com/luigi-amorfini/la_functions.git

cd la_functions/

move libs ../

rd /S .git

del .gitignore

move calcola_iva.py ../

cd ..

rd /S la_functions

cd libs/la_functions

python setup.py build

python setup.py sdist

pip install .\dist\la_functions-0.1.0.tar.gz

cd .. && cd ..

cls

exit 


# Apri il file calcola_iva.py con thonny ide.

calcola_iva.py

# Esegui con tasto "F5"



