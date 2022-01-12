import json
import pandas as pd
import os

from ..src.TEO_Model import buildmodel
from ..src.utilities import create_parameters_dataframe, create_parameters_default_dataframe, create_sets_dataframe


def run_test():
    fdef = open(os.path.join(os.path.dirname(__file__),
                'json/parameters_default.json'), 'r')
    jsdef = json.load(fdef)

    default_df = create_parameters_default_dataframe(jsdef)

    fset = open(os.path.join(os.path.dirname(__file__),
                             'json/sets.json'), 'r')
    jsset = json.load(fset)

    sets_df = create_sets_dataframe(jsset)

    df = create_parameters_dataframe(sets_df, default_df)

    pd.set_option('display.max_rows', df.shape[0]+1)
    print("GENERATED PARAMETERS", df)

    # MCS and N are not needed
    # buildmodel(sets_df, df, default_df, None, 0)
