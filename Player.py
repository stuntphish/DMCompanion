from enum import auto
import Skill

if __name__ == "__main__":
    print("Please run DMCompanion.py")
    quit()

strength = Skill.strength
dexterity = Skill.dexterity
constitution = Skill.constitution
intelligence = Skill.intelligence
wisdom = Skill.wisdom
charisma = Skill.charisma


class Player:
    def __init__(self, PlayerName: str, CharacterName: str, Str: int, Dex: int, Con: int, Int: int, Wis: int, Cha: int, MaxHP: int, Level: int=1, Xp: int=0):
        self.__stats = {strength: Str, dexterity: Dex, constitution: Con, intelligence: Int, wisdom: Wis, charisma: Cha}
        self.__playerName = PlayerName
        self.__characterName = CharacterName
        self.__maxHP = MaxHP
        self.__hp = MaxHP
        self.__level = Level
        self.__xp = Xp
        self.__skills = []

    def __repr__(self):
        return {"Player": self.__playerName, "Character": self.__characterName, "Level": self.__level, "Stats": self.__stats}

    def __str__(self):
        return f"""Player Name: {self.__playerName}
        Character Name: {self.__characterName}
        Character Class: Level {self.__level}
        ---Stats---
        STR:{self.__stats[strength]}({self.modString(strength)})
        DEX:{self.__stats[dexterity]}({self.modString(dexterity)})
        CON:{self.__stats[constitution]}({self.modString(constitution)})
        INT:{self.__stats[intelligence]}({self.modString(intelligence)})
        WIS:{self.__stats[wisdom]}({self.modString(wisdom)})
        CHA:{self.__stats[charisma]}({self.modString(charisma)})
        ------
        Passive Perception:{self.PP}
        HP:{self.__hp}/{self.__maxHP}"""

    def mod(self, stat: auto):
        """Returns the modifier of a player's requested stat
        Arguments: The auto ID of the stat
        """
        return (self.__stats[stat]-10)//2

    def modString(self, stat: auto):
        """Returns a string representation of a stat modifier
        Arguments: The auto ID of the stat
        """
        m = self.mod(stat)
        return f"+{m}" if m >= 0 else str(m)

    def longRest(self):
        """Regains all HP"""
        self.__hp = self.__maxHP
        # Regain Hit dice
        # self.__class.longRest()
        # self.__race.longRest()

    def shortRest(self, fromLong=False):
        if not fromLong:
            pass
            # Spend hit dice
        # self.__class.shortRest()
        # self.__race.shortRest()

    def assignXP(self, quantity):
        self.__xp += quantity

    @property
    def PP(self):
        """Passive perception"""
        return 10 + self.mod(wisdom) + self.profBonus * (Skill.perception in self.__skills)

    @property
    def profBonus(self):
        """Proficiency Bonus"""
        return 2 + (self.__level-1)//4

    @property
    def AC(self):
        # return self.__armour.ac(self.mod(dexterity)) + armour.shield in self.__inventory
        raise NotImplementedError

    @property
    def playerName(self):
        return self.__playerName

    @property
    def characterName(self):
        return self.__characterName
