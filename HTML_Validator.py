#!/bin/python3

def validate_html(html):
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    stack = []
    if '<' not in html and '>' not in html:
        return True
    else:
        extracted_tags = _extract_tags(html)
        if len(extracted_tags) == 0:
            return False
        for i, tags in enumerate(extracted_tags):
            if '/' not in tags:
                stack.append(tags[1:-1])
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] == tags[2:-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the class/book
    # the main difference between your code and the code from class will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''

    stack = []
    word = ""
    in_tag = False
    attribute = False
    for i, char in enumerate(html):
        if char == '<':
            if len(word) > 0:
                word = ""
                in_tag = False
            else:
                word += char
                in_tag = True
        elif char == '>':
            if in_tag:
                word += char
                stack.append(word)
                word = ""
                in_tag = False
                attribute = False
        elif in_tag:
            if char == ' ':
                attribute = True
            if not attribute: 
                word += char
    return stack
