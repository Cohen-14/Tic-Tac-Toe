# 99192 Cláudio Campos
# Tic Tac Toe vers(1.0)

def eh_tabuleiro(tab):
    """Confere se o argumento representa um tabuleiro de jogo"""
    i = 0
    if isinstance(tab, tuple) and len(tab) == 3:
        x, y, z = tab[0], tab[1], tab[2]
        if len(x) == 3 and len(y) == 3 and len(z) == 3:
            while 0 <= i < 3:
                if isinstance(x[i], int) and isinstance(y[i], int) and isinstance(z[i], int):
                    if not isinstance(x[i], bool) and not isinstance(y[i], bool) and not isinstance(z[i], bool):
                        if -1 > x[i] > 1 and -1 > y[i] > 1 and -1 > z[i] > 1:
                            return False
                        else:
                            i = i + 1
                    else:
                        return False
                else:
                    return False
            else:
                return True
        else:
            return False
    return False


def eh_posicao(n):
    """ verifica se o argumento é de uma posição do tabuleiro"""
    if isinstance(n, int) and n in range(1, 10) and not isinstance(n, bool):
        return True
    return False


def obter_coluna(tab, n):
    """ devolve os valores da coluna n de um determinado tabuleiro"""
    if eh_tabuleiro(tab):
        res = ()
        if isinstance(n, int) and 1 <= n <= 3:
            x, y, z = tab[0], tab[1], tab[2]
            res = res + (x[n - 1],) + (y[n - 1],) + (z[n - 1],)
            return res
        else:
            raise ValueError('obter_coluna: algum dos argumentos e invalido')
    else:
        raise ValueError('obter_coluna: algum dos argumentos e invalido')


def obter_linha(tab, n):
    """ devolve os valores da linha n de um determinado tabuleiro"""
    if eh_tabuleiro(tab):
        if isinstance(n, int) and 1 <= n <= 3:
            return tab[n - 1]
        else:
            raise ValueError('obter_linha: algum dos argumentos e invalido')
    raise ValueError('obter_linha: algum dos argumentos e invalido')


def obter_diagonal(tab, n):
    """ devolve os valores da diagonal n de um determinado tabuleiro"""
    if eh_tabuleiro(tab):
        x, y, z = tab[0], tab[1], tab[2]
        if isinstance(n, int) and 1 <= n <= 2 and not isinstance(n, bool):
            if n == 1:
                res = (x[0],) + (y[1],) + (z[2],)
                return res
            if n == 2:
                res = (z[0],) + (y[1],) + (x[2],)
                return res
        else:
            raise ValueError('obter_diagonal: algum dos argumentos e invalido')
    else:
        raise ValueError('obter_diagonal: algum dos argumentos e invalido')


def tabuleiro_str(tab):
    """ representa um determinado tabuleiro"""
    if eh_tabuleiro(tab):
        res = ' '
        x, y, z = tab[0], tab[1], tab[2]
        for i in range(0, 3):
            if x[i] == 1:
                res = res + 'X' + ' |'
            if x[i] == -1:
                res = res + 'O' + ' |'
            if x[i] == 0:
                res = res + ' ' + ' |'
        res = res + ' \n----------\n '
        for i in range(0, 3):
            if y[i] == 1:
                res = res + 'X' + ' |'
            if y[i] == -1:
                res = res + 'O ' + '|'
            if y[i] == 0:
                res = res + ' ' + ' |'
        res = res + ' \n----------\n '
        for i in range(0, 3):
            if z[i] == 1:
                res = res + 'X' + ' |'
            if z[i] == -1:
                res = res + 'O' + ' |'
            if z[i] == 0:
                res = res + ' ' + ' |'
        return res
    else:
        raise ValueError('tabuleiro_str: o argumento e invalido')


