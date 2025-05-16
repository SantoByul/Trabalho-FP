import datetime
import os

petslist = []
portesvalidos = ["pequeno", "medio", "grande"]
opcoespetshop = {
    "1": "Unidade Boa Viagem",
    "2": "Unidade Espinheiro",
    "3": "Unidade Caxangá",
    "4": "Unidade Recife Antigo"
}

localizacoespetshop = {
    "1": "Unidade Boa Viagem - Av. Domingos Ferreira, Recife - PE",
    "2": "Unidade Espinheiro - R. do Espinheiro, Recife - PE",
    "3": "Unidade Caxangá - Av. Caxangá, Recife - PE",
    "4": "Unidade Recife Antigo - R. do Bom Jesus, Recife - PE"
}

def arquivoexiste(nomearquivo):
    return os.path.exists(nomearquivo)

def adicionapet():
    nome = input("Nome do pet: ").lower()
    if not nome:
        print("Você não inseriu um nome.")
        return
    especie = input("Espécie: ").lower()
    if not especie:
        print("Você não inseriu uma espécie.")
        return
    porte = input("Seu animal é de porte pequeno, médio ou grande?: ").lower()
    if porte not in portesvalidos:
        print("Você só pode escolher entre pequeno, médio e grande.")
        return
    nascimento = input("Data de nascimento: ")
    if not nascimento:
        print("Você não inseriu uma data de nascimento.")
        return
    peso = input("Peso(kg): ")
    if not peso:
        print("Você não inseriu um peso.")
        return
    arquivo = open("pets.txt", "a")
    arquivo.write(f"{nome};{especie};{porte};{nascimento};{peso}\n")
    arquivo.close()
    petslist.append(nome)
    print("Pet cadastrado.")
    print("Lista dos seus pets:", petslist)

