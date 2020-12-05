# -*- coding: utf-8 -*-

try:
    with open('20k_email.txt', 'r', encoding="utf8") as file:
        for line in file.readlines():
            try:
                if '@ig.com.br' in str(line.lower()):
                    with open('dbig.txt', 'a', encoding="utf8") as file2:
                        file2.write(str(line))
                        print(f"+1   ->   {str(line)}")
                        pass
                else:
                    pass
            except Exception:
                pass
        input('\n               Processo Finalizado!!! Pressione ENTER Para Fechar!')
        exit()
except Exception as ee:
    print(f'\n\n      Erro Critico -> {ee}')
    input()
    exit()
    
    #Credits -> @Hypn0thcy