def eh_posicao_livre(tab, n):
    """ verifica se a posição n do tabuleiro está livre"""
    if eh_tabuleiro(tab):
        x, y, z = tab[0], tab[1], tab[2]
        if isinstance(n, int) and 1 <= n <= 9:
            if 1 <= n <= 3:
                if x[n - 1] == 0:
                    return True
                else:
                    return False
            if 4 <= n <= 6:
                if y[n - 4] == 0:
                    return True
                else:
                    return False
            if 7 <= n <= 9:
                if z[n - 7] == 0:
                    return True
                else:
                    return False
        else:
            raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')
    else:
        raise ValueError('eh_posicao_livre: algum dos argumentos e invalido')


def jogador_ganhador(tab):
    """ mostra atraves de um inteiro quem venceu o jogo, ou se este terminou empatado"""
    if eh_tabuleiro(tab):
        if obter_diagonal(tab, 1) == (-1, -1, -1):
            return -1
        if obter_diagonal(tab, 1) == (1, 1, 1):
            return 1
        if obter_diagonal(tab, 2) == (-1, -1, -1):
            return -1
        if obter_diagonal(tab, 2) == (1, 1, 1):
            return 1
        if obter_linha(tab, 1) == (1, 1, 1):
            return 1
        if obter_linha(tab, 2) == (1, 1, 1):
            return 1
        if obter_linha(tab, 3) == (1, 1, 1):
            return 1
        if obter_linha(tab, 1) == (-1, -1, -1):
            return -1
        if obter_linha(tab, 2) == (-1, -1, -1):
            return -1
        if obter_linha(tab, 3) == (-1, -1, -1):
            return -1
        if obter_coluna(tab, 1) == (1, 1, 1):
            return 1
        if obter_coluna(tab, 2) == (1, 1, 1):
            return 1
        if obter_coluna(tab, 3) == (1, 1, 1):
            return 1
        if obter_coluna(tab, 1) == (-1, -1, -1):
            return -1
        if obter_coluna(tab, 2) == (-1, -1, -1):
            return -1
        if obter_coluna(tab, 3) == (-1, -1, -1):
            return -1
        else:
            return 0
    raise ValueError('jogador_ganhador: o argumento e invalido')


def obter_posicoes_livres(tab):
    """ mostra todas as posicoes que estao livres no tabuleiro"""
    if eh_tabuleiro(tab):
        i = 0
        res = ()
        x, y, z = tab[0], tab[1], tab[2]
        while 0 <= i <= 2:
            if x[i] == 0:
                res = res + (i + 1,)
                i = i + 1
            else:
                i = i + 1
        while 3 <= i <= 5:
            if y[i - 3] == 0:
                res = res + (i + 1,)
                i = i + 1
            else:
                i = i + 1
        while 6 <= i <= 8:
            if z[i - 6] == 0:
                res = res + (i + 1,)
                i = i + 1
            else:
                i = i + 1
        return res
    raise ValueError('obter_posicoes_livres: o argumento e invalido')


def marcar_posicao(tab, i, p):
    """marca uma posicao livre com o inteiro que representa o jogador"""
    res = ()
    if eh_tabuleiro(tab) and isinstance(i, int) and (i == -1 or i == 1) and not isinstance(i, bool):
        if isinstance(p, int) and 1 <= p <= 9:
            if eh_posicao_livre(tab, p):
                x, y, z = tab[0], tab[1], tab[2]
                if 1 <= p <= 3:
                    res = res + x[:p - 1] + (i,) + x[p:]
                    res = (res,) + (y,) + (z,)
                    return res
                if 4 <= p <= 6:
                    res = res + y[:p - 4] + (i,) + y[p - 3:]
                    res = (x,) + (res,) + (z,)
                    return res
                if 7 <= p <= 9:
                    res = res + z[:p - 7] + (i,) + z[p - 6:]
                    res = (x,) + (y,) + (res,)
                    return res
    raise ValueError('marcar_posicao: algum dos argumentos e invalido')


