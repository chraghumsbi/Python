# Functions with output

# def format_name(f_name, l_anme):
#     full_name_f = f_name.title()
#     full_name_l = l_anme.title()
#     return f'{full_name_f} {full_name_l}'
# print(format_name('raghu', 'chilaka'))

# Docstring
# More than one return statements

def format_name(f_name, l_anme):
    """
    This function will take first and last names
    and format it to return the title case version of the name.
    """
    if f_name == '' or l_anme == '':
        return 'You didn\'t provide valid inputs'
    full_name_f = f_name.title()
    full_name_l = l_anme.title()
    return f'Result:  {full_name_f} {full_name_l}'


print(format_name(input('What is your first name: ?'),
      input('What is your last name: ?')))
