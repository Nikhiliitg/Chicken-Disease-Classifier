import setuptools

with open("README.md",'r',encoding="utf-8") as f:
    long_description=f.read()
    
__version__="0.0.0"

REPO_NAME="Chicken-Disease-Classifier"
AUTHOR_USER_NAME="Nikhiliitg"
SRC_REPO='Chicken-Disease-Classifier'
AUTHOR_NAME="d.nikhil@op.iitg.ac.in"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_NAME,
    description='A small Python package for CNN app',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"

    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)