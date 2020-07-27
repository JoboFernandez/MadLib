'''
To add more madlib stories, just do the following:
1)  in scenes list: add an instance of Scene
    format --> Scene("scene title", "source of scene to be credited", "a short description of how the scene goes", "your name")
2)  in class Scene method play: add an elif statement for your scene
    format --> elif self.title == "scene title":
'''

def main():
    option = menu()
    if option == 0: play_madlib()
    elif option == 1: display_credits()
    else: exit()

def menu():
    print("\n\n*****  WELCOME TO MAD LIB  *****")
    print("Mad Lib is a phrasal template word game where one player prompts others for a list of words to substitute for blanks in a story before reading aloud")
    print("PLEASE CHOOSE A SELECTION FROM THE MENU: ")
    options = ["PLAY GAME", "CREDITS", "EXIT"]
    for i in range(len(options)):
        print(f"{i+1}--- {options[i]}")
    while True:
        try:
            selection = int(input("Number Selection: ")) - 1
            if selection in range(len(options)): break
            else: continue
        except:
            print("Please choose a number.")
    return selection

def play_madlib():
    print("\n\nPLEASE SELECT A SCENE FROM AMONG THE LIST:")
    print("SCENE NUMBER---\tSCENE TITLE (SCENARIO)")
    for i in range(len(scenes)):
        print(f"{i + 1}{'-'*14}\t{scenes[i].title} ({scenes[i].description})")
        print(f"\t\t\t\tfrom {scenes[i].source} (contributed by: {scenes[i].contributor})")

    while True:
        try:
            scene_num = int(input("Scene Number: ")) - 1
            if scene_num in range(len(scenes)): break
            else: continue
        except:
            print("Kindly enter a number.")
    scenes[scene_num].play()
    play_again()

def play_again():
    again = ""
    while again.lower() not in ["y", "n"]:
        again = input("Would you like to play again? (Y/N)")
    if again.lower() == "y": play_madlib()
    else: exit()

def display_credits():
    print("\n\nThis project is developed by JOBO and is coded just for fun.")
    print("The scripts used herein were sourced somewhere else. Credit is given to where it is due.\n")
    print("Please select an action: ")
    print("1--- Back to main menu")
    print("2--- Exit")
    action = ""
    while action not in ["1", "2"]:
        action = input("Number: ")
    if action  == "1": main()
    else: exit()

