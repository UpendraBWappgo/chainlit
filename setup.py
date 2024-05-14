from setuptools import find_packages, setup 

setup(
    name = "zomato_bot",
    author = "Rocky Thakur",
    author_email = "upendawappgo@gmail.com", 
    packages = find_packages(), 
    install_requires = ["chainlit", "notebook", "ipywidgets", "tqdm", "python-dotenv", "openai", "langchain-google-genai"]
)