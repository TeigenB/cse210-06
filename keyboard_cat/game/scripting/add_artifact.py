from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.image import Image
from game.casting.body import Body
from game.casting.label import Label
from game.casting.artifact import Artifact


class AddArtifact(Action):
    pass

    def get_text(self):

        filename = "cse210-06/keyboard_cat/assets/data.txt"
        with open(filename, 'r') as file:
            list = file.readlines()
            text = random.choice(list)
            return text


    def execute(self, cast, script, callback):

        x = FIELD_LEFT
        y = RANDOMIZE
        scale = 0.15
        position = Point(x, y)
        size = Point(artifact_WIDTH, artifact_HEIGHT)
        velocity = Point(0, 0)
        image = Image(artifact_IMAGE, scale)
        text = self.get_text()
        #i need to figure out how to get the word to attach to the pic
        #and how to monitor the amount of artifacts on the screen at one time
        #add more, increase the number, etc.
        label = Label(text, position)
        body = Body(position, size, velocity)
        artifact = Artifact(body, image, text, True)
        cast.add_actor(artifact_GROUP, artifact)

    

