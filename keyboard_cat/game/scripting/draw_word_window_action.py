from constants import *
from game.scripting.action import Action



class DrawWordWindowAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        word_window = cast.get_first_actor(word_window_GROUP)
        body = word_window.get_body()
        image = word_window.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)

        backward_letters = cast.get_actors(input_GROUP)
        if len(backward_letters) > 0:
            user_input = []
            forward_letters = ""
            
            for letter in backward_letters:
                letter = backward_letters[len(backward_letters) - 1]
                user_input.append(letter)
                forward_letters = "".join(user_input)
                backward_letters.remove(letter)
            word_window.set_value(user_input_format.format(forward_letters))
            self._video_service.draw_text(word_window, position, 2)


       