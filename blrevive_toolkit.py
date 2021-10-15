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
from os.path import exists
from helpers_pyinstaller import resource_path
from blrevive_gear import BLReviveWeapon
from blrevive_enums import Gear


# --------------------------------------------------------------------------- #


def get_receivers():
    """
    Load the list of valid receiver friendly names for MagiCow's bot.

    Returns
    -------
    list
        List of receiver friendly names.

    """
    # return pd.read_csv(resource_path('data/receivers.csv'), dtype=str, header=None)[0].tolist()
    return list(np.genfromtxt(resource_path('data/receivers.csv'), delimiter=',', dtype=str))


def get_stocks():
    """
    Load the list of valid stock friendly names for MagiCow's bot.

    Returns
    -------
    list
        List of stock friendly names.

    """
    # return pd.read_csv(resource_path('data/stocks.csv'), dtype=str, header=None)[0].tolist()
    return list(np.genfromtxt(resource_path('data/stocks.csv'), delimiter=',', dtype=str))


def get_barrels():
    """
    Load the list of valid barrel friendly names for MagiCow's bot.

    Returns
    -------
    list
        List of barrel friendly names.

    """
    # return pd.read_csv(resource_path('data/barrels.csv'), dtype=str, header=None)[0].tolist()
    return list(np.genfromtxt(resource_path('data/barrels.csv'), delimiter=',', dtype=str))


def get_scopes():
    """
    Load the list of valid scope friendly names for MagiCow's bot.

    Returns
    -------
    list
        List of scope friendly names.

    """
    # return pd.read_csv(resource_path('data/scopes.csv'), dtype=str, header=None)[0].tolist()
    return list(np.genfromtxt(resource_path('data/scopes.csv'), delimiter=',', dtype=str))


def get_muzzles():
    """
    Load the list of valid muzzle friendly names for MagiCow's bot.

    Returns
    -------
    list
        List of muzzle friendly names.

    """
    # return pd.read_csv(resource_path('data/muzzles.csv'), dtype=str, header=None)[0].tolist()
    columns = np.genfromtxt(resource_path('data/muzzles.csv'), delimiter=',', dtype=str)
    return list(columns.T[1])


def get_magazines():
    """
    Load the list of valid magazine friendly names for MagiCow's bot.

    Returns
    -------
    list
        List of magazine friendly names.

    """
    # return pd.read_csv(resource_path('data/magazines.csv'), dtype=str, header=None)[0].tolist()
    columns = np.genfromtxt(resource_path('data/magazines.csv'), delimiter=',', dtype=str)
    return list(columns.T[1])


def get_grips():
    """
    Load the list of valid grip friendly names for MagiCow's bot.

    Returns
    -------
    list
        List of grip friendly names.

    """
    # return pd.read_csv(resource_path('data/grips.csv'), dtype=str, header=None)[0].tolist()
    return list(np.genfromtxt(resource_path('data/grips.csv'), delimiter=',', dtype=str))


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


# Define filters for configparser functions
def filter_FOXWEAPON(value):
    return value.startswith('FOXWEAPON_')


def filter_dotFoxWeapon(value):
    return value.split('.')[-1].startswith('FoxWeapon_')


def filter_FOXWEAPONMAGAZINE(value):
    return value.startswith('FOXWEAPONMAGAZINE_')


def filter_FOXWEAPONMUZZLE(value):
    return value.startswith('FOXWEAPONMUZZLE_')


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


def extract_localization_cfg(targetdir, file, filter=None, loc=None):
    """
    Open and load into configparser an *.INT file with utf-16-le encoding.

    Parameters
    ----------
    targetdir : str
        Path to the directory the target file is in.
    file : str
        Filename to open. Does not require INT postfix.
    filter : delegate
        Boolean filter to choose sections to extract. The default is None.
    loc : ConfigParser, optional
        Existing parser object to append to. The default is None.

    Returns
    -------
    loc : ConfigParser
        Parser object containing the extracted data.

    """
    if loc is None:
        loc = cfp.ConfigParser(strict=False, comment_prefixes=('#', ';', '`', '%'))
    if not file.endswith('.INT'):
        file += '.INT'
    with open(resource_path(targetdir + file), encoding='utf-16-le') as fp:
        # Skip the first line containing '\ufeff'
        fp.readline()
        loc.read_file(fp)
        if filter is not None:
            for section in loc.sections():
                if not filter(section):
                    loc.remove_section(section)
    return loc


