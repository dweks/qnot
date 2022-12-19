from ut import write_note_to_file, msg, imp, date_enc
from os import path, mkdir, getcwd

EX_PATH = "exports/"


def exec_export(note):
    if not path.exists(EX_PATH):
        mkdir(EX_PATH)
        print(msg("Export directory created."))

    full_path = EX_PATH + "qnot_exp_" + date_enc() + ".txt"
    print(imp(f"Exporting to: {getcwd()}{full_path}"))
    response = input(imp("Confirm export Y/n > "))
    if response == 'Y':
        write_note_to_file(note, full_path)
        return "exported"
    return "cancel"
