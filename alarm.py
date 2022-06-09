from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.core.audio import SoundLoader, Sound


class Alarm(App):
    def build(self):
        self.box = BoxLayout(orientation='vertical')
        parentLay = BoxLayout(orientation='vertical')

        self.childLay1 = GridLayout(cols=3)
        self.childLay2 = GridLayout(cols=3)

        l1 = Label(text='HOUR', font_size=50, color=(0, 0, 1, 1), size_hint_y=1)
        l2 = Label(text='MINUTE', font_size=50, color=(0, 0, 1, 1), size_hint_y=1)
        l3 = Label(text='SECOND', font_size=50, color=(0, 0, 1, 1), size_hint_y=1)

        self.hour = TextInput(text='', font_size=70, halign='center', size_hint=(1, None), readonly=False)
        self.min = TextInput(text='', font_size=70, halign='center', size_hint=(1,None), readonly=False)
        self.sec = TextInput(text='', font_size=70, halign='center', size_hint=(1,None), readonly=False)

        self.alarm_label = Button(text='ALARM', font_size=70, background_color=(0,1,0,1), size_hint_y=None)
        self.start = Button(text='START', font_size=70, background_color=(0,1,0,1), size_hint_y=None)
        self.start.bind(on_press= self.start_clock)

        self.childLay1.add_widget(l1)
        self.childLay1.add_widget(l2)
        self.childLay1.add_widget(l3)

        self.childLay2.add_widget(self.hour)
        self.childLay2.add_widget(self.min)
        self.childLay2.add_widget(self.sec)

        parentLay.add_widget(self.childLay1)
        parentLay.add_widget(self.childLay2)

        self.box.add_widget(self.alarm_label)
        self.box.add_widget(parentLay)
        self.box.add_widget(self.start)

        return self.box

    def start_clock(self, instance):
        self.hour.readonly = True
        self.min.readonly = True
        self.sec.readonly = True
        self.start.text = 'stop'
        self.start.bind(on_press=self.stop_clock)

        # Starting The Clock Calculation
        Clock.schedule_interval(self.calculate, 1)

    def calculate(self, instance):
        text1 = self.hour.text
        if text1 == '':
            text1 = '00'
        text2 = self.min.text
        if text2 == '':
            text2 = '00'
        text3 = self.sec.text
        if text3 == '':
            text3 = '00'

        sum1 = 0
        sum2 = 0
        sum3 = 0
        sum1 += int(text1)
        sum2 += int(text2)
        sum3 += int(text3)

        self.sec.text = str(sum3-1)
        if sum3 == 0:
            if sum2 >= 0 and sum2 <= 9:
                self.min.text = '0'+str(sum2 - 1)
            else:
                self.min.text = str(sum2 - 1)
            self.sec.text = '60'
        if sum2 == 0:
            if sum1 >= 0 and sum1 <= 9:
                self.hour.text = '0'+str(sum1 - 1)
            else:
                self.hour.text = str(sum1 - 1)
            if sum1 == 0:
                self.min.text = '00'
            else:
                self.min.text = '60'
        if sum1 == 0:
            self.hour.text = '00'
        if sum1 == 0 and sum2 == 0 and sum3 == 0:
            self.hour.text = '00'
            self.min.text = '00'
            self.sec.text = '00'
            sound = SoundLoader.load('sound.mp3')
            if sound:
                sound.play()

    def stop_clock(self, instance):
        sound.stop()
        App.get_running_app().stop()
        Alarm().run()


Alarm().run()