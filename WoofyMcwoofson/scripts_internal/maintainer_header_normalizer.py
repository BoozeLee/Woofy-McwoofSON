def normalize_header(file_path):
    maintainer_info = "Maintained by BoozeLee, 2025-09-08"

    with open(file_path, "r") as file:
        lines = file.readlines()

    # Normalize the header
    for i, line in enumerate(lines):
        if line.startswith("Maintained by"):
            lines[i] = maintainer_info + "\n"
            break
    else:
        # If no maintainer line found, append it
        lines.insert(0, maintainer_info + "\n")

    with open(file_path, "w") as file:
        file.writelines(lines)


def normalize_headers_in_directory(directory):
    import os

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                normalize_header(os.path.join(root, file))


if __name__ == "__main__":
    normalize_headers_in_directory("../docs")  # Adjust path as necessary
