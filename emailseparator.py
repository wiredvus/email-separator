filename = input("Qual o nome do arquivo .txt que você quer usar? ")
if not filename.endswith('.txt'):
    filename += '.txt'
dominio = input("Qual domínio você quer filtrar? (pressione Enter para usar '.com.br'): ").strip()
if not dominio:
    dominio = '.com.br'
try:
    with open(filename, 'r', encoding='utf-8') as fhand:
        print(f"\nLinhas contendo '{dominio}':\n")
        
        for line in fhand:
            line = line.rstrip()
            if dominio in line:
                print(line) 
        print(f"\nFiltro concluído para o domínio: {dominio}")
except FileNotFoundError:
    print(f"Erro: O arquivo '{filename}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

#feito por Vus