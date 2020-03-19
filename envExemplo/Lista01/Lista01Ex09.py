"""
O cardápio de uma lanchonete é o seguinte:

Especificação	   Código	Preço
Cachorro quente 	100	    5,20
Hambúrguer      	101	    5,20
Cheeseburguer   	102	    7,30
Refrigerante    	103	    5,00

Escrever um algoritmo que leia o código do item pedido, a quantidade e
calcule o valor a ser pago por aquele lanche. Considere que a cada execução
somente será calculado um item.
"""
codigo=int(input('Digite o codigo do produto....:'))
quantidade= int(input('Digite a quantidade do produto:'))
if codigo == 100:
    soma = (quantidade*5.20)
    print('o valor do seu cachorro-quente é de R${:.2f}'.format(soma))
elif codigo == 101:
    soma = (quantidade*5.20)
    print('o valor do seu Hambúrguer é de R${:.2f}'.format(soma))
elif codigo == 102:
    soma = (quantidade*7.30)
    print('o valor do seu Cheeseburguer é de R${:.2f}'.format(soma))
elif codigo == 103:
    soma = (quantidade*5.00)
    print('o valor do seu Refrigerante é de R${:.2f}'.format(soma))
