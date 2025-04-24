opcao = 1
lista = []
senha_correta = "1234"

while(opcao != 4):
    print('\t CADASTRO DE IMC \n 1.Cadastrar \n 2.Listar \n 3.Remover \n 4.Sair \n')
    try:
        opcao = int(input("Digite a sua opção: "))
    except ValueError:
        print("\nDigite um número válido!")
        continue

    if(opcao == 1):
        nome = input("Digite o nome: ")

        try:
            idade = float(input("Digite a idade: "))
            peso = float(input("Digite o peso (kg): "))
            altura = float(input("Digite a altura (m): "))
            imc = peso / (altura ** 2)

            if imc < 18.5:
                classificacao = "Abaixo do peso"
            elif 18.5 <= imc < 25:
                classificacao = "Peso normal"
            elif 25 <= imc < 30:
                classificacao = "Sobrepeso"
            elif 30 <= imc < 35:
                classificacao = "Obesidade Grau I"
            elif 35 <= imc < 40:
                classificacao = "Obesidade Grau II"
            else:
                classificacao = "Obesidade Grau III"

            lista.append([nome,idade,peso, altura, round(imc, 2), classificacao])
            print("\nCadastrado com sucesso!")
            print(f"IMC calculado: {round(imc, 2)} - {classificacao}")

        except ValueError:
            print("\nDigite valores numéricos válidos para peso e altura!")

    elif(opcao == 2):
        senha = input("\nDigite a senha para visualizar os dados: ")
        if senha == senha_correta:
            if len(lista) == 0:
                print("\nNenhum cadastro encontrado.")
            else:
                print("\nLista de Cadastros:")
                for i, cadastro in enumerate(lista):
                    print(f"{i+1}. Nome: {cadastro[0]}, idade: {cadastro[1]} Peso: {cadastro[2]}kg, Altura: {cadastro[3]}m")
                    print(f"   IMC: {cadastro[4]} - Classificação: {cadastro[5]}\n")
        else:
            print("\nSenha incorreta! Acesso negado.")

    elif(opcao == 3):
        if len(lista) == 0:
            print("\nNenhum cadastro para remover.")
        else:
            print("\nCadastros disponíveis para remoção:")
            for i, cadastro in enumerate(lista):
                print(f"{i+1}. Nome: {cadastro[0]}, IMC: {cadastro[3]}")

            try:
                indice = int(input("\nDigite o número do cadastro que deseja remover: ")) - 1
                if 0 <= indice < len(lista):
                    removido = lista.pop(indice)
                    print(f"\nCadastro de {removido[0]} removido com sucesso!")
                else:
                    print("\nÍndice inválido!")
            except ValueError:
                print("\nDigite um número válido!")

    elif(opcao == 4):
        sair = input("\nTem certeza que deseja sair? (s/n): ")
        if sair.lower() == "s":
            print("\n\tAté breve :)")
            break
    else:
        print("\n\tOpção inválida")
