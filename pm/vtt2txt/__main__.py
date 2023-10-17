from argparse import ArgumentParser
from pathlib import Path

from . import vtt_to_text


def main():
    parser = ArgumentParser(
        description="Create plain text output from VTT file."
    )
    parser.add_argument('vtt_file', type=Path)
    args = parser.parse_args()
    print(vtt_to_text(args.vtt_file.read_text()))


if __name__ == "__main__":
    main()
