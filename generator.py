from jinja2 import Environment, FileSystemLoader
import os

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment(loader=FileSystemLoader(templates_dir))

for dirName, subdirList, fileList in os.walk(templates_dir):
	for fname in fileList:
		template = env.get_template(fname)

		filename = os.path.join(root, 'html', fname)
		with open(filename, 'w') as fh:
			fh.write(template.render())
