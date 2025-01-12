// HEADER_START
{logo}(size: 2; align: left; p: 2;)
&nbsp;&nbsp;[~markdown~-Web](https://dangel187.github.io/markdown-web.github.io/){1}
{}

{links}(align-v: center; align: right; p: 3; grid: a-a-a; gap: 4; size: 4;)
[Get started](/markdown-web.github.io/get-started){1}
[Guides](/markdown-web.github.io/guides){1}
[~github~](https://github.com/DangeL187/Markdown-Web){1}
{}

{header}(bg-color: #010409; grid: a-a; sticky-top: true;)
{logo}
{links}
{}
// HEADER_END

// SIDE_PANEL_START
{side_panel_links_before}(border: 3-0;)
~rocket~ [Get Started](/markdown-web.github.io/get-started){1}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~shift~ [Setup](/markdown-web.github.io/get-started/setup){1}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~signpost~ [Basics](/markdown-web.github.io/get-started/basics){1}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~tools~ [How it Works](/markdown-web.github.io/get-started/how-it-works){1}
~journal-text~ [Guides](/markdown-web.github.io/guides){1}
{}

{current_page_name}(border: 3;)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~code~ [Markdown Syntax](/markdown-web.github.io/guides/md-syntax){1}
{}

{side_panel_links_after}(border: 3-0;)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~code-slash~ [Advanced Syntax](/markdown-web.github.io/guides/advanced-syntax){1}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~braces~ [Components](/markdown-web.github.io/guides/components){1}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~layout-text-window-reverse~ [Advanced Usage](/markdown-web.github.io/guides/advanced_usage){1}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~bug~ [Limitations](/markdown-web.github.io/guides/limitations){1}
{}

{side_panel}(p: 3; scroll: true; border: 1-0;)
{side_panel_links_before}
{current_page_name}
{side_panel_links_after}
{}
// SIDE_PANEL_END

{toc}(p: 3; scroll: true;)
##### Table of contents
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Paragraphs](#h_p){2}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Blank Lines](#h_blank_lines){2}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Heading](#h_heading){2}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Emphasis](#h_emphasis){2}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Blockquotes](#h_blockquotes){2}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Lists](#h_lists){2}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Code](#h_code){2}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Horizontal Rule](#h_hr){2}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Links](#h_links){2}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Images](#h_images){2}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Tables](#h_tables){2}

// Comments
// Custom links
// Underlining, strikethrough
// Icons
// Custom BQs
// Styles
{}

{overlay}(height: 100%; width: 100%; pos: fixed; grid: 1-3-2;)
{side_panel}
{ }
{toc}
{}

{side_panel_bg}(z: -1;)
{}

{next}(p: 3; border: 1; href: "/markdown-web.github.io/guides/advanced-syntax"; a: 0;)
#### ~code-slash~ **Advanced Syntax**
Learn how to use advanced Markdown syntax in Markdown-Web.
{}

{info}(color: #9198a1; align-text: center;)
~emoji-surprise~ This page was fully generated using Markdown-Web!
{}

// HEADINGS_START
{h_p}(scroll-mt: --header-height;)
# Paragraphs
{}

{h_blank_lines}(scroll-mt: --header-height;)
# Blank Lines
{}

{h_heading}(scroll-mt: --header-height;)
# Heading
{}

{h_emphasis}(scroll-mt: --header-height;)
# Emphasis
{}

{h_blockquotes}(scroll-mt: --header-height;)
# Blockquotes
{}

{h_lists}(scroll-mt: --header-height;)
# Lists
{}

{h_code}(scroll-mt: --header-height;)
# Code
{}

{h_hr}(scroll-mt: --header-height;)
# Horizontal Rule
{}

{h_links}(scroll-mt: --header-height;)
# Links
{}

{h_images}(scroll-mt: --header-height;)
# Images
{}

{h_tables}(scroll-mt: --header-height;)
# Tables
{}
// HEADINGS_END

// RESULTS_START
{p_result}(p: 3; border: 1-0;)
Paragraph1 and text in it
Paragraph2 and text in it
\<h1>\</h1>
{}

{heading_result}(p: 3; border: 1-0;)
# Heading level 1
## Heading level 2
### Heading level 3
#### Heading level 4
##### Heading level 5
###### Heading level 6
{}

{emphasis_result}(p: 3; border: 1-0;)
*Italic*
_Italic2_
**Bold**
__Bold2__
{}

{blockquotes_result}(p: 3; border: 1-0;)
> This is a blockquote
> And text in it

> Blockquotes are separated with a blank line
> 
> Empty lines inside a blockquote are being ignored
> &nbsp;
> But you can add them using `&nbsp;`

> Blockquotes can be nested
>> Like that
> > Or like that

{}

{lists_result}(p: 3; border: 1-0;)
- Item1
- Item2


1. Item1
2. Item2


- [x] Item1
- [X] Item2
- [ ] Item3

{}

{code_result}(p: 3; border: 1-0;)
`this is code`
{}

{code_block_result}(p: 3; border: 1-0;)
```python
def f():
    print('Hello')
```
{}

{hr_result}(p: 3; border: 1-0;)
***

---

___
{}

{links_result}(p: 3; border: 1-0;)
[Link Text](https://google.com)
{}

{images_result}(p: 3; border: 1-0;)
![Image Text](https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png)
{}

{tables_result}(p: 3; border: 1-0;)
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |
{}
// RESULTS_END

{page}(p: 4;)
# **Markdown Syntax**
Learn how to use basic Markdown syntax in Markdown-Web.

---

{h_p}
> [!Important]
> HTML tags, such as `<...>` and `</...>`, might be recognized by the parser.
> In order to prevent this, please use the `\<...>` and `\</...>` syntax.
> For example, use `\<h1>` instead of `<h1>`

Code:
```markdown
Paragraph1 and text in it
Paragraph2 and text in it
\<h1>\</h1>
```
Result:
{p_result}

{h_blank_lines}
**Blank lines** are used in several situations in the syntax:
1. Before and after **horizontal rules**.
2. After a **blockquote**.
3. Following the declaration of a **component**.
4. Within and after a **list**.


You don't need to worry about it for now. You will understand it better when you learn other elements.

{h_heading}
To create a heading, add number signs (`#`) in front of a word or phrase.
The number of number signs you use should correspond to the heading level.
For example, to create a heading level three `<h3>`, use three number signs (e.g., `### My Header`).

By default, headings are **not** bold.

Code:
```markdown
# Heading level 1
## Heading level 2
### Heading level 3
#### Heading level 4
##### Heading level 5
###### Heading level 6
```
Result:
{heading_result}

{h_emphasis}
You can add emphasis by making text bold or italic.

Code:
```markdown
*Italic*
_Italic2_
**Bold**
__Bold2__
```
Result:
{emphasis_result}

There is also underlining and strikethrough text, which are described in the `Advanced Syntax` section.

{h_blockquotes}

Code:
```markdown
> This is a blockquote
> And text in it

> Blockquotes are separated with a blank line
> 
> Empty lines inside a blockquote are being ignored
> &nbsp;
> But you can add them using `&nbsp;`

> Blockquotes can be nested
>> Like that
> > Or like that
```
Result:
{blockquotes_result}

{h_lists}
You can organize items into ordered, unordered and task lists.

Code:
```markdown
- Item1
- Item2


1. Item1
2. Item2


- [x] Item1
- [X] Item2
- [ ] Item3
```
Result:
{lists_result}

{h_code}
To denote a word or phrase as code, enclose it in backticks `.

Code:
```markdown
`this is code`
```
Result:
{code_result}

You can also create code blocks.
> [!Important]
> Code tags inside the code blocks, such as ( ``` ), might be recognized by the parser.
> In order to prevent this, please use the ( \\\\``` ) syntax.

Code:
```markdown
\```python
def f():
    print('Hello')
\```
```
Result:
{code_block_result}

{h_hr}
To create a horizontal rule, use three or more asterisks `***`, dashes `---`, or underscores `___` on a line by themselves.

Code:
```markdown
***

---

___
```
Result:
{hr_result}

{h_links}

Code:
```markdown
[Link Text](https://google.com)
```
Result:
{links_result}

{h_images}

Code:
```markdown
![Image Text](https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png)       
```
Result:
{images_result}

{h_tables}

Code:
```markdown
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |
```
Result:
{tables_result}

---
{next}


{info}
{}

{main}(grid: 1-3-2;)
{side_panel_bg}
{page}
{}

// FINAL RESULT:
{header}
{overlay}
{main}