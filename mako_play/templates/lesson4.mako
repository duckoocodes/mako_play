% for text_number in ['fifty', 'twenty', 'thirty', 'forty', 'ten', 'sixty']:
${loop.index}
${loop.even}
${loop.first}
## show value of text_number
${text_number}:
    % if text_number[0] == 't':
        it is ten, twenty, or thirty <br />
    % elif text_number[0] == 'f':
        it is forty or fifty <br />
    % else:
        it is sixty <br />
    % endif
% endfor
