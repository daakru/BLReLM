# -*- coding: utf-8 -*-
"""
BLRevive Gear | Classes that make saving and moving gear sets easier.

Version 1.0
Requires: N/A

@author: Kinetos#6935
"""
import numpy as np
from blrevive_enums import UIAttachment
from helpers_pyinstaller import resource_path


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


class BLReviveMuzzle(BLReviveGear):
    def __init__(self, config_name, friendly_name, image_icon_path=None, small_icon_path=None, gear_types=[]):
        super().__init__(config_name, friendly_name, image_icon_path, small_icon_path, gear_types)

    def EmptyGear():
        return BLReviveMuzzle(0, '')


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


class BLReviveMagazine(BLReviveGear):
    def __init__(self, config_name, friendly_name, image_icon_path=None, small_icon_path=None, gear_types=[]):
        super().__init__(config_name, friendly_name, image_icon_path, small_icon_path, gear_types)

    def EmptyGear():
        return BLReviveMagazine(-1, '')


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


class BLReviveGrip(BLReviveGear):
    def __init__(self, config_name, friendly_name, image_icon_path=None, small_icon_path=None, gear_types=[]):
        super().__init__(config_name, friendly_name, image_icon_path, small_icon_path, gear_types)

    def EmptyGear():
        return BLReviveGrip(None, '')


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


class BLReviveTag(BLReviveGear):
    def __init__(self, config_name, friendly_name, image_icon_path=None, small_icon_path=None, gear_types=[]):
        super().__init__(config_name, friendly_name, image_icon_path, small_icon_path, gear_types)

    def EmptyGear():
        return BLReviveTag(None, '')


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


class BLReviveCamo(BLReviveGear):
    def __init__(self, config_name, friendly_name, image_icon_path=None, small_icon_path=None, gear_types=[]):
        super().__init__(config_name, friendly_name, image_icon_path, small_icon_path, gear_types)

    def EmptyGear():
        return BLReviveCamo(None, '')


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


class BLReviveWeapon:
    def __init__(self, name, receiver, muzzle, grip, barrel, magazine, scope, stock, tag, camo):
        self.name = name
        self.receiver = receiver
        self.muzzle = muzzle
        self.grip = grip
        self.barrel = barrel
        self.magazine = magazine
        self.scope = scope
        self.stock = stock
        self.tag = tag
        self.camo = camo

# --------------------------------------------------------------------------- #

    def EmptyWeapon():
        return BLReviveWeapon(None,
                              BLReviveReceiver.EmptyGear(),
                              BLReviveMuzzle.EmptyGear(),
                              BLReviveGrip.EmptyGear(),
                              BLReviveBarrel.EmptyGear(),
                              BLReviveMagazine.EmptyGear(),
                              BLReviveScope.EmptyGear(),
                              BLReviveStock.EmptyGear(),
                              BLReviveTag.EmptyGear(),
                              BLReviveCamo.EmptyGear())

# --------------------------------------------------------------------------- #

    def ToMagiCow(self):
        columns = np.genfromtxt(resource_path('data/muzzles.csv'), delimiter=',', dtype=str)
        muzzles = list(columns.T[1])
        columns = np.genfromtxt(resource_path('data/magazines.csv'), delimiter=',', dtype=str)
        magazines = list(columns.T[1])
        weapon = {}
        weapon['Receiver'] = self.receiver.friendly_name
        if self.muzzle.friendly_name in muzzles:
            weapon['Muzzle'] = muzzles.index(self.muzzle.friendly_name)
        else:
            weapon['Muzzle'] = 0
        weapon['Stock'] = self.stock.friendly_name
        weapon['Barrel'] = self.barrel.friendly_name
        if self.magazine.friendly_name in magazines:
            weapon['Magazine'] = magazines.index(self.magazine.friendly_name)
        else:
            # TODO: Add default magazine pairs to auto set this
            weapon['Magazine'] = -1
        weapon['Scope'] = self.scope.friendly_name
        weapon['Grip'] = self.grip.friendly_name
        return weapon

    def LoadWeapon(weapon_dict):
        if 'name' not in weapon_dict:
            return BLReviveWeapon.EmptyWeapon()
        re = BLReviveReceiver(*weapon_dict['receiver'].values())
        st = BLReviveStock(*weapon_dict['stock'].values())
        ba = BLReviveBarrel(*weapon_dict['barrel'].values())
        sc = BLReviveScope(*weapon_dict['scope'].values())

        if 'muzzle' in weapon_dict:
            mz = BLReviveMuzzle(*weapon_dict['muzzle'].values())
            mg = BLReviveMagazine(*weapon_dict['magazine'].values())
            gp = BLReviveGrip(*weapon_dict['grip'].values())
            tg = BLReviveTag(*weapon_dict['tag'].values())
            cm = BLReviveCamo(*weapon_dict['camo'].values())
        else:
            mz = BLReviveMuzzle.EmptyGear()
            mg = BLReviveMagazine.EmptyGear()
            gp = BLReviveGrip.EmptyGear()
            tg = BLReviveTag.EmptyGear()
            cm = BLReviveCamo.EmptyGear()

        return BLReviveWeapon(
            weapon_dict['name'],
            re,
            mz,
            gp,
            ba,
            mg,
            sc,
            st,
            tg,
            cm
        )

    def to_dict(self):
        return {
            'name': self.name,
            'receiver': self.receiver.to_dict(),
            'muzzle': self.muzzle.to_dict(),
            'grip': self.grip.to_dict(),
            'barrel': self.barrel.to_dict(),
            'magazine': self.magazine.to_dict(),
            'scope': self.scope.to_dict(),
            'stock': self.stock.to_dict(),
            'tag': self.tag.to_dict(),
            'camo': self.camo.to_dict()
        }

    def to_enum(self):
        return {
            'name': self.name,
            UIAttachment.RECEIVER: self.receiver,
            UIAttachment.MUZZLE: self.muzzle,
            UIAttachment.GRIP: self.grip,
            UIAttachment.BARREL: self.barrel,
            UIAttachment.MAGAZINE: self.magazine,
            UIAttachment.SCOPE: self.scope,
            UIAttachment.STOCK: self.stock,
            UIAttachment.TAG: self.tag,
            UIAttachment.CAMO: self.camo
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
