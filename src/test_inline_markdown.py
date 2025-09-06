import unittest

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_links,
    extract_markdown_images,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)

from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )


    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_unmatched_raises(self):
        node = TextNode("This is **broken", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_leading_trailing(self):
        node = TextNode("**start** mid **end**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("start", TextType.BOLD),
                TextNode(" mid ", TextType.TEXT),
                TextNode("end", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/something.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/something.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is a text with a [link](https://some.domain.com) and [another one](https://cant.thinkof.more)"
        )
        self.assertListEqual(
            [
                ("link", "https://some.domain.com"),
                ("another one", "https://cant.thinkof.more"),
            ],
            matches,
        )

    
    def test_split_image(self):
        node = TextNode(
            "This is a text with a single ![image](https://link.to.image)", TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            [
                TextNode("This is a text with a single ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://link.to.image"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_link(self):
        node = TextNode(
            "This is a text with a [link](https://link.to.localhost)",
            TextType.TEXT,
            )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("This is a text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://link.to.localhost"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://link.to.localhost) and another [link](https://link.to.raspi)", TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://link.to.localhost"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://link.to.raspi"),
            ],
            new_nodes,
        )

    def test_split_image(self):
        node = TextNode(
            "This is a text with a single ![image](https://link.to.image)", TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            [
                TextNode("This is a text with a single ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://link.to.image"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_link(self):
        node = TextNode(
            "This is a text with a [link](https://link.to.localhost)",
            TextType.TEXT,
            )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("This is a text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://link.to.localhost"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://link.to.localhost) and another [link](https://link.to.raspi)", TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://link.to.localhost"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://link.to.raspi"),
            ],
            new_nodes,
        )

    def test_no_links_or_images(self):
        node = TextNode("Just plain text", TextType.TEXT)
        self.assertEqual([node], split_nodes_link([node]))
        self.assertEqual([node], split_nodes_image([node]))

    def test_trailing_text_after_link(self):
        node = TextNode("[site](https://a.b) end", TextType.TEXT)
        self.assertEqual(
            [
                TextNode("site", TextType.LINK, "https://a.b"),
                TextNode(" end", TextType.TEXT),
            ],
            split_nodes_link([node]),
        )

    def test_mixed_link_then_image(self):
        node = TextNode("[a](u1) and ![b](u2)", TextType.TEXT)
        nodes_after_link = split_nodes_link([node])
        nodes_after_image = split_nodes_image(nodes_after_link)
        self.assertEqual(
            [
                TextNode("a", TextType.LINK, "u1"),
                TextNode(" and ", TextType.TEXT),
                TextNode("b", TextType.IMAGE, "u2"),
            ],
            nodes_after_image,
        )

    def test_text_to_textnode(self):
        nodes = text_to_textnodes(
            "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)", 
        )
        self.assertEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes,
        )

if __name__ == "__main__":
    unittest.main()
