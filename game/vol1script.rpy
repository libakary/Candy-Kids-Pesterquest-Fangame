# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define harry = Character("Harry")
define imode = Character("Imode")

image harry 1 = ("images/harry 1.png")
image imode 1 = ("images/imode 1.png")
image bg sky = ("images/bg sky.png")

define dissolve = Dissolve(0.2)

init:
    $ left = Position(xpos=-350, xanchor=0, ypos=0, yanchor=0)
    $ right = Position(xpos=350, xanchor=0, ypos=0, yanchor=0)

# The game starts here.

label volume1:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg sky

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show harry 1

    # These display lines of dialogue.

    harry "This is volume 1 yoo."

    show harry 1 at left with move
    with dissolve

    show imode 1 at right
    with dissolve

    imode "Lets fucking go :D"

    # This ends the game.

    return
