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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~code~ [Markdown Syntax](/markdown-web.github.io/guides/md-syntax){1}
{}

{current_page_name}(border: 3;)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;~code-slash~ [Advanced Syntax](/markdown-web.github.io/guides/advanced-syntax){1}
{}

{side_panel_links_after}(border: 3-0;)
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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Comments](#h_comments){2}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Emphasis](#h_emphasis){2}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Icons](#h_icons){2}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Custom links](#h_custom_links){2}
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Custom Blockquotes](#h_custom_blockquotes){2}
{}

{overlay}(height: 100%; width: 100%; pos: fixed; grid: 1-3-2;)
{side_panel}
{ }
{toc}
{}

{side_panel_bg}(z: -1;)
{}

{next}(p: 3; border: 1; href: "/markdown-web.github.io/guides/components"; a: 0;)
#### ~braces~ **Components**
Learn how to create and use components.
{}

{info}(color: #9198a1; align-text: center;)
~emoji-surprise~ This page was fully generated using Markdown-Web!
{}

// HEADINGS_START
{h_comments}(scroll-mt: --header-height;)
# Comments
{}

{h_emphasis}(scroll-mt: --header-height;)
# Emphasis
{}

{h_icons}(scroll-mt: --header-height;)
# Icons
{}

{h_custom_links}(scroll-mt: --header-height;)
# Custom Links
{}

{h_custom_blockquotes}(scroll-mt: --header-height;)
# Custom Blockquotes
{}
// HEADINGS_END

// RESULTS_START
{comments_result}(p: 3; border: 1-0;)
// I am a comment
//Me too
    // Same
Text
// Ignore me :(
{}

{emphasis_result}(p: 3; border: 1-0;)
~~Strikethrough~~
++Underlined++
{}

{icons_result}(p: 3; border: 1-0;)
Some text ~cup-hot-fill~ text ~droplet-fill~ and text.
{}

{links_result}(p: 3; border: 1-0;)
[Default Link]()
[Custom Link 0](){0}
[Custom Link 1](){1}
[Custom Link 2](){2}
{}

{blockquotes_result}(p: 3; border: 1-0;)
> [!Note]
> Highlights information that users should take into account, even when skimming.

> [!Tip]
> Optional information to help a user be more successful.

> [!Important]
> Crucial information necessary for users to succeed.

> [!Warning]
> Critical content demanding immediate user attention due to potential risks.

> [!Caution]
> Negative potential consequences of an action.

> [!Custom{#ad58ef, heart-fill}]
> Customized block quote

{}
// RESULTS_END

{page}(p: 4;)
# **Advanced Syntax**
Learn how to use advanced Markdown syntax in Markdown-Web.

---

{h_comments}
Commented lines will be ignored by the parser.
> [!Note]
> You still need to be careful about blank lines, even if you're using comments.
> Comments are not **replaced** with blank lines. Instead, lines containing comments are removed.

Code:
```markdown
// I am a comment
//Me too
    // Same
Text
// Ignore me :(
```
Result:
{comments_result}

{h_emphasis}
Besides default emphasis, Markdown-Web also supports strikethrough and underlining.

Code:
```markdown
~~Strikethrough~~
++Underlined++
```
Result:
{emphasis_result}

{h_icons}
Markdown-Web supports **icons**, you can create them using the following syntax: `\~icon_name\~`.
It uses Bootstrap icons, which you can find the names of on their [website](https://icons.getbootstrap.com/).
> [!Important]
> Pair `\~` symbols might be recognized by the parser.
> In order to prevent this, please use the `\\~` syntax.
> For example, use `\\~` instead of `\~`.
> This rule does not apply to code blocks.

Code:
```markdown
Some text ~cup-hot-fill~ text ~droplet-fill~ and text.
```
Result:
{icons_result}

{h_custom_links}
You can create links with custom design by adding a `{number}` at the end of the default Markdown link syntax.
At the moment, there are three types of link styles - `0`, `1` and `2`.

Code:
```markdown
[Default Link]()
[Custom Link 0](){0}
[Custom Link 1](){1}
[Custom Link 2](){2}
```
Result:
{links_result}

{h_custom_blockquotes}
There are 5 default types of blockquotes with titles, but you can also create a custom one.
To create a custom blockquote, simply add a `{hex_color, icon_name}` construction after the name of the blockquote.
Don't forget to use a blank line after a blockquote.

Code:
```markdown
> [!Note]
> Highlights information that users should take into account, even when skimming.

> [!Tip]
> Optional information to help a user be more successful.

> [!Important]
> Crucial information necessary for users to succeed.

> [!Warning]
> Critical content demanding immediate user attention due to potential risks.

> [!Caution]
> Negative potential consequences of an action.

> [!Custom{#ad58ef, heart-fill}]
> Customized block quote

```
Result:
{blockquotes_result}

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