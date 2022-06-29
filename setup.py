from setuptools import setup

setup( name='unhcrpyplotstyle',
       version='0.1',
       author='Lei Chen',
       author_email="chen@unhcr.org",
       description="Set matplotlib style to follow UNHCR's Data Visualization Guidelines",
       packages=['unhcrpyplotstyle'],
       install_requires=['matplotlib>=3.1.0'],
       include_package_data=True
    )