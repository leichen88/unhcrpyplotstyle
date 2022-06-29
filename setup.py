from setuptools import setup

setup( name='unhcrpyplotstyle',
       version='0.0.2',
       author='Lei Chen',
       author_email="chen@unhcr.org",
       description="Set matplotlib style following UNHCR's Data Visualization Guidelines",
       packages=['unhcrpyplotstyle'],
       install_requires=['matplotlib>=3.1.0'],
       include_package_data=True
    )