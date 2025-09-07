import os
import shutil


def copy_files_recursive(src_dir_path, dst_dir_path):
	if not os.path.exists(dst_dir_path):
		os.mkdir(dst_dir_path)

	for filename in os.listdir(src_dir_path):
		src_path = os.path.join(src_dir_path, filename)
		dst_path = os.path.join(dst_dir_path, filename)
		print(f" copying: {src_path} -> {dst_path}")
		if os.path.isfile(src_path):
			shutil.copy(src_path, dst_path)
		else:
			copy_files_recursive(src_path, dst_path)
