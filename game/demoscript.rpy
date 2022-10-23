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

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg sky

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show harry 1

    # These display lines of dialogue.

    harry "So this is a demo of the typa game we're going to make."

    show harry 1 at left with move
    with dissolve

    show imode 1 at right
    with dissolve

    imode "Also gonna use this to show off all effects and possibilities i figure out."
    imode "Which i can also then use as a resource to copy code from for future use!"


    # This ends the game.

    return


    #NOTES

    #label .sublabel:
#this is a label inside a label, useful for choices possibly?

    #menu menuname:
#menuname can be used like a label, to jump to it from some points


#variables. must be declared in the beginning
    #$ choice = True
    #$ choice = False
#can be rewritten inside script to change values or add points for instance.

    #$ boolean = True
#yes no, true false etc, 2 possible choices. ACTUALLY None is also a value, the absence of a value.
    #$ string = "text"
#just a word or words, only use 'text' not "text" inside the thing bc "" are already on the outside
    #$ number = 2
#can be integer, decimal, negative

#checking variables
    #if variablename:
        #Stuff happens if boolean True
    #else:
        #Other stuff happens if boolean False

#similar with strings and numbers
    #if variablename == "value":
        #Stuff happens. remember that == is checking value and = is assigning value

    #if variablename == 100
        #Stuff happens if value is exactly 100, but if you dont need exact numbers:

    #if variablename > 20:
        #Stuff if greater than 20.
        # >= is greater or equal. < is lower. <= is lower or equal.

#excluding values
    #if not variablename == "value":
        #Stuff happens


#Persistent variables
#have to be declared before label start
    #define persistent.yourvariable = value
    #can be boolean, text or number
#modifying persistent variables works same as variables
    #$ persistent.yourvariable = value2


#Tuple
    #begin and end with parenthesis. represents a container where the number of items is important.
    #(1, 45, "#444")

#List
    #begin and end with square bracket. represents a container where number of items may vary.
    #[1,45,343]
