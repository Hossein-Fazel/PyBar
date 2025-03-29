from setuptools import setup

with open("README.md", "r") as fh: 
	description = fh.read() 

setup( 
	name="PyBar", 
	version="1.0.0", 
	author="Hossein-Fazel", 
	author_email="fazel.hosein9654@gmail.com", 
	packages=["PyBar"], 
	description="A simple progress bar with python", 
	long_description=description, 
	long_description_content_type="text/markdown", 
	url="https://github.com/Hossein-Fazel/PyBar", 
	license='MIT', 
	python_requires='>=3.6', 
	install_requires=[] 
) 
