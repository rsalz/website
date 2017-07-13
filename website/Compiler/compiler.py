import re
import argparse
import pyperclip

# Object to contain all constants
class COMPILER_CONST(object):
	TEMPLATE_FILE = 'template.html'
	RE_BODY = re.compile(r'<body>(.*)<\/body>', re.DOTALL)

def LogError(message):
	print '[ERROR]: {message}'.format(message=message)


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-html', required=True, help='markup file')
	parser.add_argument('-css', required=True, help='style file')
	parser.add_argument('-js', required=True, help='script file')
	parser.add_argument('-c', action='store_true', help='put output in clipboard')
	parser.add_argument('-o', default='out.html', help='file to output markup to')
	args = parser.parse_args()

	html = ''
	with open(args.html, 'r') as f_html:
		html_full = f_html.read()
		# extract body from html using a regular expression
		matches = COMPILER_CONST.RE_BODY.search(html_full)
		if not matches:
			LogError('No body present in html file: \'{}\''.format(args.html))
			return
		html = matches.group(1)

	css = ''
	with open(args.css, 'r') as f_css:
		css = f_css.read()

	js = ''
	with open(args.js, 'r') as f_js:
		js = f_js.read()


	out_file = ''

	markup = ''
	with open(COMPILER_CONST.TEMPLATE_FILE, 'r') as f_markup:
		markup = f_markup.read()
	
	out_html = markup.format(script=js, style=css, content=html)

	if args.c:
		pyperclip.copy(out_html)

	with open(args.o, 'w') as f_out:
		f_out.write(out_html)

			

if __name__ == '__main__':
	main()