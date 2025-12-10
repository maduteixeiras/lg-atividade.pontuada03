import os
os.system("cls")
from datetime import datetime
import time 


v_avioes = ["", "", "", ""]
v_assentos = [0, 0, 0, 0]
reservas = []

QUANT_AVIOES = 4

class DadosReserva:
    def __init__(self, numero_aviao, nome_passageiro):
        self.numero_aviao = numero_aviao
        self.nome_passageiro = nome_passageiro


    def ExibirDados(self):
        print("Passageiros do avião: ")
        print(f"Passageiro: {self.nome_passageiro}")
        print(f"Avião: {self.numero_aviao} \n")
        print("")


def ListaVazia():
    if v_avioes == ["", "", "", ""] and v_assentos == [0, 0, 0, 0]:
        print("\nNenhum avião ou assentos cadastrados!")
        print("Cadastre aviões e assentos usando as opções 1 e 2.\n")
        return True
    return False


def RegistrarNumeroAviao():
    for i in range(QUANT_AVIOES):
        codigo = input(f"Digite o código do avião {i+1}: ")
        v_avioes[i] = codigo
    print("\nCódigos cadastrados com sucesso!\n")


def RegistrarAssentosDisponiveis():
    for i in range(QUANT_AVIOES):
        while True:
            try:
                quant = int(input(f"Digite o número de assentos do avião {i+1} (máx 20): "))
                if 0 < quant <= 20:
                    v_assentos[i] = quant
                    break
                else:
                    print("Digite um valor entre 1 e 20!")
            except:
                print("Digite um número inteiro válido!")
    print("\nAssentos cadastrados!\n")



def Reserva():
    if ListaVazia():
        return

    codigo = input("\nDigite o código do avião desejado: ")

    if codigo not in v_avioes:
        print("Avião não encontrado!\n")
        return

    i = v_avioes.index(codigo)

    if v_assentos[i] == 0:
        print("Avião lotado! Não é possível reservar.\n")
        return

    nome = input("Nome do passageiro: ")
    reservas.append(DadosReserva(codigo, nome))
    v_assentos[i] -= 1

    print("\nReserva concluída com sucesso!\n")


def ConsultaPorAviao():
    codigo = input("\nDigite o código do avião: ")

    achou = False
    for i in reservas:
        if i.numero_aviao == codigo:
            i.ExibirDados()
            achou = True

    if not achou:
        print("Nenhuma reserva encontrada para este avião.\n")

def ConsultaPorPassageiro():
    nome = input("\nNome do passageiro: ")

    achou = False
    for i in reservas:
        if i.nome_passageiro.lower() == nome.lower():
            i.ExibirDados()
            achou = True

    if not achou:
        print("Passageiro não encontrado.\n")


def menu():
    while True:
        print("""
 --- Menu de Opções ---
1 - Registrar código dos aviões
2 - Registrar assentos dos aviões
3 - Reservar passagem aérea
4 - Consultar reservas por avião
5 - Consultar reservas por passageiro
6 - Sair
        """)

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                RegistrarNumeroAviao()
            case "2":
                RegistrarAssentosDisponiveis()
            case "3":
                Reserva()
            case "4": 
                ConsultaPorAviao()
            case "5":
                ConsultaPorPassageiro()
            case "6":
                print("Encerrando...")
                time.sleep(1)
                os.system("cls")
                break
            case _:
                print("Opção inválida!")


menu()
