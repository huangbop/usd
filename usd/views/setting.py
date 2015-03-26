



MAIN_WIDTH = 1024
MAIN_HEIGHT = 768


title_style = """
#bg {
background-color: qlineargradient(spread:pad,
x1:0, y1:1, x2:0, y2:0,
stop:0 rgb(208, 208, 208), stop:1 rgb(224, 224, 224)); 
}

#btn_setting, #btn_min, #btn_close, #tab_uart, #tab_gpio, #tab_config, #tab_register {
background-color: rgba(0, 0, 0, 0);
}

QToolButton {
color: rgb(64, 64, 64);
font: 8pt "dejavu sans mono";
}

"""


status_style = """
#bg {
background-color: rgb(192, 192, 192);

}


"""

tabs_style = """
#bg {
background-color: white;
}

QPlainTextEdit {
border-radius: 8px;
background-color: rgb(208, 224, 240);
font: 10pt "dejavu sans mono";
}

QPushButton {
color: rgb(64, 64, 64);
border-color: rgba(80, 80, 80, 0);
background-color: qlineargradient(spread:pad,
x1:0, y1:1, x2:0, y2:0,
stop:0 rgb(208, 208, 208), stop:1 rgb(208, 208, 208));
border-style: solid;
border-width: 2px;
border-radius: 10px;
font: 8pt "dejavu sans mono";
}

QPushButton:hover {
background-color: qlineargradient(spread:pad,
x1:0, y1:1, x2:0, y2:0,
stop:0 rgb(208, 208, 208), stop:1 rgb(224, 224, 224));
}

QPushButton:pressed {
border-width: 4px;
}

QPushButton:disabled {
background-color: qlineargradient(spread:pad,
x1:0, y1:1, x2:0, y2:0,
stop:0 rgb(240, 240, 240), stop:1 rgb(240, 240, 240));
}

"""

colors = (
    (255, 0, 0, 255),
    (255, 165, 0, 255),
    (240, 240, 0, 255),
    (0, 255, 0, 255),
    (0, 0, 255, 255),
    (0, 128, 128, 255),
    (128, 0, 128, 255),
    (128, 128, 0, 255),
    (0, 0, 0, 0),         # Disable color
)

