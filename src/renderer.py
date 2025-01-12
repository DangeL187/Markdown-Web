import re

js_vars = []

block_quote_icons_and_colors = {
    'note': ('bi-info-circle', '#1f6feb'),
    'tip': ('bi-lightbulb', '#238636'),
    'important': ('bi-fire', '#8957e5'),
    'warning': ('bi-exclamation-triangle', '#9e6a03'),
    'caution': ('bi-exclamation-octagon', '#da3633')
}


def parse_css_style(style: str) -> dict:
    pattern = r"([\w-]+)\s*:\s*([^;]+)\s*;"
    matches = re.findall(pattern, style)
    return {key.strip(): value.strip() for key, value in matches}


def parse_block(line):
    if line[0] != '{':
        return None

    end_brace = line.find("}", 0)
    if end_brace == -1:
        return None

    start_parens = end_brace + 1
    if start_parens >= len(line) or line[start_parens] != "(":
        return None

    end_parens = line.find(")", start_parens)
    if end_parens == -1:
        return None

    name = line[1:end_brace]
    params = line[start_parens + 1:end_parens]
    return [name, parse_css_style(params)]


def parse_element(line):
    if not line:
        return None

    if line[0] != '{':
        return None

    end_brace = line.find("}", 0)
    if end_brace == -1:
        return None

    return line[1:end_brace]


def expand_element(element, blocks):
    parsed_element = parse_element(element)
    if parsed_element is not None and parsed_element in blocks:
        new_content = [parsed_element, blocks[parsed_element][0]]
        for _ in blocks[parsed_element][1:]:
            new_content.append(expand_element(_, blocks))
        return new_content
    else:
        return element


