import markdown

def task_b9(markdown_path: str, html_path: str):
    with open(markdown_path, "r") as file:
        md_content = file.read()
    html_content = markdown.markdown(md_content)
    with open(html_path, "w") as file:
        file.write(html_content)