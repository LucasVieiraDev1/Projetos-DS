from colorama import Fore, Style
niveis = [1, 2, 3, 4, 5]
mensagens = ["Muito baixo (crítico)", "Baixo", "Médio", "Alto", "Muito alto (alerta)"]
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
nivel_atual = 5

cor = definir_cor(nivel_atual)
mensagem = mensagens[nivel_atual - 1]

print("Sistema de Monitoramento do Reservatório")
print("Situação atual do reservatório:\n")

print(cor + f"Nível atual: {nivel_atual} - {mensagem}" + Style.RESET_ALL)

