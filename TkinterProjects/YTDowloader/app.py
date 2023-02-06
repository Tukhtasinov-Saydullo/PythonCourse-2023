from pytube import YouTube
from tkinter import Tk, Label, Button, messagebox, Entry

# Window
window = Tk()
window.title('YouTube Downloader')
window.geometry('480x240')


# Func Command
def show_info():
    url = entry_url.get()
    if len(url) == 0:
        messagebox.showinfo('Error', 'Paste Link Video!')
    else:
        yt = YouTube(url)
        title = yt.title
        author = yt.author
        views = yt.views
        time = yt.length
        messagebox.showinfo('Info', f'Title {title}\nAuthor {author}\nViews {views}\nTime {time}')


def download_video():
    url = entry_url.get()
    if len(url) == 0:
        messagebox.showinfo('Error', 'Paste Link Video!')
    else:
        yt = YouTube(url)
        video = yt.streams.filter(resolution='720p').first()
        video.download('../')
        messagebox.showinfo('News', 'Download Complete!')


# Input and Label
label_url = Label(window, text='URL: ', padx=10, pady=10)
label_url.grid(row=1, column=0)
entry_url = Entry(window, width=50)
entry_url.grid(row=1, column=1, pady=10, padx=10)

# Buttons
down_btn = Button(window, padx=10, pady=10, text='Download', command=download_video)
down_btn.grid(row=2, column=1)

info_button = Button(window, padx=10, pady=10, text='Video Info', command=show_info)
info_button.grid(row=3, column=1)
if __name__ == '__main__':
    window.mainloop()
