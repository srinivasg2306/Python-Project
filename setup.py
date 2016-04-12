import  os 
from  setuptools  import  setup

with  open ( os . path . join ( os . path . dirname ( __file__ )  'README.rst' ))  as  readme : 
    README  =  readme . read ()

# Allow to be run setup.py from Any path 
bones . Chdir ( os . Path . Normpath ( os . Path . Join ( os . Path . Abspath ( __file__ )  bone . Pardir )))

setup ( 
    name = 'django-polls' , 
    Version = '0.1' , 
    packages = [ 'polls' ] 
    include_package_data = True , 
    license = BSD License ' ,   # example license 
    description = ' A Python package. ' , 
    long_description = README , 
    url = "http://www.example.com/" , 
    author = ' Your Name ' , 
    author_email = ' yourname@example.com ' , 
    classifiers = [ 
        ' Environment :: Web Environment ' , 
        ':: Django Framework' , 
        'Intended Audience :: Developers' , 
        ' License OSI Approved :: :: BSD License ' ,  # example license 
        ' Operating System :: OS Independent ' , 
        ' Programming Language :: Python , 
        # Replace Appropriately thesis if you are stuck on Python 2. 
        "Programming Language :: Python :: 3 ' , 
        ' Programming Language :: Python :: 3.2 ' , 
        ' Programming Language :: Python :: 3.3 ' , 
        ' Topic :: Internet :: WWW / HTTP ' , 
        ' Topic :: :: Internet WWW / HTTP :: Dynamic Content ' , 
    ] 
)
