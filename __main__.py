"""Data Element Profiler main module,Argument -1 still needs to be passed."""

import configparser
import json
import logging
import click
import avro.schema
from typing import List, Sequence, TextIO, Tuple
from grp_bank_dq_engine_dindu.netezza import NetezzaClient
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import pathlib
from dataclasses import dataclass

logger = logging.getLogger(__name__)
logger.debug("debug logging initialized")

config = configparser.ConfigParser()
config.read('database_logins.ini')

SQL_DIR = pathlib.Path(__file__).parent / 'sql'
AVRO_DIR = pathlib.Path(__file__).parent / 'asset'


def do_our_task(connection, table: str) -> Sequence[Tuple[str, str]]:
    """Get all "*SK*" elements of `table` that are an int* type.

    yeild {columnname, datatype}
    """
    logger.debug('running query...')

    for _ in connection.sql(SQL_DIR / "_sk_column_name_type_int.sql",
                            dict(table=table)).itertuples():
        yield tuple(_)[1:]


@dataclass
class TableScanOutput:
    tablename: str
    elements: List[str]

    @property
    def _schema(self):
        """Output my avro schema.need to pass try except here of avro passing-sean."""

        return schema

    def __str__(self):
        """Stringify myself to a json object."""
        return json.dumps(dict(tablename=self.tablename, elements=self.elements))

    def _to_avro(self, tablename, elements):
        """Output my avro representation."""
        # return avro.write(self._schema, self)


@click.command()
@click.argument('input_file', type=click.File('r'))
def main(input_file: TextIO):
    """Run from the cli."""
    logger.debug(f'recieved {input_file}')
    # setup task from input
    args = dict(config[input_file.name])
    # connect to database
    client = NetezzaClient(**args)
    logger.debug(f'{client}')

    with client.connection as connection:
        logger.debug('connected to db')
        for table in input_file:
            table = table.rpartition('.')[-1].strip()
            logger.debug(f'processing {table}')
            sk_elements = do_our_task(connection, table)
            print(dict(tablename=table,
                       elements=[element_name for element_name, _ in
                                 sk_elements]))
            '''
            print(TableScanOutput(tablename=table,
                                  elements=[element_name for element_name, _ in
                                            sk_elements]))
            '''


main()
