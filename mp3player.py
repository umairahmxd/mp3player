from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title('MP3 Player')
root.geometry("400x650")
root.iconbitmap('C:\\projects\\image\\icon.ico')

pygame.mixer.init()

global is_paused
is_paused = True

#add song function
def add_song():
    song = filedialog.askopenfilename(initialdir="C:\\projects\\audio\\", title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
    
    #strip out anything uness
    song = song.replace("C:/Users/umair/Music/", "")
    song = song.replace(".mp3", "")
    song_library.select_set(0)
    #song add to library 
    song_library.insert(END, song)
    
#add multiple songs
def add_many_song():
    songs = filedialog.askopenfilenames(initialdir="C:\\projects\\audio\\", title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
#add a bunch of songs
    for song in songs:
        #strip out anything uness
        song = song.replace("C:/Users/umair/Music/", "")
        song = song.replace(".mp3", "")

        #song add to library 
        song_library.insert(END, song)
        song_library.select_set(1)

#play a song
def play():
    song = song_library.get(ACTIVE)
    song = f"C:\\Users\\umair\\Music\\{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_library.selection_clear(ACTIVE)


#pause a song
def pause():
    global is_paused

    if is_paused:
        pygame.mixer.music.pause()
        is_paused = False
    else:
        pygame.mixer.music.unpause()
        is_paused = True
#invert colours to make dark mode
def dark_mode():
    pass

#rewind a song
def rewind():
    pygame.mixer.music.rewind()

#forward a song
def forward():
    x = song_library.curselection()
    x = x[0]
    song = song_library.get(x)
    song = f"C:\\Users\\umair\\Music\\{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

#list of songs
song_library = Listbox(root, bg="black", fg="white", height=33, width=60, selectbackground='gray', selectforeground="black")
song_library.pack(pady=20)

#images for buttons
play_image = PhotoImage(file= 'C:\\projects\\image\\play.png')
rewind_image = PhotoImage(file= 'C:\\projects\\image\\rewind.png')
pause_image = PhotoImage(file= 'C:\\projects\\image\\pause.png')
unpause_image = PhotoImage(file = 'C:\\projects\\image\\unpause.png')
forward_image = PhotoImage(file= 'C:\\projects\\image\\forward.png')


#frame for buttons
controls_frame = Frame(root)
controls_frame.pack()

#create buttons
play_button = Button(controls_frame, image=play_image, borderwidth=0, command=play)
play_button.grid(row=2, column=1)
rewind_button = Button(controls_frame, image=rewind_image, borderwidth=0, command=rewind)
rewind_button.grid(row=2, column=0)
pause_button = Button(controls_frame, image=pause_image, borderwidth=0, command=pause)
pause_button.grid(row=2, column=2)
forward_button = Button(controls_frame, image=forward_image, borderwidth=0, command=forward)
forward_button.grid(row=2, column=3)



#create menu

mp3_menu = Menu(root)
root.config(menu=mp3_menu)

#adding songs
add_songs = Menu(mp3_menu)
mp3_menu.add_cascade(label="Add Songs", menu=add_songs)
add_songs.add_command(label= "Add one song to the playlist", command=add_song)

add_many_songs = Menu(mp3_menu)
mp3_menu.add_cascade(label="Add Many Songs", menu=add_many_songs)
add_many_songs.add_command(label= "Add multiple songs to the playlist", command=add_many_song)

view = Menu(mp3_menu)
mp3_menu.add_cascade(label="View", menu=view)
view.add_command(label= "Change to Dark Mode", command=dark_mode)

root.mainloop()