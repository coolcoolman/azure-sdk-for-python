# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class RegionCategory(str, Enum):
    """The category of the region.
    """

    recommended = "Recommended"
    other = "Other"

class RegionType(str, Enum):
    """The type of the region.
    """

    physical = "Physical"
    logical = "Logical"

class SpendingLimit(str, Enum):
    """The subscription spending limit.
    """

    on = "On"
    off = "Off"
    current_period_off = "CurrentPeriodOff"

class SubscriptionState(str, Enum):
    """The subscription state. Possible values are Enabled, Warned, PastDue, Disabled, and Deleted.
    """

    enabled = "Enabled"
    warned = "Warned"
    past_due = "PastDue"
    disabled = "Disabled"
    deleted = "Deleted"

class TenantCategory(str, Enum):
    """Category of the tenant.
    """

    home = "Home"
    projected_by = "ProjectedBy"
    managed_by = "ManagedBy"
