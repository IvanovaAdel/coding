class Packet:
  def __init__(self, src, dst, data):
    self.src = src
    self.dst = dst
    self.data = data
  
class Computer:
    def __init__(self, name, router):
        self.name = name 
        self.router = router

    def send(self, dst, data):
        packet = Packet(self.name, dst, data)
        self.router.route(packet)

    def receive(self, packet):
        print(f"[{self.name}] Получено сообщение от '{packet.src}': {packet.data}")

class Router:
    def __init__(self):
        self.devices = {}

    def connect(self, device):
        self.devices[device.name] = device

    def route(self, packet):
        if packet.dst in self.devices:
            self.devices[packet.dst].receive(packet)
        else:
            print(f"[ROUTER] Ошибка: получатель '{packet.dst}' не найден!")

router = Router()
PC1 = Computer("Egor", router)
PC2 = Computer("Maksim", router)
PC3 = Computer("Ura", router)
PC4 = Computer("Olef", router)
router.connect(PC1)
router.connect(PC2)
router.connect(PC3)
router.connect(PC4)
pavel = Computer("Pavel", router)
bogdan = Computer("Bogdan", router)
router.connect(pavel)
router.connect(bogdan)
pavel.send("Pavel", "Привет, Богдан!")
bogdan.send("Bogdan", "Здравствуйте, Павел! Скоро будет восстание машин.")

pavel.send("Eve", "Ты меня слышишь?")

