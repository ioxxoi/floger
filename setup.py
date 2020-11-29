import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='floger',  
     version='0.1.0',
     scripts=['Scripts/floger'] ,
     author="Daniel San Miguel Reyero",
     author_email="dani@downby.net",
     description="Firewall LOG viewER",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/ioxxoi/floger",
     packages=setuptools.find_packages(),
    install_requires=[ 'PyQt5',  'argparse' ],
     data_files=[ ('bitmaps',['bitmaps/floger.png','bitmaps/floger_long.png']),],
     include_package_data=True,
     license="OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
     platforms=['any'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
         "Operating System :: OS Independent",
         "Development Status :: 4 - Beta",
         "Environment :: X11 Applications :: Qt",
         "Environment :: Win32 (MS Windows)",
         "Intended Audience :: System Administrators",
         "Topic :: Security"
     ],
)
