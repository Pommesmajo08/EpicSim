print("AluStudios 2021")
class Server(object):
  def __init__(self, ram, mode):
    self.ram = ram
    self.mode = mode
  def set_Mode(self, mode):
    self.mode = mode
    self.ram = ram
  def set_ram(self, ram):
    self.ram = ram
def buy_server():
  globals()
  ram = int(input("Wie viel Gb Ram? (1, 2, 3, 4, 5, 6, 7, 8, 9, 10"))
  mode = input("Modus? (Solo, Duo, Team)")
  if ram == 1:
    kosten = 100
  elif ram == 2:
    kosten = 200
  elif ram == 3:
    kosten = 300
  elif ram == 4:
    kosten = 400
  elif ram == 5:
    kosten = 500
  elif ram == 6:
    kosten = 600
  elif ram == 7:
    kosten = 700
  elif ram == 8:
    kosten = 800
  elif ram == 9:
    kosten = 900
  elif ram == 10:
    kosten = 1000
  print(kosten)
  if(money < kosten):
    print("Du hast nicht genug Geld!")
  else:
    print("Erfolgreich gekauft!")

servers= [Server("1G", "Solo")]

num_servers = 1

money= 500
def default():
  print("\n\n\n\n\n\n\n")
  print("Was möchtest du machen? (1 Server Kaufen, 2 Server verkaufen, 3 Server Modifizieren)")
  action = input("")
  if action == "1":
    buy_server()
    
if __name__ == "__main__":
  default()