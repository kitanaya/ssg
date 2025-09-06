import unittest

from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType


class TestMarkdownToBlocks:
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

def test_block_to_block_type(self):
	block = "# heading"
	self.assertEqual(block_to_block_type(block), BlockType.HEADING)
	block = "```\ncode\n```"
	self.assertEqual(block_to_block_type(block), BlockType.CODE)
	block = "> quote"
	self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
	block = "- u\n- l\n- i\n- s\n- t"
	self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
	block = "1. o\n2. l\n3. i\n4. s\n5. t"
	self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
	block = "paragraph"
	self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

	# Edge Cases
	block = "#NoSpace"
	self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
	block = "```\ncode"
	self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
	block = "> a\na"
	self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
	block = "-a\n- b"
	self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
	block = "1. a\n3. b"
	self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
	block = "####### too many"
	self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)



if __name__ == "__main__":
	unittest.main()