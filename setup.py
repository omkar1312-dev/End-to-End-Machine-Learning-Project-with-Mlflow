import setuptools

with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()
    
_version_ = "0.0.0"

REPO_NAME = "End-to-End-Machine-Learning-Project-with-Mlflow"
AUTHOR_USER_NAME = "omkar1312-dev"
SRC_REPO = "Machine Learning Project"
AUTHOR_EMAIL = "omkar.a.1325@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=_version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Machine learning project using Mlflow for end to end machine learning pipeline.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),)