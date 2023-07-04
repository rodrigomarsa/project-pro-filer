"""Arquivo que estudantes devem editar"""


def show_deepest_file(context):
    deepest_file = ""
    depth_max = 0
    if not context["all_files"]:
        return print("No files found")
    for path in context["all_files"]:
        file_name = path.split("/")
        depth = len(file_name)
        if depth > depth_max:
            depth_max = depth
            deepest_file = path
    print(f"Deepest file: {deepest_file}")
    # else:
    #     deepest_file = max(context["all_files"], key=len)
    #     print(f"Deepest file: {deepest_file}")


def find_file_by_name(context, search_term, case_sensitive=True):
    if not search_term:
        return []

    found_files = []

    for path in context["all_files"]:
        file_name = path.split("/")[-1]

        if not case_sensitive:
            file_name.lower()
            search_term.lower()

        if search_term in file_name:
            found_files.append(path)

    return found_files
