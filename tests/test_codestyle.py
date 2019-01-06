import unittest
import pycodestyle


class TestCodeFormat(unittest.TestCase):

    def test_codestyle_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(ignore=['E701'], max_line_length=160)
        style.input_dir("pykakasi")
        report = style.check_files()
        self.assertEqual(report.total_errors, 0, "Found code style errors (and warnings).")
