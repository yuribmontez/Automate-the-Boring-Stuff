#re = regular expressions
import re
#'r' = raw string = geralmente não tem scape characters
phoneNumRegex = re.compile(r'(\(\d\d\))? (\d\d\d\d\d-\d\d\d\d)') # parenteses separando as expressões em grupos
mo1 = phoneNumRegex.search('Meu numero é (11) 95580-7775.') #variavel mo = padrão para Match Objects
mo1.group()
mo2 = phoneNumRegex.search('Meu numero é 95580-7775.')
mo2.group()