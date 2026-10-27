from custom_components.edgeos.common.consts import DEFAULT_NAME
from custom_components.edgeos.common.enums import DeviceTypes
from custom_components.edgeos.data_processors.base_processor import BaseProcessor
from custom_components.edgeos.data_processors.device_processor import DeviceProcessor
from custom_components.edgeos.data_processors.interface_processor import (
    InterfaceProcessor,
)
from custom_components.edgeos.models.config_data import ConfigData
from custom_components.edgeos.models.edge_os_device_data import EdgeOSDeviceData

ROUTER_HOSTNAME = "router"
PARENT_DEVICE_ID = (DEFAULT_NAME, ROUTER_HOSTNAME)


def test_base_processor_device_info_uses_parent_device_id():
    processor = BaseProcessor(ConfigData())
    processor._hostname = ROUTER_HOSTNAME
    processor.processor_type = DeviceTypes.SYSTEM

    device_info = processor.get_device_info()

    assert device_info["via_device_id"] == PARENT_DEVICE_ID
    assert "via_device" not in device_info


def test_device_processor_device_info_uses_parent_device_id():
    processor = DeviceProcessor(ConfigData())
    processor._hostname = ROUTER_HOSTNAME
    processor._devices["00:11:22:33:44:55"] = EdgeOSDeviceData(
        "client", "192.0.2.2", "00:11:22:33:44:55", None, False
    )

    device_info = processor.get_device_info("00:11:22:33:44:55")

    assert device_info["via_device_id"] == PARENT_DEVICE_ID
    assert "via_device" not in device_info


def test_interface_processor_device_info_uses_parent_device_id():
    processor = InterfaceProcessor(ConfigData())
    processor._hostname = ROUTER_HOSTNAME

    device_info = processor.get_device_info("eth0")

    assert device_info["via_device_id"] == PARENT_DEVICE_ID
    assert "via_device" not in device_info
