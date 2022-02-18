# ----------------------------------------------------------------------------------------------------------------------
#    FUNCTIONS
# ----------------------------------------------------------------------------------------------------------------------

import os
import datetime as dt
import logging
import numpy as np
import pandas as pd
import pulp 
import itertools

def loadData(filePath, sheetSets, sheetParams, sheetParamsDefault, sheetMcs, sheetMcsNum):

    """
    This function loads all data from the input data set to dataframes.
    """

    # Data: SETS
    sets_df = pd.read_excel(io=filePath, sheet_name=sheetSets)
    sets_df['REGION'] = sets_df['REGION'].astype(str)
    sets_df['REGION2'] = sets_df['REGION2'].astype(str)
    sets_df['DAYTYPE'] = sets_df['DAYTYPE'].astype(str)
    sets_df['EMISSION'] = sets_df['EMISSION'].astype(str)
    sets_df['FUEL'] = sets_df['FUEL'].astype(str)
    sets_df['DAILYTIMEBRACKET'] = sets_df['DAILYTIMEBRACKET'].astype(str)
    sets_df['SEASON'] = sets_df['SEASON'].astype(str)
    sets_df['TIMESLICE'] = sets_df['TIMESLICE'].astype(str)
    sets_df['MODE_OF_OPERATION'] = sets_df['MODE_OF_OPERATION'].astype(str)
    sets_df['STORAGE'] = sets_df['STORAGE'].astype(str)
    sets_df['TECHNOLOGY'] = sets_df['TECHNOLOGY'].astype(str)
    sets_df['YEAR'] = sets_df['YEAR'].astype(str)
    sets_df['FLEXIBLEDEMANDTYPE'] = sets_df['FLEXIBLEDEMANDTYPE'].astype(str)

    # Data: PARAMETERS
    df = pd.read_excel(io=filePath, sheet_name=sheetParams)
    df['PARAM'] = df['PARAM'].astype(str)
    df['VALUE'] = df['VALUE'].apply(pd.to_numeric, downcast='signed')
    df['REGION'] = df['REGION'].astype(str)
    df['REGION2'] = df['REGION2'].astype(str)
    df['DAYTYPE'] = df['DAYTYPE'].astype('Int64')
    df['DAYTYPE'] = df['DAYTYPE'].astype(str)
    df['EMISSION'] = df['EMISSION'].astype(str)
    df['FUEL'] = df['FUEL'].astype(str)
    df['DAILYTIMEBRACKET'] = df['DAILYTIMEBRACKET'].astype('Int64')
    df['DAILYTIMEBRACKET'] = df['DAILYTIMEBRACKET'].astype(str)
    df['SEASON'] = df['SEASON'].astype('Int64')
    df['SEASON'] = df['SEASON'].astype(str)
    df['TIMESLICE'] = df['TIMESLICE'].astype('Int64')
    df['TIMESLICE'] = df['TIMESLICE'].astype(str)
    df['MODE_OF_OPERATION'] = df['MODE_OF_OPERATION'].astype('Int64')
    df['MODE_OF_OPERATION'] = df['MODE_OF_OPERATION'].astype(str)
    df['STORAGE'] = df['STORAGE'].astype(str)
    df['TECHNOLOGY'] = df['TECHNOLOGY'].astype(str)
    df['YEAR'] = df['YEAR'].astype('Int64')
    
    # Data: Monte Carlo Simulation (MCS)
    mcs_df = pd.read_excel(io=filePath, sheet_name=sheetMcs)
    mcs_df['DEFAULT_SETTING'] = mcs_df['DEFAULT_SETTING'].apply(pd.to_numeric, downcast='signed')
    mcs_df['REL_SD'] = mcs_df['REL_SD'].astype('Int64')
    mcs_df['REL_MIN'] = mcs_df['REL_MIN'].astype('Int64')
    mcs_df['REL_MAX'] = mcs_df['REL_MAX'].astype('Int64')
    mcs_df['DISTRIBUTION'] = mcs_df['DISTRIBUTION'].astype(str)
    mcs_df['ARRAY'] = [[float(i) for i in str(x).split(",")] for x in mcs_df['ARRAY']]

    mcs_df['PARAM'] = mcs_df['PARAM'].astype(str)
    mcs_df['REGION'] = mcs_df['REGION'].astype(str)
    mcs_df['REGION2'] = mcs_df['REGION2'].astype(str)
    mcs_df['DAYTYPE'] = mcs_df['DAYTYPE'].astype('Int64')
    mcs_df['DAYTYPE'] = mcs_df['DAYTYPE'].astype(str)
    mcs_df['EMISSION'] = mcs_df['EMISSION'].astype(str)
    mcs_df['FUEL'] = mcs_df['FUEL'].astype(str)
    mcs_df['DAILYTIMEBRACKET'] = mcs_df['DAILYTIMEBRACKET'].astype('Int64')
    mcs_df['DAILYTIMEBRACKET'] = mcs_df['DAILYTIMEBRACKET'].astype(str)
    mcs_df['SEASON'] = mcs_df['SEASON'].astype('Int64')
    mcs_df['SEASON'] = mcs_df['SEASON'].astype(str)
    mcs_df['TIMESLICE'] = mcs_df['TIMESLICE'].astype(str)
    mcs_df['MODE_OF_OPERATION'] = mcs_df['MODE_OF_OPERATION'].astype('Int64')
    mcs_df['MODE_OF_OPERATION'] = mcs_df['MODE_OF_OPERATION'].astype(str)
    mcs_df['STORAGE'] = mcs_df['STORAGE'].astype(str)
    mcs_df['TECHNOLOGY'] = mcs_df['TECHNOLOGY'].astype(str)
    mcs_df['YEAR'] = mcs_df['YEAR'].astype('Int64')


    # Data: Parameters default values
    defaults_df = pd.read_excel(io=filePath, sheet_name=sheetParamsDefault)
    defaults_df = defaults_df.fillna(0)
    defaults_df['PARAM'] = defaults_df['PARAM'].astype(str)
    defaults_df['VALUE'] = defaults_df['VALUE'].apply(pd.to_numeric, downcast='signed')
    
    # Number of MCS simulations
    n_df = pd.read_excel(io=filePath, sheet_name=sheetMcsNum)
    n = n_df.at[0, 'MCS_num']
    
    return (sets_df, df, defaults_df, mcs_df, n)


