import tkinter as tk
from tkinter import Button, Entry, Checkbutton
from tkinter.constants import BOTTOM, RIGHT

import ttkbootstrap as ttk

import web_interaction


def bunpro_bot(start_page, end_page, decks):
    bunpro = web_interaction.Bunpro()

    bunpro.get_vocab()
    bunpro.login()

    for deck in decks:
        print(deck)
        start_mastered = len(bunpro.mastered_vocab)
        bunpro.edit_deck(start_page, end_page, deck)
        print(f"Mastered {len(bunpro.mastered_vocab) - start_mastered} in deck {deck.split("/")[1]}")

    print(f"Mastered {len(bunpro.mastered_vocab)} items")
    print(bunpro.mastered_vocab)

root = ttk.Window(themename="darkly")
root.title("Bunpro Progress Updater")
root.geometry("500x600")

label = ttk.Label(root, text="Update your SRS stage on all the vocabulary you already know!")
label.pack(pady=5)

def wanikani_button_click():
    wanikani_message_str.set("Success!")


wanikani_api_key = tk.StringVar()

wanikani_frame = ttk.Frame(borderwidth= 10, relief=tk.GROOVE)

wanikani_heading = ttk.Label(wanikani_frame, text="Wanikani")
wanikani_heading.pack(pady=5)

wanikani_api_frame = ttk.Frame(wanikani_frame)

wanikani_api_entry = ttk.Entry(wanikani_api_frame, textvariable=wanikani_api_key, width=30)
wanikani_api_entry.insert(0, "Enter your Wanikani API Key")
wanikani_api_entry.pack(pady=5, side="left", padx=5)

wanikani_import_button = ttk.Button(wanikani_api_frame, text="Find all the known words from Wanikani", command=wanikani_button_click)
wanikani_import_button.pack(pady=5, padx=5, side=RIGHT)

wanikani_api_frame.pack()

wanikani_message_str = tk.StringVar()
wanikani_message = ttk.Label(wanikani_frame, textvariable=wanikani_message_str)
wanikani_message.pack(pady=5)



wanikani_frame.pack(pady=5)


# Anki --------------------------------------------------------------------
anki_frame = ttk.Frame(root, borderwidth= 10, relief=tk.GROOVE)
def anki_button_click():
    anki_message_str.set("Success")

anki_heading = ttk.Label(anki_frame, text="Anki")
anki_heading.pack(pady=5)

anki_import_button = ttk.Button(anki_frame, text="import words from anki", command=anki_button_click)
anki_import_button.pack(pady=5)

anki_message_str = tk.StringVar()
anki_message = ttk.Label(anki_frame, textvariable=anki_message_str)
anki_message.pack()

anki_frame.pack(pady=5)

# Bunpro -------------------------------------------------------------------------
bunpro_frame = ttk.Frame(borderwidth= 10, relief=tk.GROOVE)

bunpro_section_heading = ttk.Label(bunpro_frame, text="Bunpro")
bunpro_section_heading.pack()

deck_frame = ttk.Frame(bunpro_frame)

check_var1 = tk.IntVar()
check_var2 = tk.IntVar()
check_var3 = tk.IntVar()
check_var4 = tk.IntVar()
check_var5 = tk.IntVar()


n5_check = ttk.Checkbutton(deck_frame, text="N5 Deck", onvalue=5, offvalue=0, variable=check_var5)
n5_check.pack(side="left", padx=5)

n4_check = ttk.Checkbutton(deck_frame, text="N4 Deck", onvalue=4, offvalue=0, variable=check_var4)
n4_check.pack(side="left", padx=5)

n3_check = ttk.Checkbutton(deck_frame, text="N3 Deck", onvalue=3, offvalue=0, variable=check_var3)
n3_check.pack(side="left", padx=5)

n2_check = ttk.Checkbutton(deck_frame, text="N2 Deck", onvalue=2, offvalue=0, variable=check_var2)
n2_check.pack(side="left", padx=5)

n1_check = ttk.Checkbutton(deck_frame, text="N1 Deck", onvalue=1, offvalue=0, variable=check_var1)
n1_check.pack(side="left", padx=5)

def deck_select_btn():
    text = deck_select_text.get()
    if text == "uncheck all":
        print("unselect all")
        deck_select_text.set("select all")
        check_var1.set(0)
        check_var2.set(0)
        check_var3.set(0)
        check_var4.set(0)
        check_var5.set(0)


    elif text == "select all":
        print("select all")
        deck_select_text.set("uncheck all")
        check_var1.set(1)
        check_var2.set(2)
        check_var3.set(3)
        check_var4.set(4)
        check_var5.set(5)

deck_select_text = ttk.StringVar()
deck_select_text.set("select all")
deck_select = ttk.Button(deck_frame, textvariable=deck_select_text, command=deck_select_btn)
deck_select.pack(side="left", padx=5)

deck_frame.pack(pady=10)

page_frame = ttk.Frame(bunpro_frame)

start_page_int = tk.IntVar()
start_page_label = ttk.Label(page_frame, text="Starting Page: ")
start_page_entry = ttk.Entry(page_frame, textvariable=start_page_int)
start_page_label.pack(side="left", padx=5)
start_page_entry.pack(side="left", padx=5)

end_page_int = tk.IntVar()
end_page_label = ttk.Label(page_frame, text="Ending Page: ")
end_page_entry = ttk.Entry(page_frame, textvariable=end_page_int)
end_page_label.pack(side="left", padx=5)
end_page_entry.pack(side="left", padx=5)

page_frame.pack(pady=10)




def all_pages():
    if all_pages_int.get() == 1:
        start_page_entry.config(state="disable")
        end_page_entry.config(state="disable")
        start_page_int.set(1)
        end_page_int.set(0)
    elif all_pages_int.get() == 0:
        start_page_entry.config(state="normal")
        end_page_entry.config(state="normal")


all_pages_int = tk.IntVar()
all_pages = Checkbutton(bunpro_frame, text="Go through all pages", onvalue=1, offvalue=0, command=all_pages, variable=all_pages_int)
all_pages.pack()

def start_bot():
    selected_decks = [DECKS[check_var1.get()], DECKS[check_var2.get()], DECKS[check_var3.get()], DECKS[check_var4.get()], DECKS[check_var5.get()]]
    selected_decks = [deck for deck in selected_decks if deck]
    if not selected_decks:
        bunpro_message_str.set("Please select at least one deck")
    else:
        bunpro_message_str.set("Starting the Bot")
        bunpro_bot(start_page_int.get(), end_page_int.get(), selected_decks)


start_btn = ttk.Button(bunpro_frame, text="Start mastering Bot", command=start_bot)
start_btn.pack()

bunpro_message_str = tk.StringVar()
bunpro_message = ttk.Label(bunpro_frame, textvariable=bunpro_message_str)
bunpro_message.pack()

bunpro_frame.pack(pady=5)

DECKS = ["", "qqovik/Bunpro-N1-Vocab",
         "dxbsvk/Bunpro-N2-Vocab", "mvt76c/Bunpro-N3-Vocab", "lh0vxb/Bunpro-N4-Vocab" , "resqiy/Bunpro-N5-Vocab"]

root.mainloop()

