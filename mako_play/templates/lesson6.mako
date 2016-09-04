<%!
MY_CONSTANT = "module level constant"
import os
# funciton does not have access to template context but does not need to.
# template context is what is returned from the view function
def i_am_pretty(character):
    return "pretty: " + character
%>

<%
# available in template context
my_letters = ['a', '   b   ', 'c']

# function HAS access to template context which is why it can use
# my_view_var variable
def show_my_view_var():
    return "[" + my_view_var + "]"

%>

<html>
## mako comment
    <pre>
${MY_CONSTANT}

% for letter in my_letters:
${i_am_pretty(letter) | trim}.
% endfor
${show_my_view_var()}
    </pre>
</html>

