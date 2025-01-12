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
{}

{current_page_name}(border: 3;)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~signpost~ [Basics](/markdown-web.github.io/get-started/basics){1}
{}

{side_panel_links_after}(border: 3-0;)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~tools~ [How it Works](/markdown-web.github.io/get-started/how-it-works){1}
~journal-text~ [Guides](/markdown-web.github.io/guides){1}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~code~ [Markdown Syntax](/markdown-web.github.io/guides/md-syntax){1}
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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[General](#h_general){2}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Start](#h_start){2}
{}

{overlay}(height: 100%; width: 100%; pos: fixed; grid: 1-3-2;)
{side_panel}
{ }
{toc}
{}

{side_panel_bg}(z: -1;)
{}

{next}(p: 3; border: 1; href: "/markdown-web.github.io/guides"; a: 0;)
#### ~journal-text~ **Guides**
All the information you need to create a website using Markdown-Web is provided here!
{}

{info}(color: #9198a1; align-text: center;)
~emoji-surprise~ This page was fully generated using Markdown-Web!
{}

{h_general}(scroll-mt: --header-height;)
# General
{}

{h_start}(scroll-mt: --header-height;)
# Start
{}

{page}(p: 4;)
# **Basics**
This section will provide you with all the basic information you need to use Markdown-Web.

---

{h_general}
**Markdown-Web** is written in `Python` and allows you to easily create web pages using the familiar Markdown syntax, with a few additional features.

Besides the converting Markdown to HTML code, it provides advanced features such as:
- Creating **components** for further reuse
- **Icons**
- Customizing **components** using CSS-like styling
- Customizable **links**
- Customizable **block quotes**


It is also powerful enough to create **sidebars** and **headers**!

{h_start}
Let's create your first web page using Markdown-Web!
```markdown
# Hello World
This is my first web page written using Markdown-Web.
```

1. Copy this code into a `.md` file.
2. Create a new directory called `MyFirstPage` and move the file into it.
3. Convert it to HTML using Markdown-Web:
```bash
python main.py MyFirstPage
```


Now, all `.md` files in the `MyFirstPage` directory have been converted to HTML.
You can find them in the `output` directory.

Check out the section `Guides` to learn more!

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