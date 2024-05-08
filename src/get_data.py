import re

def parse_readme_sections(readme_content):
    """
    Parses the contents of a README file and extracts sections and projects.

    Args:
    readme_content (str): The content of the README file.

    Returns:
    list: A list of dictionaries representing sections and projects.
    """
    pattern = r'##\s+(.*?)\s*\n((?:.|\n)*?)(?=\n##|\Z)'
    matches = re.findall(pattern, readme_content)
    sections = []
    for match in matches:
        section_title = match[0]
        projects_raw = match[1].strip().split("\n- ")
        projects = []
        for project_raw in projects_raw:
            project_match = re.match(r'\[([^\]]+)\]\(([^)]+)\)\s*-\s*(.*)', project_raw)
            if project_match:
                name = project_match.group(1)
                url = project_match.group(2)
                description = project_match.group(3)
                projects.append({
                    "name": name,
                    "url": url,
                    "description": description.strip(),
                    "images": "../images/download/" + name.replace("/","_").replace(".","_").replace(" ","_").replace('"', '')+ ".png"
                })
        sections.append({"title": section_title, "projects": projects})
    return sections


def parse_readme_subsubsections(readme_content):
    """
    Parses the contents of a README file and extracts sections and projects.

    Args:
    readme_content (str): The content of the README file.

    Returns:
    list: A list of dictionaries representing sections and projects.
    """
    pattern = r'####\s+(.*?)\s*\n((?:.|\n)*?)(?=####|\Z)'
    matches = re.findall(pattern, readme_content, re.DOTALL)
    sections = []
    for match in matches:
        section_title = match[0]
        projects_raw = match[1].strip().split("\n- ")
        projects = []
        for project_raw in projects_raw:
            project_match = re.match(r'\[([^\]]+)\]\(([^)]+)\)', project_raw)
            if project_match:
                name = project_match.group(1)
                url = project_match.group(2)
                projects.append({
                    "name": name.strip(),
                    "url": url.strip()+"#readme",
                    "images": "../images/download/" + name.replace("/", "_").replace(".", "_").replace(" ","_").replace('"','') + ".png"

                })
        sections.append({"title": section_title, "projects": projects})
    return sections

def extract_section_from_readme(readme_content):
    """
    Extracts the section starting from '## Creating GIFs' from the README content.

    Args:
    readme_content (str): The content of the README file.

    Returns:
    str: The extracted section including the section header.
    """
    # Define the regex pattern for the '## Creating GIFs' section and everything that follows
    pattern = r'(## Tutorials\s*(?:.|\n)*)'

    # Find all matches
    matches = re.findall(pattern, readme_content)

    # If a match is found, return the content of the section
    if matches:
        return matches[0].strip()
    else:
        return ""  # If the section is not found, return an empty string


def extract_urls_and_images(parsed_data):
    """
    Extracts URLs and images from parsed data.

    Args:
    parsed_data (list): Parsed data containing sections and projects.

    Returns:
    dict: A dictionary containing URLs and images.
    """
    urls_and_images = {}
    for section in parsed_data:
        for project in section['projects']:
            name = project['name']
            url = project['url']
            image = project['images']
            urls_and_images[url] = image
    return urls_and_images

