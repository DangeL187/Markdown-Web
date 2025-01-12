import os
import re
import sys

from markdown_it import MarkdownIt

import renderer
import default_template


def render_md_file(file_path, file_dir, file_name):
    with open(file_path, 'r') as f:
        md_page_code = f.read()

    md_it = (
        MarkdownIt('commonmark', {'breaks': True, 'html': True})
        .enable('table')
    )

    md_page_code = renderer.remove_comments_outside_code_blocks(md_page_code)
    md_page_code, blocks = renderer.extract_blocks(md_it, md_page_code)
    md_page_code, js_vars = renderer.render(md_page_code, blocks)

    html_text = md_it.render(md_page_code)

    html_text = re.sub(r'<!--\s*(<a.*?>)\s*-->', r'\1', html_text)
    html_text = re.sub(r'<!--\s*(<div.*?>)\s*-->', r'\1', html_text)
    html_text = re.sub(r'<!--\s*(<i.*?>)\s* -->', r'\1', html_text)
    html_text = re.sub(r'\\\{(.*?)}', r'{\1}', html_text)
    html_text = html_text.replace('<!-- </div> -->', '</div>')
    html_text = html_text.replace('<!-- </a> -->', '</a>')
    html_text = html_text.replace('\n</code></pre>', '</code></pre>')
    html_text = html_text.replace('\\~', '~')
    html_text = html_text.replace('\\/', '/')
    html_text = html_text.replace('\\`', '`')
    html_text = html_text.replace('\|', '|')

    html_text = default_template.html_start(js_vars) + html_text + default_template.html_end(js_vars)

    output_dir = os.path.join('output', file_dir)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(os.path.join(output_dir, file_name.split('.md')[0] + '.html'), 'w') as f:
        f.write(html_text)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python main.py [DIRECTORY]')
        exit(1)

    for root, _, files in os.walk(sys.argv[1]):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                try:
                    render_md_file(path, root, file)
                    print(f'[OK] "{path}" was successfully rendered!')
                except Exception as e:
                    print(f'[FAIL] Failed to render "{path}": {e}')
