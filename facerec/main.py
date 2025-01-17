'''
Hey Hey!
This is a simple GUI that makes use of your PC's camera and the Face Recognition Python Library to compare a face captured by
the camera with a reference image or reference images.
Keep your reference images in the same directory as this Python program, saving each of them with the name "refx.png" where x = 1, 2, 3,...

'''

from kivy.lang import Builder
from kivy.app import App
# from kivy.core.camera import Camera
# from kivy.uix.camera import Camera, CoreCamera
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

from recognizer import recognize_face_from_file

Window.borderless = True
Window.size = 350, 700

#KVLang
style = '''

<CustomButton@Button>:
    background_down: ''
    background_normal: ''
    background_color: 123/255, 23/255, 133/255, 1.0
    color: 1, 1, 1, 1
    on_press:
        self.background_color = 123/255, 23/255, 133/255, 0.7
    on_release:
        self.background_color = 123/255, 23/255, 133/255, 1.0
<Main>:
    Label:
        text: "[b]Messing Around with Face Recognition[/b]"
        markup: True
        font_size: 18
        pos_hint: {"top": 1, "center_x": 0.5}
        size_hint: None, None

    CustomButton:
        pos_hint: {"right": 1,"top": 1}
        text: "x"
        size_hint: None, None
        size: 30, 30
        background_color:  1, .2, 0, 1
        on_release: exit()

    Label:
        markup: True
        y: button.height + 10
        size_hint: [None, None]
        width: root.width
        font_size: 13
        
    CustomButton:
        id: button
        text: "CHECK FOR MATCHES"
        width: root.width
        height: 70
        size_hint: [None, None]
        pos: 0, 0
        on_release:
            app.recognize_face()

    Widget:
        id: camera_bkg
        size_hint: [None, None]
        size: [300, 300]
        center: root.center
        canvas.before:
            Color:
                rgba: 0.98, 0.58, 0.15, 1
            RoundedRectangle:
                radius: [20,]
                size: self.size
                pos: self.pos

    Camera:
        id: cam
        center: camera_bkg.center
        size: 290, 290
        resolution: 290, 290
        play: True
        size_hint: None, None
        keep_ratio: False
        allow_stretch: True

'''

class Main(FloatLayout):
    def recognize_face(self):
        texture = self.ids.cam.texture
        texture.save("tempcam.png", flipped=False)
        results = recognize_face_from_file()
        # if results:
        print("Matches found in: ", results)

class FaceRecognitionTest(App):
    def build(self):
        self.root = Main()
        return self.root
    
    def recognize_face(self):
        self.root.recognize_face()
    

if __name__ == '__main__':
    Builder.load_string(style)
    FaceRecognitionTest().run()