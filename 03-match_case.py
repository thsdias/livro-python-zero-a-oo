
def num_cor(num):
    match num: 
        case 1:
            return "Vermelho"
        case 2:
            return "Verde"
        case 3:
            return "Azul"
        case 4:
            return "Branco"
        case 5:
            return "Preto"

cor_atual = 1

print(num_cor(cor_atual))