def escolher_posicao_manual(tab):
    """ permite ao jogador humano escolher uma posicao livre """
    if eh_tabuleiro(tab):
        n = eval(input('Turno do jogador. Escolha uma posicao livre: '))
        if 1 <= n <= 9 and eh_posicao_livre(tab, n):
            return n
        else:
            raise ValueError('escolher_posicao_manual: a posicao introduzida e invalida.')
    else:
        raise ValueError('escolher_posicao_manual: o argumento e invalido')


def escolher_posicao_auto(tab, i, difficulty):
    """ marca automaticamente e de acordo com a estrategia desejada uma posicao livre com um inteiro representativo
    do jogador"""
    if eh_tabuleiro(tab):
        if difficulty == 'basico':
            if 5 in obter_posicoes_livres(tab):
                return 5
            elif 1 in obter_posicoes_livres(tab):
                return 1
            elif 3 in obter_posicoes_livres(tab):
                return 3
            elif 7 in obter_posicoes_livres(tab):
                return 7
            elif 9 in obter_posicoes_livres(tab):
                return 9
            elif 2 in obter_posicoes_livres(tab):
                return 2
            elif 4 in obter_posicoes_livres(tab):
                return 4
            elif 6 in obter_posicoes_livres(tab):
                return 6
            elif 8 in obter_posicoes_livres(tab):
                return 8
        if difficulty == 'normal':
            if i == 1 or i == -1:
                if obter_linha(tab, 1) == (1, 1, 0) or obter_linha(tab, 1) == (-1, -1, 0):
                    return 3
                elif obter_linha(tab, 1) == (1, 0, 1) or obter_linha(tab, 1) == (-1, 0, -1):
                    return 2
                elif obter_linha(tab, 1) == (0, 1, 1) or obter_linha(tab, 1) == (0, -1, -1):
                    return 1
                elif obter_linha(tab, 2) == (1, 1, 0) or obter_linha(tab, 2) == (-1, -1, 0):
                    return 6
                elif obter_linha(tab, 2) == (1, 0, 1) or obter_linha(tab, 2) == (-1, 0, -1):
                    return 5
                elif obter_linha(tab, 2) == (0, 1, 1) or obter_linha(tab, 2) == (0, -1, -1):
                    return 4
                elif obter_linha(tab, 3) == (1, 1, 0) or obter_linha(tab, 3) == (-1, -1, 0):
                    return 9
                elif obter_linha(tab, 3) == (1, 0, 1) or obter_linha(tab, 3) == (-1, 0, -1):
                    return 8
                elif obter_linha(tab, 3) == (0, 1, 1) or obter_linha(tab, 3) == (0, -1, -1):
                    return 7
                elif obter_coluna(tab, 1) == (1, 1, 0) or obter_coluna(tab, 1) == (-1, -1, 0):
                    return 7
                elif obter_coluna(tab, 1) == (1, 0, 1) or obter_coluna(tab, 1) == (-1, 0, -1):
                    return 4
                elif obter_coluna(tab, 1) == (0, 1, 1) or obter_coluna(tab, 1) == (0, -1, -1):
                    return 1
                elif obter_coluna(tab, 2) == (1, 1, 0) or obter_coluna(tab, 2) == (-1, -1, 0):
                    return 8
                elif obter_coluna(tab, 2) == (1, 0, 1) or obter_coluna(tab, 2) == (-1, 0, -1):
                    return 5
                elif obter_coluna(tab, 2) == (0, 1, 1) or obter_coluna(tab, 2) == (0, -1, -1):
                    return 2
                elif obter_coluna(tab, 3) == (1, 1, 0) or obter_coluna(tab, 3) == (-1, -1, 0):
                    return 9
                elif obter_coluna(tab, 3) == (1, 0, 1) or obter_coluna(tab, 3) == (-1, 0, -1):
                    return 6
                elif obter_coluna(tab, 3) == (0, 1, 1) or obter_coluna(tab, 3) == (0, -1, -1):
                    return 3
                elif obter_diagonal(tab, 1) == (0, 1, 1) or obter_diagonal(tab, 1) == (0, -1, -1):
                    return 1
                elif obter_diagonal(tab, 1) == (1, 0, 1) or obter_diagonal(tab, 1) == (-1, 0, -1):
                    return 5
                elif obter_diagonal(tab, 1) == (1, 1, 0) or obter_diagonal(tab, 1) == (-1, -1, 0):
                    return 9
                elif obter_diagonal(tab, 2) == (0, 1, 1) or obter_diagonal(tab, 2) == (0, -1, -1):
                    return 7
                elif obter_diagonal(tab, 2) == (1, 0, 1) or obter_diagonal(tab, 2) == (-1, 0, -1):
                    return 5
                elif obter_diagonal(tab, 2) == (1, 1, 0) or obter_diagonal(tab, 2) == (-1, -1, 0):
                    return 3
                elif 5 in obter_posicoes_livres(tab):
                    return 5
                elif i == 1:
                    if obter_diagonal(tab, 1) == (-1, 0, 0):
                        return 9
                    if obter_diagonal(tab, 1) == (0, 0, -1):
                        return 1
                    if obter_diagonal(tab, 2) == (-1, 0, 0):
                        return 3
                    if obter_diagonal(tab, 2) == (0, 0, -1):
                        return 7
                elif i == -1:
                    if obter_diagonal(tab, 1) == (1, 0, 0):
                        return 9
                    if obter_diagonal(tab, 1) == (0, 0, 1):
                        return 1
                    if obter_diagonal(tab, 2) == (1, 0, 0):
                        return 3
                    if obter_diagonal(tab, 2) == (0, 0, 1):
                        return 7
                elif 1 in obter_posicoes_livres(tab):
                    return 1
                elif 3 in obter_posicoes_livres(tab):
                    return 3
                elif 7 in obter_posicoes_livres(tab):
                    return 7
                elif 9 in obter_posicoes_livres(tab):
                    return 9
                elif 2 in obter_posicoes_livres(tab):
                    return 2
                elif 4 in obter_posicoes_livres(tab):
                    return 4
                elif 6 in obter_posicoes_livres(tab):
                    return 6
                elif 8 in obter_posicoes_livres(tab):
                    return 8
    else:
        raise ValueError('escolher posicao auto: algum dos argumentos e invalido')


