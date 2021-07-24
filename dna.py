import csv
import sys


def main():

    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # Atribuindo os arquivos
    database = sys.argv[1]
    sequence = sys.argv[2]

    # Lendo database e colocando no dict
    with open(database, "r") as f:
        reader = csv.DictReader(f)
        dict_list = list(reader)

    # Atribuindo a sequencia
    with open(sequence, "r") as f:
        STR_seq = f.readline().rstrip("\n")

    # Pegando todos as colunas menos o name da database
    STRs = []
    for i in range(1, len(reader.fieldnames)):
        STR = reader.fieldnames[i]
        STRs.append(STR)

    # Contando o maximo de repetições consecutivas de um STR da sequencia completa
    seq = {}
    for STR in STRs:
        seq[STR] = verify_dna(STR_seq, STR)

    # Buscando e comparando os valores para o match
    for people in dict_list:
        matches = 0

        # Iteragindo com cada pessoa especificamente
        for STR in people:
            if STR != 'name':

                # Verificando se determinado STR é igual
                if int(seq[STR]) == int(people[STR]):
                    matches += 1

                if matches == (len(reader.fieldnames) - 1):
                    print(people['name'])
                    exit(0)

    print("No match")

# Função que retorna o numero maximo de repetiçoes de um STR
def verify_dna(STR_seq, STR):

    #Definindo contador fora do looping pra que não seja resetado.
    max_count = 0

    for i in range(len(STR_seq)):
        STR_count = 0
        if STR_seq[i:(i + len(STR))] == STR:
            k = 0

            # Quando é encontrado uma correspondencia, ele adiciona o tamanho da
            # correspondencia na busca e verifica se ainda é compativel, e vai
            # fazendo isso até não ser mais.
            while STR_seq[(i + k):(i + k + len(STR))] == STR:
                STR_count += 1
                k += len(STR)

                # Guardando o valor maximo e depois resetando o valor da contagem
                # pois apenas interessa a maiior sequencia consecutiva do STR
                if STR_count > max_count:
                    max_count = STR_count


    return max_count


if __name__ == "__main__":
    main()
