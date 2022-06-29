import atexit
import glob
import os
import shutil

import matplotlib
from setuptools import setup
from setuptools.command.install import install


def install_styles():
    # Find all style files
    stylefiles = glob.glob('styles/**/*.mplstyle', recursive=True)
    # Find stylelib directory (where the *.mplstyle files go)
    mpl_stylelib_dir = os.path.join(matplotlib.get_configdir(), "stylelib")
    if not os.path.exists(mpl_stylelib_dir):
        os.makedirs(mpl_stylelib_dir)
    # Copy files over
    print("Installing styles into", mpl_stylelib_dir)
    for stylefile in stylefiles:
        print(os.path.basename(stylefile))
        shutil.copy(
            stylefile,
            os.path.join(mpl_stylelib_dir, os.path.basename(stylefile)))


class PostInstallMoveFile(install):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        atexit.register(install_styles)


# Get description from README
# root = os.path.abspath(os.path.dirname(__file__))
# with open(os.path.join(root, 'README.md'), 'r', encoding='utf-8') as f:
#     long_description = f.read()

setup( name='unhcrpyplotstyle',
       version='0.0.2',
       author='Lei Chen',
       author_email="chen@unhcr.org",
       description="Set matplotlib style following UNHCR's Data Visualization Guidelines",
       keywords=[
        "matplotlib-style-sheets",
        "unhcr-plot-style",
        "matplotlib-styles",
        "python"
    ],
       url="https://github.com/leichen88/unhcrpyplotstyle",
       install_requires=['matplotlib',],
       cmdclass={'install': PostInstallMoveFile, },
    )