def saveResultsToCSV(dataframe, fileDir, fileName):
    """
    This function saves all results to a CSV file.
    """
    _df = dataframe
    # Shorten abstract variable names
    _df['NAME'].replace(
        regex={'Total': 'Tot', 'Annual': 'Ann', 'Technology': 'Tech', 'Discounted': 'Disc', 'Production': 'Prod'},
        inplace=True)

    if not os.path.exists(fileDir):
        os.makedirs(fileDir)
        
    _df.to_csv(path_or_buf=os.path.join(fileDir, fileName), sep=',', index=False)
    return


def saveResultsToExcel(dataframe, fileDir, fileName):
    """
    This function saves all results to an Excel file.
    """
    _df = dataframe
    # Shorten abstract variable names to keep Excel worksheet name limit of 31 characters
    _df['NAME'].replace(
        regex={'Total': 'Tot', 'Annual': 'Ann', 'Technology': 'Tech', 'Discounted': 'Disc', 'Production': 'Prod', 'Emission': 'EM', 'Penalty': 'Pen'},
        inplace=True)

    dataframe_list = [_df[_df['NAME'] == str(name)] for name in _df['NAME'].unique()]

    if not os.path.exists(fileDir):
        os.makedirs(fileDir)

    writer = pd.ExcelWriter(os.path.join(fileDir, fileName))

    for d, name in zip(dataframe_list, _df['NAME'].unique()):
        d.to_excel(writer, sheet_name=name, index=False)

    writer.save()
    return

