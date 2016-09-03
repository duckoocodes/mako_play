% for text_number in ['one', 'two', 'three', 'four', 'five']:
${loop.reverse_index}
${loop.even}
${loop.first}
## show valude of text_number
${text_number}:
    % if text_number[0] == 't':
        it is two or three <br />
    % elif text_number[0] == 'f':
        it is four or five <br />
    % else:
        it is one <br />
    % endif
% endfor
