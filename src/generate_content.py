import os

from pathlib import Path
from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
	lines = markdown.split("\n")
	for line in lines:
		if line.startswith("# "):
			stripped = line.strip()
			return stripped[2:]

	raise Exception("no h1 Title found")


def generate_page(from_path, template_path, dest_path):
	print(f"Generating page from {from_path} to {dest_path} using {template_path}")
	from_file = open(from_path, "r")
	markdown_content = from_file.read()
	from_file.close()

	template_file = open(template_path, "r")
	template_content = template_file.read()
	template_file.close()

	node = markdown_to_html_node(markdown_content)
	html_content = node.to_html()

	title = extract_title(markdown_content)
	template_content = template_content.replace("{{ Title }}", title)
	template_content = template_content.replace("{{ Content }}", html_content)


	dest_dir_path = os.path.dirname(dest_path)
	if dest_dir_path != "":
		os.makedirs(dest_dir_path, exist_ok=True)
	write_content_to_file = open(dest_path, "w")
	write_content_to_file.write(template_content)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
	for filename in os.listdir(dir_path_content):
		from_path = os.path.join(dir_path_content, filename)
		dest_path = os.path.join(dest_dir_path, filename)
		if os.path.isfile(from_path):
			dest_path = Path(dest_path).with_suffix(".html")
			generate_page(from_path, template_path, dest_path)
		else:
			generate_pages_recursive(from_path, template_path, dest_path)
