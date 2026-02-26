#!/usr/bin/env python3
# encoding: utf-8

import ursgal
import os


def main():
    """
    Downloads an example file from PRIDE

    usage:
        ./get_file_from_ftp_server_example.py


    This is an simple example which shows how to load data from a ftp server.


    """
    # from ftplib import FTP
    # ftp = FTP("ftp.pride.ebi.ac.uk")
    # ftp.login()
    # ftp.cwd('pride/data/archive/2020/06/PXD014877/')
    # ftp.retrlines('LIST')
    params = {
        "ftp_url": "ftp://ftp.pride.ebi.ac.uk",
        # 'ftp_login': 'PASS00269',
        # 'ftp_password': 'FI4645a',
        "ftp_folder": "pride/data/archive/2014/02/PXD000202",
        "ftp_include_ext": [
            "110224_OV3_P3_BH_HA_SACO_1_1.raw",
            "110224_OV3_P3_BH_HA_SACO_1_10.raw",
            "110224_OV3_P3_BH_HA_SACO_1_2.raw",
            "110224_OV3_P3_BH_HA_SACO_1_3.raw",
            "110224_OV3_P3_BH_HA_SACO_1_4.raw",
        ],
        "ftp_output_folder": "/Volumes/Pohlschroder_1/ArcPP/PXD000202",
    }
    if os.path.exists(params["ftp_output_folder"]) is False:
        print("Ceated folder: {0}".format(params["ftp_output_folder"]))
        os.mkdir(params["ftp_output_folder"])
    R = ursgal.UController(params=params)
    R.fetch_file(engine="get_ftp_files_1_0_0")
    return


if __name__ == "__main__":
    main()
