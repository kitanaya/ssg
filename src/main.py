import os
import shutil

from copystatic import copy_files_recursive
from generate_content import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
content_file_path = "./content/index.md"
public_file_path = "./public/index.html"
template_path = "./template.html"


def main():
	print("Deleting public directory...")
	if os.path.exists(dir_path_public):
		shutil.rmtree(dir_path_public)

	print("Copying static files to public directory...")
	copy_files_recursive(dir_path_static, dir_path_public)

	print("Generating page...")
	generate_page(content_file_path, template_path, public_file_path)



main()
