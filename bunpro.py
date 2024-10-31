import tkinter as tk
from tkinter import Button, Entry

root = tk.Tk()
root.title("Bunpro Progress Updater")
root.geometry("400x300")

label = tk.Label(root, text="Update your SRS stage on all the vocabulary you already know!")
label.grid(row=0, column=0, columnspan=3)

def wanikani_button_click():
    label.config(text="clicked")

wanikani_api_entry = Entry(root)
wanikani_api_entry.insert(0, "Enter your Wanikani API Key")
wanikani_api_entry.grid(row=1, column=0)

wanikani_import_button = Button(root, text="Find all the known words from Wanikani", command=wanikani_button_click)
wanikani_import_button.grid(row=1, column=2)

def anki_button_click():
    pass

anki_import_button = Button(root, text="import words from anki", command=anki_button_click)
anki_import_button.grid(row=2, column = 1)

root.mainloop()

"""
bunpro = web_interaction.Bunpro()

bunpro.get_vocab()
bunpro.login()
bunpro.edit_deck()


STARTING_PAGE = int(input("On what page do you want to start? Smallest is 1: "))
END_PAGE = int(input("On what page do you want to end? If you want every page enter 0; Max is 20: "))


DECKS = ["resqiy/Bunpro-N5-Vocab", "lh0vxb/Bunpro-N4-Vocab ,mvt76c/Bunpro-N3-Vocab",
         "dxbsvk/Bunpro-N2-Vocab", "qqovik/Bunpro-N1-Vocab"]

for deck in DECKS:
    start_mastered = len(mastered_vocab)
    edit_deck(STARTING_PAGE, END_PAGE, deck)
    print(f"Mastered {len(mastered_vocab) - start_mastered} in deck {deck.split("/")[1]}")

print(f"Mastered {len(mastered_vocab)} items")
print(mastered_vocab)
"""