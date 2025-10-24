import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()        

setuptools.setup(
    name="TextSummarizer",
    version="0.0.1",
    author="Karthik Katakam",
    author_email="karthikkatakam2926@gmail.com",
    description="A text summarization package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/karthik-katakam/TextSummarization",
    project_urls={
        "Bug Tracker": "https://github.com/karthik-katakam/TextSummarization/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)   