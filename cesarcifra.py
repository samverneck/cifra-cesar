#!/usr/bin/env python 
# *-* coding: utf-8 *-*


alfabeto = 'abcdefghijklmnopqrstuvwxyz'


def cifrar(cadeia, chave): 
    resultado = ''    
    for letra in cadeia:
        ascii = ord(letra)
        rotated = ascii
        if(ascii>64)and(ascii<91):
            rotated = rotated + chave;
            if(rotated > 90): rotated += -90 + 64;
            if(rotated < 65): rotated += -64 + 90;
        elif(ascii>96)and(ascii<123):
            rotated = rotated + chave;
            if(rotated > 122): rotated += -122 + 96;
            if(rotated < 97): rotated += -96 + 122; 
        resultado += chr(rotated)
    return resultado


def decifrar(cadeia, chave): 
    text_cifrado = ''
    
    for letra in cadeia:
        soma = alfabeto.find(letra) + chave
        modulo = int(soma) % len(alfabeto)
        text_cifrado = text_cifrado + str(alfabeto[modulo])
    return text_cifrado

def main():
    c = str(input('cadeia a cifrar: ')).lower()
    n = int(input('chave numerica: '))
    
#input = raw_input
cc = str(input('cadeia a decifrar:' )).lower()
cn = int(input('cadeia numerica: '))
print (cifrar(cc,cn))
#print (decifrar(cc, cn)) 

if __name__ == '___main__': main()