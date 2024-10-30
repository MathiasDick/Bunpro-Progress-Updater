from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import re
import os
import web_interaction
# SETUP -------------------------------------------------------------------------------------#





# ----------------------------------------------------------------------------------------------#

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