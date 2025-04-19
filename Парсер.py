import requests
from bs4 import BeautifulSoup
import tkinter as tk

class Parser():
    def __init__(self,url):
        self.url = url
        req = requests.get(url).text
        self.soup = BeautifulSoup(req,"html.parser")
    def getcity(self):
        data = self.soup.find_all("a")
        towns = {}
        exeption = [">>>","Мобильная версия", "О сайте", "Частые вопросы (FAQ)","Контакты", "Беларусь",
                     "Литва","Россия","Украина","Все страны","См. на карте","Главная",""]
        for tag in data:
            if tag.text not in exeption:
                name = tag.text
                #print(name)
                url = str(tag)
                url = url[9:]
                url = url[:url.find('"')]
                towns[name] = "https://rp5.ru"+url
        return towns

class Window():
    def __init__(self,urls):
        self.window = tk.Tk()
        self.window.geometry("800x650")
        self.window.title("Прогноз погоды")
        self.window["bg"] = "white"
        self.search = tk.Label(self.window,font=("arial",10),fg="black",bg="grey",wraplength=750)
        keys = list(urls)
        keys = ", ".join(keys)
        self.search.configure(text=keys)
        self.search.pack()
        self.entry = tk.Entry(self.window,font=("arial",20),justify="center")
        self.entry.pack()
        self.sbutton = tk.Button(self.window,text="ИСКАТЬ",font=("arial",30),fg="black",bg="grey",command=self.searching)
        self.sbutton.pack()
        self.weath = tk.Label(self.window, font=("arial", 20), fg='black', bg="white",wraplength=750)
        self.weath.pack()
        self.urls = {}
        for i in urls:
            self.urls[i.lower()] = urls[i]
    def searching(self):
        result = self.entry.get()
        if result.lower() in self.urls:
            self.pars(self.urls[result.lower()],result)
        else:
            self.weath.configure(text="Город не найден")
    def pars(self,url,cityname):
        page = Parser(url)
        soder = page.soup.find("div",{"id":"archiveString"})
        description = page.soup.find("div",{"id":"forecastShort-content"})
        if soder:
            weather = soder.find("span",{"class":"t_0"}).text
            weather_des = description.find("b").text
            self.weath.configure(text=f"{weather},{cityname},\n {weather_des}")
        else:
            reg_towns = page.getcity()
            self.urls.update(reg_towns)
            keys = list(reg_towns)
            keys = ", ".join(keys)
            self.search.configure(text=keys)
parser = Parser("https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8")
towns = parser.getcity()
#print(towns)
okno = Window(towns)
tk.mainloop()