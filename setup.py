from setuptools import setup, find_packages


with open("README.md", "r") as readme_file:
  readme = readme_file.read()

requirements = [
  "opencv-python==4.6.0.66"
]

setup(
  name="cvforall",
  version="0.0.2",
  author="Sergei Svechnikov",
  author_email="srgcandle@gmail.com",
  description="Collection of methods to facilitate work on computer vision projects",
  long_description=readme,
  long_description_content_type="text/markdown",
  url="https://github.com/cvforall/cvforall.git",
  packages=find_packages(),
  install_requires=requirements,
  classifiers=[
    "Programming Language :: Python :: 3.7",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
  ]
)
