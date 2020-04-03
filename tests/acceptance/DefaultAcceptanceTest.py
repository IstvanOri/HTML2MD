import difflib
import os
import unittest

from html2md import LOCATIONS, runner


class DefaultAcceptanceTest(unittest.TestCase):

    def run_case(self, file_name):
        converted = runner.convert(LOCATIONS["SAMPLES"] + os.sep + file_name)
        etalon = open(LOCATIONS["SAMPLES_DEFAULT"] + os.sep + file_name.replace(".html", ".md"), "r")
#        self.write_debug_file(converted, file_name)
        etalon_content = etalon.read()
        etalon.close()
        self.assertEqual(etalon_content, converted)

#    def write_debug_file(self, converted, file_name):
#        debug = open(file_name.replace(".html", ".md.dbg"), "wb")
#        debug.write(converted.encode('utf-8'))
#        debug.flush()
#        debug.close()

    def test_basic_document(self):
        self.run_case("basic_document.html")

    def test_headings(self):
        self.run_case("headings.html")

    def test_paragraphs(self):
        self.run_case("paragraphs.html")

    def test_basic_link(self):
        self.run_case("basic_link.html")

    def test_basic_image(self):
        self.run_case("basic_image.html")

    def test_lists(self):
        self.run_case("lists.html")

    def test_tables(self):
        self.run_case("tables.html")
