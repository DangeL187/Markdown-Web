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
{}

{current_page_name}(border: 3;)
~journal-text~ [Guides](/markdown-web.github.io/guides){1}
{}

{side_panel_links_after}(border: 3-0;)
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

{overlay}(height: 100%; width: 100%; pos: fixed; grid: 1-5;)
{side_panel}
{}

{side_panel_bg}(z: -1;)
{}

{md_syntax}(p: 3; border: 1; href: "/markdown-web.github.io/guides/md-syntax"; a: 0;)
#### ~code~ **Markdown Syntax**
Learn how to use basic Markdown syntax in Markdown-Web.
{}

{advanced_syntax}(p: 3; border: 1; href: "/markdown-web.github.io/guides/advanced-syntax"; a: 0;)
#### ~code-slash~ **Advanced Syntax**
Learn how to use advanced Markdown syntax in
Markdown-Web.
{}

{components}(p: 3; border: 1; href: "/markdown-web.github.io/guides/components"; a: 0;)
#### ~braces~ **Components**
Learn how to create and use components.
{}

{advanced_usage}(p: 3; border: 1; href: "/markdown-web.github.io/guides/advanced_usage"; a: 0;)
#### ~layout-text-window-reverse~ **Advanced Usage**
Learn how to create complicated components.
{}

{limitations}(p: 3; border: 1; href: "/markdown-web.github.io/guides/limitations"; a: 0;)
#### ~bug~ **Limitations**
Known limitations and bugs of Markdown-Web.
{}

{cells}(grid: 1-1-1; gap: 4;)
{md_syntax}
{advanced_syntax}
{components}
{advanced_usage}
{limitations}
{}

{info}(color: #9198a1; align-text: center;)
~emoji-surprise~ This page was fully generated using Markdown-Web!
{}

{page}(p: 4;)
# **Guides**
Guides on each aspect of creating a website using Markdown-Web.

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