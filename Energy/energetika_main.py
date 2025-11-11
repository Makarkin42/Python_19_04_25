from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QMessageBox
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from energetika_table import session, Engine
from energetikaui import Ui_MainWindow
from loguru import logger
logger.add("logi.logs", level="DEBUG", retention="3 days")

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Энергетика")
        self.potreb_graph = []
        self.count()
        self.graph()
        self.grafik()
        self.horizontalSlider_3.valueChanged.connect(self.naselenie)
        self.horizontalSlider.valueChanged.connect(self.temperature)
        self.horizontalSlider_2.valueChanged.connect(self.night)
        self.horizontalSlider_4.valueChanged.connect(self.power)
        self.pushButton_2.clicked.connect(self.best_score)
        self.pushButton.clicked.connect(self.commit)

    def graph(self):
        layout = QHBoxLayout()
        self.widget.setLayout(layout)
        self.view = QChartView()
        layout.addWidget(self.view)

    def naselenie(self):
        nasel = self.horizontalSlider_3.value()
        self.label_2.setText(f"Население города: {nasel}тыс. чел.")
        self.count()
        self.grafik()

    def temperature(self):
        temp = self.horizontalSlider.value()
        self.label_4.setText(f"Температура: {temp}℃")
        self.count()
        self.grafik()

    def night(self):
        ntime = self.horizontalSlider_2.value()
        self.label_5.setText(f"Продолжительность ночи: {ntime}ч")
        self.count()
        self.grafik()

    def power(self):
        pow = self.horizontalSlider_4.value()
        self.label_3.setText(f"Мощность ТЭС: {pow}кВт")
        self.count()
        self.grafik()

    def count(self):
        self.potreb_graph.clear()
        nasel = self.horizontalSlider_3.value()
        temp = self.horizontalSlider.value()
        night = self.horizontalSlider_2.value()
        #print(temp)
        if temp <= 10 and temp >= 0:
            temp = 25
        elif temp <= -1 and temp >= -24:
            temp = 50
        elif temp <= -25:
            temp = 100
        else:
            temp = 0
        #print(temp)
        night_hours = range(2 - night // 2, 2 + night - night // 2)
        night_hours = [hour if hour >= 0 else 24 + hour for hour in night_hours]
        #print(night_hours)
        morning_plus = [night_hours[0] - hour for hour in range(1, 4)] + [night_hours[-1] + hour for hour in range(1, 4)]
        #print(morning_plus)
        for i in range(24):
            potreb = (2.5 + (temp/100 * 0.35)) * nasel * 1000
            if i in night_hours:
                potreb *= 0.8
            elif i in morning_plus:
                potreb *= 1.2
            self.potreb_graph.append(potreb)

    def grafik(self):
        chart = QChart()
        chart.setTitle("График энергопотребления")
        series = QLineSeries()
        series.setName("График потребления(кВт)")
        for i in range(24):
            series.append(i, int(self.potreb_graph[i]))
        power = self.TES()
        chart.addSeries(series)
        chart.addSeries(power)
        chart.createDefaultAxes()
        self.view.setChart(chart)

    def TES(self):
        series = QLineSeries()
        series.setName("Выработка энергии(кВт)")
        series.append(0, self.horizontalSlider_4.value())
        series.append(23, self.horizontalSlider_4.value())
        return series

    def best_score(self):
        best = session.get(Engine, 1)
        print(best)
        if best is not None:
            self.horizontalSlider_3.setValue(best.naselenie)
            self.horizontalSlider.setValue(best.degree)
            self.horizontalSlider_2.setValue(best.night)
            self.horizontalSlider_4.setValue(best.power)
        else:
            self.pushButton_2.setText("Значение не выставлено")

    def commit(self):
        try:
            print("коммит")
            nasel = self.horizontalSlider_3.value()
            degreee = self.horizontalSlider.value()
            nightt = self.horizontalSlider_2.value()
            powwer = self.horizontalSlider_4.value()
            print(nasel,degreee, nightt, powwer)
            score = Engine(naselenie=nasel, power=powwer, degree=degreee, night=nightt)
            print(score)
            session.merge(score)
            session.commit()
            box = QMessageBox()
            box.setWindowTitle("Сохранение результата")
            box.setText(f"Ваш результат был успешно сохранен!")
            box.setIcon(QMessageBox.Icon.Information)
            box.exec()
        except Exception as e:
            box = QMessageBox()
            box.setWindowTitle("Ошибка!")
            box.setText(f"Возникла ошибка: {e}")
            logger.error("Ошибка сохранения!!!")
            box.setIcon(QMessageBox.Icon.Warning)
            box.exec()


def run():
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()