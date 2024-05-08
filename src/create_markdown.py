import json
from jinja2 import Environment, FileSystemLoader

def generate_markdown_from_projects(template_file, projects, output_file, templates_dir='templates'):
    """
    Generates Markdown content using Jinja2 template and project data.

    Args:
    template_file (str): The file path of the Jinja2 template.
    projects (list): A list of dictionaries containing project data.
    output_file (str): The file path where the generated Markdown will be saved.
    templates_dir (str, optional): The directory containing Jinja2 templates. Defaults to 'templates'.
    """
    # Configure Jinja2 environment to load the template from the specified directory
    env = Environment(loader=FileSystemLoader(templates_dir))

    # Load the template from the specified file
    template = env.get_template(template_file)

    # Render the template with the project data
    markdown_output = template.render(projects=projects)

    # Write the generated content to the output file using UTF-8 encoding
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_output)


def generate_markdown_from_content(template_file, content, output_file, templates_dir='templates'):
    """
    Generates Markdown content using Jinja2 template and provided content.

    Args:
    template_file (str): The file path of the Jinja2 template.
    content (str): The content to be inserted into the template.
    output_file (str): The file path where the generated Markdown will be saved.
    templates_dir (str, optional): The directory containing Jinja2 templates. Defaults to 'templates'.
    """
    # Configure Jinja2 environment to load the template from the specified directory
    env = Environment(loader=FileSystemLoader(templates_dir))

    # Load the template from the specified file
    template = env.get_template(template_file)

    # Render the template with the provided content
    markdown_output = template.render(text=content)

    # Write the generated content to the output file using UTF-8 encoding
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_output)