# --------------------------------------------------------------------------- #


def extract_config_cfg(targetdir, file, filter=None, cfg=None):
    """
    Open and load into configparser an *.ini file with standard encoding.

    Parameters
    ----------
    targetdir : str
        Path to the directory the target file is in.
    file : str
        Filename to open. Does not require INT postfix.
    filter : delegate
        Boolean filter to choose sections to extract. The default is None.
    cfg : ConfigParser, optional
        Existing parser object to append to. The default is None.

    Returns
    -------
    cfg : ConfigParser
        Parser object containing the extracted data.

    """
    if cfg is None:
        cfg = cfp.ConfigParser(strict=False,
                               comment_prefixes=('#', ';', '`', '*', '/', 'WhiteRecievers.Empty'),
                               delimiters=('=', ':'))
    if not file.endswith('.ini'):
        file += '.ini'
    with open(resource_path(targetdir + file)) as fp:
        cfg.read_file(fp)
        if filter is not None:
            for section in cfg.sections():
                if not filter(section):
                    cfg.remove_section(section)
    return cfg


# --------------------------------------------------------------------------- #


def get_weapon_localization_cfg(load=True, export=False, filter=filter_FOXWEAPON):
    output_file = 'data/filegen/foxgamecontent_loc.ini'
    if not load:
        # Build the config parser object and append the desired files
        configpath = 'resource/FoxGame/Localization/INT/'
        filenames = ['CHA', 'DLC1', 'DLC2', 'DLC3', 'DLC4', 'DLC5', 'DLC6',
                     'OS', 'PL', 'SND', 'WPN', 'WPNC', 'WPNG', 'WPNS']
        cfg = extract_localization_cfg(resource_path(configpath),
                                       'FoxGame',
                                       filter)
        for fgc in filenames:
            cfg = extract_localization_cfg(resource_path(configpath),
                                           'FoxGameContent_' + str(fgc),
                                           filter, cfg)
        if export:
            # Open the output file and write the parser object to it
            with open(resource_path(output_file), 'w') as fp:
                cfg.write(fp)
        return cfg
    else:
        # Read the pre-existing localization file
        with open(resource_path(output_file)) as fp:
            cfg = cfp.ConfigParser(strict=False,
                                   comment_prefixes=('#', ';', '`'))
            cfg.read_file(fp)
            return cfg


# --------------------------------------------------------------------------- #


def get_default_weapon_cfg(load=True, export=False, filter=filter_dotFoxWeapon):
    output_file = 'data/filegen/defaultweapon_cfg.ini'
    if not load:
        # Build the config parser object and append the desired files
        configpath = 'resource/FoxGame/Config/'  # 'data/v3.0494/'
        filenames = list(np.genfromtxt(resource_path('data/targets/t_defaultconfig.csv'), delimiter=',', dtype=str))

        cfg = extract_config_cfg(resource_path(configpath),
                                 filenames.pop(0),
                                 filter)
        for filename in filenames:
            cfg = extract_config_cfg(resource_path(configpath),
                                     filename,
                                     filter, cfg)
        if export:
            # Open the output file and write the parser object to it
            with open(resource_path(output_file), 'w') as fp:
                cfg.write(fp)
        return cfg
    else:
        # Read the pre-existing config file
        with open(resource_path(output_file)) as fp:
            cfg = cfp.ConfigParser(strict=False,
                                   comment_prefixes=('#', ';', '`'))
            cfg.read_file(fp)
            return cfg


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


def config_parser_to_pandas(cfg):
    option_set = set()
    sections = cfg.sections()
    for section in sections:
        for a in cfg.options(section):
            option_set.add(a)

    df = pd.DataFrame(columns=sorted(option_set))

    for section in sections:
        values = []
        for col in df.columns:
            if cfg.has_option(section, col):
                values.append(cfg.get(section, col))
            else:
                values.append(np.nan)
        df.loc[section] = values

    return df

# --------------------------------------------------------------------------- #


