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
{}

{current_page_name}(border: 3;)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~shift~ [Setup](/markdown-web.github.io/get-started/setup){1}
{}

{side_panel_links_after}(border: 3-0;)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~signpost~ [Basics](/markdown-web.github.io/get-started/basics){1}
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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[How to install](#h_install){2}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[How to run](#h_run){2}
{}

{overlay}(height: 100%; width: 100%; pos: fixed; grid: 1-3-2;)
{side_panel}
{ }
{toc}
{}

{side_panel_bg}(z: -1;)
{}

{next}(p: 3; border: 1; href: "/markdown-web.github.io/get-started/basics"; a: 0;)
#### ~signpost~ **Basics**
Learn Markdown-Web basics.
{}

{info}(color: #9198a1; align-text: center;)
~emoji-surprise~ This page was fully generated using Markdown-Web!
{}

{h_install}(scroll-mt: --header-height;)
# How to install
{}

{h_run}(scroll-mt: --header-height;)
# How to run
{}

{page}(p: 4;)
# **Setup**
This section will guide you through the process of installing and running Markdown-Web.

---

{h_install}
Clone repository:
```bash
git clone https://github.com/DangeL187/Markdown-Web.git
cd Markdown-Web
```
Install the required dependencies:
```bash
pip install markdown-it-py
```

{h_run}
1. Create a new directory and move your `.md` files into it.
2. Run `main.py` with the directory name as an argument.

For example:
```bash
cd src
python main.py MyProject
```
Output of the script will be located in the `output` directory.

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