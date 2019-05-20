from setuptools import find_packages, setup

def read_requirements_txt():
    with open("requirements.txt") as fp:
        requirements = [line.strip() for line in fp]
    return requirements
setup(
    name="tests",
    version="0.0.1",
    description="MOD21 Homework - test",
    packages=find_packages(),
    install_requires=read_requirements_txt(),
    include_package_data=True,
    author="Amazing Author",
    author_email="author@example.com",
    url="https://github.com/KznRkjp/tests",
)
