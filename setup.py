from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

REPO_NAME = "Movie-Recommender_System using_Content_Based_Analysis"
AUTHOR_USER_NAME = "Yoyobun1"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ["streamlit","numpy","pandas","scikit-learn","scipy","matplotlib","seaborn","nltk"]

setup(
    name=SRC_REPO,
    version="0.0.1",
    author = "Yoyobun1",
    descritpion = "A simple Movie recommender system using Content Based Analysis",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = f"https://github.com/Yoyobun1/Movie-recomendation-system-using-Content-Based-Analysis",
    author_email = "marcgeorgenow@gmail.com",
    packages = [SRC_REPO],
    python_requires = ">=3.6",
    install_requires = LIST_OF_REQUIREMENTS,
)