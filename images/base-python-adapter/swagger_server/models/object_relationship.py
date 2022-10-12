# coding: utf-8

#  Copyright 2022 VMware, Inc.
#  SPDX-License-Identifier: Apache-2.0

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.object_key import ObjectKey  # noqa: F401,E501
from swagger_server import util


class ObjectRelationship(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, parent: ObjectKey=None, children: List[ObjectKey]=None, add: bool=True, clear_first: bool=True):  # noqa: E501
        """ObjectRelationship - a model defined in Swagger

        :param parent: The parent of this ObjectRelationship.  # noqa: E501
        :type parent: ObjectKey
        :param children: The children of this ObjectRelationship.  # noqa: E501
        :type children: List[ObjectKey]
        :param add: The add of this ObjectRelationship.  # noqa: E501
        :type add: bool
        :param clear_first: The clear_first of this ObjectRelationship.  # noqa: E501
        :type clear_first: bool
        """
        self.swagger_types = {
            'parent': ObjectKey,
            'children': List[ObjectKey],
            'add': bool,
            'clear_first': bool
        }

        self.attribute_map = {
            'parent': 'parent',
            'children': 'children',
            'add': 'add',
            'clear_first': 'clearFirst'
        }
        self._parent = parent
        self._children = children
        self._add = add
        self._clear_first = clear_first

    @classmethod
    def from_dict(cls, dikt) -> 'ObjectRelationship':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ObjectRelationship of this ObjectRelationship.  # noqa: E501
        :rtype: ObjectRelationship
        """
        return util.deserialize_model(dikt, cls)

    @property
    def parent(self) -> ObjectKey:
        """Gets the parent of this ObjectRelationship.


        :return: The parent of this ObjectRelationship.
        :rtype: ObjectKey
        """
        return self._parent

    @parent.setter
    def parent(self, parent: ObjectKey):
        """Sets the parent of this ObjectRelationship.


        :param parent: The parent of this ObjectRelationship.
        :type parent: ObjectKey
        """
        if parent is None:
            raise ValueError("Invalid value for `parent`, must not be `None`")  # noqa: E501

        self._parent = parent

    @property
    def children(self) -> List[ObjectKey]:
        """Gets the children of this ObjectRelationship.

        Collection of children for the current parent.  # noqa: E501

        :return: The children of this ObjectRelationship.
        :rtype: List[ObjectKey]
        """
        return self._children

    @children.setter
    def children(self, children: List[ObjectKey]):
        """Sets the children of this ObjectRelationship.

        Collection of children for the current parent.  # noqa: E501

        :param children: The children of this ObjectRelationship.
        :type children: List[ObjectKey]
        """

        self._children = children

    @property
    def add(self) -> bool:
        """Gets the add of this ObjectRelationship.

        If the value is true, then this relationship will be added to VMware Aria Operations Manager, if false, this relationship will be removed from VMware Aria Operations Manager.  # noqa: E501

        :return: The add of this ObjectRelationship.
        :rtype: bool
        """
        return self._add

    @add.setter
    def add(self, add: bool):
        """Sets the add of this ObjectRelationship.

        If the value is true, then this relationship will be added to VMware Aria Operations Manager, if false, this relationship will be removed from VMware Aria Operations Manager.  # noqa: E501

        :param add: The add of this ObjectRelationship.
        :type add: bool
        """

        self._add = add

    @property
    def clear_first(self) -> bool:
        """Gets the clear_first of this ObjectRelationship.

        If the value is true all children will be removed from the parent before adding this list.  # noqa: E501

        :return: The clear_first of this ObjectRelationship.
        :rtype: bool
        """
        return self._clear_first

    @clear_first.setter
    def clear_first(self, clear_first: bool):
        """Sets the clear_first of this ObjectRelationship.

        If the value is true all children will be removed from the parent before adding this list.  # noqa: E501

        :param clear_first: The clear_first of this ObjectRelationship.
        :type clear_first: bool
        """

        self._clear_first = clear_first
