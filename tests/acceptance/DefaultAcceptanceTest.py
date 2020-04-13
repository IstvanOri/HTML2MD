import difflib
import os
import unittest

from html2md import LOCATIONS, runner


class DefaultAcceptanceTest(unittest.TestCase):

    def run_case(self, file_name):
        converted = runner.convert(LOCATIONS["SAMPLES"] + os.sep + file_name)
        etalon = open(LOCATIONS["SAMPLES_DEFAULT"] + os.sep + file_name.replace(".html", ".md"), "r")
        self.write_debug_file(converted, file_name)
        etalon_content = etalon.read()
        etalon.close()
        self.assertEqual(etalon_content, converted)

    def write_debug_file(self, converted, file_name):
        debug = open(LOCATIONS["SAMPLES_DEFAULT"] + os.sep + file_name.replace(".html", ".md.dbg"), "wb")
        debug.write(converted.encode('utf-8'))
        debug.flush()
        debug.close()

    def test_basic_document(self):
        self.run_case("basic_document.html")

    def test_headings(self):
        self.run_case("headings.html")

    def test_paragraphs(self):
        self.run_case("paragraphs.html")

    def test_paragraphs2(self):
        self.run_case("paragraphs2.html")

    def test_basic_link(self):
        self.run_case("basic_link.html")

    def test_basic_image(self):
        self.run_case("basic_image.html")

    def test_lists(self):
        self.run_case("lists.html")

    def test_lists_nested(self):
        self.run_case("lists_nested.html")

    def test_lists_nested2(self):
        self.run_case("lists_nested2.html")

    def test_tables(self):
        self.run_case("tables.html")

    def test_table_headings(self):
        self.run_case("table_headings.html")

    def test_table_colspan(self):
        self.run_case("table_colspan.html")

    def test_table_rowspan(self):
        self.run_case("table_rowspan.html")

    def test_html_special_chars(self):
        self.run_case("html_special_chars.html")

    def test_basic_button(self):
        self.run_case("basic_button.html")

    def test_headings_hr(self):
        self.run_case("headings_hr.html")

    def test_line_breaks(self):
        self.run_case("line_breaks.html")

    def test_pre(self):
        self.run_case("pre.html")

    def test_pre_in_table(self):
        self.run_case("pre_in_table.html")

    def test_html_formatting(self):
        self.run_case("html_formatting.html")
