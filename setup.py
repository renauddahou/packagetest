import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="testrenaud",
    version="0.0.1",
    author="Renaud",
    author_email="dahou.r@yahoo.com",
    packages=["testrenaud"],
    description="A sample test package",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/renauddahou/packagetest.git",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[]
)
