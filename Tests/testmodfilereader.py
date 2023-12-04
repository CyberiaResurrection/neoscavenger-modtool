import unittest

from Modtool.ModFileReader import ModFileReader
from Tests.BaseTest import BaseTest
from xml.sax.saxutils import escape, unescape


class testModFileReader(BaseTest):
    def test_check_strname_encoded_in_xml_file_after_parsing(self):
        filename = self.unpack_filename('sample_files/frankies_wild_ride/treasuretable.xml')
        escape_dir = {'\'': '&apos;'}
        escape_reverse = {'&apos;': '\''}

        foo = ModFileReader(filename)
        root = foo.modfile.getroot()
        # dig out strName fields and check they have been htmlencoded
        for child in root.iter('column'):
            if 'strName' == child.attrib['name']:
                child_text = child.text
                returned = unescape(child_text, escape_reverse)
                remix_text = escape(returned, escape_dir)

                self.assertEqual(remix_text, child_text, "strName content should be escaped after read-in")


if __name__ == '__main__':
    unittest.main()
