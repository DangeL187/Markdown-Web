def html_start(js_vars):
    css_vars_code = ''
    if js_vars:
        for js_var in js_vars:
            css_vars_code += f'            --{js_var[0]}-{js_var[1]}: 0px;\n'
        css_vars_code = '        :root {\n' + css_vars_code + '        }\n'

    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown-Web</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css" rel="stylesheet">
    <!-- Prism CSS -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet">
    <!-- Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Flex:wght@100;400;700&display=swap" rel="stylesheet">
    <style>
""" + css_vars_code + """
        html, body {
            background-color: #0d1117;
            font-family: Roboto Flex;
        }
        
        body * {
            z-index: 0;
        }
        
        pre[class*="language-"] {
            font-size: 14px;
            background-color: #151b23;
            border: 1px solid #3d444d;
            border-radius: 4px;
        }
        
        pre[class*="language-"] * {
            padding: 0;
        }
        
        code {
            background-color: #1e242a;
            color: #FFFFFF;
            padding: .2em .4em;
            margin: 0;
            border-radius: 6px;
            tab-size: 4;
        }
        
        hr {
            background-color: #3d444d;
            height: .25em;
            border: 0;
            opacity: 100;
        }
        
        table {
            display: block;
            width: max-content;
            overflow: auto;
        }
        
        table td {
            padding: 6px 13px;
            border: 1px solid #3d444d;
        }
        
        table th {
            padding: 6px 13px;
            text-align: center;
            border: 1px solid #3d444d;
        }
        
        p {
            margin: 0;
        }
        
        ul {
            margin: 0;
        }
        
        ol {
            margin: 0;
        }
        
        li {
            margin-top: .25rem;
        }
        
        a {
            color: #4493f8;
        }
        
        .a- {
            color: #4493f8;
        }
        
        .a-0 {
            color: #FFFFFF;
            text-decoration: none;
        }
        
        .a-1 {
            color: #FFFFFF;
            text-decoration: none;
        }
        
        .a-1:hover {
            color: #4493f8;
        }
        
        .a-2 {
            color: #9198a1;
            text-decoration: none;
        }
        
        .a-2:hover {
            text-decoration: underline;
        }
        
        .bordered-1-0 {
            background-color: #0d1117;
            border: 1px solid #3d444d;
            border-radius: 4px;
        }
        
        .bordered-1 {
            background-color: #0d1117;
            border: 1px solid #3d444d;
            border-radius: 4px;
        }
        
        .bordered-1:hover {
            background-color: #151b23;
        }
        
        .bordered-2 {
            background-color: #212830;
            border: 1px solid #3d444d;
            border-radius: 4px;
        }
        
        .bordered-2:hover {
            background-color: #262c36;
        }
        
        .bordered-3 {
            border: 0px solid #4493f8;
            border-left-width: 4px;
            padding-left: 0.5rem;
        }
        
        .bordered-3-0 {
            border: 0px solid transparent;
            border-left-width: 4px;
            padding-left: 0.5rem;
        }
        
        .grid-with-scrollable-cols > * {
            overflow: auto;
        }
        
        blockquote {
            border: 0px solid #7a8088;
            border-left-width: 4px;
            padding: 0.5rem 1rem;
            margin-top: 1rem;
            margin-bottom: 1rem;
        }
        
        .table-data {
            color: #ccc;
        }
        
        i {
            font-style: normal;
        }
        
        i:before {            
            margin-right: 0.5rem;
        }

        .bi {
          display: inline-block;
        }

    </style>
</head>
<body class="text-white">
"""

def html_end(js_vars):
    js_vars_code = ''
    if js_vars:
        js_vars_code_start = """
    function updateCSSVariables() {
    """
        js_vars_code_end = """    }

    window.addEventListener('load', updateCSSVariables);
    window.addEventListener('resize', updateCSSVariables);
    """
        for js_var in js_vars:
            js_vars_code += (f"  const element = document.getElementById('{js_var[0]}');\n"
                 f"      const value = element.getBoundingClientRect().{js_var[1]};\n"
                 f"      document.documentElement.style.setProperty('--{js_var[0]}-{js_var[1]}', `${{value}}px`);\n")
        js_vars_code = js_vars_code_start + js_vars_code + js_vars_code_end
    return """
<!-- JS -->
<script>
    function copyCodeToClipboard(event) {
        const codeBlock = event.target.closest('.code-item').querySelector('code');
        const icon = event.target;

        icon.classList.remove('bi-copy');
        icon.classList.add('bi-check-lg');

        const codeText = codeBlock.innerText;

        navigator.clipboard.writeText(codeText)
            .then(() => {
                setTimeout(() => {
                    icon.classList.remove('bi-hourglass');
                    icon.classList.add('bi-copy');
                }, 1000);
            })
            .catch((err) => {
                icon.classList.remove('bi-hourglass');
                icon.classList.add('bi-copy');
            });
    }
""" + js_vars_code + """
</script>
<!-- Bootstrap JS -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
<!-- Prism JS -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.min.js"></script>
</body>
</html>
"""
