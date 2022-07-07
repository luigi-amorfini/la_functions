# Luigi Amorfini - Library My Functions
>> Thonny IDE https://thonny.org/ vers: 3.3.13 stable version

# Tools->Open system shell

[code]
python -m pip --no-cache-dir install -U pip && pip --no-cache-dir install setuptools --upgrade && pip --no-cache-dir install wheel

pip --no-cache-dir install pillow requests numpy

git clone https://github.com/luigi-amorfini/la_functions.git temp

cd temp

RMDIR /S /Q .git

del .gitignore

del LICENSE

xcopy /s *.* ..

cd ..

RMDIR /S /Q temp

cd libs/la_functions/

python setup.py build

python setup.py sdist

pip install .\dist\la_functions-0.1.0.tar.gz

cd .. && cd ..

exit
[code]

