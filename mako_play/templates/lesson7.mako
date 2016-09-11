<html>
    <body>

<pre>
Sidebar: Let's learn how tags work

A tag has a beginning and an end.

HTML tag begins with: ${"<" | h}
HTML tag ends with: ${">" | h}

A mako tag begins with : ${"<" | h}
A mako tag ends with : ${">" | h}
Each tag name starts with : ${"%" | h}

Every tag has to have a beginning tag and an end tag.
Beginning BODY tag: ${"<body>" | h}
Ending BODY tag uses forward slash at the beginning of the tag name: ${"</body>" | h}
A special type of tag is one that opens and closes itself: ${"<br />" | h}
It has a forward slash after the tag name (space is optional but more readable).

Tag can have multiple attributes (also called properties).
An attribute is a key/pair value: ${"<%include file='/foo.text' />'"| h}
Do not use the same attribute key twice within the same tag.
${"<%include file='/foo.text' file='/bar.txt' />'"| h}
</pre>

    <body>
</html>
