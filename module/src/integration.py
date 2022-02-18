import json
from .TEO_Model import buildmodel
from .utilities import (
    create_parameters_dataframe,
    create_parameters_default_dataframe,
    create_sets_dataframe,
)
from .kb import kb


def run_build_model(input_data):

    sets_df, df, default_df = _prepare_inputs(input_data)

    model_output = buildmodel(sets_df, df, default_df, None, 0)

    return _prepare_outputs(model_output)


def _prepare_inputs(input_data):

    default_df = create_parameters_default_dataframe(kb["parameters_default"])
    sets_df = create_sets_dataframe(input_data["sets_df"])

    df = create_parameters_dataframe(sets_df, default_df)

    return sets_df, df, default_df


def _prepare_outputs(output_data):

    output = open("./output.json", "x")
    json.dump(output_data, output)

    return output_data