def jogo_do_galo(jog, dif):
    """funcao final que permite jogar o jogo do galo de acordo com a dificuldade e com a marca pretendida"""
    if jog in ('X', 'O') and dif in ('basico', 'normal', 'perfeito'):
        tab = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
        x, y, z = tab[0], tab[1], tab[2]
        print('Bem_vindo ao JOGO DO GALO.\nO jogador joga com', jog)
        if jog == 'O':
            while 0 in x or 0 in y or 0 in z and jogador_ganhador(tab) == 0:
                print('Turno do computador(' + dif + ') :')
                tab = marcar_posicao(tab, 1, escolher_posicao_auto(tab, 1, dif))
                print(tabuleiro_str(tab))
                if jogador_ganhador(tab) != 0:
                    break
                tab = marcar_posicao(tab, -1, escolher_posicao_manual(tab))
                print(tabuleiro_str(tab))
            if jogador_ganhador(tab) == 1:
                return 'X'
            if jogador_ganhador(tab) == -1:
                return '0'
            else:
                return 'EMPATE'
        if jog == 'X':
            while 0 in x or 0 in y or 0 in z and jogador_ganhador(tab) == 0:
                tab = marcar_posicao(tab, 1, escolher_posicao_manual(tab))
                print(tabuleiro_str(tab))
                if jogador_ganhador(tab) != 0:
                    break
                print('Turno do computador (' + dif + '):')
                tab = marcar_posicao(tab, -1, escolher_posicao_auto(tab, -1, dif))
                print(tabuleiro_str(tab))
            if jogador_ganhador(tab) == 1:
                return 'X'
            elif jogador_ganhador(tab) == -1:
                return '0'
            else:
                return 'EMPATE'
    else:
        raise ValueError('jogo_do_galo: algum dos argumentos e invalido')
