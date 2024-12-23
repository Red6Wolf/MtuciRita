class Component:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

class Worker:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    def __str__(self):
        return f"{self.name} ({self.role})"

class Station:
    def __init__(self, name, equipment, workers, materials=None):
        self.name = name
        self.equipment = equipment
        self.workers = workers
        self.materials = materials
    def operate(self, board):
        pass

class AssemblyStation(Station):
    def operate(self, board):
        print(f"Станция {self.name}: сборка началась.")
        print(f"Используем оборудование: {', '.join(self.equipment)}")
        print(f"На станции работают: {', '.join(map(str, self.workers))}")
        board.assembled = True
        print("Плата собрана.\n")

class TestingStation(Station):
    def operate(self, board):
        print(f"Станция {self.name}: тестирование началось.")
        print(f"Используем оборудование: {', '.join(self.equipment)}")
        print(f"На станции работают: {', '.join(map(str, self.workers))}")
        if board.assembled:  # Проверяем, собрана ли плата
            board.tested = True
            print("Плата прошла тестирование.\n")
        else:
            print("Ошибка: плата не собрана!\n")

class PackagingStation(Station):
    def operate(self, board):
        if board.tested:
            print(f"Станция {self.name}: упаковка началась.")
            print(f"Используем оборудование: {', '.join(self.equipment)}")
            print(f"На станции работают: {', '.join(map(str, self.workers))}")
            board.packaged = True
            print("Плата упакована и отправлена на склад.\n")
        else:
            print("Ошибка: плата не прошла тестирование!\n")

class CircuitBoard:
    def __init__(self, size, components):
        self.size = size
        self.components = components
        self.assembled = False
        self.tested = False
        self.packaged = False
    def __str__(self):
        return f"Плата {self.size} размера с компонентами: {', '.join(self.components)}"

# Инициализация данных
workers_assembly = [Worker("Иван", "электронщик"), Worker("Ольга", "оператор")]
workers_testing = [Worker("Сергей", "контролер качества")]
workers_packaging = [Worker("Анна", "оператор оборудования")]

assembly_station = AssemblyStation(
    name="Станция сборки",
    equipment=["Сборочная линия", "Роботы-манипуляторы", "Паяльные станции"],
    workers=workers_assembly,
    materials=["Печатные платы", "Электронные компоненты"]
)

testing_station = TestingStation(
    name="Станция тестирования",
    equipment=["Тестовые стенды"],
    workers=workers_testing
)

packaging_station = PackagingStation(
    name="Станция упаковки",
    equipment=["Упаковочные машины", "Роботы-манипуляторы"],
    workers=workers_packaging
)
# Процесс производства
def manufacture_circuit_board(size, requested_components):
    board = CircuitBoard(size=size, components=requested_components)
    print(f"Начинаем производство: {board}\n")

    assembly_station.operate(board)
    testing_station.operate(board)
    packaging_station.operate(board)

    if board.packaged:
        print("Производственный процесс завершен: плата на складе.")
    else:
        print("Производственный процесс завершен с ошибками.")

requested_components = ["микросхема", "резисторы", "диоды", "провода"]
manufacture_circuit_board(size="маленький", requested_components=requested_components)
