from setuptools import find_namespace_packages, setup

setup(
    name="ml4ir",
    packages=find_namespace_packages(include=["ml4ir.*"]),
    version="0.0.1",
    description="Machine Learning libraries for Information Retrieval",
    author="Search Relevance, Salesforce",
    author_email="searchrelevancyscrumteam@salesforce.com ",
    license="ASL 2.0",
)
