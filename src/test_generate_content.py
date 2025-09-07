import unittest

from generate_content import extract_title


class TestExtractTitle(unittest.TestCase):
	def test_eq(self):
		h1_title = extract_title("# This is a h1 title")
		self.assertEqual("This is a h1 title", h1_title)

	def test_eq_multi(self):
		h1_title = extract_title(
"""
# This is a h1 title

# and another one
"""
		)
		self.assertEqual("This is a h1 title", h1_title)