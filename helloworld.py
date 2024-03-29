import toga
from toga.style.pack import COLUMN, LEFT, RIGHT, ROW, Pack


def build(app):
    c_box = toga.Box()
    f_box = toga.Box()
    box = toga.Box()
        
    def calculateFahrenheight(widget):
        c_input.value = (float(f_input.value) - 32.0) * 5.0 / 9.0

    def calculateCelsius(widget):
        f_input.value = ((float(c_input.value)) * 9/ 5) + 32

    c_input = toga.TextInput(on_lose_focus=calculateCelsius)
    f_input = toga.TextInput(on_lose_focus=calculateFahrenheight)

    c_label = toga.Label("Celsius", style=Pack(text_align=RIGHT))
    f_label = toga.Label("Fahrenheigt", style=Pack(text_align=RIGHT))
    join_label = toga.Label("is equivalent to", style=Pack(text_align=RIGHT))

    # def calculate(widget):
    #     try:
    #         c_input.value = (float(f_input.value) - 32.0) * 5.0 / 9.0
    #     except ValueError:
    #         c_input.value = "???"

    # button = toga.Button("Calculate", on_press=calculate)

    f_box.add(f_input)
    f_box.add(f_label)

    c_box.add(join_label)
    c_box.add(c_input)
    c_box.add(c_label)

    box.add(f_box)
    box.add(c_box)
    # box.add(button)

    box.style.update(direction=COLUMN, padding=10)
    f_box.style.update(direction=ROW, padding=5)
    c_box.style.update(direction=ROW, padding=5)

    c_input.style.update(flex=1)
    f_input.style.update(flex=1, padding_left=210)
    c_label.style.update(width=100, padding_left=10)
    f_label.style.update(width=100, padding_left=10)
    join_label.style.update(width=200, padding_right=10)

    # button.style.update(padding=15)

    return box


def main():
    return toga.App("Temperature Converter", "org.beeware.toga.tutorial", startup=build)


if __name__ == "__main__":
    main().main_loop()