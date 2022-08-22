#  Copyright 2022 VMware, Inc.
#  SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from vrops.object import Key, Object


def create_relationships(result, matcher):
    pass


def get_external_object(key: Key) -> Object | None:
    pass


def get_external_objects(adapter_type: str,
                         object_type: str,
                         name: str = None,
                         identifier_values: [KeyValue] = None,
                         property_values: [KeyValue] = None,
                         status=None) -> [Object]:
    adapter_type = [adapter_type]
    object_type = [object_type]
    name = name
    if identifier_values is None:
        identifier_values = []
    if property_values is None:
        property_values = []
    if status is None:
        status = [Status.DATA_RECEIVING]
    pass


class Status(Enum):
    NONE = 0
    ERROR = 1
    UNKNOWN = 2
    DOWN = 3
    DATA_RECEIVING = 4
    OLD_DATA_RECEIVING = 5
    NO_DATA_RECEIVING = 6
    NO_PARENT_MONITORING = 7
    COLLECTOR_DOWN = 8


class Matcher:
    def __init__(self,
                 adapter_type: str,
                 object_type: str,
                 name: str = None,
                 identifier: str = None,
                 prop: str = None
                 ):
        pass


@dataclass
class KeyValue:
    key: str
    value: str