class Scene:
    def __init__(self, title, source, description, contributor):
        self.title = title
        self.source = source
        self.description = description
        self.contributor = contributor

    def play(self):
        print(f"\n\n{self.title.upper()} ({self.source.upper()})\n")
        if self.title == "Mad Lib Theater with Benedict Cumberbatch":
            male_name = input("Give me a male name: ").lower().capitalize()
            teacher_name = input("Name of your favorite teacher: ").lower().capitalize()
            exclamation = input("Exclamation: ").upper()
            number = input("Number: ")
            objects = input("Plural objects: ").lower()
            store_name = input("Store name: ").lower().capitalize()
            body_part = input("Body part: ").lower()
            silly_word = input("Silly word: ").lower()
            holiday_name = input("Name of a holiday: ").lower().capitalize()
            movie_title = input("Movie title: ").lower().capitalize()
            gerund = input("Verb ending in -ing: ").lower()
            amount_of_distance = input("Amount of distance: ").lower()
            country = input("Country: ").lower().capitalize()
            animal = input("Animal: ").lower()
            movie_quote = input("Famous movie quote: ").lower().capitalize()
            body_part2 = input("Another body part: ").lower()
            children_song = input("Children song: ").lower().capitalize()
            adjective = input("Adjective: ").lower()

            speaker1 = male_name.upper()
            speaker2 = teacher_name.upper()
            self.start_dialogue()
            print(f"{speaker1}: Hello. I'm detective {male_name}. And you are?")
            print(f"{speaker2}: {teacher_name}.")
            print(f"{speaker1}: You're here today under suspicion of second degree robbery.")
            print(f"{speaker2}: {exclamation}!")
            print(f"{speaker1}: That's right. {number} {objects} were stolen from {store_name}, and the crime scene has your {body_part} written all over it.")
            print(f"{speaker2}: That is {silly_word}!")
            print(f"{speaker1}: Where were you on the night of {holiday_name}?")
            print(f"{speaker2}: We were watching {movie_title}.")
            print(f"{speaker1}: Then why does the security camera footage show you {gerund} just {amount_of_distance} away from the crime scene?")
            print(f"{speaker2}: ...")
            print(f"{speaker1}: Alright. I'm through playing games. Where are you from?")
            print(f"{speaker2}: {country}.")
            print(f"{speaker1}: Yeah, just as I suspected. You know, one of the best part of being a detective is that I get to lock up criminals like you and go home to my children and my pet {animal} and say, '{movie_quote}'.")
            print(f"{speaker2}: Fine! I did this. I committed the robbery. But I only did it because I needed the money to buy myself {body_part2} implant.")
            print(f"{speaker1}: I knew it all along. I knew it all along! And everytime I solve a crime, I like to sing my favorite song, {children_song}.")
            print(f"{speaker2}: You have a {adjective} voice!")
            self.end_dialogue()
        elif self.title == "Mad Lib Theater with John Cena":
            adjective = input("Give me an adjective: ").lower()
            cat_name = input("Cat name: ").lower().capitalize()
            kid_nickname = input("Nickname for a kid: ").lower().capitalize()
            profession = input("Type of profession: ").lower()
            shout = input("What would you shout if you stabbed your toe? ").upper()
            number = input("Give me a number: ")
            chicken_fact = input("Give me a made-up fact about chickens: ").lower()
            rhyme = input("Two words that rhyme (separate by space)? ").lower()
            food_type = input("Type of food: ").lower()
            drink_type = input("Type of drink: ").lower()
            gerund = input("Verb ending in -ing: ").lower()
            advice = input("Advice you would give to a shy teenager: ").lower().capitalize()
            body_part = input("Body part: ").lower()
            object = input("Object: ").lower()
            plural_noun = input("A plural noun: ").lower()
            plural_animals = input("Plural animals: ").lower()
            reaction = input("What would you say if you got an A+ on your chemistry test? ").upper()
            color = input("Give me a color: ").lower()
            profession2 = input("Another profession: ").lower()
            body_part2 = input("Another body part: ").lower()
            verb = input("A verb: ").lower()

            speaker1 = cat_name.upper()
            speaker2 = kid_nickname.upper()
            self.start_dialogue()
            print(f"{speaker1}: Ahh... I love Christmas. It's the most {adjective} time of the year. Hey, what's wrong?")
            print(f"{speaker2}: There's something I want to tell you, {cat_name}.")
            print(f"{speaker1}: What is it, {kid_nickname}? I'm your brother and best {profession}, you can tell me anything.")
            print(f"{speaker2}: Well, it isn't easy but, here it goes. I don't believe in Santa Claus.")
            print(f"{speaker1}: {shout.upper()}!")
            print(f"{speaker2}: Hey. Hey. I understand why you'd react that way. We've been writing Santa letters everyday in the past {number} decades.")
            print(f"{speaker1}: Wah, this is more shocking than when I found out {chicken_fact}. What made you stop believing?")
            print(f"{speaker2}: All I wanted for Christmas was the most popular toy everyone had. The {rhyme}. And there's a {food_type} and {drink_type}. But one Christmas morning, there was nothing under the tree. So I ran into my room and stared {gerund}.")
            print(f"{speaker1}: Little bro, I'm gonna tell you the same thing dad used to tell me every night before bed.")
            print(f"{speaker2}: Yes? What is that?")
            print(f"{speaker1}: {advice.capitalize()}.")
            print(f"{speaker2}: Truer words have never been spoken.")
            print(f"{speaker1}: All you have to do is let it deep within your {body_part}. Come on man, you can do it.")
            print(f"{speaker2}: You're right brother. The holidays are magical! Decorating the Christmas {object}, hanging the {plural_noun} on the mantle, and spending time with all my {plural_animals}. I believe again. THERE IS A SANTA CLAUS!")
            print(f"{speaker1}: {reaction.upper()}!")
            print(f"{speaker2}: You know, the best part about believing in Santa is getting to sing my favourite song with you.")
            print(f"{speaker1}: Sure you don't wanna do it by yourself? What is the song?")
            print(f"{speaker2}: Rudolph the {color}-nosed {profession2}.")
            print(f"{speaker1}: That is my favourite song! Let's sing...")
            print(f"{speaker1} & {speaker2}: Rudolph the {color}-nosed {profession2}, had a very shiny {body_part2}, and if you ever saw it, you would even say it {verb}.")
            self.end_dialogue()
        elif self.title == "The Baby on the Bus":
            baby_name = input("Give me a baby name: ").lower().capitalize()
            pet = input("A pet animal: ").lower()
            profession = input("A profession: ").lower()
            body_part = input("A body part: ").lower()

            speaker1 = "CHANDLER"
            speaker2 = "JOEY"
            self.start_dialogue()
            print(f"{speaker1}: Hey {baby_name}!")
            print(f"{speaker2}: Hey buddy...")
            print(f"{speaker1}: Please tell me you know which one is our baby?")
            print(f"{speaker2}: Well, that one has a {pet} on his T-shirt and this one has {profession}. And {baby_name} was definitely wearing a {pet}!")
            print(f"{speaker1}: Okay! *relieved*")
            print(f"{speaker2}: ...or {profession}.")
            print(f"{speaker1}: ...")
            print(f"{speaker2}: OHH! Ohh Wait! That one's definitely {baby_name}. Remember he had that cute little mole by his {body_part}?")
            print(f"{speaker1}: Yeah?")
            print(f"{speaker2}: Yeah!")
            print(f"{speaker1}: Hi {baby_name}! Remember us?")
            print(f"**{speaker1} reaches for {baby_name}**")
            print(f"{speaker1}: Okay, the mole came off. What are we gonna do? What are we gonna do?!?")
            print(f"{speaker2}: Uhhh. Uhhh. We'll flip coin! {pet.capitalize()} or {profession}.")
            print(f"{speaker1}: Oh we're gonna flip for the baby?!?")
            print(f"{speaker2}: You got a better idea?")
            print(f"{speaker1}: Alright, calling it in. Heads or tails?")
            print(f"**{speaker1} tosses the coin**")
            print(f"{speaker2}: Heads.")
            print(f"**coin landed**")
            print(f"{speaker1}: Heads it is.")
            print(f"{speaker2}: YESSS! WHEW~")
            print(f"{speaker1}: Ugh, we have to assign heads to something!")
            print(f"{speaker2}: Ohh. Ohh. Right. Okay. Okay. {pet.capitalize()} is heads, because {pet} has a head.")
            print(f"{speaker1}: What kind of scary-ass {profession} came to your birthday?")
            self.end_dialogue()
        elif self.title == "Joey on Pyramid":
            show_title = input("A movie/show title: ").lower().capitalize()
            person2 = input("Give me another person's name: ").lower().capitalize()
            profession = input("A profession: ").lower()
            saying = input("A short saying: ").lower().capitalize()
            store = input("A store name: ").lower().capitalize()
            stationery = input("An object you can write: ").lower().strip().capitalize()
            location = input("A place/location: ").lower().capitalize()
            activity = input("A type of an activity: ").lower()
            utensil = input("A kitchen utensil: ").lower()
            body_part1 = input("A body part: ").lower()
            body_part2 = input("Another body part: ").lower()
            white1 = input("A white object: ").lower().capitalize()
            white2 = input("Another white object: ").lower().capitalize()
            object1 = input("An heavy object: ").lower()
            animal = input("An animal: ").lower()
            body_part3 = input("Another body part: ").lower()
            number = input("A number: ").lower()

            person1 = "Joey"
            speaker1 = "GAME SHOW HOST"
            speaker2 = person1.upper()
            speaker3 = person2.upper()
            self.start_dialogue()
            print(f"{speaker1}: Welcome to the Pyramid! Let's meet our contestants. First, {person2} is a {profession}. He's gonna be playing with {show_title} star, {person1}.")
            print(f"**audience applaud while {speaker1} introduces the other contestants**")
            print(f"{speaker1}: Welcome everybody. Goodluck to all of you. Let's play Pyramid!")
            print(f"**audience applauded once again**")
            print(f"{speaker1}: Alright, now. We flipped a coin before the show, {person2} you won the toss, so you're gonna start. Which category would you like?")
            print(f"{speaker3}: I'll take '{saying}'.")
            print(f"{speaker1}: '{saying}'. {person1}, describe for {person2} these things that have lines. Give me 20 seconds on the clock, please. Ready? Go!")
            print(f"**Word to guess: {store}**")
            print(f"{speaker2}: Okay. It's a store, like a {store}.")
            print(f"**sound buzzes**")
            print(f"{speaker2}: Ohh. I said it. I said it. Okay. Okay.")
            print(f"**Word to guess: {stationery}**")
            print(f"{speaker2}: I'm writing in my...")
            answer = "Diary" if stationery != "Diary" else "Notebook"
            print(f"{speaker3}: {answer}.")
            print(f"{speaker2}: No. More like a {stationery}.")
            print(f"**sound buzzes**")
            print(f"{speaker2}: Ohh, dammit.")
            print(f"{speaker1}: Hey. That's invalid.")
            print(f"**Word to guess: Blueprint**")
            print(f"{speaker2}: Ahh. Ohh! If I'm building a house, the plan isn't called a schmo~print...")
            print(f"**sound buzzes**")
            print(f"{speaker2}: Not that one either?")
            print(f"**Word to guess: {location}**")
            print(f"{speaker2}: Ohh. In high school, I once had {activity} in the middle of the...")
            print(f"{speaker3}: Cafeteria.")
            print(f"{speaker2}: Yah, but that's not what they were looking for.")
            print(f"**sounds buzzes -end of time-**")
            print(f"{speaker2}: Ohhh~")
            print(f"{speaker1}: Ok, next round. Now I must remind you, you need all 6 of these to stay in the game, alright? Describe for {person1} things you find in your refrigerator.")
            print(f"{speaker2}: Haaa~ They might just as well as give us the points.")
            print(f"{speaker1}: 20 seconds on the clock. Ready? Go.")
            print(f"**Word to guess: Cream**")
            print(f"{speaker3}: You put this in your coffee.")
            print(f"{speaker2}: A {utensil}. Your {body_part1}. Your {body_part2}!")
            print(f"{speaker3}: It's white.")
            print(f"{speaker2}: {white1}. {white2}. A GHOST!!!")
            print(f"{speaker3}: It's heavier than milk.")
            print(f"{speaker2}: Ahh, {object1}. Ahh, {animal}. The Earth.")
            print(f"{speaker3}: PASS!")
            print(f"{speaker2}: Ahh~")
            print(f"**Word to guess: Mayonnaise**")
            print(f"{speaker3}: You put this on a sandwich.")
            print(f"{speaker2}: Sanami. Anchovies. Jam.")
            print(f"{speaker3}: It's white.")
            print(f"{speaker2}: {white1}. {white2}. A GHOST!!!")
            print(f"{speaker3}: It's made from eggs.")
            print(f"{speaker2}: Chickens?")
            print(f"{speaker3}: PASS!")
            print(f"{speaker2}: Ugh!")
            print(f"**Word to guess: Ketchup**")
            print(f"{speaker3}: You put this on a hamburger.")
            print(f"{speaker2}: Ketchup.")
            print(f"**sound tings -answer is correct-**")
            print(f"{speaker3}: Yes!!!")
            print(f"{speaker2}: Radish.")
            print(f"{speaker3}: Stop.")
            print(f"{speaker2}: Ohh.")
            print(f"**sounds buzzes -end of time-**")
            print(f"{speaker1}: Ohh, time's up. {person1}, you were almost on a roll there. Hahaha.")
            print(f"{speaker2}: Yah...")
            print(f"DIRECTOR: And... we're out!")
            print(f"{speaker2}: Ohh, so we didn't win. It's fun to play the game, right?")
            print(f"{speaker3}: Hey. I got kids turning college. I'm gonna get surgery on my {body_part3}. You just lost me {number} grand.")
            print(f"{speaker2}: Ohh wow. Look, I'm so sorry. I promise, we will do better next time.")
            print(f"{speaker3}: Ohh I will, because I won't be playing with you.")
            print(f"{speaker2}: Well you know, some of those were pretty hard. Like why would there be a ghost in my fridge?")
            self.end_dialogue()

    def start_dialogue(self):
        print("\n\n--------------------START OF DIALOGUE--------------------")
        print(f"***Scenario: {self.description}***\n")

    def end_dialogue(self):
        print("\n--------------------END OF STORY--------------------\n")


scenes = [Scene("Mad Lib Theater with Benedict Cumberbatch", "The Tonight Show Starring Jimmy Fallon", "A detective interrogates a suspect for a crime", "Jobo"),
Scene("Mad Lib Theater with John Cena", "The Tonight Show Starring Jimmy Fallon", "Two brothers talk about Christmas", "Jobo"),
Scene("The Baby on the Bus", "FRIENDS Series", "Two friends had to choose between two babies after they lost a baby they were sitting", "Jobo"),
Scene("Joey on Pyramid", "FRIENDS Series", "A participant playing in a game show", "Jobo"),
]


main()