def build_receivers_dataframe():
    # Load configparser objects
    cfg_default_weapons = get_default_weapon_cfg()
    cfg_foxgamecontent_wpn = get_weapon_localization_cfg()

# --------------------------------------------------------------------------- #

    def sort_image_paths(*a):
        im = ''
        ui = ''
        if type(a[0]) == str:
            if a[0].startswith('UI_NewItemIcons'):
                im = a[0]
            elif a[0].startswith('UI_Icons'):
                ui = a[0]
        if type(a[1]) == str:
            if a[1].startswith('UI_NewItemIcons'):
                im = a[1]
            elif a[1].startswith('UI_Icons'):
                ui = a[1]
        return [im, ui]

    def fix_image_paths(df):
        ImageIconRef = pd.DataFrame([sort_image_paths(*a) for a in zip(df['ImageIconRef'], df['imageiconref'])])

        df['ImageIconRef'] = list(ImageIconRef[0])
        df['imageiconref'] = list(ImageIconRef[1])

        df.rename(columns={'imageiconref': 'UIIconRef'}, inplace=True)

    def get_section(wpn):
        if type(wpn) != str:
            return np.nan
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

    def match_wpn(*wpn):
        if type(wpn[0]) != str:
            return '_' + str(wpn[1])
        return cfg_foxgamecontent_wpn.get(wpn[0].upper(), 'friendlyname')

# --------------------------------------------------------------------------- #

    receivers = pd.read_json(resource_path('data/filegen/default_weapon_presets.json'))

    depots = pd.read_json(resource_path('data/filegen/depot_presets.json'))
    depots.rename(columns={'UnlockId': 'UnlockID'}, inplace=True)

    receivers = receivers.append(depots, ignore_index=True, verify_integrity=True)

    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.width', None)
    # pd.set_option('display.max_colwidth', None)

    idx = []
    idx.append(list(receivers['WPN']).index('FoxWeapon_DeployableJammer'))
    idx.append(list(receivers['WPN']).index('FoxWeapon_HardSuitTargeterLight'))

    receivers = receivers.drop(labels=idx, axis=0)

    receivers = receivers.reset_index()

    receivers.insert(0, 'FriendlyName',
                     [match_wpn(*wpn) for wpn in zip(receivers['WPN'], receivers['NameID'])])

    new_index = [get_section(a) for a in receivers['WPN']]
    fix_index = []
    remove_rows = []
    for i in range(len(new_index)):
        if type(new_index[i]) != str:
            remove_rows.append(i)
        else:
            fix_index.append(new_index[i])

    receivers = receivers.drop(labels=remove_rows, axis=0)

    receivers.index = fix_index

    dwini = config_parser_to_pandas(cfg_default_weapons)

    df_primary = pd.merge(receivers, dwini, left_index=True, right_index=True)
    df_primary['imageiconref'] = df_primary['imageiconref'].apply(lambda a: str(a).strip('"'))
    df_primary['shortname'] = df_primary['shortname'].apply(lambda a: str(a).strip('"'))

    fix_image_paths(df_primary)

    return df_primary


def generate_df_magazines():
    cfg = extract_config_cfg('resource/FoxGame/Config/', 'DefaultMagazine.ini', None)
    dmini = config_parser_to_pandas(cfg)

    wloc = get_weapon_localization_cfg(False, False, filter_FOXWEAPONMAGAZINE)
    df_wloc = config_parser_to_pandas(wloc)

    df_wloc.index = [a.split(' ')[0] for a in df_wloc.index]
    dmini = dmini.drop(labels=['FoxGame.FoxWeaponMagazine_Base'], axis=0)
    dmini.index = [a.split(' ')[0].upper() for a in dmini.index]

    df_magazines = pd.merge(dmini, df_wloc, left_index=True, right_index=True)
    df_magazines.insert(0, 'LoadIndex', range(len(df_magazines.index)))
    df_smaller_mags = df_magazines.filter(['LoadIndex', 'friendlyname', 'descriptorname', 'whiterecievers'], axis=1)

    return df_magazines, df_smaller_mags


