import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='data_factory',  
     version='0.1',
     scripts=['data_factory.py'] ,
     author="Allen (Yi Xin) Hu",
     author_email="allen00414@gmail.com",
     description="A data cleaning utility package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/ayhu414/data_factory",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )