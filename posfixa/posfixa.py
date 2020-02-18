# =====================================================
# ======           FUNCOES                       ======
# =====================================================
def imprime_cabecalho():
    print('==================================================================')
    print('====                                                         =====')
    print('==== Programa que converte uma expressao Infixa para Posfixa =====')
    print('====                                                         =====')
    print('==================================================================')

def infixaToPosfixa(expressao):
    saida = []
    pilha = []

    for i in expressao:
        if ehNumero(i):
            saida.append(i)
        else:
            if len(pilha) == 0:
                pilha.append(i)
            elif len(pilha) > 0:
                topo_pilha = pilha[-1]
                if prioridade_operadores(i, topo_pilha):
                    pilha.append(i)
                else:
                    while len(pilha) > 0:
                        topo_pilha = pilha.pop()
                        saida.append(topo_pilha)
                    pilha.append(i)

    #
    while len(pilha) > 0:
        topo_pilha = pilha.pop()
        saida.append(topo_pilha)

    return saida

def prioridade_operadores(c, t):
    pc = -1
    pt = -1

    if c == '^':
        pc = 4
    elif (c == '*') or (c == '/'):
        pc = 2
    elif (c == '+') or (c == '-'):
        pc = 1
    elif c == '(':
        pc = 4

    if t == '^':
        pt = 3
    elif (t == '*') or (t == '/'):
        pt = 2
    elif (t == '+') or (t == '-'):
        pt = 1
    elif t == '(':
        pt = 0

    return (pc > pt);

def ehNumero(c):
    return isinstance(c,(int,float))

def ehLetra(c):
    return isinstance(c, (str))

def ehOperador(c):
    return not isinstance(c,(int,float))

# =====================================================
# ======           MAIN                          ======
# =====================================================
expressao = [-5.0, '-', 2.0, '*', 3.0, '+', 14.0, '/', -7.0]
saida = [-5.0, 2.0, 3.0, '*', '-', 14.0, -7.0, '/', '+']
imprime_cabecalho()
print('Expressao de Entrada = {}'.format(expressao))
print('Expressao de Saida = {}'.format(infixaToPosfixa(expressao)))
