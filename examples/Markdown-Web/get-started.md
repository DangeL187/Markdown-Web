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
{current_page_name}(border: 3;)
~rocket~ [Get Started](/markdown-web.github.io/get-started){1}
{}

{side_panel_links}(border: 3-0;)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~shift~ [Setup](/markdown-web.github.io/get-started/setup){1}
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
{current_page_name}
{side_panel_links}
{}
// SIDE_PANEL_END

{overlay}(height: 100%; width: 100%; pos: fixed; grid: 1-5;)
{side_panel}
{}

{side_panel_bg}(z: -1;)
{}

{setup}(p: 3; border: 1; href: "/markdown-web.github.io/get-started/setup"; a: 0;)
#### ~shift~ **Setup**
How to get and run
Markdown-Web.
{}

{basics}(p: 3; border: 1; href: "/markdown-web.github.io/get-started/basics"; a: 0;)
#### ~signpost~ **Basics**
Learn Markdown-Web basics.
{}

{how_it_works}(p: 3; border: 1; href: "/markdown-web.github.io/get-started/how-it-works"; a: 0;)
#### ~tools~ **How it Works**
Advanced information about how the Markdown-Web works under the hood.
{}

{cells}(grid: 1-1-1; gap: 4;)
{setup}
{basics}
{how_it_works}
{}

{info}(color: #9198a1; align-text: center;)
~emoji-surprise~ This page was fully generated using Markdown-Web!
{}

{page}(p: 4;)
# **Get Started**
If you're new to Markdown-Web, this section guides you through the essential resources to get started.

---
{cells}


{info}
{}

{main}(grid: 1-3-2;)
{side_panel_bg}
{page}
{ }
{}

// FINAL RESULT:
{header}
{overlay}
{main}