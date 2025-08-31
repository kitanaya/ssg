import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://some.domain.com"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://some.domain.com"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could fly",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could fly",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What is this",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What is this, children: None, {'class': 'primary'})",
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "click here", {"href": "https://some.domain.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://some.domain.com">click here</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "no tag here")
        self.assertEqual(node.to_html(), "no tag here")

if __name__ == "__main__":
    unittest.main()
