from typing import Optional


class Observable:
    def __init__(self):
        self.observers: set["Observer"] = set()

    def add_observer(self, observer):
        self.observers.add(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)


class Observer:
    def update(self, observable: Observable):
        pass


class WeatherStation(Observable):
    temperature: Optional[int] = None

    def set_temperature(self, temperature: int):
        self.temperature = temperature
        self.notify_observers()


class PhoneDisplay(Observer):
    def update(self, observable, *args, **kwargs):
        if isinstance(observable, WeatherStation):
            temperature = observable.temperature
            print(f"Temperature is {temperature} degrees Celsius")


if __name__ == "__main__":
    weather_station = WeatherStation()
    phone_display_1 = PhoneDisplay()
    phone_display_2 = PhoneDisplay()
    weather_station.add_observer(phone_display_1)
    weather_station.add_observer(phone_display_2)
    # when 2 displays subscribed
    weather_station.set_temperature(25)
    # after removal of one subscriber
    weather_station.remove_observer(phone_display_1)
    weather_station.set_temperature(26)