def extract_blocks(md_it, md_text):
    """
    :param md_it: Markdown-it parser object
    :param md_text: Markdown text
    :return: Cleared text and extracted blocks
    """
    rendered_text = []

    blocks = {' ': [{}, '&nbsp;']}
    current_block = None

    is_block_quote = False
    is_code = False
    is_list = False

    i_prefix = ''

    md_text_lines = md_text.split('\n')

    for idx, i in enumerate(md_text_lines):
        if (i.lstrip().startswith('- ') or bool(re.match(r"^\d+\.\s", i.lstrip()))) and not is_code:
            md_rendered = ''
            checked = ''
            if i.lstrip().startswith('- [ ] '):
                md_rendered = md_it.render(i.split("- [ ] ")[1])
            elif i.lstrip().startswith('- [X] '):
                md_rendered = md_it.render(i.split("- [X] ")[1])
                checked = 'checked'
            elif i.lstrip().startswith('- [x] '):
                md_rendered = md_it.render(i.split("- [x] ")[1])
                checked = 'checked'

            if md_rendered:
                md_rendered = re.sub(r'<p>(.*?)</p>', r'\1', md_rendered)
                i = (f'<div style="padding-left: 0.8em;">'
                     f'<input type="checkbox" disabled="" class="task-list-item-checkbox" {checked}>'
                     f'<label>&nbsp;{md_rendered}</label>'
                     f'</div>')
            is_list = True
        # else:
        # if is_list:
        #     i_prefix = '<!---->\n\n'
        # is_list = False

        if i.lstrip().startswith('>') and not is_code:
            is_custom_block_quote = bool(re.match(r"> \[!.*]", i.lstrip()))
            if not is_custom_block_quote:
                i = md_it.render('>'.join(i.lstrip().split(">")[1:]))

            i = f'<p>{i}</p>'

            if not is_block_quote:
                icon, color = '', '#7a8088'

                if is_custom_block_quote:
                    block_quote_type = i.lstrip().split("[")[1].split("]")[0][1:].lower()
                    if '{' in block_quote_type and '}' in block_quote_type:
                        color_and_icon = re.findall(r'\{(.*?)}', block_quote_type)[0]
                        block_quote_type = block_quote_type.replace(f'{{{color_and_icon}}}', '')
                        color_and_icon = color_and_icon.replace(' ', '').split(',')
                        color, icon = color_and_icon[0], 'bi-' + color_and_icon[1]
                    elif block_quote_type in block_quote_icons_and_colors:
                        icon, color = block_quote_icons_and_colors[block_quote_type]

                    i = f'<i class="bi {icon}" style="margin-bottom: 1rem; color: {color}">{block_quote_type.capitalize()}</i>'
                i_prefix = f'<blockquote style="border-color: {color}">'
                is_block_quote = True
        elif not is_code:
            if is_block_quote:
                i_prefix = '</blockquote>\n<!---->\n\n'
            is_block_quote = False

        if i.lstrip().startswith('```'):
            if is_code:
                i += '\n<!-- </div> -->'
                is_code = False
            else:
                i_prefix = ('<!-- <div class="code-item" style="position: relative;"> -->\n'
                            '<!-- <i class="bi bi-copy bordered-2"'
                            ' style="padding-bottom: 0.25rem; padding-top: 0.25rem; padding-left: 0.5rem; position: absolute; top: 0.5rem; right: 0.5rem;"'
                            ' onclick="copyCodeToClipboard(event)"></i> -->\n')
                is_code = True

        if not is_code:
            i = re.sub(r"~~(.*?)~~", r"<s>\1</s>", i)
            i = re.sub(r'(?<!\\)~(.*?)~', r'<i class="bi bi-\1" style="margin-right: -0.5rem;"></i>', i)
            i = re.sub(r"\+\+(.*?)\+\+", r"<u>\1</u>", i)
            i = re.sub(r'\[(.*?)]\((.*?)\)\{(.*?)}', r'<a class="a-\3" href="\2">\1</a>', i)

        if i == '{}' and not is_block_quote and not is_code and not is_list:
            if current_block is not None:
                if i_prefix:
                    blocks[current_block].append(i_prefix)
                current_block = None
            elif i_prefix:
                rendered_text.append(i_prefix)
            i_prefix = ''
            continue

        if i == '':
            if (len(md_text_lines) > 1
                    and not md_text_lines[idx - 1].startswith('---')
                    and not md_text_lines[idx + 1].startswith('---')
                    and not md_text_lines[idx - 1].startswith('>')
                    and not is_list
                    and not is_code
                    and not is_block_quote
            ):
                i = '<p>&nbsp;</p>\n'

            if is_list:
                # i_prefix = '<!---->\n\n'
                is_list = False

            if current_block is not None:
                blocks[current_block].append(i_prefix + i)
                i_prefix = ''
            elif md_text_lines[idx - 1] != '{}':
                rendered_text.append(i_prefix + i)
                i_prefix = ''
            continue

        i = i_prefix + i
        i_prefix = ''

        block_info = None
        if not is_block_quote and not is_list and not is_code:
            block_info = parse_block(i)
        elif re.match(r'\{(.*?)}', i):
            i = '\\' + i

        if block_info is None:
            if current_block is not None:
                blocks[current_block].append(i)
            else:
                rendered_text.append(i)
            continue

        current_block = block_info[0]
        blocks[current_block] = [block_info[1]]

    return '\n'.join(rendered_text), blocks


def remove_comments_outside_code_blocks(text):
    code_blocks_ranges = []
    new_text = []

    code_block_range = [-1, -1]

    text = text.split('\n')

    for i, line in enumerate(text):
        if line.startswith('```'):
            if code_block_range[0] == -1:
                code_block_range[0] = i
            else:
                code_block_range[1] = i
        if -1 not in code_block_range:
            code_blocks_ranges.append(code_block_range)
            code_block_range = [-1, -1]

    for i, line in enumerate(text):
        if line.lstrip().startswith('//'):
            for code_block_range in code_blocks_ranges:
                if code_block_range[0] < i < code_block_range[1]:
                    new_text.append(line)
                    break
        else:
            new_text.append(line)

    return '\n'.join(new_text)


