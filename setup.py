from setuptools import setup, find_packages

try:
    import pypandoc

    long_descr = pypandoc.convert("README.md", "rst")
except (IOError, ImportError):
    long_descr = open("README.md").read()

setup(
    name="dbcommon",
    version="0.1.1",
    description="A set of db connectors specific to our DB",
    long_description=long_descr,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
    ],
    keywords=["mariadb", "dbcommon"],
    author="Mike Williamson",
    author_email="mvw@kapacity.dk",
    license="MIT",
    packages=find_packages(where="src"),
    install_requires=["pandas", "toml", "mariadb"],
    package_dir={"": "src"},
    test_suite="tests",
    include_package_data=True,
    zip_safe=True,
)
