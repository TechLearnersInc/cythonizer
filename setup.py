import os

# Always prefer setuptools over distutils
from setuptools import find_packages, setup


def main():
    here = os.path.abspath(os.path.dirname(__file__))

    # Get the long description from the relevant file
    long_description = ""
    # noinspection PyBroadException
    try:
        with open(os.path.join(here, "README.rst"), encoding="utf-8") as f:
            long_description = f.read()
    except Exception:
        pass

    setup(
        name="Cythonizer",
        # Versions should comply with PEP440.  For a discussion on single-sourcing
        # the version across setup.py and the project code, see
        # http://packaging.python.org/en/latest/tutorial.html#version
        version="1.2.0b3",
        description="Convert .py and .pyx to (.pyd | .so) very easily.",
        long_description=long_description,
        long_description_content_type="text/x-rst",
        # The project's main homepage.
        url="https://github.com/TechLearnersInc/cythonizer",
        # Author details
        author="Rizwan Hasan",
        author_email="rizwan.hasan486@gmail.com",
        # Choose your license
        license="MIT",
        # Minimum Python version required
        python_requires=">=3.6",
        # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
        project_urls={
            "Source": "https://github.com/TechLearnersInc/cythonizer",
            "Tracker": "https://github.com/TechLearnersInc/cythonizer/issues",
            "Facebook": "https://www.facebook.com/TechLearnersInc",
            "Linkedin": "https://www.linkedin.com/company/techlearners/",
            "Telegram": "https://t.me/TechLearners",
        },
        classifiers=[
            # How mature is this project? Common values are
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            # Indicate who your project is intended for
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "Topic :: Software Development :: Build Tools",
            "Programming Language :: Cython",
            # Pick your license as you wish (should match "license" above)
            "License :: OSI Approved :: MIT License",
            # Specify the Python versions you support here. In particular, ensure
            # that you indicate whether you support Python 2, Python 3 or both.
            "Programming Language :: Python :: 3",
            "Topic :: Software Development :: Build Tools",
        ],
        # What does your project relate to?
        keywords="cython Cythonizer",
        # You can just specify the packages manually here if your project is
        # simple. Or you can use find_packages().
        packages=find_packages(),
        # List run-time dependencies here. These will be installed by pip
        # when your project is installed. For an analysis of "install_requires"
        # vs pip's requirements files see:
        # https://packaging.python.org/en/latest/technical.html#install-requires-vs-requirements-files
        install_requires=["cython", "numpy"],
        # To provide executable scripts, use entry points in preference to the
        # "scripts" keyword. Entry points provide cross-platform support and allow
        # pip to create the appropriate form of executable for the target platform.
        entry_points={
            "console_scripts": [
                "cythonizer = cythonizer:main",
            ],
        },
    )


if __name__ == "__main__":
    main()