def createParameter(_df, _name):
    return _df[_df['PARAM'] == _name].set_index('INDEX').to_dict()['VALUE']


def createVariable(_name, _v):
    return newVarDict(_name, _v[_name]['lb'], _v[_name]['ub'], _v[_name]['cat'], _v[_name]['sets'])

def createTuple(_df, _set_name):
    if _set_name in ['DAYTYPE', 'DAILYTIMEBRACKET', 'SEASON', 'MODE_OF_OPERATION', 'YEAR', 'TIMESLICE']:
        return tuple([str(int(float(x))) for x in _df[_set_name] if x != 'nan'])
    else:
        return tuple([x for x in _df[_set_name] if x != 'nan'])

def permutateSets(_sets_list):
    """ Permutation of sets """
    return tuple(itertools.product(*_sets_list))


def ci(_tuple):
    """ Combine indices """
    return "-".join([str(i) for i in _tuple])


def newVarDict(_name, _lb, _ub, _cat, _sets):
    """
    This function create a dictionary for a variable having a lower bound (lb),
    upper bound (ub), category (cat), using combined indices from the SETS
    """
    return {ci(v): pulp.LpVariable(f"{_name}_" + ci(v), lowBound=_lb, upBound=_ub, cat=_cat)
            for v in permutateSets(_sets)}
    

def saveResultsTemporary(_model, _scenario_i, variables):
            """
            This function saves results from one simulation temporary.
            """

            df = pd.DataFrame()

            # Cost
            cost_df = pd.DataFrame(data={'NAME': ['Cost'],
                                         'VALUE': [_model.objective.value()],
                                         'INDICES': [[np.nan]],
                                         'ELEMENTS': [[np.nan]],
                                         'SCENARIO': [_scenario_i]
                                         })

            df = pd.concat([df, cost_df])

            # All other variables
            res = tuple([v for v in _model.variables() if v.name != "Cost" and v.name != "RateOfProductionByTechnologyByMode"])
            other_df = pd.DataFrame(data={'NAME': [v.name.split('_')[0] for v in res],
                                         'VALUE': [v.value() for v in res],
                                         'INDICES': [variables[str(v.name.split('_')[0])]['indices'] for v in res],
                                         'ELEMENTS': [v.name.split('_')[1:] for v in res],
                                         'SCENARIO': [_scenario_i for v in res]
                                         })

            df = pd.concat([df, other_df])
            df['REGION'] = [e[i.index('r')] if 'r' in i else np.nan for i, e in zip(df['INDICES'], df['ELEMENTS'])]
            df['REGION2'] = [e[i.index('rr')] if 'rr' in i else np.nan for i, e in zip(df['INDICES'], df['ELEMENTS'])]
            df['DAYTYPE'] = [e[i.index('ld')] if 'ld' in i else np.nan for i, e in zip(df['INDICES'], df['ELEMENTS'])]
            df['FUEL'] = [e[i.index('f')] if 'f' in i else np.nan for i, e in zip(df['INDICES'], df['ELEMENTS'])]
            df['EMISSION'] = [e[i.index('e')] if 'e' in i else np.nan for i, e in zip(df['INDICES'], df['ELEMENTS'])]
            df['DAILYTIMEBRACKET'] = [e[i.index('lh')] if 'lh' in i else np.nan for i, e in zip(df['INDICES'], df['ELEMENTS'])]
            df['SEASON'] = [e[i.index('ls')] if 'ls' in i else np.nan for i, e in zip(df['INDICES'], df['ELEMENTS'])]
            df['TIMESLICE'] = [e[i.index('l')] if 'l' in i else np.nan for i, e in zip(df['INDICES'], df['ELEMENTS'])]
            df['MODE_OF_OPERATION'] = [e[i.index('m')] if 'm' in i else np.nan for i, e in zip(df['INDICES'], df['ELEMENTS'])]
            df['STORAGE'] = [e[i.index('s')] if 's' in i else np.nan for i, e in zip(df['INDICES'], df['ELEMENTS'])]
            df['TECHNOLOGY'] = [e[i.index('t')] if 't' in i else np.nan for i, e in zip(df['INDICES'], df['ELEMENTS'])]
            df['YEAR'] = [e[i.index('y')] if 'y' in i else np.nan for i, e in zip(df['INDICES'], df['ELEMENTS'])]
            df.drop(columns={'INDICES', 'ELEMENTS'}, inplace=True)
            return df


