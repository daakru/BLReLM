# -*- coding: utf-8 -*-
"""
BLRevive Toolkit | Tools used for filtering information from game configs etc.

Version 1.0
Requires: json, numpy, pandas, configparser, helpers_pyinstaller.py (v1.0)

@author: Kinetos#6935
"""
import json
import numpy as np
import pandas as pd
import configparser as cfp
from os import getcwd
from os.path import exists
from helpers_pyinstaller import resource_path


# --------------------------------------------------------------------------- #


def modify_filepath(filepath):
    current_dir = getcwd().split('\\')[-1].split('/')[-1]
    if current_dir == 'resource':
        if not filepath.startswith('../'):
            filepath = '../' + filepath
    return resource_path(filepath)


# --------------------------------------------------------------------------- #


def get_receivers():
    # return pd.read_csv(modify_filepath('data/receivers.csv'), dtype=str, header=None)[0].tolist()
    return np.genfromtxt(modify_filepath('data/receivers.csv'), delimiter=',', dtype=str)


def get_stocks():
    # return pd.read_csv(modify_filepath('data/stocks.csv'), dtype=str, header=None)[0].tolist()
    return np.genfromtxt(modify_filepath('data/stocks.csv'), delimiter=',', dtype=str)


def get_barrels():
    # return pd.read_csv(modify_filepath('data/barrels.csv'), dtype=str, header=None)[0].tolist()
    return np.genfromtxt(modify_filepath('data/barrels.csv'), delimiter=',', dtype=str)


def get_scopes():
    # return pd.read_csv(modify_filepath('data/scopes.csv'), dtype=str, header=None)[0].tolist()
    return np.genfromtxt(modify_filepath('data/scopes.csv'), delimiter=',', dtype=str)


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


# Define filters for configparser functions
def filter_FOXWEAPON(value):
    return value.startswith('FOXWEAPON_')


def filter_dotFoxWeapon(value):
    return value.split('.')[-1].startswith('FoxWeapon_')


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


def get_localization_cfg(targetdir, file, filter, loc=None):
    if loc is None:
        loc = cfp.ConfigParser(strict=False, comment_prefixes=('#', ';', '`'))
    if not file.endswith('.INT'):
        file += '.INT'
    with open(modify_filepath(targetdir + file), encoding='utf-16-le') as fp:
        # Skip the first line containing '\ufeff'
        fp.readline()
        loc.read_file(fp)
        if filter is not None:
            for section in loc.sections():
                if not filter(section):
                    loc.remove_section(section)
    return loc


# --------------------------------------------------------------------------- #


def get_weapon_cfg(targetdir, file, filter=None, cfg=None):
    if cfg is None:
        cfg = cfp.ConfigParser(strict=False, comment_prefixes=('#', ';', '`'), delimiters=('=', ':', '.'))
    if not file.endswith('.ini'):
        file += '.ini'
    with open(modify_filepath(targetdir + file)) as fp:
        cfg.read_file(fp)
        if filter is not None:
            for section in cfg.sections():
                if not filter(section):
                    cfg.remove_section(section)
    return cfg


# --------------------------------------------------------------------------- #


def get_weapon_loc_cfg(load=True, export=False):
    if not load:
        configpath = 'resource/FoxGame/Localization/INT/'
        filenames = ['CHA', 'DLC1', 'DLC2', 'DLC3', 'DLC4', 'DLC5', 'DLC6', 'OS', 'PL', 'SND', 'WPN', 'WPNC', 'WPNG', 'WPNS']
        cfg = get_localization_cfg(modify_filepath(configpath), 'FoxGameContent_' + filenames.pop(0), filter_FOXWEAPON)
        for fgc in filenames:
            cfg = get_localization_cfg(modify_filepath(configpath), 'FoxGameContent_' + str(fgc), filter_FOXWEAPON, cfg)
        if export:
            with open(modify_filepath('data/filegen/foxgamecontent_loc.ini'), 'w') as fp:
                cfg.write(fp)
        return cfg
    else:
        with open(modify_filepath('data/filegen/foxgamecontent_loc.ini')) as fp:
            cfg = cfp.ConfigParser(strict=False, comment_prefixes=('#', ';', '`'))
            cfg.read_file(fp)
            return cfg


