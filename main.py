from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


kv = """
<MyScreenManager>:
    NameScreen:
    GenderScreen:
    MaritalScreen:
    JobScreen:
    ThankYouScreen:

<NameScreen>:
    name: 'name_screen'
    RelativeLayout:
        canvas.before:
            Color: 
                rgba: 0.6, 0.82, 0.53, 1
            Rectangle: 
                pos: self.pos
                size: self.size
        Label:
            text: 'Adınız:'
            color: 0,0,0,1
            size_hint: 1, 0.2
            pos_hint: {"center_x": 0.5, "center_y": 0.8}
            font_size: 50
            font_name: "Comic"
            
        TextInput:
            id: name_input
            multiline: True
            size_hint: 1, 0.2
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            font_size: 50
        Button:
            text: 'Sonraki'
            color: 0,0,0,1
            size_hint: 0.6, 0.15
            pos_hint: {"center_x": 0.5, "center_y": 0.2}
            font_size: 50
            font_name: "Comic"
            background_color: (.06, .45, .45, 1)
            on_press: root.submit_name()

<GenderScreen>:
    name: 'gender_screen'
    RelativeLayout:
        canvas.before:
            Color: 
                rgba: 0.6, 0.82, 0.53, 1
            Rectangle: 
                pos: self.pos
                size: self.size
        Label:
            text: 'Cinsiyetiniz:'
            color: 0,0,0,1
            size_hint: 1, 0.2
            pos_hint: {"center_x": 0.5, "center_y": 0.8}
            font_size: 50
            font_name: "Comic"
        TextInput:
            id: gender_input
            multiline: True
            size_hint: 1, 0.2
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            font_size: 50
        Button:
            text: 'Sonraki'
            color: 0,0,0,1
            size_hint: 0.6, 0.15
            pos_hint: {"center_x": 0.5, "center_y": 0.2}
            font_size: 50
            font_name: "Comic"
            background_color: (.06, .45, .45, 1)
            on_press: root.submit_gender()

<MaritalScreen>:
    name: 'marital_screen'
    RelativeLayout:
        canvas.before:
            Color: 
                rgba: 0.6, 0.82, 0.53, 1
            Rectangle: 
                pos: self.pos
                size: self.size
        orientation: 'vertical'
        Label:
            text: 'Medeni Hal:'
            color: 0,0,0,1
            size_hint: 1, 0.2
            pos_hint: {"center_x": 0.5, "center_y": 0.8}
            font_size: 50
            font_name: "Comic"
        TextInput:
            id: marital_input
            multiline: True
            size_hint: 1, 0.2
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            font_size: 50
        Button:
            text: 'Sonraki'
            color: 0,0,0,1
            size_hint: 0.6, 0.15
            pos_hint: {"center_x": 0.5, "center_y": 0.2}
            font_size: 50
            font_name: "Comic"
            background_color: (.06, .45, .45, 1)
            on_press: root.submit_marital()

<JobScreen>:
    name: 'job_screen'
    RelativeLayout:
        canvas.before:
            Color: 
                rgba: 0.6, 0.82, 0.53, 1
            Rectangle: 
                pos: self.pos
                size: self.size
        orientation: 'vertical'
        Label:
            text: 'Mesleğiniz:'
            color: 0,0,0,1
            size_hint: 1, 0.2
            pos_hint: {"center_x": 0.5, "center_y": 0.8}
            font_size: 50
            font_name: "Comic"
        TextInput:
            id: job_input
            multiline: True
            size_hint: 1, 0.2
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            font_size: 50
        Button:
            text: 'Gönder'
            color: 0,0,0,1
            size_hint: 0.6, 0.15
            pos_hint: {"center_x": 0.5, "center_y": 0.2}
            font_size: 50
            font_name: "Comic"
            background_color: (.06, .45, .45, 1)
            on_press: root.submit_job()

<ThankYouScreen>:
    name: 'thankyou_screen'
    BoxLayout:
        canvas.before:
            Color: 
                rgba: 0.6, 0.82, 0.53, 1
            Rectangle: 
                pos: self.pos
                size: self.size
        orientation: 'vertical'
        Label:
            text: 'Teşekkürler'
            color: 0,0,0,1
            size_hint: 1, 0.2
            pos_hint: {"center_x": 0.5, "center_y": 0.8}
            font_size: 50
            font_name: "Comic"
"""

Builder.load_string(kv)


class NameScreen(Screen):
    def submit_name(self):
        app = App.get_running_app()
        name = self.ids.name_input.text
        app.name = name
        gender_screen = GenderScreen()
        app.root.add_widget(gender_screen)
        app.root.current = "gender_screen"


class GenderScreen(Screen):
    def submit_gender(self):
        app = App.get_running_app()
        gender = self.ids.gender_input.text
        app.gender = gender
        app.root.current = "marital_screen"


class MaritalScreen(Screen):
    def submit_marital(self):
        app = App.get_running_app()
        marital = self.ids.marital_input.text
        app.marital = marital
        app.root.current = "job_screen"


class JobScreen(Screen):
    def submit_job(self):
        app = App.get_running_app()
        job = self.ids.job_input.text
        app.job = job
        app.root.current = "thankyou_screen"


class ThankYouScreen(Screen):
    pass


class MyScreenManager(ScreenManager):
    pass


class MyApp(App):
    name = ""
    gender = ""

    def build(self):
        self.screen_manager = MyScreenManager()
        return self.screen_manager


if __name__ == "__main__":
    MyApp().run()
