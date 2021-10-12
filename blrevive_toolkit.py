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
    """
    Adjusts the filepath if the code is not being run as a module.
    TODO: Remove this and replace with resource_path()

    Parameters
    ----------
    filepath : str
        DESCRIPTION.

    Returns
    -------
    str
        DESCRIPTION.

    """
    current_dir = getcwd().split('\\')[-1].split('/')[-1]
    if current_dir == 'resource':
        if not filepath.startswith('../'):
            filepath = '../' + filepath
    return resource_path(filepath)


# --------------------------------------------------------------------------- #


def get_receivers():
    """
    Load the list of valid receiver friendly names for MagiCow's bot.

    Returns
    -------
    list
        List of receiver friendly names.

    """
    # return pd.read_csv(modify_filepath('data/receivers.csv'), dtype=str, header=None)[0].tolist()
    return np.genfromtxt(modify_filepath('data/receivers.csv'), delimiter=',', dtype=str)


def get_stocks():
    """
    Load the list of valid stock friendly names for MagiCow's bot.

    Returns
    -------
    list
        List of stock friendly names.

    """
    # return pd.read_csv(modify_filepath('data/stocks.csv'), dtype=str, header=None)[0].tolist()
    return np.genfromtxt(modify_filepath('data/stocks.csv'), delimiter=',', dtype=str)


def get_barrels():
    """
    Load the list of valid barrel friendly names for MagiCow's bot.

    Returns
    -------
    list
        List of barrel friendly names.

    """
    # return pd.read_csv(modify_filepath('data/barrels.csv'), dtype=str, header=None)[0].tolist()
    return np.genfromtxt(modify_filepath('data/barrels.csv'), delimiter=',', dtype=str)


def get_scopes():
    """
    Load the list of valid scope friendly names for MagiCow's bot.

    Returns
    -------
    list
        List of scope friendly names.

    """
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
                               comment_prefixes=('#', ';', '`'),
                               delimiters=('=', ':', '.'))
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


def get_weapon_localization_cfg(load=True, export=False):
    output_file = 'data/filegen/foxgamecontent_loc.ini'
    if not load:
        # Build the config parser object and append the desired files
        configpath = 'resource/FoxGame/Localization/INT/'
        filenames = ['CHA', 'DLC1', 'DLC2', 'DLC3', 'DLC4', 'DLC5', 'DLC6',
                     'OS', 'PL', 'SND', 'WPN', 'WPNC', 'WPNG', 'WPNS']
        cfg = extract_localization_cfg(modify_filepath(configpath),
                                       'FoxGameContent_' + filenames.pop(0),
                                       filter_FOXWEAPON)
        for fgc in filenames:
            cfg = extract_localization_cfg(modify_filepath(configpath),
                                           'FoxGameContent_' + str(fgc),
                                           filter_FOXWEAPON, cfg)
        if export:
            # Open the output file and write the parser object to it
            with open(modify_filepath(output_file), 'w') as fp:
                cfg.write(fp)
        return cfg
    else:
        # Read the pre-existing localization file
        with open(modify_filepath(output_file)) as fp:
            cfg = cfp.ConfigParser(strict=False,
                                   comment_prefixes=('#', ';', '`'))
            cfg.read_file(fp)
            return cfg


# --------------------------------------------------------------------------- #


def get_default_weapon_cfg(load=True, export=False):
    output_file = 'data/filegen/defaultweapon_cfg.ini'
    if not load:
        # Build the config parser object and append the desired files
        configpath = 'resource/FoxGame/Config/'  # 'data/v3.0494/'
        filenames = [
            'DefaultAirStrike.ini',
            'DefaultAK47.ini', 'DefaultAR2.ini', 'DefaultAR3.ini',
            'DefaultAssaultRifle.ini', 'DefaultAutoPistol.ini',
            'DefaultAutoShotgun.ini', 'DefaultBASniper.ini', 'DefaultBKT.ini',
            'DefaultBullpup.ini', 'DefaultBullpup2.ini',
            'DefaultCompoundBow.ini', 'DefaultDartGun.ini',
            'DefaultFlameThrower.ini',
            'DefaultGearInfo.ini', 'DefaultHealGun.ini',
            'DefaultHeavySniper.ini', 'DefaultKnife.ini', 'DefaultLauncher.ini',
            'DefaultM4.ini',
            'DefaultMachinePistol.ini', 'DefaultMagazine.ini',
            'DefaultPawn.ini', 'DefaultPistol_45.ini', 'DefaultPistol_9mm.ini',
            'DefaultProjectile.ini', 'DefaultRailGun.ini', 'DefaultRBKT.ini',
            'DefaultRepairGun.ini',
            'DefaultRevolver.ini', 'DefaultScoring.ini', 'DefaultShotgun.ini',
            'DefaultSMG.ini', 'DefaultSMG2.ini', 'DefaultSMGi.ini',
            'DefaultSniperRifle.ini', 'DefaultSniperRifle2.ini',
            'DefaultSnubNose.ini', 'DefaultTacticalGear.ini',
            'DefaultTargeter.ini',
            'DefaultThrowingKnives.ini', 'DefaultThrowingStar.ini',
            'DefaultTomahawk.ini',
            'DefaultGrenadeLauncher',
            'DefaultMiniGun',
            'DefaultDeployableAI',
            'DefaultHRVDecoy',
        ]
        cfg = extract_config_cfg(modify_filepath(configpath),
                                 filenames.pop(0),
                                 filter_dotFoxWeapon)
        for filename in filenames:
            cfg = extract_config_cfg(modify_filepath(configpath),
                                     filename,
                                     filter_dotFoxWeapon, cfg)
        if export:
            # Open the output file and write the parser object to it
            with open(modify_filepath(output_file), 'w') as fp:
                cfg.write(fp)
        return cfg
    else:
        # Read the pre-existing config file
        with open(modify_filepath(output_file)) as fp:
            cfg = cfp.ConfigParser(strict=False,
                                   comment_prefixes=('#', ';', '`'))
            cfg.read_file(fp)
            return cfg


# --------------------------------------------------------------------------- #

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
        print(f'wpn:  {wpn}\ntype: {type(wpn)}')
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
            print(f'wpn:  {wpn[0]}\ntype: {type(wpn[0])}')
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

    # breakpoint()

    idx = []
    idx.append(list(receivers['WPN']).index('FoxWeapon_DeployableJammer'))
    idx.append(list(receivers['WPN']).index('FoxWeapon_HardSuitTargeterLight'))

    receivers = receivers.drop(labels=idx, axis=0)

    receivers = receivers.reset_index()

    receivers.insert(0, 'FriendlyName',
                     [match_wpn(*wpn) for wpn in zip(receivers['WPN'], receivers['NameID'])])

    # breakpoint()

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

    # breakpoint()

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
    df_primary['imageiconref'] = df_primary['imageiconref'].apply(lambda a: str(a).strip('"'))
    df_primary['shortname'] = df_primary['shortname'].apply(lambda a: str(a).strip('"'))

    fix_image_paths(df_primary)

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
    generate_blrlm_config_json()

    # build_receivers_dataframe()

    # nan.TGA: Flamethrower, Grenade Launcher, Minigun, MK1 Assault AI, Railgun, Rhino Hardsuit, Rocket Stinger, Rocket Swarm
