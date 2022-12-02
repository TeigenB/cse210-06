from constants import *
from game.directing.director import Director
from game.directing.scene_manager import SceneManager


def main():
    print("off to director")
    director = Director(SceneManager.VIDEO_SERVICE)
    print("director done")
    director.start_game()

if __name__ == "__main__":
    main()
    print("main")
