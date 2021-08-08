from datetime import datetime, timedelta
from types import SimpleNamespace
from random import randint
import argparse
import logging
import json
import sys
import requests
import os
import time


def load_config(config_file):
    config = {}

    try:
        with open(config_file, mode='r') as f:
            # logging.info('loading config: {}'.format(config_file))
            config = json.load(f)
            return config
    except FileNotFoundError:
        # logging.info('creating default config file...')
        return {}
    except json.decoder.JSONDecodeError as e:
        print('Error reading config file "{}": {}.'.format(config_file, str(e)))
        return {}


def save_config(filename, args, force):
    config = {}

    if args.session_cookie:
        config['session-cookie'] = args.session_cookie
    if args.year:
        config['year'] = args.year
    if args.day:
        config['day'] = args.day
    if args.src_template:
        config['src-template'] = args.src_template
    if args.src_template:
        config['src-output'] = args.src_output
    if args.src_template:
        config['test-template'] = args.test_template
    if args.src_template:
        config['test-output'] = args.test_output
    if args.input_output:
        config['input-output'] = args.input_output
    if args.wait:
        config['wait'] = args.wait
    if args.force:
        config['force'] = args.force
    if args.log:
        config['log'] = args.log

    exists = os.path.isfile(filename)

    if config:
        if not exists or force:
            with open(filename, "w+") as f:
                logging.info('Writing config file: {} ...'.format(filename))
                json.dump(config, f, indent=4)
        elif exists:
            print(
                'Config File "{}" already exists. Skipped writing file.'.format(filename))


def process_args(args):
    config = {} if args.ignore_config else load_config(args.config_file)

    if args.save_config:
        save_config(args.save_config_output, args, args.force if (
            args.force is not None) else False)

    n = SimpleNamespace()

    n.session_cookie = args.session_cookie if args.session_cookie else (
        config['session-cookie'] if 'session-cookie' in config else None)
    n.year = args.year if args.year else (
        int(config['year']) if 'year' in config else None)
    n.day = args.day if args.day else (
        int(config['day']) if 'day' in config else None)
    n.src_template = args.src_template if args.src_template else (
        config['src-template'] if 'src-template' in config else None)
    n.src_output = args.src_output if args.src_output else (
        config['src-output'] if 'src-output' in config else 'src/day{{day}}.py')
    n.test_template = args.test_template if args.test_template else (
        config['test-template'] if 'test-template' in config else None)
    n.test_output = args.test_output if args.test_output else (
        config['test-output'] if 'test-output' in config else 'tests/test_day{{day}}.py')
    n.input_output = args.input_output if args.input_output else (
        config['input-output'] if 'input-output' in config else 'inputs/day{{day}}/input')
    n.force = args.force if args.force is not None else (
        config['force'] if 'force' in config else False)
    n.wait = args.wait if args.wait is not None else (
        config['wait'] if 'wait' in config else False)
    n.log = args.log if args.log is not None else (
        config['log'] if 'log' in config else False)

    return n


def load_input_file(year, day, session_id):
    uri = 'https://adventofcode.com/{}/day/{}/input'.format(year, day)
    aoc_cookie = {'session': session_id}

    r = requests.get(uri, cookies=aoc_cookie)

    if r.status_code == 200:
        logging.info('Got input from {}'.format(uri))
        return r.text
    else:
        logging.info('Invalid request return: {} for {}'.format(
            r.status_code, uri))
        print('Error: Failed to load input: {} returned {}.'.format(
            uri, r.status_code))
        return None


def write_file(filename, content, force=False):
    if not filename:
        logging.info('Missig filename: {}!'.format(filename))
        return

    if not content:
        logging.info('No content to write for file: {}!'.format(filename))
        return

    dirs = os.path.dirname(filename)
    exists = os.path.isfile(filename)

    if dirs:
        logging.info('Creating directories: {} ...'.format(dirs))
        os.makedirs(dirs, exist_ok=True)

    if not exists or force:
        with open(filename, "w+") as f:
            logging.info('Writing file: {} ...'.format(filename))
            f.write(content)
    elif exists:
        print('File "{}" already exists. Skipped writing file.\nUse -f if you want to overwrite existing files.'.format(filename))


def replace_placeholder(content: str, year, day):
    content = content.replace('{{day}}', '{:02d}'.format(day))
    content = content.replace('{{year}}', '{}'.format(year))
    return content


def write_template(template, output, year, day, force):
    if template and output:
        try:
            with open(template, 'r') as f:
                logging.info(
                    'Reading & processing template: {} ...'.format(template))
                tmp = f.read()
                tmp = replace_placeholder(tmp, year, day)
                write_file(replace_placeholder(output, year, day), tmp, force)
        except FileNotFoundError as e:
            print('{}'.format(str(e)))