# --------------------------------------------------------------------------- #


def get_default_weapon_cfg(load=True, export=False, cfgpath='resource/FoxGame/Config/'):
    if not load:
        configpath = cfgpath  # 'data/v3.0494/'
        filenames = ['DefaultAK47.ini', 'DefaultAR2.ini', 'DefaultAR3.ini', 'DefaultAssaultRifle.ini', 'DefaultAutoPistol.ini', 'DefaultAutoShotgun.ini', 'DefaultBASniper.ini', 'DefaultBKT.ini', 'DefaultBullpup.ini', 'DefaultBullpup2.ini', 'DefaultCompoundBow.ini', 'DefaultDartGun.ini', 'DefaultGearInfo.ini', 'DefaultHealGun.ini', 'DefaultHeavySniper.ini', 'DefaultKnife.ini', 'DefaultM4.ini', 'DefaultMachinePistol.ini', 'DefaultMagazine.ini', 'DefaultPawn.ini', 'DefaultPistol_45.ini', 'DefaultPistol_9mm.ini', 'DefaultProjectile.ini', 'DefaultRBKT.ini', 'DefaultRepairGun.ini', 'DefaultRevolver.ini', 'DefaultScoring.ini', 'DefaultShotgun.ini', 'DefaultSMG.ini', 'DefaultSMG2.ini', 'DefaultSMGi.ini', 'DefaultSniperRifle.ini', 'DefaultSniperRifle2.ini', 'DefaultSnubNose.ini', 'DefaultTacticalGear.ini', 'DefaultThrowingKnives.ini', 'DefaultThrowingStar.ini', 'DefaultTomahawk.ini']
        cfg = get_weapon_cfg(modify_filepath(configpath), filenames.pop(0), filter_dotFoxWeapon)
        for filename in filenames:
            cfg = get_weapon_cfg(modify_filepath(configpath), filename, filter_dotFoxWeapon, cfg)
        if export:
            with open(modify_filepath('data/filegen/defaultweapon_cfg.ini'), 'w') as fp:
                cfg.write(fp)
        return cfg
    else:
        with open(modify_filepath('data/filegen/defaultweapon_cfg.ini')) as fp:
            cfg = cfp.ConfigParser(strict=False, comment_prefixes=('#', ';', '`'))
            cfg.read_file(fp)
            return cfg


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


def build_receivers_dataframe():
    # Load configparser objects
    cfg_default_weapons = get_default_weapon_cfg()
    cfg_foxgamecontent_wpn = get_weapon_loc_cfg()

# --------------------------------------------------------------------------- #

    def get_section(wpn):
        target = cfg_default_weapons.sections()
        target = next(x for x in target if x.split('.')[-1] == wpn)
        return target

# --------------------------------------------------------------------------- #

    def get_damage_values(section):
        option = 'instanthitdamage[0]'
        if cfg_default_weapons.has_option(section, option):
            return cfg_default_weapons.get(section, option)
        elif section == 'FoxGameContent_DLC6.FoxWeapon_CompoundBow':
            return 240
        else:
            print(f'ERROR: Section "{section}" has no option "{option}"!')
            return np.nan

# --------------------------------------------------------------------------- #

    def match_wpn(wpn):
        return cfg_foxgamecontent_wpn.get(wpn.upper(), 'friendlyname')

