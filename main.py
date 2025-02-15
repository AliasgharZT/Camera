from kivymd.app import MDApp
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.lang import Builder 
# from kivy.uix.image import Image
# import datetime

from kivy.core.window import Window
Window.size = (275,600) 

Builder.load_file('style.kv')

class Style(MDAnchorLayout):
    def click_start(self):
        if self.ids.start.text=='START':
            self.ids.cam.play=True
            self.ids.start.text='FINISH'
        else:
            # now=datetime.datetime.now()
            # im=Image()  
            # im.export_to_png("im_{}.png".format(now))
            # im.source="im_{}.png".format(now) 
            self.ids.cam.play=False   
            self.ids.start.text='START'


class Main(MDApp):
    def build(self):
        self.theme_cls.theme_style='Dark'
        self.title=' TEMP '
        return Style() 

Main().run()
