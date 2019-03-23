COLOUR_HEX = {'aquamarine2': '#76eec6', 'azure3': '#c1cdcd', 'bisque1': '#ffe4c4', 'BlueViolet': '#8a2be2',
              'CadetBlue': '#5f9ea0', 'chocolate': '#d2691e', 'coral1': '#ff7256', 'CornflowerBlue': "#6495ed",
              'cyan4': '#008b8b', 'DarkGreen': '#006400'}

colour_name = input('Enter colour name: ')
while colour_name != "":
    if colour_name in COLOUR_HEX:
        print("The code for {} is {}".format(colour_name, COLOUR_HEX[colour_name]))
    else:
        print('Invalid colour name, try again.')
    colour_name = input("Enter a colour name: ")
