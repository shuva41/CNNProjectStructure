import setuptools

__version__ = "0.0.1"

REPO_NAME = "CNNProjectStructure"
AUTHOR_NAME = "Shuvankar Ray"
SRC_REPO = "CNNClassifier"
AUTHOR_EMAIL = "shuvankarray@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A template for a CNN project structure",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": "https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)

