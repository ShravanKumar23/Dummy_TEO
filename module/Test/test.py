import json
import pandas as pd
import os

from .data.get_input_data import get_input_data
from ..src.TEO_Model import buildmodel
from ..src.utilities import (
    create_parameters_dataframe,
    create_parameters_default_dataframe,
    create_sets_dataframe,
)
from .prepare_inputs import *


def run_test():
    fdef = open(
        os.path.join(os.path.dirname(__file__), "json/parameters_default.json"), "r"
    )
    jsdef = json.load(fdef)
    input_data = get_input_data()

    # Start Module Prepare Input
    gis_module = input_data["gis-module"]
    cf_module = input_data["cf-module"]
    platform = input_data["platform"]

    default_df = create_parameters_default_dataframe(jsdef)
    jsset = platform["platform_sets"]
    jsset["TECHNOLOGY"] = cf_module["sets_technologies"]
    jsset["FUEL"] = cf_module["sets_fuels"]

    sets_df = create_sets_dataframe(jsset)

    df = create_parameters_dataframe(sets_df, default_df)

    df = prepare_inputs(sets_df, df, input_data)

    pd.set_option("display.max_rows", df.shape[0] + 1)
    print("GENERATED PARAMETERS", df)

    # MCS and N are not needed
    # buildmodel(sets_df, df, default_df, None, 0)
