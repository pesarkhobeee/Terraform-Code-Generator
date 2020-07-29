#!/usr/bin/env python3

import argparse
import logging
import sys
import os
import yaml
from jinja2 import Environment, FileSystemLoader


def yaml_generator(args):
    """
    The code generator accept the path to a yaml config file,
    Then it will generate the yaml file with help of a Jinja2 template
    And at last it wil use the output directory to save the generated .tf file
    """

    if not os.path.exists(args.Source):
        raise Exception('The source file doesn\'t exist: {}'.format(args.Source))

    if not os.path.exists(args.Destination):
        raise Exception('The destination folder doesn\'t exist: {}'.format(args.Destination))

    config_data = yaml.load(open(args.Source), Loader=yaml.FullLoader)
    logging.info(config_data)
    env = Environment(
            loader = FileSystemLoader('./templates'),
            trim_blocks=True,
            lstrip_blocks=True)
    template = env.get_template('db_tmpl.py')
    return(template.render(identifiers=config_data))


def main(args):
    try:
        print(yaml_generator(args))
    except Exception as e:
        logging.critical("Fatal error hapend: {}".format(e))
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Source Destination")
    parser.add_argument(
        'Source', type=str,
        help='The configuration file location'
    )
    parser.add_argument(
        'Destination', type=str,
        help='The output directory for the generated .tf file'
    )
    parser.add_argument(
        '--log-level', type=str, default="WARNING",
        help='Set the logging level. Defaults to WARNING.'
    )
    parsed_args = parser.parse_args()
    logging.getLogger()
    logging.basicConfig(
        format='%(asctime)s %(levelname)s %(message)s',
        level=parsed_args.log_level,
        datefmt='%Y-%m-%dT%H:%M:%S%z')
    logging.info(
        "Starting with given arguments: {}".format(parsed_args)
    )
    main(parsed_args)
