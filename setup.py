from setuptools import setup, find_packages
def get_requirements(filepath):
    requirements = []
    with open(filepath,'r')as f:
        requirements = f.readlines()
        requirements = [r.replace('\n','') for r in requirements]
    return requirements

setup(
    name = 'flaskproject',
    version = '0.0.1',
    author = 'rafayshaikh',
    authoremail = 'rafayshaikh633@gmail.com',
    packages=find_packages(),
    install_require = get_requirements('requirements.txt')




)