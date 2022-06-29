from setuptools import setup

setup( name='unhcrpyplotstyle',
       version='0.15',
       author='Lei Chen',
       author_email="chen@unhcr.orgt",
       description="Set matplotlib style to follow UNHCR's brand policies",
       packages=['unhcrpyplotsytle'],
       install_requires=['matplotlib>=3.1.0'],
       include_package_data=True
    )