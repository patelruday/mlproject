from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT="-e ."
def get_requrements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requrements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements    



setup(
    name="mlproject",
    version="0.0.1",
    author="Uday patel",
    author_email="udayraj2005@gmail.com",
    packages=find_packages(),
    install_requires=get_requrements("requirements.txt")
    
)
