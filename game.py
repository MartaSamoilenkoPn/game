"""Module Game"""
class Room:
    """class Room"""
    def __init__(self, name, floor) -> None:
        self.name = name
        self.floor = floor
        self.links = []
        self.description = None
        self.character = None
        self.item = None

    def set_description(self, description):
        """_summary_

        Args:
            description (_type_): _description_
        """
        self.description = description

    def set_character(self, character):
        """_summary_

        Args:
            character (_type_): _description_
        """
        self.character = character

    def get_character(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.character

    def set_item(self, item):
        """_summary_

        Args:
            item (_type_): _description_
        """
        self.item = item

    def get_item(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.item

    def get_details(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        print(self.name)
        print('--------------------')
        print(self.description)
        for link in self.links:
            print(f'The {link[0].name} is {link[1]}')

    def move(self, way):
        """_summary_
        """
        for link in self.links:
            if link[1] == way:
                return link[0]

    def link_room(self, room, way):
        """_summary_

        Args:
            room (_type_): _description_
            way (_type_): _description_
        """
        self.links.append((room, way))

    def draw(self):
        pass

DEFEATED_ENEMIES = 0
class Enemy:
    """class Enemy"""
    def __init__(self, name, enemy_type) -> None:
        self.name = name
        self.enemy_type = enemy_type
        self.conversation = None
        self.weakness = None

    def set_conversation(self, conversation):
        """_summary_

        Args:
            conversation (_type_): _description_
        """
        self.conversation = conversation

    def set_weakness(self, weakness):
        """_summary_

        Args:
            weakness (_type_): _description_
        """
        self.weakness = weakness

    def talk(self):
        """_summary_

        Args:
            talk (_type_): _description_

        Returns:
            _type_: _description_
        """
        print(f'[{self.name} says]: {self.conversation}')

    def get_defeated(self):
        """_summary_
        """
        global DEFEATED_ENEMIES
        DEFEATED_ENEMIES += 1
        return DEFEATED_ENEMIES

    def fight(self, item_to_fight):
        """_summary_
        """
        if item_to_fight == self.weakness:
            return True
        return False

    def describe(self):
        print(f'{self.name} is here!')
        print(self.enemy_type)

class Item:
    """class Item"""
    def __init__(self, name) -> None:
        self.name = name
        self.description = None

    def get_name(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.name

    def set_description(self, description):
        """_summary_

        Args:
            description (_type_): _description_
        """
        self.description = description

    def describe(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        print(self.description)

class Friend:
    """class Friend"""
    def __init__(self, name, friend_type) -> None:
        self.name = name
        self.friend_type = friend_type
        self.conversation = None
        self.weakness = None

    def set_conversation(self, conversation):
        """_summary_

        Args:
            conversation (_type_): _description_
        """
        self.conversation = conversation

    def set_weakness(self, weakness):
        """_summary_

        Args:
            weakness (_type_): _description_
        """
        self.weakness = weakness

    def talk(self):
        """_summary_

        Args:
            talk (_type_): _description_

        Returns:
            _type_: _description_
        """
        print(f'[{self.name} says]: {self.conversation}')

    def fight(self, item_to_fight):
        """_summary_
        """
        if item_to_fight == self.weakness:
            return True
        return False

    def describe(self):
        print(f'{self.name} is here!')