def visualizapet():
    if not arquivoexiste("pets.txt"):
        print("Nenhum pet cadastrado.")
        return
    arquivo = open("pets.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()
    for linha in sorted(linhas):
        partes = linha.strip().split(";")
        if len(partes) == 5:
            nome, especie, porte, nascimento, peso = partes
            print(f"Nome: {nome} | Espécie: {especie} | Porte: {porte} | Nascimento: {nascimento} | Peso: {peso}kg")
        else:
            print(f"[⚠️ Linha inválida ignorada]: {linha.strip()}")

def editapet():
    nomepet = input("Digite o nome do pet que deseja editar: ")
    if not arquivoexiste("pets.txt"):
        print("Arquivo de pets não encontrado.")
        return
    pets = []
    encontrado = False
    arquivo = open("pets.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()
    for linha in linhas:
        if linha.startswith(nomepet + ";"):
            print("Digite os novos dados:")
            nome = input("Novo nome: ")
            especie = input("Nova espécie: ")
            porte = input("Novo porte: ")
            nascimento = input("Nova data de nascimento: ")
            peso = input("Novo peso: ")
            pets.append(f"{nome};{especie};{porte};{nascimento};{peso}\n")
            encontrado = True
        else:
            pets.append(linha)
    if encontrado:
        arquivo = open("pets.txt", "w")
        arquivo.writelines(pets)
        arquivo.close()
        print("Pet atualizado com sucesso!")
    else:
        print("Pet não encontrado.")

def excluipet():
    nomepet = input("Digite o nome do pet que deseja excluir: ")
    if not arquivoexiste("pets.txt"):
        print("Arquivo de pets não encontrado.")
        return
    pets = []
    excluido = False
    arquivo = open("pets.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()
    for linha in linhas:
        if linha.startswith(nomepet + ";"):
            excluido = True
        else:
            pets.append(linha)
    if excluido:
        arquivo = open("pets.txt", "w")
        arquivo.writelines(pets)
        arquivo.close()
        print(f"Pet {nomepet} excluído.")
    else:
        print("Pet não encontrado.")

def registraevento():
    data = input("Data do evento: ")
    nomepet = input("Nome do pet: ")
    tipoevento = input("Tipo de evento (vacina, consulta, remédio): ").lower()
    observacoes = input("Observações: ")
    arquivo = open("eventos.txt", "a")
    arquivo.write(f"{data};{nomepet};{tipoevento};{observacoes}\n")
    arquivo.close()
    print("Evento registrado.")

def exibeeventos():
    if not arquivoexiste("eventos.txt"):
        print("Nenhum evento registrado.")
        return
    arquivo = open("eventos.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()
    for linha in linhas:
        data, nomepet, tipo, obs = linha.strip().split(";")
        print(f"Data: {data} | Pet: {nomepet} | Tipo: {tipo} | Obs: {obs}")

def definemeta():
    descricao = input("Descrição da meta: ")
    frequencia = input("Frequência: ")
    arquivo = open("metas.txt", "a")
    arquivo.write(f"{descricao};{frequencia}\n")
    arquivo.close()
    print("Meta registrada.")

def exibemetas():
    if not arquivoexiste("metas.txt"):
        print("Nenhuma meta definida.")
        return
    arquivo = open("metas.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()
    for linha in linhas:
        descricao, frequencia = linha.strip().split(";")
        print(f"Meta: {descricao} | Frequência: {frequencia}")

def cumprameta():
    descricao = input("Digite a descrição exata da meta que você cumpriu: ")
    data = datetime.datetime.now().strftime("%d/%m/%Y")
    arquivo = open("cumprimentos.txt", "a")
    arquivo.write(f"{descricao};{data}\n")
    arquivo.close()
    print("Cumprimento registrado.")

def verificacumprimento():
    if not arquivoexiste("metas.txt"):
        print("Nenhuma meta registrada.")
        return
    arquivo = open("metas.txt", "r")
    linhasmetas = arquivo.readlines()
    arquivo.close()
    metas = [linha.strip().split(";")[0] for linha in linhasmetas]
    registros = []
    if arquivoexiste("cumprimentos.txt"):
        arquivo = open("cumprimentos.txt", "r")
        linhascumprimentos = arquivo.readlines()
        arquivo.close()
        registros = [linha.strip().split(";")[0] for linha in linhascumprimentos]
    for meta in metas:
        vezes = registros.count(meta)
        print(f"Meta: {meta} | Cumprimentos registrados: {vezes}")

def sugestoescuidados():
    especie = input("Espécie do pet (cachorro/gato): ").lower()
    idade = float(input("Idade do pet (em anos, use número com vírgula se necessário): ").replace(',', '.'))
    porte = input("Porte do pet (pequeno/medio/grande): ").lower()
    if especie == "cachorro":
        if idade < 1:
            print("• Vacinação completa")
            print("• Rações específicas para filhotes")
            print("• Visitas ao veterinário a cada 2 a 3 meses")
            print("• Brinquedos para dentição")
        else:
            print("• Alimentação equilibrada com ração para adultos")
            print("• Consultas veterinárias a cada 6 meses")
            print("• Atividades físicas regulares")
            if porte == "pequeno":
                print("• Caminhadas curtas diárias")
                print("• Cuidados com o frio (roupas, caminhas quentes)")
            elif porte == "medio":
                print("• Exercícios moderados")
                print("• Espaço razoável para se movimentar")
            elif porte == "grande":
                print("• Exercícios intensos e caminhadas longas")
                print("• Acesso a áreas abertas e maiores")
            else:
                print("Porte não reconhecido. Informe pequeno, medio ou grande.")
    elif especie == "gato":
        if idade < 1:
            print("• Brinquedos leves e seguros")
            print("• Caixa de areia acessível")
            print("• Ração para filhotes")
            print("• Vacinação completa")
        else:
            print("• Ração específica para adultos")
            print("• Escovação regular (principalmente se peludo)")
            print("• Sessões de brincadeiras interativas")
            if porte == "pequeno":
                print("• Brinquedos pequenos e acessíveis")
            elif porte == "medio":
                print("• Arranhadores de tamanho médio")
            elif porte == "grande":
                print("• Espaço vertical (prateleiras, torres)")
                print("• Monitoramento do peso")
            else:
                print("Porte não reconhecido. Informe pequeno, médio ou grande.")
    else:
        print("Espécie não reconhecida. Informe 'cachorro' ou 'gato'.")

def escolherpetshopproximo():
    print("\n--- Escolha o Petshop Mais Próximo ---")
    for chave, nomepetshop in opcoespetshop.items():
        print(f"{chave}. {nomepetshop}")
    while True:
        opcao = input("Digite o número do petshop desejado: ")
        if opcao in opcoespetshop:
            petshopescolhido = opcoespetshop[opcao]
            localizacao = localizacoespetshop[opcao]
            print(f"Você escolheu: {petshopescolhido}")
            print(f"Localização: {localizacao}")
            arquivo = open("petshopescolhido.txt", "a")
            arquivo.write(f"{petshopescolhido} - {localizacao}\n")
            arquivo.close()
            break
        else:
            print("Opção inválida. Por favor, digite um número da lista.")

while True:
    print("\n--- VIDA PET ---")
    print("1. Adicionar Pet")
    print("2. Visualizar Pets")
    print("3. Editar Pet")
    print("4. Excluir Pet")
    print("5. Registrar Evento")
    print("6. Exibir Eventos")
    print("7. Definir Meta de Saúde")
    print("8. Exibir Metas")
    print("9. Cumprir Meta")
    print("10. Verificar Cumprimento de Metas")
    print("11. Sugestões de Cuidados")
    print("12. Escolher Petshop Próximo")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        adicionapet()
    elif opcao == "2":
        visualizapet()
    elif opcao == "3":
        editapet()
    elif opcao == "4":
        excluipet()
    elif opcao == "5":
        registraevento()
    elif opcao == "6":
        exibeeventos()
    elif opcao == "7":
        definemeta()
    elif opcao == "8":
        exibemetas()
    elif opcao == "9":
        cumprameta()
    elif opcao == "10":
        verificacumprimento()
    elif opcao == "11":
        sugestoescuidados()
    elif opcao == "12":
        escolherpetshopproximo()
    elif opcao == "0":
        break
    else:
        print("Opção inválida. Tente novamente.")
