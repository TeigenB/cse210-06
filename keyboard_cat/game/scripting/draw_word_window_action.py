from constants import *
from game.scripting.action import Action


class DrawWordWindowAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        word_window = cast.get_first_actor(word_window_GROUP)
        body = word_window.get_body()
            
        #animation = word_window.get_animation()
        image = word_window.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)