# --------------------------------------------------------------------------- #

    receivers = pd.read_json(resource_path('data/filegen/default_weapon_presets.json'))
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)

    receivers.insert(0, 'FriendlyName', [match_wpn(wpn) for wpn in receivers['WPN']])

    receivers.index = [get_section(a) for a in receivers['WPN']]

    option_set = set()
    for section in cfg_default_weapons.sections():
        for a in cfg_default_weapons.options(section):
            option_set.add(a)

    dwini = pd.DataFrame(columns=sorted(option_set))

    for section in cfg_default_weapons.sections():
        values = []
        for col in dwini.columns:
            if cfg_default_weapons.has_option(section, col):
                values.append(cfg_default_weapons.get(section, col))
            else:
                values.append(np.nan)
        dwini.loc[section] = values

    df_primary = pd.merge(receivers, dwini, left_index=True, right_index=True)
    df_primary['imageiconref'] = df_primary['imageiconref'].apply(lambda a: a.strip('"'))
    df_primary['shortname'] = df_primary['shortname'].apply(lambda a: a.strip('"'))

    return df_primary


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


# DefaultUnlocks.ini -> DefaultWeaponPresets & DepotPresets
def generate_weapon_and_depot_presets(filepath='resource/FoxGame/Config/DefaultUnlocks.ini'):
    filepath = modify_filepath(filepath)
    default_weapon_presets = []
    depot_presets = []
    dwp = []
    dep = []
    with open(filepath) as fp:
        for line in fp.readlines():
            if line.startswith('DefaultWeaponPresets'):
                dwp.append((line.split('=(', 1)[1]).split(')')[0])
            elif line.startswith('DepotPresets'):
                dep.append((line.split('=(', 1)[1]).split(')')[0])

    for entry in dwp:
        e = {}
        pairs = entry.split(',')
        for pair in pairs:
            sp = pair.split('=')
            sp[0]
            e[sp[0].strip()] = sp[1].strip().strip('"')
        default_weapon_presets.append(e)

    for entry in dep:
        e = {}
        pairs = entry.split(', ')
        for pair in pairs:
            sp = pair.split('=')
            e[sp[0].strip()] = sp[1].strip().strip('"')
        depot_presets.append(e)

    with open(modify_filepath('data/filegen/default_weapon_presets.json'), 'w') as fp:
        json.dump(default_weapon_presets, fp, indent=4)

    with open(modify_filepath('data/filegen/depot_presets.json'), 'w') as fp:
        json.dump(depot_presets, fp, indent=4)


# --------------------------------------------------------------------------- #


def generate_blrlm_config_json(cfgpath='resource/FoxGame/Config/DefaultUnlocks.ini', rebuild_deps=True):
    if rebuild_deps:
        generate_weapon_and_depot_presets(cfgpath)

    with open(modify_filepath('data/filegen/default_weapon_presets.json')) as fp:
        dwp = json.load(fp)
        out = {'allowedWeapons': []}
        for weap in dwp:
            out['allowedWeapons'].append(weap['WPN'])
    with open(modify_filepath('data/filegen/config.json'), 'w') as fp:
        json.dump(out, fp, indent=4)


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


def get_user_config():
    if not exists('./settings.json'):
        with open('./settings.json', 'w') as fp:
            json.dump({'PlayerName': 'Player'}, fp, indent=4)
    with open('./settings.json') as fp:
        return json.load(fp)


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


def build_magicow_loadout(playername, loadout1, loadout2, loadout3):
    mcloadout = {'DiscordId': 0, 'PlayerName': playername, 'Loadout1': loadout1.ToMagiCow(), 'Loadout2': loadout2.ToMagiCow(), 'Loadout3': loadout3.ToMagiCow()}
    return 'register\n' + json.dumps(mcloadout, indent=4)
    # with open(filepath, 'w') as fp:
    #     json.dump(mcloadout, fp, indent=4)


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


def generate_default_weapon_cfg():
    get_default_weapon_cfg(False, True)


def generate_weapon_loc_cfg():
    get_weapon_loc_cfg(False, True)


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


def calcrange(*args):
    pass


def calcrecoil(*args):
    pass


def calcspread_h(*args):
    pass


def calcspread_a(*args):
    pass


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


if __name__ == "__main__":
    # This shouldn't require anything else to be generated first
    generate_default_weapon_cfg()
    generate_weapon_loc_cfg()

    # Generate the main config file for the BLRevive Loadout Manager App
    generate_blrlm_config_json()
