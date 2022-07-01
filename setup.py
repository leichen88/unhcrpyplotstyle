from setuptools import setup

setup( name='unhcrpyplotstyle',
       version='0.0.7',
       author='Lei Chen',
       author_email="chen@unhcr.org",
       description="Set matplotlib style following UNHCR's Data Visualization Guidelines",
       packages=['unhcrpyplotstyle'],
       license="MIT",
       keywords=[
        "matplotlib-style-sheets",
        "unhcr-plot-style",
        "matplotlib-styles",
        "python"
       ],
       url="https://github.com/leichen88/unhcrpyplotstyle",
       install_requires=['matplotlib>=3.1.0'],
       include_package_data=True
    )