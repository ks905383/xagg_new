from setuptools import setup
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
	name="xagg_new",
    version="0.1.3",
    author="Kevin Schwarzwald",
    author_email="kschwarzwald@iri.columbia.edu",
    description="Aggregating raster data over polygons",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ks905383/xagg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    use_scm_version={
        "write_to": "xagg_new/_version.py",
        "write_to_template": '__version__ = "{version}"',
        "tag_regex": r"^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$",
    }
)
