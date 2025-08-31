import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is not equal", TextType.ITALIC)
        node2 = TextNode("not equal", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_url_none(self):
        node = TextNode("url = None", TextType.LINK, None)
        node2 = TextNode("url = None", TextType.LINK, None)
        self.assertEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("different url", TextType.LINK, "https://some.domain.com")
        node2 = TextNode("different url", TextType.LINK, "somedifferent.domain.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_texttype(self):
        node = TextNode("different text_type", TextType.IMAGE)
        node2 = TextNode("different text_type", TextType.BOLD)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
