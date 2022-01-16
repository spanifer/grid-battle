'''String helper methods'''


def center(string, length, left_align=True):
    '''Centers the 'string' by wrapping it in whitespaces
    in the 'length' length; if odd number of whitespaces, optional
    'left' param can be set to false to align it to the right
    Returns empty string or the formated string'''
    str_l = len(string)
    if str_l <= length:
        whitesp = length-str_l
        left = whitesp-whitesp//2 if left_align else whitesp//2
        right = whitesp-left
        return f'{" "*left}{string}{" "*right}'
    return ''
