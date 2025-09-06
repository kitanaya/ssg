from enum import Enum

class BlockType(Enum):
	PARAGRAPH = "paragraph"
	HEADING = "heading"
	CODE = "code"
	QUOTE = "quote"
	UNORDERED_LIST = "unordered_list"
	ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
	blocks = markdown.split("\n\n")
	stripped = []
	for block in blocks:
		if not block:
			continue
		stripped.append(block.strip())
	return stripped


def block_to_block_type(block):
	lines = block.split("\n")

	if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
		return BlockType.HEADING
	
#	if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
	if block.startswith("```") and block.endswith("```"):
		return BlockType.CODE
	
	if all(line.startswith(">") for line in lines):
		return BlockType.QUOTE
	
	if all(line.startswith("- ") for line in lines):
		return BlockType.UNORDERED_LIST

	if all(line.startswith(f"{i}. ") for i, line in enumerate(lines, start=1)):
		return BlockType.ORDERED_LIST

	return BlockType.PARAGRAPH
