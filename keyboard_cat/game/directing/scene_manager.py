import csv
from constants import *
from game.scripting.user_input import UserInput
from game.casting.animation import Animation
from game.casting.artifact import Artifact
from game.casting.image import Image
from game.casting.label import Label
from game.casting.body import Body
from game.casting.point import Point
from game.casting.word_window import Word_Window
from game.casting.cat import Cat
from game.casting.stats import Stats
from game.casting.text import Text 
from game.scripting.get_text import GetText
from game.scripting.check_match import CheckMatch
from game.scripting.check_over_action import CheckOverAction
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.collide_borders_action import CollideBordersAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_artifact_action import DrawArtifactAction
from game.scripting.draw_cat_action import DrawCatAction
from game.scripting.draw_word_window_action import DrawWordWindowAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_artifact_action import MoveArtifactAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_video_service import RaylibVideoService


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    CHECK_OVER_ACTION = CheckOverAction()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)
    COLLIDE_BORDERS_ACTION = CollideBordersAction( AUDIO_SERVICE)
    CHECK_MATCH_ACTION = CheckMatch()
    DRAW_ARTIFACT_ACTION = DrawArtifactAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_CAT_ACTION= DrawCatAction(VIDEO_SERVICE)
    DRAW_WORD_WINDOW_ACTION = DrawWordWindowAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_ARTIFACT_ACTION = MoveArtifactAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    USER_INPUT = UserInput(KEYBOARD_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):
        self._add_stats(cast)
        self._add_lives(cast)
        self._add_score(cast)
        self._add_artifact(cast)
        self._add_word_window(cast)
        self._add_cat(cast)
        self._add_dialog(cast, INSTRUCTIONS)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)

    def _prepare_in_play(self, cast, script):
        cast.clear_actors(DIALOG_GROUP)
        script.clear_actions(INPUT)
        
        #instead of having the input of ther user moving the racket, this is where I want the user input of typing to be
        script.add_action(INPUT, self.USER_INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, 2))
        self._add_update_script(script, cast)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        self._add_artifact(cast)
        self._add_cat(cast)
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        script.add_action(INPUT)
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    

    def _add_artifact(self, cast):
        x = FIELD_LEFT
        y = RANDOMIZE
        scale = 0.15
        position = Point(x, y)
        size = Point(artifact_WIDTH, artifact_HEIGHT)
        velocity = Point(0, 0)
        image = Image(artifact_IMAGE, scale)
        text = GetText()
        #i need to figure out how to get the word to attach to the pic
        label = Label(text, position)
        body = Body(position, size, velocity)
        artifact = Artifact(body, image, text, True)
        cast.add_actor(artifact_GROUP, artifact)

    """def _add_bricks(self, cast):

        
        stats = cast.get_first_actor(STATS_GROUP)
        filename = "CSE210-06/keyboard_cat/assets/data.txt"

        with open(filename, 'r') as file:
            reader = Text.reader(file, skipinitialspace=False)

            for row in enumerate(reader):
                x = FIELD_LEFT + c * BRICK_WIDTH
                y = FIELD_TOP + r * BRICK_HEIGHT
                
                if frames == 1:
                    points *= 2
                
                position = Point(x, y)
                size = Point(BRICK_WIDTH, BRICK_HEIGHT)
                velocity = Point(0, 0)
                images = BRICK_IMAGES[color][0:frames]

                body = Body(position, size, velocity)
                animation = Animation(images, BRICK_RATE, BRICK_DELAY)

                brick = Brick(body, animation, points)
                cast.add_actor(BRICK_GROUP, brick)"""

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, FONT_LARGE, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)

    
    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y/3)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_LARGE, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)
    
    def _add_user_input(self, cast):
        text = Text(user_input_format, FONT_FILE, FONT_LARGE, ALIGN_LEFT)
        position = Point(CENTER_X ,FIELD_BOTTOM - HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(input_GROUP, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_cat(self, cast):
        cast.clear_actors(cat_GROUP)
        x = CENTER_X /2  -  cat_WIDTH
        y = SCREEN_HEIGHT * 0.7
        scale = 0.2
        position = Point(x, y)
        size = Point(cat_WIDTH, cat_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(cat_IMAGES)
        cat = Cat(body, animation)
        cast.add_actor(cat_GROUP, cat)

    def _add_word_window(self, cast):
        cast.clear_actors(word_window_GROUP)
        x = CENTER_X/2 - cat_WIDTH
        y = SCREEN_HEIGHT * 0.8
        scale = 0.2
        position = Point(x, y)
        size = Point(word_window_WIDTH, word_window_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(word_window_IMAGES, scale)
        word_window = Word_Window(body, image)
        cast.add_actor(word_window_GROUP, word_window)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_ARTIFACT_ACTION)
        script.add_action(OUTPUT, self.DRAW_WORD_WINDOW_ACTION)
        script.add_action(OUTPUT, self.DRAW_CAT_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script, cast):
        script.clear_actions(UPDATE)
        self._add_artifact(cast)
        script.add_action(OUTPUT, self.DRAW_ARTIFACT_ACTION)
        script.add_action(UPDATE, self.MOVE_ARTIFACT_ACTION)
        script.add_action(UPDATE, self.CHECK_MATCH_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)