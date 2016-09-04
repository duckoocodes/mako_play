<html>
    <body>

         <pre>
## uses default filters in mako
${show_this_text}
        </pre>

        <pre>
## disables default filters in mako
${show_this_text | n}
        </pre>

        <pre>
## disables all the default filters in mako then uses h and trim filters
${show_this_text | n, h, trim}
        </pre>

    </body>
</html>
