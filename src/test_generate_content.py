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

	def test_eq_long(self):
		actual = extract_title(
			"""
# title

this is a bunch

of text

- and
- a
- list
"""
		)
		self.assertEqual(actual, "title")

	def test_none(self):
		try:
			extract_title(
"""
no title
"""
			)
			self.fail("Should have raised an exception")
		except Exception as e:
			pass


if __name__ == "__main__":
	unittest.main()