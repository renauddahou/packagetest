import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="test-package199925",
    version="0.0.1",
    author="GeeksforGeeks",
    author_email="dahou.r@yahoo.com",
    packages=["test-package"],
    description="A sample test package",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/renauddahou/packagetest.git",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[]
)
