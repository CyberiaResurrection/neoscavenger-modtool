import os
import unittest


class BaseTest(unittest.TestCase):
    def unpack_filename(self, filename):
        # try unpacked filename directly
        sourcefile = os.path.abspath(filename)
        if not os.path.isfile(sourcefile):
            sourcefile = os.path.abspath('../' + filename)
        if not os.path.isfile(sourcefile):
            sourcefile = os.path.abspath('Tests/' + filename)
        if not os.path.isfile(sourcefile):
            sourcefile = os.path.abspath('../Tests/' + filename)

        return sourcefile

    def unpack_workdir(self, dirname):
        # try unpacked directory directly
        workdir = os.path.abspath(dirname)

        cwd = os.getcwd()
        if not os.path.isdir(workdir):
            workdir = os.path.abspath(cwd + dirname)

        return workdir


if __name__ == '__main__':
    unittest.main()
