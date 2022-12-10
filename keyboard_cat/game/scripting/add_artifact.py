from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.image import Image
from game.casting.body import Body
from game.casting.label import Label
from game.casting.artifact import Artifact


class AddArtifact(Action):
    pass

    def __init__(self):
        with open(TEXT_FILE, 'r') as file:
            self.list = file.read().splitlines()


    def execute(self, cast, script, callback):
        artifacts = len(cast.get_actors(artifact_GROUP))

        if artifacts < 2:
            x = FIELD_LEFT
            y = RANDOMIZE
            scale = 0.1
            position = Point(x, y)
            size = Point(artifact_WIDTH, artifact_HEIGHT)
            velocity = Point(2, 0)
            image = Image(artifact_IMAGE, scale)
            text = random.choice(self.list)
            body = Body(position, size, velocity)
            artifact = Artifact(body, image, text, True)
            cast.add_actor(artifact_GROUP, artifact)

    