def GIS_ExchangeCapacities(UseByTechnology, ProductionByTechnology):

        #ProductionByTechnology
        df = ProductionByTechnology
        df = df.drop(['NAME', 'STORAGE'], axis = 1)
        df = df.loc[df['FUEL'] == 'CONVHEAT']
        #df = df.loc[df['VALUE'] != 0]
        df.reset_index(drop=True, inplace=True)
        df3 = df.loc[df['YEAR'] == df['YEAR'].max()]
        df3.reset_index(drop=True, inplace=True)

        #UseByTechnology
        df1 = UseByTechnology
        df1 = df1.drop(['NAME', 'STORAGE'], axis = 1)
        df1 = df1.loc[df1['FUEL'] == 'DHWATER']
        #df1 = df1.loc[df1['VALUE'] != 0]
        df2 = df1.loc[df1['YEAR'] == df1['YEAR'].max()]
        df2.reset_index(drop=True, inplace=True)

        #Creating a combined data frame
        df4 = df3.append(df2, ignore_index=False)
        df4 = df4.drop(['FUEL'], axis = 1)
   
       #Changing to platform nomenclature - THIS MUST BE HASHED LATER 
#         Tech_list = df4['TECHNOLOGY'].tolist()
#         Assign = []
#         for x in Tech_list:
#             if "HEA" in x:
#                 Assign.append('Sink1_HEX')
#             elif "HEB" in x:
#                 Assign.append('Sink2_HEX')
#             elif "HEC" in x:
#                 Assign.append('Sink3_HEX')
#             elif "WHRB" in x:
#                 Assign.append('Source1_WHRB') 
#         df4['Assignment'] = Assign  
#         df4 = df4.drop(['TECHNOLOGY'], axis = 1)
#         df4 = df4[['VALUE', 'TIMESLICE', 'Assignment', 'YEAR']]
#         df4.rename(columns={'Assignment': 'TECHNOLOGY'}, inplace=True)

        #Source or Sink Aggregation
        Tech_list1 = df4['TECHNOLOGY'].tolist()
        Assign1 = []
        for x in Tech_list1:
            for i in range (1,500000):
                if (','.join(["Source%d" % i ])) in x:
                    Assign1.append(','.join(["Source%d" % i ]))
            for j in range (1,500000):
                if (','.join(["Sink%d" % j ])) in x:
                    Assign1.append(','.join(["Sink%d" % j ]))
        df4['Assignment'] = Assign1
        df4 = df4.drop(['TECHNOLOGY'], axis = 1)
        df4 = df4[['VALUE', 'TIMESLICE', 'Assignment', 'YEAR']]

        #Creating a Pivot Table
        table = pd.pivot_table(df4,index=['TIMESLICE'],columns=['Assignment'],values=['VALUE'],aggfunc=np.sum)

        #Sorting the Pivot Table
        sortedtable = table.reindex(table['VALUE'].sort_values(by=table.columns.droplevel(level = 0)[0], ascending=False).index)
        append_df = sortedtable.head(table['VALUE', table.columns.droplevel(level = 0)[0]].value_counts()[table['VALUE', table.columns.droplevel(level = 0)[0]].max()])
        for col_name in table.columns.droplevel(level = 0):
            sortedtable = table.reindex(table['VALUE'].sort_values(by=col_name, ascending=False).index)
            append_df = append_df.append(sortedtable.head(table['VALUE', col_name].value_counts()[table['VALUE', col_name].max()]))
        #a = (sortedtable.iloc[0])
        append_df1 = append_df.drop_duplicates()
        append_df1.index.name = None
        append_df1 = append_df1.transpose()


        #Creating classification
        append_df2 = append_df1.droplevel(level = 0)
        append_df2 = append_df2.reset_index()
        list1 = list(append_df2["Assignment"])

        list2 = []

        for x in list1:
            if "Sink" in x:
                list2.append('Sink')
            else:
                list2.append('Source')

        Classification_Type = pd.Series(list2)
        append_df2.insert(loc=1, column='Classification', value=Classification_Type)



        #Creating ID

        list4 = list(append_df2["Assignment"])

        list5 = []

        for x in list4:
            for i in range (1,100):
                if (','.join(["%d" % i ])) in x:
                    list5.append(','.join(["%d" % i ]))

        ID = pd.Series(list5)
        append_df2.insert(loc=0, column='ID', value=ID)
        append_df2.drop('Assignment', axis=1, inplace=True)

        return(append_df2)      
        
        
        
