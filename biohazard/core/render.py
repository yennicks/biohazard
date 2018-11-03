from jinja2 import Environment, PackageLoader, select_autoescape


def render(data: dict) -> str:
    template_name = data.get('template', 'bio')
    content = data['content']

    env = Environment(
        loader=PackageLoader('biohazard', 'templates'),
        autoescape=select_autoescape(['html'])
    )

    template = env.get_template(template_name + '.html')

    return template.render(**content)
