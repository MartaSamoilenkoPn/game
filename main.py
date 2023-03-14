import game

trapezna = game.Room("Trapezna", 1, 1)
trapezna.set_description("The place where everyone become happier or not because of food, 1st floor")

hall_1 = game.Room("Hall_1", 1, 0)
hall_1.set_description("Choose your side: Trapezna or Cafe?, 1st floor")

cafe = game.Room("Cafe", 1, 2)
cafe.set_description("Wanna coffee with a cinnabon? You're welcome, 1st floor")

it_space = game.Room("IT SPACE", 0, 2)
it_space.set_description("A special space for apps faculty. Some people call it psycho clinic, 0th floor")

hall_0 = game.Room("Hall_0", 0,0)
hall_0.set_description("You can go to main it space or lecture room, 0th floor")

lectrure_room = game.Room("Lecture Room", 0, 1)
lectrure_room.set_description("Multi-functional space. For lectures, games, chill(not often), 0th floor")

room_308 = game.Room("Room 308", 3, 2)
room_308.set_description("Everyone knows where mathimatical analysis consultation is..., 3rd floor")

hall_3 = game.Room("Hall 3", 3, 0)
hall_3.set_description("Documents in deanery or math analysis?), 3rd floor")

deanery = game.Room("Deanery", 3, 1)
deanery.set_description("Wanna meet with your documents?:), 3rd floor")

trapezna.link_room(hall_1, "west")
hall_1.link_room(trapezna, "east")
hall_1.link_room(cafe, "north")
cafe.link_room(hall_1, "south")

it_space.link_room(hall_0, "south")
hall_0.link_room(it_space, "north")
hall_0.link_room(lectrure_room, "east")
lectrure_room.link_room(hall_0, "west")

room_308.link_room(hall_3, "south")
hall_3.link_room(room_308, "north")
hall_3.link_room(deanery, "south")
deanery.link_room(hall_3, "north")

hall_0.link_room(hall_1, "up")
hall_1.link_room(hall_0, "down")
hall_1.link_room(hall_3, "up")
hall_3.link_room(hall_1, "down")

apps_quee = game.Friend("APPS QUEE", "Apps students in the beginning of quee")
apps_quee.set_conversation("Well, we're in the beginning only for other apps students")
apps_quee.set_weakness("air alert")
trapezna.set_character(apps_quee)

ucu_guest = game.Enemy("UCU GUEST", "An annoying person in cafe without lokal card")
ucu_guest.set_conversation("Why so expensive?...")
ucu_guest.set_weakness("lokal")
cafe.set_character(ucu_guest)

kushnir = game.Friend("Dmytro Kushnir", "Alghorythm teacher")
kushnir.set_conversation("Hey, what's up?")
it_space.set_character(kushnir)

pan_oleg = game.Enemy("Farenyuk", "POC teacher, superboss")
pan_oleg.set_conversation("Well, ready to fight?")
pan_oleg.set_weakness("documents")
lectrure_room.set_character(pan_oleg)

pan_stepan = game.Friend("Pan Stepan", "Mathimatical Analysis teacher")
pan_stepan.set_conversation("Aga or ne-aga?")
room_308.set_character(pan_stepan)

lokal = game.Item("lokal")
lokal.set_description("special card")
trapezna.set_item(lokal)

documents = game.Item("documents")
documents.set_description("Your documents, such a strong weapon....")
deanery.set_item(documents)

current_room = hall_1
current_room.draw()
backpack = []
friends = []

dead = False

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west", "up", "down"]:
        # Move in the given direction
        current_room = current_room.move(command)
        current_room.draw()
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, game.Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    if inhabitant.name == "Farenyuk":
                        if len(friends) < 3:
                            print("not enough friends:( you died")
                            dead = True
                    # What happens if you win?
                        else:
                            print("Hooray, you won the fight!")
                            current_room.character = None
                            if inhabitant.get_defeated() == 2:
                                print("Congratulations, you have vanquished the enemy horde!")
                                dead = True
                    else:
                        print("Hooray, you won the fight!")
                        current_room.character = None
                        if inhabitant.get_defeated() == 2:
                            print("Congratulations, you have vanquished the enemy horde!")
                            dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    elif command == "friendship":
        if inhabitant is not None and isinstance(inhabitant, game.Friend):
            print("Make a friendship? y/n")
            answer = input('> ')
            if answer == 'y':
                friends.append(inhabitant)
                print(f"Congratulations! {inhabitant.name} is your friend now")
                current_room.set_character(None)
            elif answer == 'n':
                continue
    else:
        print("I don't know how to " + command)
