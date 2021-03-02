import re, sys
from pathlib import Path


def read_file(filepath):
    
    data = filepath.read_text()
    data = re.sub(r"^ +", "", data, flags=re.M)  # Remove leading space

    return data


def write_file(content, filename):
    with open(Path(__file__).parent / filename, "w") as file_object:
    #with open(Path(sys._MEIPASS).absolute() / filename, "w") as file_object:
        for line in content:
            file_object.write(line)
            file_object.write("\n")


def add_offset(hex_input):
    hexin = hexout = []
    offset = 0

    hexin = hex_input.splitlines()

    for line in hexin:
        line = str(offset).zfill(4) + " " + line
        offset = offset + (len(line) + 1 - 5) // 3
        hexout.append(line)

    return "\n".join(hexout)


rx_packet = re.compile(
    r"""
    ^
    Packet\S*:\s(?P<packet_name>\d+)\n
    -+\s
    (?P<hex_content>[\s\S]+?)
    (?=^-+)
""",
    re.MULTILINE | re.VERBOSE,
)

if __name__ == "__main__":

    filepath = sys.argv[1]
    data = read_file(Path(filepath))

    print(f'Input from: {filepath}')
    print(f'Output to: {Path(__file__).parent.absolute()}')

    hexdata = [p.group("hex_content") for p in rx_packet.finditer(data)]

    print(f'Read {len(hexdata)} potential packets')

    hexdata = [add_offset(r) for r in hexdata]

    write_file(hexdata, "hex-" + Path(filepath).stem + ".txt")