def generate_df_muzzles():
    cfg = extract_config_cfg('resource/FoxGame/Config/', 'DefaultMuzzle.ini', None)
    dmini = config_parser_to_pandas(cfg)

    wloc = get_weapon_localization_cfg(False, False, filter_FOXWEAPONMUZZLE)
    df_wloc = config_parser_to_pandas(wloc)

    df_wloc.index = [a.split(' ')[0] for a in df_wloc.index]
    dmini = dmini.drop(labels=['FoxGame.FoxWeaponMuzzle_Base'], axis=0)
    dmini.index = [a.split(' ')[0].upper() for a in dmini.index]

    df_muzzles = pd.merge(dmini, df_wloc, left_index=True, right_index=True)
    df_muzzles.insert(0, 'LoadIndex', range(len(df_muzzles.index)))
    df_smaller_muzzles = df_muzzles.filter(['LoadIndex', 'friendlyname', 'descriptorname', 'whiterecievers'], axis=1)

    return df_muzzles, df_smaller_muzzles


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


# DefaultUnlocks.ini -> DefaultWeaponPresets & DepotPresets
def generate_weapon_and_depot_presets(filepath='resource/FoxGame/Config/DefaultUnlocks.ini'):
    filepath = resource_path(filepath)
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
            # sp[0]
            e[sp[0].strip()] = sp[1].strip().strip('"')
        default_weapon_presets.append(e)

    for entry in dep:
        e = {}
        pairs = entry.split(',')
        for pair in pairs:
            sp = pair.split('=')
            e[sp[0].strip()] = sp[1].strip().strip('"')
        depot_presets.append(e)

    with open(resource_path('data/filegen/default_weapon_presets.json'), 'w') as fp:
        json.dump(default_weapon_presets, fp, indent=4)

    with open(resource_path('data/filegen/depot_presets.json'), 'w') as fp:
        json.dump(depot_presets, fp, indent=4)


# --------------------------------------------------------------------------- #


def generate_blrlm_config_json(cfgpath='resource/FoxGame/Config/DefaultUnlocks.ini', rebuild_deps=True):
    if rebuild_deps:
        generate_weapon_and_depot_presets(cfgpath)

    with open(resource_path('data/filegen/default_weapon_presets.json')) as fp:
        dwp = json.load(fp)
        out = {'allowedWeapons': []}
        for weap in dwp:
            out['allowedWeapons'].append(weap['WPN'])
    with open(resource_path('data/filegen/config.json'), 'w') as fp:
        json.dump(out, fp, indent=4)


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


def get_user_config():
    if not exists('./settings.json'):
        with open('./settings.json', 'w') as fp:
            json.dump({'PlayerName': 'Player'}, fp, indent=4)
    with open('./settings.json') as fp:
        return json.load(fp)


def write_saved_session(session):
    with open('./session.json', 'w') as fp:
        json.dump({'SavedSession': session}, fp, indent=4)


def load_saved_session():
    if not exists('./session.json'):
        with open('./session.json', 'w') as fp:
            json.dump({'SavedSession': {}}, fp, indent=4)
    with open('./session.json') as fp:
        session = {}
        i = 0
        gearlist = json.load(fp)['SavedSession']
        # breakpoint()
        for gear in gearlist.values():
            # breakpoint()
            session[Gear(i).name] = BLReviveWeapon.LoadWeapon(gear)
            i += 1
        return session

# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


def build_magicow_loadout(playername, loadout1, loadout2, loadout3):
    mcloadout = {'DiscordId': 0, 'PlayerName': playername, 'Loadout1': loadout1.ToMagiCow(), 'Loadout2': loadout2.ToMagiCow(), 'Loadout3': loadout3.ToMagiCow()}
    return 'register\n' + json.dumps(mcloadout, indent=4)
    # return json.dumps(mcloadout, indent=4)
    # with open(filepath, 'w') as fp:
    #     json.dump(mcloadout, fp, indent=4)


# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #


def generate_default_weapon_cfg():
    get_default_weapon_cfg(False, True)


def generate_weapon_loc_cfg():
    get_weapon_localization_cfg(False, True)


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
    # generate_blrlm_config_json()

    build_receivers_dataframe()

    # nan.TGA: Flamethrower, Grenade Launcher, Minigun, MK1 Assault AI, Railgun, Rhino Hardsuit, Rocket Stinger, Rocket Swarm
