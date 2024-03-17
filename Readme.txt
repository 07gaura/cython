To run Cython code first we need to install cython library using below command
<< pip install Cython --install-option="--no-cython-compile" >>
we have cython sample code in cython_code.pyx to run cython code we need to create setup.py and run build command
<< python setup.py build_ext --inplace >>
Now create python file and import cython_code and use the function and see the difference
