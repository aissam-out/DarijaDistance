from setuptools import setup, find_packages

setup(
    name='DarijaDistance',
    version='0.1',
    description='A library for finding the closest words and calculating word distances for the Moroccan Dialect Darija',
    author='Aissam Outchakoucht',
    author_email='aissam.outchakoucht@gmail.com',
    url='https://github.com/aissam-out/DarijaDistance',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'DarijaDistance': ['data/*'],
    },
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
)
