class Patient:
    def __init__(self, name, age, is_new, med, dis, pref):
        self.name = name
        self.age = age
        self.is_new = is_new
        self.med = med
        self.dis = dis
        self.pref = pref

    def __str__(self):
        return f"• {self.name}({self.age} anos, primeira visita: {self.is_new}, pref: {self.pref}) \n- Medicamentos em uso: {self.med} \n- Doenças autoimunes: {self.dis}"

## Indice de preferência: 1 = preferencial, 2 = não preferencial

# verifica se os valores(números) inseridos são positivos e inteiros
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("A idade deve ser um número inteiro positivo")
            else:
                return value
        except ValueError:
            print("A idade deve ser um número inteiro positivo")

# verifica o valor inserido e retorna True ou False (se for válido)
def get_yes_no_input(prompt):
    while True:
        response = input(prompt).lower()
        if response in ["sim", "s", "yes", "y"]:
            return True
        elif response in ["não", "n", "no"]:
            return False
        else:
            print("Por favor, responda com 'sim' ou 'não' (ou variações).")

# verifica se há e se os medicamentos inseridos são válidos (ValueError)
def get_med_info(prompt):
    res = get_yes_no_input(prompt)
    if res:
        try:
            med = str(input("Quais? "))
        except ValueError:
            print("Por favor insira um medicamento válido.")
    else:
        med = "Nenhum"

    return med


def get_dis_info(prompt):
    res = get_yes_no_input(prompt)
    if res:
        try:
            dis = str(input("Por favor cite-as abreviadamente: "))
        except ValueError:
            print("Por favor insira as doenças a seguir.")
    else:
        dis = "Nenhuma"

    return dis

# recebe os valores primários do paciente
def get_patient_information():
    try:
        name = input("Insira o nome do paciente: ").title()
        age = get_integer_input("Insira a idade do paciente: ")
        pref = 1 if age <= 10 or age >= 55 else 2
        is_new = get_yes_no_input("É a primeira vez? (s/n): ")
        med = get_med_info("Está tomando algum medicamento? (s/n): ")
        dis = get_dis_info("Possui alguma doença autoimune? (s/n): ")
        return name, age, "Sim" if is_new else "Não", med, dis, pref

    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário.")
        exit(1)


if __name__ == "__main__":
    name, age, is_new, med, dis, pref = get_patient_information()
    patient = Patient(name, age, is_new, med, dis, pref)
    print(patient)