def CreateResults(res_df):

    Names_NZ = ['Cost', 'AccumulatedNewCapacity', 'AccumulatedNewStorageCapacity', 'AnnualVariableOperatingCost', 'AnnualFixedOperatingCost', 'AnnualTechnologyEmissionsPenalty', 'AnnualTechnologyEmission', 'NewCapacity', 'ProductionByTechnology', 'ProductionByTechnologyAnnual', 'StorageLevelTimesliceStart', 'StorageLosses', 'UseByTechnology']
    Results_NZ = pd.DataFrame()
    for name_nz in Names_NZ:
        Results_NZ = Results_NZ.append((res_df[res_df['NAME'] == str(name_nz)]))
    Results_NZ1 = Results_NZ.dropna(axis=1, how='all')
    Results_NZ2 = Results_NZ1.drop(['SCENARIO', 'REGION'], axis = 1)

    TEO_Results_NZ = {}
    for name in Results_NZ2['NAME'].unique():
        TEO_Results_NZ[name] = Results_NZ2[Results_NZ2['NAME'] == str(name)]
    
    ProductionByTechnology = TEO_Results_NZ['ProductionByTechnology']
    
    UseByTechnology = TEO_Results_NZ['UseByTechnology']
    
    del TEO_Results_NZ["UseByTechnology"]
    
    ex_capacities1 = GIS_ExchangeCapacities(UseByTechnology, ProductionByTechnology)
    
    ex_capacities = {'ex_capacities' : ex_capacities1}
    
    Names_z1 = ['DiscountedCapitalInvestmentByTechnology', 'DiscountedCapitalInvestmentByStorage', 'DiscountedSalvageValueByTechnology', 'DiscountedSalvageValueByStorage']
    
    
    Results_Z1 = pd.DataFrame()
    
    for name_z1 in Names_z1:
        Results_Z1 = Results_Z1.append((res_df[res_df['NAME'] == str(name_z1)])) 

    
    Results_Z2 = Results_Z1.dropna(axis=1, how='all')
    
    Results_Z3 = Results_Z2.drop(['SCENARIO', 'REGION'], axis = 1)


    TEO_Results_Z = {}
    
    for name_z1 in Names_z1:
        TEO_Results_Z[name_z1] = Results_Z3[Results_Z3['NAME'] == str(name_z1)]
        
    output = {**TEO_Results_NZ, **TEO_Results_Z, **ex_capacities}
    
    TEO_Results = {}
    
    for key in TEO_Results.keys():
        
        TEO_Results[key] = output[key].to_dict(orient = 'records')
    
    return(output)
