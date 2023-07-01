HEX_CODE_TO_COLOUR = {"RED": "#ff0000", "BLUE": "#0000ff", "GREEN": "#00ff00", "YELLOW": "#ffff00",
                      "ORANGE": "#ffa500", "PURPLE": "#a020f0", "BLACK": "#000000", "WHITE": "#ffffff",
                      "BROWN": "#a52a2a", "GRAY": "#bebebe"}

colour = input("Enter colour: ").upper()
while colour != "":
    try:
        print(f"The Hex code for {colour.title()} is {HEX_CODE_TO_COLOUR[colour]}")
    except KeyError:
        print("Invalid colour")
    colour = input("Enter colour: ").upper()