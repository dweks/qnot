from util import prs_note, date_enc, user_editor, file_str, os, sp, save_note, write_to_file


# Entry-point for cmds called from dispatch table in Admin
# def exec_edit(note):
#     TEMP_PATH = r"./.temp/temp_note_" + date_enc()
#     func = exec_edit()
#
#     editor = user_editor()
#     if editor is not None:
#         run_editor = sp.run([editor, TEMP_PATH])
#         # Cases when opened editor is interrupted before exiting.
#         if run_editor.returncode != 0:
#             raise OSError(f"Editor interrupted; note not created ({func})")
#
#     else:
#         raise RuntimeError(f"No default editor found; check $EDITOR or $VISUAL? ({func})")
#
#     # Remove temp file, parse note, insert to database
#     if os.path.isfile(TEMP_PATH):
#         note = file_str(TEMP_PATH)
#         os.remove(TEMP_PATH)
#         note = prs_note(note)
#
#         save_note(note)
#     else:
#         raise FileNotFoundError(f"Temporary note file not created, qnot not saved ({func})")
