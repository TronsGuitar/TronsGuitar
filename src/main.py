import os
from loguru import logger
from src.create_markdown import generate_markdown_from_projects, generate_markdown_from_content
from src.get_data import parse_readme_sections, extract_section_from_readme, extract_urls_and_images, parse_readme_subsubsections
from src.get_images import take_screenshot

if __name__ == '__main__':
    logger.info("Read Data")
    path_readme = "README.md"
    path_images = "docs/images/download/"
    path_templates = "templates/"
    path_output = "docs/"
    valid_titles = ['articles','tools']

    with open(path_readme, "r", encoding="utf-8") as file:
        readme_content = file.read()

    logger.info("Parse Readme file")
    parsed_data_sections = parse_readme_sections(readme_content)
    parsed_data_subsubsections = parse_readme_subsubsections(readme_content)
    parsed_data = parsed_data_sections + parsed_data_subsubsections

    logger.info("Extract Images")
    urls_and_images = extract_urls_and_images(parsed_data)
    for url, image_path in urls_and_images.items():
        image_path = path_images + image_path.replace("../images/download/", "")
        # Check if the image already exists
        if not os.path.exists(image_path):
            try:
                # Take screenshot and save to the specified image path
                take_screenshot(url, image_path)
                logger.info(f"Image downloaded: {image_path}")
            except Exception as e:
                logger.warning(f"Error downloading image for URL '{url}': {e}")
        else:
            logger.info(f"Image already exists: {image_path}")


    logger.info("Parse 'Templates' file")
    for i in range(len(parsed_data_sections)):
        data = parsed_data_sections[i]
        title = data['title'].lower()
        if title in valid_titles:
            projects = data['projects']
            generate_markdown_from_projects(f'{title}.md', projects, path_output + f'{title}.md',path_templates)
        elif title == "categories":
            subsections = parsed_data_subsubsections
            generate_markdown_from_projects(f'{title}.md', subsections, path_output + f'{title}.md',path_templates)

    logger.info("Parse 'others.md' file")
    title = 'others'
    content = extract_section_from_readme(readme_content)
    generate_markdown_from_content(f'{title}.md', content, path_output + f'{title}.md', path_templates)




