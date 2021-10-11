import argparse
import BAC0
import os
import pandas as pd
import sys


def get_bacnet_objects_props(addr):
    BAC0.log_level('silence')
    bacnet = BAC0.lite()

    # get device ID of controller in given IP address
    info = bacnet.whois(addr)
    if len(info) == 0:
        raise Exception("Could not find a BACnet controller " +
                        "on the specified address")

    # create device object
    dev = BAC0.device(info[0][0], info[0][1], bacnet, poll=0)

    # get points properties
    prop_list = [point.properties.asdict for point in dev.points]

    # apply some changes in the property list
    for prop in prop_list:
        prop['device'] = str(prop['device'])
        prop['address'] = int(prop['address'])
        prop['type_value'] = \
            BAC0.bacpypes.object.ObjectType.enumerations[prop['type']]
        prop['device_id'] = info[0][1]

    # return property list
    return prop_list


def save_bacnet_objects_props(var, file):
    df = pd.DataFrame(data=var, columns=["device", "device_id", "name",
        "type", "type_value", "address", "description", "units_state",
        "simulated", "overridden", "priority_array", "history_size",
        "bacnet_properties"])
    if file.endswith(".csv"):
        df.to_csv(file)
    else:
        df.to_excel(file)
    print("Saved information of", len(var), "objects to", file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=
        "Save properties of BACnet objects to a CSV or a spreadsheet file.")
    parser.add_argument('-f', '--file', required=True, help='output file')
    parser.add_argument('-a', '--address', required=True,
                        help='IP address of the BACnet device')
    args = parser.parse_args()

    try:
        data = get_bacnet_objects_props(args.address)
        save_bacnet_objects_props(data, args.file)
    except Exception as e:
        print("Error:", e)
