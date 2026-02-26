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
        "ftp_folder": "pride/data/archive/2018/12/PXD009111/",
        "ftp_include_ext": [
            "Saci_Stavation_01.raw",
            "Saci_Stavation_02.raw",
            "Saci_Stavation_03.raw",
            "Saci_Stavation_04.raw",
            "Saci_Stavation_05.raw",
            "Saci_Stavation_06.raw",
            "Saci_Stavation_POOL-1.raw",
            "Saci_Stavation_POOL.raw",
            "Saci_Stavation_Pool_1-2.raw",
            "Saci_Stavation_Pool_3-4.raw",
            "Saci_Stavation_Pool_5-6.raw",
        ],
        "ftp_output_folder": "C:\\Users\\Admin\\Documents\\ProGlycProt_collab\\tutorial\\PXD009111",
    }
    if os.path.exists(params["ftp_output_folder"]) is False:
        print("Ceated folder: {0}".format(params["ftp_output_folder"]))
        os.mkdir(params["ftp_output_folder"])
    R = ursgal.UController(params=params)
    R.fetch_file(engine="get_ftp_files_1_0_0")
    return


if __name__ == "__main__":
    main()
