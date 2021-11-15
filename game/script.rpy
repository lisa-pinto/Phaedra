# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image euripides one = "euripides.png"
image side author:
     "euripides.png"
     size(150,195)

image phaedra one = ("phaedra_one.jpg")
image phaedra two = ("theseus and phaedra.png")
image phaedra hippo = ("phaedra_two.png")
image phaedra resurrect = ("Phaedra_resurrect.png")
image phaedra death = ("phaedra_death.png")
image theseus one = ("theseus_one.png")
image theseus two = ("theseus_two.png")

image nurse right = Image("nurse_one.png", xalign = 1.0,yalign = 0.1)
image nurse praying = "nurse_two.png"
image nurse convincing = im.Scale("nurse_convincing.png", 750, 450)

image hippolytus one = "hippolytus_one.png"
image hippolytus two = Image("Hippolytus_two.png")
image hippolytus three = "hippolytus_three.png"
image hippolytus death = "hippo_death.jpg"
image hippolytus dragged = "hippo_dragged.jpg"

image aphrodite one = "Aphrodite.png"
image artemis one = "artemis.png"
image black = "black.jpg"
image shocked = "shocked.jpg"




define e = Character("Euripides")
define a = Character("Euripides", image="author")
define aph = Character("Aphrodite", who_color = "#FF265c")
define ar = Character("Artemis", who_color = "#FFFFFF")
define p = Character("Phaedra", who_color = "#FFB3E3")
define n = Character("Nurse", who_color = "#EBD72A")
define h = Character("Hippolytus", who_color = "#EB2A2A")
define t = Character("Theseus", who_color = "#B9CEF0")

label start:
    $ rant = False
    $ epilogue_view = False
    scene black
    show euripides one at truecenter
    e "Good morning all. My name is Euripides."
    e "You must be wondering why I have gathered you all, Oh wait...."
    e "Well. This is a smaller crowd than expected."
    e "Oh Yes! Social Distancing. How could I forget? "
    e "Very well, here we go."
    e "Let me tell you a tale from a long time ago."
    e "From an age where the gods could walk amongst us."
    e " I must warn you, everyone is very mood"
    e "But really, deep down, who isn't?"
    e "I was thinking of just telling you a story, but let’s shake things up."
    e "Today since there is just one of you, Ill make it interactive, how does that sound? "
    menu:
        "Wait I'm confused, tell me a little more":
            jump S1
        "Great! Let's dive in":
            jump S2

label S1:
    scene black
    show euripides one at truecenter
    e "The following story is from myth of Hippolytus and Phaedra."
    e "I first produced my version of it for the City Dionysia in Athens in 428 BC and won first prize as part of a trilogy."
    e "Pretty groovy, huh?"
    e "But I digress."
    e "Let's get on with it."
    jump S2

label S2:
    scene black
    show phaedra one at truecenter
    a "This is Phaedra. She's great."
    a "At this point she is the queen of Athens."
    a "You must be wondering how she got into this situation"
    a "Let's jump right in"
    show phaedra one at truecenter with None
    show nurse right with fade
    n "Child you’re baffling me! What do all of your words mean?"
    p "They take us back. Back to that time… This misery of mine is old. It comes from long ago."
    n "That does not make things any clearer for me, child…"
    p "Oh, nurse! If only you could utter my words instead of me!"
    n "Phaedra, I am not a seer to uncover what is hidden in your mind."
    p "Nurse, tell me, please: What do people mean when they say, they’re in love?"
    n "Ah, love! They mean to say, my girl that they feel great pleasure and great pain all the very same time!"
    p "Well then, it would be the second that I feel."
    n "What are you saying, my child? That you are in love? But who is the man?"
    p "His name?"
    a "Guess his name"
    menu:
        "Jon Snow":
            jump S3
        "Brad":
            jump S3
        "Hippolytus, son of Theseus and the Amazon Hippolyta":
            jump S4

label S3:
    a "Nice Try"
    a "She is talking about Hippolytus"
    jump S5

label S4:
    a "Good Job!"
    jump S5

label S5:
    scene black
    show hippolytus two at truecenter with fade
    a "Hippolytus was the son of Theseus"
    a "Here's something you might not know:"
    a "Theseus is Phaedra's husband."
    a "Yes, that makes Hippolytus....."
    show shocked
    a "Her STEPSON."
    a "I know, it is shocking."
    a "Although maybe not by ancient greek standards."
    scene black
    show euripides one with fade
    e "Now here's the thing"
    e "This story has had many variations through the years."
    e "One thing is common:"
    e "Phaedra accuses Hippolytus of rape and he always dies in the end."
    e "He is fated to a gruesome end."
    e "Now that we're retelling the story, would you like to change the ending?"
    jump S5menu

