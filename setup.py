from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    :param file_path: file path of requirements.txt
    :return: list of libraries
    '''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='student-performance-prediction',
    version='0.0.1',
    author='Tushar Bose',
    author_email='tushar009@e.ntu.edu.sg',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
