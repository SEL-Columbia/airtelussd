from mako.template import Template


index = Template(
"""Welcome to SharedSolar
   Please select the following options
   %for option in menu:
     ${option['menu']}. ${option['title']}
   %endfor
"""
)

error = Template('Unable to understand your request: ${user_input}')
