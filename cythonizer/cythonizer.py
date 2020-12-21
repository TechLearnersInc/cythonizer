import argparse
import logging
import os
import pathlib
import sys

# Always prefer setuptools over distutils
from setuptools import Extension, setup
import Cython.Compiler.Options
from Cython.Build import cythonize
from Cython.Distutils import build_ext

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


class cythonizer:
    def __init__(self) -> None:
        self.__extension: list = []
        self.__args = self.__Arguments()
        self.__Checking()
        self.__Compiling()
        # self.__Cleanup()

    # Argumebts Parser ↓
    def __Arguments(self):
        parser = argparse.ArgumentParser(
            description="A script that will attempt to automatically convert one or more .py and .pyx files into the corresponding compiled .pyd or .so binary modules files."
        )

        # Taking Files ↓
        parser.add_argument(
            "filenames", type=pathlib.Path, nargs="+", help=".py and .pyx files only"
        )

        # Cython Annotation ↓
        parser.add_argument(
            "--annotation",
            default=False,
            action="store_true",
            help="(default: False)",
        )

        # Numpy Includes ↓
        parser.add_argument(
            "--numpy-includes",
            default=False,
            action="store_true",
            help="(default: False)",
        )

        # Cython Debugmode ↓
        parser.add_argument(
            "--debugmode",
            default=False,
            action="store_true",
            help="(default: False)",
        )

        return parser.parse_args().__dict__

    # Received File Checking ↓
    def __Checking(self):
        for file in self.__args.get("filenames"):
            if not os.path.exists(file):
                logging.error(f'"{file}" doesn\'t exist.')
                sys.exit(-1)
            if not os.path.isfile(file):
                logging.error(f'"{file}" is not a file')
                sys.exit(-1)
            if os.path.splitext(file)[-1] not in (".py", ".pyx"):
                logging.error(f'"{file}" is not a valid file')
                sys.exit(-1)

    # Includes Directory ↓
    def __Includes_Dir(self):
        # Extra include folders. Mainly for numpy.
        if self.__args.get("numpy_includes"):
            try:
                import numpy as np

            except ModuleNotFoundError:
                logging.error("Numpy is required, but not found. Please install it")
                sys.exit(-1)
            return [np.get_include()]
        else:
            return []

    # Cython Compilation ↓
    def __Compiling(self):
        Cython.Compiler.Options.annotate = self.__args.get("annotation")

        ext_modules: list = []
        for _ in self.__args.get("filenames"):
            file: str = str(_)
            # The name must be plain, no path
            module_name = os.path.basename(file)
            module_name = os.path.splitext(module_name)[0]
            ext_modules.append(
                Extension(
                    module_name, [file], extra_compile_args=["-O2", "-march=native"]
                )
            )

        sys.argv = [sys.argv[0], "build_ext", "--inplace"]

        setup(
            cmdclass={"build_ext": build_ext},
            include_dirs=self.__Includes_Dir(),
            ext_modules=cythonize(module_list=ext_modules, language_level="3"),
        )

    def __Cleanup(self):
        # Delete intermediate C files.
        for _ in self.__args.get("filenames"):
            filename = str(_)
            filename = f"{filename}.c"
            if os.path.exists(filename):
                os.remove(filename)


def main():
    cythonizer()


if __name__ == "__main__":
    main()
