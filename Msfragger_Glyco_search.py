#!/usr/bin/env python3.4
# encoding: utf-8

import ursgal
import os
import sys
import shutil
import glob


def main(database=None, file_folder=None):
    """
    Executes a search with MSFragger Glyco

    usage:
        ./simple_example_search.py <mzml_folder> <database>


    """
    uc = ursgal.UController(
        profile="QExactive+",
        params={
            "-xmx": "10g",
            "cpus": 4,
            "database": database,
            "enzyme": "trypsin",
            "modifications": [
                "M,opt,any,Oxidation",
                "*,opt,Prot-N-term,Acetyl",
                "C,fix,any,Carbamidomethyl",
            ],
            "csv_filter_rules": [
                ["Is decoy", "equals", "false"],
                ["PEP", "lte", 0.01],
            ],
            "precursor_mass_tolerance_minus": 10,
            "precursor_mass_tolerance_plus": 10,
            "precursor_mass_tolerance_unit": "ppm",
            "precursor_true_tolerance": 10,
            "frag_mass_tolerance": 20,
            "frag_mass_tolerance_unit": "ppm",
            "modifications_offsets": {
                "chemical_formulas": [],
                "masses": [
                    0,
                ],
                "glycans": list(
                    set(
                        [
                            "HexNAc(2)Hex(3)SQv(1)",
                            # "Hex(1)HexA(3)",
                            # "Hex(2)HexA(2)",
                        ]
                    )
                ),
                "unimods": [],
            },
            "modifications_y_ion_offsets": {
                "chemical_formulas": [],
                "masses": [
                    0,
                    # 203.07937,
                    # 406.15874,
                ],
                "glycans": [
                    # "HexNAc(1)",
                    # "HexNAc(2)",
                ],
                "unimods": [],
            },
            "diagnostic_fragments": {
                "chemical_formulas": [],
                "masses": [
                    0
                    # 204.086646,
                    # 186.076086,
                ],
                "glycans": [
                    # "HexNAc(1)"
                ],
                "unimods": [],
            },
            "calibrate_mass": True,
            "msfragger_labile_mode": "labile",
            "score_ion_list": ["b", "y"],
            "deltamass_allowed_residues": "N",
            "peptide_mapper_class_version": "UPeptideMapper_v4",
            "use_pyqms_for_mz_calculation": False,
            "use_spectrum_charge": False,
            "percolator_post_processing": "tdc",
        },
    )

    mzML_files = []
    for mzml in glob.glob(os.path.join("{0}".format(file_folder), "*.mzML")):
        mzML_files.append(mzml)

    result_file_list = []
    for ms_file in mzML_files:
        unified_search_result = uc.search(
            input_file=ms_file,
            engine="msfragger_3_0",
        )
        validated_file = uc.validate(
            input_file=unified_search_result,
            engine="percolator_3_4_0",
            force=False,
        )

        filtered_file = uc.execute_misc_engine(
            input_file=validated_file,
            engine="filter_csv",
        )
        result_file_list.append(filtered_file)

    merged_file = uc.execute_misc_engine(
        input_file=result_file_list,
        engine="merge_csv",
    )
    print(
        """
        All done.
    """
    )
    return


if __name__ == "__main__":
    main(database=sys.argv[2], file_folder=sys.argv[1])
