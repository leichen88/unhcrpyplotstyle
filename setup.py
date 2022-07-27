from setuptools import setup

# Get description from README
with open("README.md", "r") as fh:
    long_description = fh.read()

setup( name='unhcrpyplotstyle',
       version='0.1.2',
       author='Lei Chen',
       author_email="chen@unhcr.org",
       description="Set matplotlib style following UNHCR's Data Visualization Guidelines",
       long_description = long_description,
       long_description_content_type='text/markdown',
       license="MIT",
       keywords=[
        "matplotlib-style-sheets",
        "unhcr-plot-style",
        "matplotlib-styles",
        "python"
       ],
       classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
       ],
       url="https://github.com/leichen88/unhcrpyplotstyle",
       install_requires=['matplotlib'],
       include_package_data=True
)