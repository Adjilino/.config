import darkdetect, time

def detectTheme():
    data = ""

    if darkdetect.isDark():
        with open("alacritty-dark.toml", "r") as f:
            data = f.read() 
    else:
        with open("alacritty-light.toml", "r") as f:
            data = f.read()

    with open("alacritty.yml", "w") as f:
        f.write(data)

    time.sleep(2)
    detectTheme()

detectTheme()

