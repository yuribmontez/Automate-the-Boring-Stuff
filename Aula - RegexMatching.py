#USANDO CHARACTER PIPE '|' PARA DAR MATCH EM VARIAS EXPRESSÕES.
import re

heroRegex = re.compile(r'Batman|Tina Fey') #Aqui tanto batman quanto tina fey darão match
#mas somente o primeiro que aparecer será retornado.
mo1 = heroRegex.search('Batman e Tina Fey')
mo2 = heroRegex.search('Tina Fey e Batman')
mo1.group()
mo2.group()

#USANDO PIPE PARA DAR MATCH EM PADRÕES
batRegex = re.compile(r'Bat(man|carro|copter|bat)')
mo = batRegex.search('Batcarro perdeu uma roda')
mo.group()#retorna tudo
mo.group(1)#retorna o match somente dentro do parenteses
#Se precisar usar pipe em uma expressão usar \| 

#USANDO CHARACTER '?' PARA RETORNAR INSTANCIAS OPCIONAIS NOS MATCHES
batRegex = re.compile(r'Bat(wo)?man') #(wo)? = padrão opcional ou seja vai dar match com ou sem
mo1 = batRegex.search('As aventuras de Batman')
mo2 = batRegex.search('As aventuras de Batwoman')
mo1.group()
mo2.group()
#Se precisar usar ? em uma expressão usar \?

#USANDO CHARACTER '*' PARA RETORNAR ZERO OU MAIS INSTANCIAS NOS MATCHES
batRegex = re.compile(r'Bat(wo)*man') #(wo)? = padrão opcional ou seja vai dar match com ou sem
mo1 = batRegex.search('As aventuras de Batman') #Match com zero instacias de wo
mo2 = batRegex.search('As aventuras de Batwoman') #Match com 1 instacia de wo
mo3 = batRegex.search('As aventuras de Batwowowowowoman') #Match com 5 de wo
mo1.group()
mo2.group()
mo3.group()
#Se precisar usar * em uma expressão usar \*

#USANDO CHARACTER '+' PARA RETORNAR UM OU MAIS INSTACIAS NOS MATCHES
batRegex = re.compile(r'Bat(wo)+man') 
mo1 = batRegex.search('As aventuras de Batman') # = None
mo2 = batRegex.search('As aventuras de Batwoman') 
mo3 = batRegex.search('As aventuras de Batwowowowowoman') 
mo1.group() 
mo2.group()
mo3.group()
mo1 == None #Expressão retorna como none pq precisa de pelo menos umas instancia de wo para funcionar.
#Se precisar usar + em uma expressão usar \+

#RETORNANDO REPETIÇÕES ESPECIFICAS COM '{}'
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo2 = haRegex.search('Ha')
mo1.group()
mo2.group() #None pq especifiquei exatamente 3

haRegex = re.compile(r'(Ha){3,5}')
mo1 = haRegex.search('HaHa') 
mo2 = haRegex.search('HaHaHa')
mo3 = haRegex.search('HaHaHaHa')
mo4 = haRegex.search('HaHaHaHaHa')
mo1.group() #None pq especifiquei de 3 até 5
mo2.group()
mo3.group()
mo4.group()

haRegex = re.compile(r'(Ha){,5}')#Aqui é para dar match somente até o quinto Ha
mo1 = haRegex.search('Ha')
mo2 = haRegex.search('HaHa')
mo3 = haRegex.search('HaHaHaHaHaHaHaHa')
mo1.group()
mo2.group() 
mo3.group() 

haRegex = re.compile(r'(Ha){3,}')
mo1 = haRegex.search('HaHaHa')
mo2 = haRegex.search('Ha')
mo3 = haRegex.search('HaHaHaHaHaHaHaHaHaHa')
mo1.group()
mo2.group() #None pq especifiquei a partir de 3
mo3.group()

#Em situações ambiguas o python sempre vai retornar a maior string possivel numa expressão regular

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()

nongreedyHaRegex = re.compile(r'(Ha){3,5}?') #'?' também serve para retornar a menor string possivel dentro da condição
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()