label S5menu:
    scene black
    show hippolytus two at truecenter
    menu:
        "Nah, why change it?":
            jump S7
        "Sure why not, Let's try to save the man!":
            jump S6

label S6:
    scene black
    $rant = True
    show euripides one
    e "You have a good heart, and sympathize for the man."
    e "But what if I showed you this speech from my play?"
    e "Of what he says when he finds out that Phaedra is in love with him."
    scene black
    show hippolytus one
    h "Zeus, Oh, Zeus! Why did you bring woman into the light of the sun?"
    h "Woman, this impure, this evil destroyer of mortals!"
    h "As it is now, even before we want to bring this… this curse, into our house, we must squander away our whole estate!"
    h "And here’s what I mean by this. Here’s the clear proof of it: The woman’s father, "
    h "The man who had begotten that beast and who had raised her-that poor man, "
    h "Not only has to lay a dowry out for her, but he must also send her away, so he can shed from himself this unbearable burden!"
    h "And then, her husband, the other poor creature, the one who has brought this… fake statue, into his house, this ruinous beast."
    h "Her husband, the moment he gets her into his house, he begins to happily decorate her!"
    h "But the man who gets it the easiest is the one who brings into his house a woman who is totally useless."
    h "A nothing. A zero. A simple, simple- minded woman. A useless woman."
    h "But I hate the smart ones! I simply loathe that sort!"
    h "Oh, Zeus, spare me!"
    h "I hope I’ll never end up with a woman in my house who’s cleverer than women should be!"
    h "Aphrodite, plants a lot more evil schemes in the minds of those clever ones! "
    h "The dumb ones are kept on the straight and narrow because of their… rather diminutive wit."
    h "And, if you do get a wife, give her no slave. Instead, give her animals. Give her dumb brutes for companions."
    h "Wild beasts that you can’t talk to and they can’t talk back."
    h "Give a bitch of a wife a servant and what have you got? The two talk together inside, "
    h "Hatch up all sorts of evil plans and then the servant goes off and carry those plans outside the house!"
    a "Now tell me, would you still like to save him?"
    jump S6post_rant

label S6post_rant:
    $scene_eight = False
    scene black
    show hippolytus one
    menu:
       "KILL HIM":
           jump S7
       "This is just your version. He doesn't always deserve a gruesome death":
           jump S8
label S7:
    scene black
    show euripides one
    #scene_seven = True
    e "Okay, you have chosen to not show mercy on the man."
    e "In your story, he dies a gruesome death."
    e "But there still are a few things that have to conspire before that comes true."
    e "And now that I am giving you the reigns, you have to make it happen."
    e "Are you ready?"
    menu:
        "Hell yeah!":
            jump S13
        "I don't have a choice do I?":
            jump S13


label S8:
    scene black
    $scene_eight = True
    hide hippolytus one
    show euripides one
    e "Interesting decision."
    e "But there is still another choice to make."
    e "For Hippolytus not to die ,Phaedra cannot accuse him of rape."
    e "But Phaedra is a woman part of a forbidden love in ancient times."
    e "She does not have any power over what happens if her secret gets out."
    e "It is now your job to keep her alive."
    e "May the odds be in your favour."
    jump S9

label S9:
     scene black
     hide euripides
     show phaedra one at truecenter
     a "We are back to the middle of the story."
     a "Phaedra is about to tell her nurse who the man she falls in love with is."
     show nurse right
     p " The man I love, He is the son of the Amazon goddess."
     n "Hippolytus? Do you mean Hippolytus, child?"
     p "You uttered the words, not me!"
     n "Oh, no! My child, what could you mean by this? You have destroyed me with this!"
     n "What is your explanation?"
     menu:

         "I am an innocent woman. There is not other explanation than a wretched curse from the gods.":
             jump S10
         "Oh nurse, it is my own lust, for the son of my husband is an irresistable man!":
             jump S15

