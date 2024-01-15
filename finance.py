while True:
    opcoes = input("Olá, deseja calcular seu salário bruto para líquido [1] ou calcular finanças pelo salário líquido [2]? ")

    if opcoes == "1":
        #cálculo salário bruto para líquido
        while True: 
            valorSalário = input("Qual é o seu salário? ")

            is_int = isinstance(valorSalário, int)

            validarInput = input(f"Confirmando, o salário é de: R${valorSalário}? ")

            if validarInput.startswith("S") or validarInput.startswith("s"):
                break
            else:
                continue

        if valorSalário >= 13184:
            irpf = 0.275
        elif valorSalário >= 9922 and valorSalário < 13184:
            irpf = 0.225
        elif valorSalário >= 6677 and valorSalário < 9922:
            irpf = 0.15 
        elif valorSalário >= 3382 and valorSalário < 6677:
            irpf = 0.075
        else:
            irpf = 0

        if valorSalário >= 4225:
            inss = None
        elif valorSalário >= 2112 and valorSalário < 4225:
            inss = 0.12
        elif valorSalário >= 1267 and valorSalário < 2112:
            inss = 0.09
        else:
            inss = 0.075

        if inss is None:
            inssFixo = valorSalário - 508
            inssValor = 508
        else:
            inssFixo = None
            inssValor = valorSalário * inss

        irpfValor = valorSalário * irpf

        bL = valorSalário - irpfValor - inssValor

        print(f"Seu salário bruto é R${valorSalário} e em líquido é de R${bL}")

    elif opcoes == "2":
        #cálculo finanças
        while True:
            valorSalário = input("Qual é o seu salário? ")

            is_int = isinstance(valorSalário, int)

            validarInput = input(f"Confirmando, o salário é de: R${valorSalário}? ")

            if validarInput.startswith("S") or validarInput.startswith("s"):
                break
            else:
                continue

        print("Salário confirmado: R$ ", valorSalário)

        print("Por favor, responda a algumas perguntas para se iniciar o cálculo: ")
        gastosFixos = 0.50
        pensaoAlimenticia = input("Você tem que pagar algum tipo de pensão? ")
        custosVariados = input("Você tem costume de ter um gasto zero, baixo, médio, alto ou extremo para custos variados? ")

        if pensaoAlimenticia.startswith("S") or pensaoAlimenticia.startswith("s"):
            temPensaoAlimenticia = True
        else:
            temPensaoAlimenticia = False

        def pAcalc(x, y, z):
            if temPensaoAlimenticia == True and valorSalário >= x and valorSalário < y:
                return z
            else:
                return 0        

        valorPensaoAlimenticia1 = pAcalc(1000, 3000, 300)
        valorPensaoAlimenticia2 = pAcalc(3000, 6000, 800)
        valorPensaoAlimenticia3 = pAcalc(6000, 10000, 1100)
        valorPensaoAlimenticia4 = pAcalc(10000, 1000000000000, None)

        if valorPensaoAlimenticia4 is None:
            valorPensaoAlimenticia4 = valorSalário * 0.20

        valorPensaoAlimenticia = valorPensaoAlimenticia1 + valorPensaoAlimenticia2 + valorPensaoAlimenticia3 + valorPensaoAlimenticia4

        if custosVariados.startswith("z") or custosVariados.startswith("Z"):
            valorCustosVariados = 0
        elif custosVariados.startswith("b") or custosVariados.startswith("B"):
            valorCustosVariados = 0.10
        elif custosVariados.startswith("m") or custosVariados.startswith("M"):  
            valorCustosVariados = 0.20
        elif custosVariados.startswith("a") or custosVariados.startswith("A"):
            valorCustosVariados = 0.30
        elif custosVariados.startswith("E") or custosVariados.startswith("e"):
            valorCustosVariados = 0.45

        vCV = valorSalário * valorCustosVariados
        gF = valorSalário * gastosFixos
        resultadosFinais = valorSalário - gF - valorPensaoAlimenticia - vCV

        print("Aqui está o cálculo final de acordo com suas respostas: ")
        print(f"Salário: R${valorSalário}")
        print(f"Gastos fixos(50%): R${gF}")
        if temPensaoAlimenticia == True:
            print(f"Pensão Alimenticia: R${valorPensaoAlimenticia}")
        print(f"Custos Variados: R${vCV}")
        print(f"Com base nisso, você terá um valor final no mês de R${resultadosFinais}")
        if resultadosFinais >= valorSalário * 0.10:
            print("Muito bem! Aparentemente você tem um bom controle financeiro ")
        else:
            print(f"Aparentemente você tem um gasto alto e está sobrando menos de 10% da sua renda, tente economizar mais.")

    else:
        print("Você não inseriu uma opção válida, por favor escolha novamente.")
    continue