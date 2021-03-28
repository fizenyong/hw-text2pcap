import PySimpleGUIWx as sg
import subprocess
from pathlib import Path


def execute_command(*args):
    # Wait until return, blocking

    expanded_args = []
    for a in args:
        expanded_args.append(a)

    try:
        sp = subprocess.Popen(
            expanded_args,
            shell=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        out, err = sp.communicate()
        if out:
            print(out.decode("utf-8"))
        if err:
            print(err.decode("utf-8"))
    except:
        pass


def set_path():
    with open("path.txt", "r") as file_object:
        path = file_object.readlines()[1].split(";")

    # hex_path = Path(sys._MEIPASS).absolute() / "convert-hex.exe" #Standalone Bulid
    # hex_path = Path(__file__).parent / "convert-hex.exe"
    hex_path = Path(path[0].strip()) / "convert-hex.exe"
    pcap_path = Path(path[1].strip()) / "text2pcap.exe"

    return hex_path, pcap_path


if __name__ == "__main__":

    sg.LOOK_AND_FEEL_TABLE["Native"] = {
        "BACKGROUND": sg.COLOR_SYSTEM_DEFAULT,
        "TEXT": sg.COLOR_SYSTEM_DEFAULT,
        "INPUT": sg.COLOR_SYSTEM_DEFAULT,
        "TEXT_INPUT": sg.COLOR_SYSTEM_DEFAULT,
        "SCROLL": sg.COLOR_SYSTEM_DEFAULT,
        "BUTTON": (sg.COLOR_SYSTEM_DEFAULT, sg.COLOR_SYSTEM_DEFAULT),
        "PROGRESS": sg.DEFAULT_PROGRESS_BAR_COLOR,
        "BORDER": 1,
        "SLIDER_DEPTH": 0,
        "PROGRESS_DEPTH": 0,
    }

    sg.wx.NO_BORDER = 0  # No styling
    sg.theme("Native")

    hex_path, pcap_path = set_path()

    layout = [
        [
            sg.Frame(
                "Exe Path",
                [
                    [
                        sg.Text("convert-hex", size=(12, 1)),
                        sg.Input(key="hex_path", default_text=hex_path),
                        sg.FileBrowse(file_types=(("EXE", "convert-hex.exe"),)),
                    ],
                    [
                        sg.Text("text2pcap", size=(12, 1)),
                        sg.Input(key="pcap_path", default_text=pcap_path),
                        sg.FileBrowse(file_types=(("EXE", "text2pcap.exe"),)),
                    ],
                ],
            )
        ],
        [sg.Text("Select text file:")],
        [
            sg.Text("File", size=(12, 1)),
            sg.Input(key="file_path"),
            sg.FileBrowse(initial_folder=".\\", file_types=(("TXT", "*.txt"),)),
        ],
        [
            sg.Button("txt", size=(8, 2), auto_size_button=False),
            sg.Button("pcap", size=(8, 2), auto_size_button=False),
        ],
        [sg.Output(size=(45, 7))],
    ]

    window = sg.Window("Window Title", layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED):
            break
        if event == "txt":
            execute_command(values["hex_path"], values["file_path"])
        elif event == "pcap":
            fname = "hex-" + Path(values["file_path"]).stem
            execute_command(
                values["pcap_path"], "-o", "dec",
                str(Path(__file__).parent / (fname + ".txt")),
                str(Path(__file__).parent / (fname + ".pcap")),
            )

    window.close()