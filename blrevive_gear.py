# -*- coding: utf-8 -*-
"""
BLRevive Gear | Classes that make saving and moving gear sets easier.

Version 1.0
Requires: N/A

@author: Kinetos#6935
"""


class BLReviveGear:
    def __init__(self, config_name, friendly_name, image_icon_path=None, small_icon_path=None, gear_types=[]):
        self.config_name = config_name
        self.friendly_name = friendly_name
        self.image_icon_path = image_icon_path
        self.small_icon_path = small_icon_path
        self.gear_types = gear_types

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #

    def GetName(self):
        return self.config_name

    def SetName(self, config_name):
        self.config_name = config_name

# --------------------------------------------------------------------------- #

    def GetFriendlyName(self):
        return self.friendly_name

    def SetFriendlyName(self, friendly_name):
        self.friendly_name = friendly_name

# --------------------------------------------------------------------------- #

    def GetImageIconPath(self):
        return self.image_icon_path

    def SetImageIconPath(self, path):
        self.image_icon_path = path

# --------------------------------------------------------------------------- #

    def GetSmallIconPath(self):
        return self.small_icon_path

    def SetSmallIconPath(self, path):
        self.small_icon_path = path

# --------------------------------------------------------------------------- #

    def GetGearTypes(self):
        return self.gear_types

    def SetGearTypes(self, types):
        self.gear_types = types

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #

    def IsType(self, type):
        return type in self.gear_types

# --------------------------------------------------------------------------- #

    def EmptyGear():
        return BLReviveGear(None, '')

# --------------------------------------------------------------------------- #

    def to_dict(self):
        return {
            'config_name': self.config_name,
            'friendly_name': self.friendly_name,
            'image_path': self.image_icon_path,
            'icon_path': self.small_icon_path,
            'gear_types': self.gear_types
        }


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


class BLReviveReceiver(BLReviveGear):
    def __init__(self, config_name, friendly_name, image_icon_path=None, small_icon_path=None, gear_types=[]):
        super().__init__(config_name, friendly_name, image_icon_path, small_icon_path, gear_types)

    def EmptyGear():
        return BLReviveReceiver(None, '')


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


class BLReviveStock(BLReviveGear):
    def __init__(self, config_name, friendly_name, image_icon_path=None, small_icon_path=None, gear_types=[]):
        super().__init__(config_name, friendly_name, image_icon_path, small_icon_path, gear_types)

    def EmptyGear():
        return BLReviveStock(None, '')


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


class BLReviveBarrel(BLReviveGear):
    def __init__(self, config_name, friendly_name, image_icon_path=None, small_icon_path=None, gear_types=[]):
        super().__init__(config_name, friendly_name, image_icon_path, small_icon_path, gear_types)

    def EmptyGear():
        return BLReviveBarrel(None, '')


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


class BLReviveScope(BLReviveGear):
    def __init__(self, config_name, friendly_name, image_icon_path=None, small_icon_path=None, gear_types=[]):
        super().__init__(config_name, friendly_name, image_icon_path, small_icon_path, gear_types)

    def EmptyGear():
        return BLReviveScope(None, '')


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


class BLReviveWeapon:
    def __init__(self, name, receiver, stock, barrel, scope):
        self.name = name
        self.receiver = receiver
        self.stock = stock
        self.barrel = barrel
        self.scope = scope

# --------------------------------------------------------------------------- #

    def EmptyWeapon():
        return BLReviveWeapon(None, BLReviveReceiver.EmptyGear(), BLReviveStock.EmptyGear(), BLReviveBarrel.EmptyGear(), BLReviveScope.EmptyGear())

# --------------------------------------------------------------------------- #

    def ToMagiCow(self):
        weapon = {}
        weapon['Receiver'] = self.receiver.friendly_name
        weapon['Stock'] = self.stock.friendly_name
        weapon['Barrel'] = self.barrel.friendly_name
        weapon['Scope'] = self.scope.friendly_name
        return weapon

    def LoadWeapon(weapon_dict):
        if 'name' not in weapon_dict:
            return BLReviveWeapon.EmptyWeapon()
        return BLReviveWeapon(
            weapon_dict['name'],
            BLReviveReceiver(*weapon_dict['receiver'].values()),
            BLReviveStock(*weapon_dict['stock'].values()),
            BLReviveBarrel(*weapon_dict['barrel'].values()),
            BLReviveScope(*weapon_dict['scope'].values())
        )

    def to_dict(self):
        return {
            'name': self.name,
            'receiver': self.receiver.to_dict(),
            'stock': self.stock.to_dict(),
            'barrel': self.barrel.to_dict(),
            'scope': self.scope.to_dict()
        }


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


class BLReviveLoadout:
    def __init__(self, name, primary, secondary, tactical, gear1, gear2, gear3, gear4):
        self.name = name
        self.primary = primary
        self.secondary = secondary
        self.tactical = tactical
        self.gear1 = gear1
        self.gear2 = gear2
        self.gear3 = gear3
        self.gear4 = gear4

# --------------------------------------------------------------------------- #

    def ToMagiCow(self):
        loadout = {}
        if self.primary is not None:
            loadout['Primary'] = self.primary.ToMagiCow()
        else:
            loadout['Primary'] = BLReviveWeapon.EmptyWeapon().ToMagiCow()

        if self.secondary is not None:
            loadout['Secondary'] = self.secondary.ToMagiCow()
        else:
            loadout['Secondary'] = BLReviveWeapon.EmptyWeapon().ToMagiCow()

        return loadout

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