def render_element(element):
    if isinstance(element, list):
        new_element = []

        is_grid = 'grid' in element[1]

        class_style, css_style, link, tag_id = render_style(element[1])

        tag_id = element[0]

        if link[0]:
            new_element.append('<!-- <div> -->')
            new_element.append(f'<!-- <a class="{link[0]}" href={link[1]}> -->')
            new_element.append(f'<!-- <div id={tag_id} class="{class_style}" style="height: 100%; {css_style}"> -->')
        else:
            new_element.append(f'<!-- <div id={tag_id} class="{class_style}" style="{css_style}"> -->')

        for i in element[2:]:
            new_i = render_element(i)
            if is_grid:
                new_i += '\n'
            new_element.append(new_i)

        if link[0]:
            new_element.append('<!-- </div> -->')
            new_element.append('<!-- </a> -->')
            new_element.append('<!-- </div> -->')
        else:
            new_element.append('<!-- </div> -->')
        return '\n'.join(new_element)
    else:
        return element


def render_style(style):
    global js_vars

    class_style = ''
    css_style = ''
    tag_id = '""'
    link = ['', '']  # [link_class, href]

    for i in style:
        if re.match(r'--([\w-]+)', style[i]):
            var_name_and_param = style[i].split('--')[1].split('-')
            name, param = var_name_and_param[0], var_name_and_param[1]
            if param in ['height', 'width']:
                if [name, param] not in js_vars:
                    js_vars.append([name, param])
                style[i] = re.sub(r'--([\w-]+)', r'var(--\1)', style[i])

        if i == 'a':
            if style[i].isdigit():
                link[0] = f'a-{style[i]}'
        elif i == 'scroll-mt':
            css_style += f'scroll-margin-top: {style[i]};'
        elif i == 'id':
            tag_id = style[i]
        elif i == 'size':
            if style[i].isdigit():
                class_style += f'fs-{style[i]} '
        elif i == 'href':
            link[1] = style[i]
            if not link[0]:
                link[0] = 'a-'
        elif i == 'align':
            if style[i] == 'left':
                css_style += 'display: grid;'
                css_style += 'justify-content: flex-start;'
            elif style[i] == 'right':
                css_style += 'display: grid;'
                css_style += 'justify-content: flex-end;'
            elif style[i] == 'center':
                css_style += 'display: grid;'
                css_style += 'justify-content: center;'
        elif i == 'align-v':
            if style[i] == 'left':
                css_style += 'display: grid;'
                css_style += 'align-items: flex-start;'
            elif style[i] == 'right':
                css_style += 'display: grid;'
                css_style += 'align-items: flex-end;'
            elif style[i] == 'center':
                css_style += 'display: grid;'
                css_style += 'align-items: center;'
        elif i == 'align-text':
            css_style += f'text-align: {style[i]};'
        elif i == 'bg-color':
            css_style += f'background-color: {style[i]};'
        elif i == 'border':
            class_style += f'bordered-{style[i]} '
        elif i == 'color':
            css_style += f'color: {style[i]};'
        elif i == 'gap':
            class_style += f'gap-{style[i]} '
        elif i == 'grid':
            grid = style[i].split('-')
            grid.append('')
            grid = f'grid-template-columns: {"fr ".join(grid)};'
            grid = grid.replace('afr', 'auto')

            css_style += 'display: grid;'
            css_style += grid
            class_style += 'grid-with-scrollable-cols '
        elif i == 'height':
            css_style += f'height: {style[i]};'
        elif i == 'p':
            class_style += f'p-{style[i]} '
        elif i == 'pos':
            css_style += f'position: {style[i]};'
        elif i == 'scroll':
            if style[i] == 'true':
                css_style += 'overflow: scroll;'
                css_style += 'pointer-events: auto;'
            elif style[i] == 'false':
                css_style += 'overflow: hidden;'
        elif i == 'sticky-top':
            css_style += 'position: sticky;'
            css_style += 'top: 0;'
            css_style += 'z-index: 1020;'
        elif i == 'width':
            css_style += f'width: {style[i]};'
        elif i == 'z':
            css_style += f'z-index: {style[i]};'

    return class_style, css_style, link, tag_id


def render(md_text, blocks):
    # for i in blocks:
    #     print(i, blocks[i])

    rendered_text = []

    for i in md_text.split('\n'):
        element = expand_element(i, blocks)
        element = render_element(element)

        rendered_text.append(element)

    return '\n'.join(rendered_text), js_vars
