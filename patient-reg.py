class Patient:
    def __init__(self, name, age, is_new):
        self.name = name
        self.age = age
        self.is_new = is_new

    def __str__(self):
        return f"{self.name}({self.age} anos, primeira visita: {self.is_new})"


def get_patient_information():
    try:
        name = input("Insira o nome do paciente: ")
        while True:
            try:
                age = int(input("Insira a idade do paciente: "))
                if age <= 0:
                    print("A idade deve ser um número inteiro positivo")
                else:
                    break
            except ValueError:
                print("A idade deve ser um número inteiro válido.")

        is_new = input("É a primeira vez?(s/n): ").lower() == 's'
        return name, age, is_new

    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário.")
        exit(1)


if __name__ == "__main__":
    name, age, is_new = get_patient_information()
    patient = Patient(name, age, is_new)
    print(patient)
