from os.path import join
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def read_template(template_name: str, data: dict):
    try:
        env = Environment(loader=FileSystemLoader(
            join(Path().absolute(), 'src\\static\\templates')))
        template = env.get_template(f'{template_name}.html')
        output = template.render(data)
        return output
    except Exception as e:
        raise e