label S10:
     scene black
     show nurse praying with fade
     n "Aphrodite!"
     n "Now I see!"
     n "Now I see that you is not just a mere god but some force far mightier than that!"
     n "You have destroyed Phaedra!"
     n "You have destroyed me!"
     n "You have destroyed the Palace!"
     n "Oh Goddess, I beg of you to answer my prayers"
     hide nurse praying
     show aphrodite one at truecenter with fade
     aph "I, Aphrodite."
     aph "Also called Cypris."
     aph "The great goddess among the mortals, as well as throughout the heavens."
     aph "Of those mortals who look upon the light of the sun "
     aph "and all who live between the very edges of the East, the Black Sea and the farthest ends of the West, the great Pillars of Atlas."
     aph "of all those of them who respect my power, I, respect them, also."
     aph "But those of them who treat me with disrespect, them, I crush and destroy!"
     show aphrodite one at topleft with fade
     show nurse right
     aph "You see, nurse, Hippolytus, that child of the Amazon Hippolyta, by the seed of Theseus, who was raised by that pure man, Pittheus, is the only one -the only one in the whole of Troezen, who hates me."
     aph "He says that I am the worst of all the gods!"
     aph "Hippolytus, says this! He is the only mortal, the only man, who says this!"
     aph "It is true, I cursed your Phaedra"
     aph "But dear nurse you pray for your mistress"
     aph "So I will make you an offer"
     aph "Do you accept?"
     menu:
        "Cooperate with Aphrodite":
            jump S20
        "Decline, You are a bit suspicious":
            jump S11

label S11:
    scene black
    show euripides one at truecenter
    e "I am intrigued by your mistrust in the gods"
    e "After all, reading all the things that they have done, what sound person would?"
    e "I'll give you a happy ending."
    e "Where both of them live. "
    hide euripides one
    a "Brace yourself, it has to include some gods."
    a "Don't worry, I won't make it too tedious."
    show aphrodite one at left
    aph "Hello Artemis."
    show artemis one at right with dissolve
    ar "Leave Hippolytus and Phaedra alone."
    aph "Or what?"
    ar "Or I will kill your mortal beloved."
    aph "Truce?"
    ar " 'Kay'"
    jump epilogue_menu

label S13:
    a "Let us start from the middle."
    a "Hippolytus has just returned home to show reverence to a statue of Artemis."
    jump S16

label S12:
    aph "Good decision."
    aph "Your choice will save the life of your mistress."
    aph "Although as I prevent a life from being taken, I must have a life in return."
    aph "But I cannot withdraw my curse."
    aph "I will plant a seed of deception in the mind of your mistress."
    aph "Her actions that represent her sense of self-preservation will be the downfall of another."
    jump S19

label S15:
    scene black
    show nurse convincing at truecenter
    p "I do not know what to do"
    n "I am surprised, there is no doubt, But I have a plan"
    n "What huge words! What piousness!"
    n "Forget the big words, dear girl! We must think of this man of yours! Find him immediately!"
    n "and tell him with straight talk what’s really going on here."
    n "Now listen, my girl!"
    n "If you hadn’t strayed and fallen into such a great mountain of troubles, I wouldn’t have talked to you"
    n "..the way I did about love and lust and all that!"
    n "But trying to save your life, my dear girl, requires lots of hard work and so, who would argue with my method?"
    n "(A maid comes in with the some news). Speak of the man himself! Hippolytus has arrived, I must go greet him"
    jump S16

label S16:
    scene black
    show hippolytus one at left with fade
    show nurse right
    n "Master, what an unexpected surprise!"
    h "What news, nurse?"
    n "(sighs) Some troubling events have occurred in this household"
    a "The poor nurse tells him of the news"
    a "The recent troubles of Phaedra"
    a "But then she goes on to make the most unexpected request..."
    a "That Hippolytus satisfy his stepmother's desires"
    a "What do you think should happen next?"
    menu:
        "Hippolytus Accepts":
         jump S17
        "Hippolytus Rejects":
         jump S18

label S17:
    scene black
    show phaedra hippo at truecenter
    a "Interesting choice."
    a "Morally, ambiguous, but my peers have been known to enjoy this sort of thing."
    a "I'll give you a good ending"
    a "Hippolytus and Phaedra live happily ever after together"
    hide phaedra hippo
    a "But they have to kill Theseus first, that is a compulsion."
    show theseus two at truecenter with dissolve
    a "Let's throw him off a cliff."
    a "There has to be some Tragedy after all."
    jump epilogue_menu

label S18:
    scene black
    show hippolytus three at topleft
    show nurse praying at right
    h "Oh, mother Earth! Oh, broad sunlight!"
    h "The things I hear! Unspeakable stuff!"
    n "Hush, my boy! Quiet!"
    n "Someone will hear you, shouting like that!"
    h "Quiet? How can I be quiet after the words I’ve heard?"
    n "My, son, I beg you!"
    n "Please, by your beautiful, hands, I beg you!"
    h "Keep your distance woman!"
    n "By your knees, my son!"
    n "I beg you, my son! You will ruin me!"
    hide hippolytus three with dissolve
    h "(storms out)"
    scene black
    a "Phaedra could not handle this situation any further"
    show phaedra one at truecenter
    p "I have found a means by which I can remedy my situation in such a way that my sons can live with an honourable reputation "
    p "and for me to get some benefit out of my present troubles."
    p "I will never disgrace the homes of Crete, nor will I appear before Theseus after having committed shameful deeds, just so I can save my one life!"
    e "What does Phaedra do?"
    menu:
        "Starts preparing a speech":
            jump S19
        "Goes to her absolute last resort":
            jump S22

