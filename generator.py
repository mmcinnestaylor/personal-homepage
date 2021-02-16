import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
from errors import error_codes

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment(
	loader=FileSystemLoader(templates_dir),
	autoescape=select_autoescape(['html'])
)

for dirName, subdirList, fileList in os.walk(templates_dir):
	for fname in fileList:
		template = env.get_template(fname)

		if fname == 'error.html':
			for code, description in error_codes.items():
				filename = os.path.join(root, 'production', code + '.html')

				with open(filename, 'w') as fh:
					fh.write(template.render(error_code=code, error_description=description))
		else:
			filename = os.path.join(root, 'production', fname)

			with open(filename, 'w') as fh:
				fh.write(template.render())
