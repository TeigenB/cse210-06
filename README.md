# cse210-06
Final Project
Keyboard Cat (working title)
3 screens
    1. Main Screen
        cat picture
        name of the game
        rules
        start button (hit enter)
    2. Game Screen
        lives counter
        points counter
        typing cat animation
        current word window
        moving objects of words-cute pic attached
    3. End Screen
        game over announcement
        cat animation/pic
        play again button (hit enter)

 main
 director
 casting
    cast(parent) 
        goodies(child)
            this is each item crawling across the screen
        text
            this is a text file with the words for typing. 
        score(child)
            this is a child because I want to appear on the screen,
            but not a child of goodies bc I want it to stay still, not move
        lives(child)
            same as score
        word window(child)
            this is where the player's typing will appear
        cat animation(child)
            synced up to keyboard service so the cat will move with every key click
services
    keyboard service
    video service
    audio service
shared
    color
    point
constants
assets
    data
    fonts
    images
    sounds          