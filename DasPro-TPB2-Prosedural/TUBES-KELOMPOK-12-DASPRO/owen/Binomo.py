import functions
from list_game_toko import list_game_toko  
from tambah_game import tambah_game
from  ubah_stok import ubah_stok
from search_game_at_store import search_game_at_store


def start():
    f = open("game.csv",'r')
    isi_file = f.read()
    temp_game_matrix = functions.gamecsv_pars(isi_file)
    
    command = input("Masukkan command: ")
    while command.lower() != "exit":
        if command.lower() == "list_game_toko":
            list_game_toko(temp_game_matrix)
        if command.lower() == "tambah_game":
            temp_game_matrix = tambah_game(temp_game_matrix)
        if command.lower() == "ubah_stok":
            temp_game_matrix = ubah_stok(temp_game_matrix)
        if command.lower() == "search_game_at_store":
            search_game_at_store(temp_game_matrix)
        command = input("Masukkan command: ")

start()
