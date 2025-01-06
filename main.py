from class_produto import Produto
from class_acessorio import Acessorio
from class_brinquedo import Brinquedo
from class_medicamento import Medicamento
from class_racao import Racao

acessorios = []
brinquedos = []
medicamentos = []
racoes = []

def verificar_nome_existente(nome):
    for lista in [acessorios, brinquedos, medicamentos, racoes]:
        for produto in lista:
            if produto.nome == nome:
                return True  
    return False 

def cadastrar_acessorio():
    continuar = 1
    while continuar == 1:
        print("Informe os dados do acessorio")
        nome = input("Nome: ")

        if verificar_nome_existente(nome):
            print("Produto com esse nome já existe! Tente outro nome.")
            continue

        preco = float(input("Preço: "))
        qnt = int(input("Quantidade em estoque: "))
        categoria = input("Categoria (Coleira, Guia, Cama): ")
        tamanho = input("Tamanho (Pequeno, Médio, Grande): ")

        acessorio = Acessorio(nome, preco, qnt, categoria, tamanho)
        acessorios.append(acessorio)

        continuar = int(input("Deseja continuar? 1: Sim, 0: Não\n"))
        
    return print("Acessório cadastrado com sucesso!\n")

def cadastrar_brinquedo():
    continuar = 1
    while continuar == 1:
        print("Informe os dados do brinquedo")
        nome = input("Nome: ")

        if verificar_nome_existente(nome):
            print("Produto com esse nome já existe! Tente outro nome.")
            continue

        preco = float(input("Preço: "))
        qnt = int(input("Quantidade em estoque: "))
        material = input("Material (Plástico, Borracha, Tecido): ")
        faixa_etaria = input("Faixa etária (Filhote, Adulto, Idoso): ")

        brinquedo = Brinquedo(nome, preco, qnt, material, faixa_etaria)
        brinquedos.append(brinquedo)

        continuar = int(input("Deseja continuar? 1: Sim, 0: Não\n"))
        
    return print("Acessório cadastrado com sucesso!\n")

def cadastrar_medicamento():
    continuar = 1
    while continuar == 1:
        print("Informe os dados do acessorio")
        nome = input("Nome: ")

        if verificar_nome_existente(nome):
            print("Produto com esse nome já existe! Tente outro nome.")
            continue

        preco = float(input("Preço: "))
        qnt = int(input("Quantidade em estoque: "))
        tipo = input("Tipo: ")
        dosagem = input("Dosagem recomendada: ")

        medicamento = Medicamento(nome, preco, qnt, tipo, dosagem)
        medicamentos.append(medicamento)

        continuar = int(input("Deseja continuar? 1: Sim, 0: Não\n"))
        
    return print("Acessório cadastrado com sucesso!\n")

def cadastrar_racao():
    continuar = 1
    while continuar == 1:
        print("Informe os dados do acessorio")
        nome = input("Nome: ")

        if verificar_nome_existente(nome):
            print("Produto com esse nome já existe! Tente outro nome.")
            continue

        preco = float(input("Preço: "))
        qnt = int(input("Quantidade em estoque: "))
        tipo_animal = input("Tipo do animal: ")
        peso = float(input("Peso: "))

        racao = Racao(nome, preco, qnt, tipo_animal, peso)
        racoes.append(racao)

        continuar = int(input("Deseja continuar? 1: Sim, 0: Não\n"))
        
    return print("Acessório cadastrado com sucesso!\n")

def vender_produto():
    produto = int(input("Informe o produto que deseja vender:\n1: Acessorio\n2: Brinquedo\n3: Medicamento\n4: Ração\n:"))
    if produto == 1:
        nome = input("Informe o nome do acessório que deseja vender: ")
        acessorio = next((a for a in acessorios if a.nome == nome), None)
        if not acessorio:
            print("Acessório não encontrado! Cadastre-o primeiro.")
            return
        quant = int(input("Informe a quantidade a ser vendida: "))
        acessorio.vender(quant)
    elif produto == 2:
        nome = input("Informe o nome do brinquedo que deseja vender: ")
        brinquedo = next((b for b in brinquedos if b.nome == nome), None)
        if not brinquedo:
            print("Brinquedo não encontrado! Cadastre-o primeiro.")
            return
        quant = int(input("Informe a quantidade a ser vendida: "))
        brinquedo.vender(quant)
    elif produto == 3:
        nome = input("Informe o nome do medicamento que deseja vender: ")
        medicamento = next((m for m in medicamentos if m.nome == nome), None)
        if not medicamento:
            print("Medicamento não encontrado! Cadastre-o primeiro.")
            return
        quant = int(input("Informe a quantidade a ser vendida: "))
        medicamento.vender(quant)
    elif produto == 4:
        nome = input("Informe o nome da ração que deseja vender: ")
        racao = next((r for r in racoes if r.nome == nome), None)
        if not racao:
            print("Ração não encontrado! Cadastre-a primeiro.")
            return
        quant = int(input("Informe a quantidade a ser vendida: "))
        racao.vender(quant)
    else:
        print("Opção inválida!!")

def consultar_estoque():
    nome = input("Consultar estoque do produto: ")
    produto = next((p for p in acessorios + brinquedos + medicamentos + racoes if p.nome == nome), None)
    if not produto:
        print("Produto não encontrado! Cadastre-o primeiro.")
        return
    produto.exibir_informacoes()

def repor_estoque():
    nome = input("Informe o nome do produto que deseja repor o estoque: ")
    produto = next((p for p in acessorios + brinquedos + medicamentos + racoes if p.nome == nome), None)
    if not produto:
        print("Produto não encontrado! Cadastre-o primeiro.")
        return
    quant = int(input("Informe a quantidade a ser reposta: "))

    produto.repor_estoque(quant)

def relatorio_mais_vendidos():
    produtos = acessorios + brinquedos + medicamentos + racoes
    
    produtos_ordenados = sorted(produtos, key=lambda p: p.vendas, reverse=True)
    
    print("Relatório de Produtos Mais Vendidos:")
    for produto in produtos_ordenados:
        print(f"{produto.nome}: {produto.vendas} unidades vendidas")

switch = {
    1: cadastrar_acessorio,
    2: cadastrar_brinquedo,
    3: cadastrar_medicamento,
    4: cadastrar_racao,
    5: vender_produto,
    6: consultar_estoque,
    7: repor_estoque,
    8: relatorio_mais_vendidos
}

print("Sistema de gerenciamento de estoque")
while True:
    try:
        escolha = int(input("1: Cadastrar Acessório\n2: Cadastrar Brinquedo\n3: Cadastrar Medicamento\n4: Cadastrar Ração\n5: Vender produto\n6: Consultar estoque\n7: Repor estoque\n8: Verificar produtos mais vendidos\n0: Sair\nInsira: "))
        if escolha == 0:
            print("Sistema finalizado!")
            break
        acao = switch.get(escolha, lambda: print("Opção inválida!\n"))
        acao()
    except ValueError:
        print("Insira um número válido!\n")
