from jinja2 import Environment, PackageLoader


def render(data: dict) -> str:
    """
    Run the jinja2 render according to the parameters defined in the data dictionary.

    :param data: Any complaint biohazard data dictionary.
    :return: string of rendered data
    """
    template_name = data.get('template', 'bio')
    content = data['content']

    env = Environment(
        loader=PackageLoader('biohazard', 'templates'),
    )

    template = env.get_template(template_name + '.html')

    return template.render(**content)
