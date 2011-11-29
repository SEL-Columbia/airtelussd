from mako.template import Template


index = Template(
"""Welcome to SharedSolar's USSD menu
   Please select the following options
   %for i, option in enumerate(menu):
     ${option[0]}. ${option[1]}
   %endfor
"""
)

error = Template('Unable to understand your request: ${user_input}')

user_account = Template('Please input your account number')