label S19:
    scene black
    a "Theseus, husband of Phaedra and father of Hippolytus,"
    a "returns from the exile he has been in for a year."
    show phaedra two with dissolve
    p "There is a confession I have to make."
    p "If I had another choice, I would have taken that path."
    t "Anything, my beloved"
    a "She begins with an accusation of rape by her husband's son"
    a "Describes a faux ordeal in sordid detail."
    hide phaedra two
    show theseus one at truecenter with fade
    t "My son, Hippolytus!"
    t "He dared assault my bridal bed!"
    t "Hippolytus has shamed the holy eye of Zeus!"
    t "Well then, my father Poseidon, I call upon you!"
    t "You have promised me three curses, once! Grant me one of them now!"
    t "Strike dead my son and let him not live beyond the end of this day!"
    t "Show me, father, that your gift is true!"
    jump S20

label S20:
    scene black
    show hippolytus death at truecenter with fade
    e "In this ending, like many endings, Hippolytus dies his fated death"
    e "Poseidon grants the wish of Theseus"
    e "A bull emerges from the sea that makes Hippolytus' horses go wild"
    e "He gets dragged, and his chariot crashes on a rock."
    e "He dies knowing the truth and Phaedra gets to live "
    if scene_eight:
        e "But since you chose to Let Hippolytus live inspite of his speech, I will give you one more chance to decide"
        menu:
            "Sacrifice Phaedra for Hippolytus":
                jump S21
            "Stay with the this ending":
               jump epilogue
    else:
        jump epilogue_menu



label S21:
    scene black
    a "Another Interesting Decision."
    a "Sacrificing the Queen herself."
    a "Well since I asked, I guess I have no choice"
    show phaedra resurrect at truecenter with fade
    p "(On seeing Hippolytus' dead body being brought back)"
    p "Oh Hippolytus, You did not deserve this fate!"
    p "You were proud but noble"
    p "Artemis Strike me down!"
    hide phaedra resurrect
    p "I have caused the downfall of one of your most noble followers"
    p "Take me instead"
    show phaedra death at truecenter with fade
    p " "
    jump epilogue_menu

label S22:
    show phaedra death at truecenter
    a "Well, this is my favourite ending."
    a "Because this is the way I told it."
    a "Phaedra commits suicide for the sake of her honor."
    a "Theseus then returns home after his exile to hear of her death."
    a "She leaves a note accusing Hippolytus of rape "
    hide phaedra death
    show theseus one at truecenter with fade
    t "My son, Hippolytus!"
    t "He dared assault my bridal bed!"
    t "Hippolytus has shamed the holy eye of Zeus!"
    t "Well then, my father Poseidon, I call upon you!"
    t "You have promised me three curses, once! Grant me one of them now!"
    t "Strike dead my son and let him not live beyond the end of this day!"
    t "Show me, father, that your gift is true!"
    scene black
    show hippolytus dragged at truecenter
    e "A monster emerges from the sea that makes Hippolytus' horses go wild."
    e "He gets dragged, and his chariot crashes on a rock."
    e "Hippolytus dies and then everybody is unhappy."
    jump epilogue_menu


label epilogue_menu:
    if epilogue_view:
        menu:
            "Read Epilogue":
                jump epilogue
            "Skip Epilogue":
                jump post_epilogue
    else:
        jump epilogue



label epilogue:
    $epilogue_view = True
    scene black
    show euripides one at truecenter with fade
    e "(Epilogue)"
    e "You are probably a little bewildered by a few of the events that have transpired before you in this story."
    e "But there is a fantastical element to this game."
    e "This was from an era where people belived in the stories where gods walked among men."
    e "Its themes have trickled down for centuries."
    e "Certainly some, if not many of them are highly problematic."
    e "Like I said, that's why we talk about how things could be different."
    e "And retell the stories from time to time."
    e "Maybe, just maybe "
    e "It's just a side-effect of being a Classic (not to brag)."
    jump post_epilogue

label post_epilogue:
    menu:
        "End Game":
            return
        "Explore a different ending":
            if rant:
                jump S6post_rant
            jump S5menu