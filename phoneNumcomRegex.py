#re = regular expressions
import re
#'r' = raw string = geralmente não tem scape characters
phoneNumRegex = re.compile(r'(\(\d\d\)) (\d\d\d\d\d-\d\d\d\d)') # parenteses separando as expressões em grupos
mo = phoneNumRegex.search('Meu numero é (11) 95580-7775.') #variavel mo = padrão para Match Objects

print('Phone number found:' + mo.group(1))#parametro vazio ou 0 = tudo, 1 = primeiro grupo '11', 2 = segundo grupo '95580-7775'

print(mo.groups())#printa todos os grupos