def write_input(output, session_cookie, year, day, force):
    if output and session_cookie:
        input_file = load_input_file(year, day, session_cookie)
        write_file(replace_placeholder(output, year, day), input_file, force)


def wait():
    utc_present = datetime.utcnow()
    delay = randint(2, 10)
    utc_aoc_release = utc_present.replace(
        month=12, hour=5, minute=0, second=delay, microsecond=0)

    if utc_aoc_release < utc_present:
        utc_aoc_release = utc_aoc_release + timedelta(days=1)

    time_until_release = utc_aoc_release - utc_present
    hours_until_release = time_until_release.seconds / 3600

    if hours_until_release > 24:
        print('Error: The next AoC Day is not tommorrow! (>24 hours).')
        print("We don't want to wait that long. Consider using -y <YEAR> and -d <DAY>")
        sys.exit(0)

    logging.info('Starting wait for {}'.format(time_until_release))
    
    while time_until_release.seconds >= 0:
        time_until_release = utc_aoc_release - datetime.utcnow()
        hours, remainder = divmod(time_until_release.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        sys.stdout.write('\r')
        sys.stdout.write('{:02}:{:02}:{:02} until Day {}!'.format(
            int(hours), int(minutes), int(seconds), utc_aoc_release.day))
        sys.stdout.flush()
        time.sleep(1)

    return utc_aoc_release.year, utc_aoc_release.day


def main():
    today = datetime.today()

    parser = argparse.ArgumentParser(
        description='Advent of Code (AOC) utility to download problem input and setup python files for a given day.')
    parser.add_argument('-s', '--session-cookie', type=str, default=None,
                        help='Session cookie which is used to dowload problem input')
    parser.add_argument('-y', '--year', type=int, default=None,
                        help='Download the aoc input for a given year')
    parser.add_argument('-d', '--day', type=int, default=None,
                        help='Download the aoc input for a given day')
    parser.add_argument('-st', '--src-template', type=str,
                        default=None, help='Source template file')
    parser.add_argument('-so', '--src-output', type=str,
                        default=None, help='Source output file')
    parser.add_argument('-tt', '--test-template', type=str,
                        default=None, help='Test template file')
    parser.add_argument('-to', '--test-output', type=str,
                        default=None, help='Test output file')
    parser.add_argument('-io', '--input-output', type=str,
                        default=None, help='Input output file')
    parser.add_argument('-w', '--wait', action='store_true',
                        default=None, help='Wait for the next problem release')
    parser.add_argument('-l', '--log', action='store_true',
                        default=None, help='Enable logging')
    parser.add_argument('-f', '--force', action='store_true',
                        default=None, help='Overwrite existing files')
    parser.add_argument('-cf', '--config-file', type=str,
                        default='aocsetup.conf', help='Config file')
    parser.add_argument('-ic', '--ignore-config', action='store_true',
                        default=False, help='Ignores any existing config files')
    parser.add_argument('-sc', '--save-config', action='store_true',
                        default=False, help='Generates (default: aocsetup.conf) config file from current arguments')
    parser.add_argument('-sco', '--save-config-output', type=str,
                        default="aocsetup.conf", help='Generated config file output')

    args = parser.parse_args()
    args = process_args(args)

    if args.log:
        logging.basicConfig(level=logging.INFO)

    logging.info('arguments: {}'.format(args))

    if args.wait:
        args.year, args.day = wait()
    else:
        if args.day is None:
            if today.month != 12:
                print(
                    '''Error: Can't use current day because it's not december! Consider using -d <DAY>''')
                sys.exit(0)
            else:
                args.day = today.day
        if args.year is None:
            args.year = today.year
        
        if not 2015 <= args.year <= today.year:
            logging.info('year: {} out of acceptable range'.format(args.year))
            print('Invalid input: year has to be between 2015 and {}. (input was: {})'.format(
                today.year, args.year))
            sys.exit(0)

        if not 1 <= args.day <= 25:
            logging.info('day: {} out of acceptable range'.format(args.day))
            print(
                'Invalid input: there are 1-25 days in one AoC. (input was: {})'.format(args.day))
            sys.exit(0)

    write_input(args.input_output, args.session_cookie,
                args.year, args.day, args.force)
    write_template(args.src_template, args.src_output,
                   args.year, args.day, args.force)
    write_template(args.test_template, args.test_output,
                   args.year, args.day, args.force)

    logging.info('aocsetup done.')


if __name__ == "__main__":
    main()