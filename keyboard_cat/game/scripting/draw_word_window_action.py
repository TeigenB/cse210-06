from constants import *
from game.scripting.action import Action
from game.casting.cast import Cast
from game.casting.point import Point



class DrawWordWindowAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
        
    def execute(self, cast, script, callback):
        word_window = cast.get_first_actor(word_window_GROUP)
        body = word_window.get_body()
        image = word_window.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)

        letters = cast.get_actors(input_GROUP)
        user_word = "".join(letters)
       
        word_window.set_value(user_input_format.format(user_word))

        word_x = position.get_x() + 150
        word_point = Point(word_x, position.get_y())

        self._video_service.draw_text(word_window, word_point, 2)
        

       