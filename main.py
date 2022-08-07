from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

from pytube import YouTube
import os

Window.size = (350, 600)

KV = """ 

ScreenManager:
    HomeScreen:

<HomeScreen>:
    name: 'home'
    canvas.before:
        Color:
            rgba: 227/255, 235/255, 254/255, 1
        Rectangle:
            pos: self.pos
            size: self.size
            
    MDCard:
        size_hint: None, None
        size: 300, 475
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 40
        padding: 20
        spacing: 30
        orientation: 'vertical'
        radius: [5]
        md_bg_color: 0/255, 165/255, 86/255, 1
        
        MDLabel:
            id: login_label
            text: 'YTube Downloader '
            font_size: 25
            halign: 'center'
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            bold: True
            size_hint_y: None
            height: self.texture_size[1]
            
        AsyncImage:
            source: 'https://yt3.ggpht.com/584JjRp5QMuKbyduM_2k5RlXFqHJtQ0qLIPZpwbUjMJmgzZngHcam5JMuZQxyzGMV5ljwJRl0Q=s900-c-k-c0x00ffffff-no-rj'
            size: 200, 200
            center_x: self.parent.center_x
            center_y: self.parent.center_y
            
        MDTextField:
            id: url
            mode: "rectangle"
            hint_text: "Enter Url"
            color_mode: 'custom'
            line_color_focus: 1, 1, 1, 1
            font_size:"18dp"
            margin_vertical: 5
            
        CurvedButton:
            id: mp4btn
            size_hint: None, None
            size: 250, 40
            text: "Download Mp4"
            on_release: app.YouTube_Video_download()
            
        CurvedButton:
            id: mp3btn
            size_hint: None, None
            size: 250, 40
            text: "Download Mp3"
            on_release: app.YouTube_Audio_download()
        
    MDLabel:
        id: login_label
        text: '© 2022 | GSS All Right Reserved.'
        font_size: 18
        theme_text_color: "Custom"
        text_color: 0, 0, 0, .5
        halign: 'center'                
        size_hint_y: None
        height: self.texture_size[1]
        padding_y: 20
        
<CurvedButton@Button>:
    background_color: (0, 0, 0, 0)
    background_normal: ''
    font_size: 22
    canvas.before:
        Color: 
            rgba: (0/255, 150/255, 0/255, 1)
                
        RoundedRectangle:
            size:self.size
            pos: self.pos
            radius: [10]
    
"""


class HomeScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))


class YTubeApp(MDApp):
    def build(self):
        Window.clearcolor = (227 / 255, 235 / 255, 254 / 255, 1)
        self.screen = Builder.load_string(KV)
        return self.screen

    def YouTube_Video_download(self):
        path = "C:/Users/Admin/Documents/YTube/Videos"
        url = self.screen.get_screen('home').ids.url.text
        print(url)
        yt = YouTube(url)

        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        if not os.path.exists(path):
            os.makedirs(path)

        print('Loading....')
        video.download(path)
        print('downloaded successfully at', path)

    def YouTube_Audio_download(self):
        path = "C:/Users/Admin/Documents/YTube/Audios"
        url = self.screen.get_screen('home').ids.url.text
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()

        if not os.path.exists(path):
            os.makedirs(path)

        out_file = audio.download(path)

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)


if __name__ == '__main__':
    YTubeApp().run()
