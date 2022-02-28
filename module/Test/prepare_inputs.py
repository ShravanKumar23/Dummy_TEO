import json
import pandas as pd
import os
import itertools
import warnings
import numpy
import itertools

def prepare_inputs (sets_df, df, input_platform, input_gis, input_cf)
  
    import json
    import pandas as pd
    import os
    import itertools
    import warnings
    import numpy
    import itertools
    
    sets_df = sets_df
    df = df
    #GIS_LOSSES
    df555 = gis_module
    loss_list198 = df555['losses_in_kw'].tolist()
    df1 = df.loc[df['PARAM'] == 'GIS_Losses']
    a = loss_list198[0]
    Fuel_list1 = df1['FUEL'].tolist()
    Assign1 = []
    Fuel_list1

    for x in Fuel_list1:
            if (','.join(["sink"])) in x:
                Assign1.append(a)
            else:
                Assign1.append(0)

    Assign1            
    df1['Assignment'] = Assign1
    df1.drop('VALUE', axis=1, inplace=True)
    df1.rename(columns={'Assignment': 'VALUE'}, inplace=True)
    df1 = df1[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'GIS_Losses']
    df = df.reset_index(drop=True)
    df1 = df1.reset_index(drop=True)
    df = df.append(df1, ignore_index=True)

    #GISCAPITALCOSTS
    df556 = gis_module
    cost_list199 = df556['cost_in_kw'].tolist()
    df2 = df.loc[df['PARAM'] == 'CapitalCost']
    a = cost_list199[0]
    Tech_list2 = df2['TECHNOLOGY'].tolist()

    Assign1 = []

    for y in Tech_list2:
            if (','.join(["dhn"])) in y:
                Assign1.append(a)
            else:
                Assign1.append(0)

    Assign1            
    df2['Assignment'] = Assign1
    sum_column = df2["Assignment"] + df2["VALUE"]
    df2["SUM"] = sum_column
    df2
    df2.drop('VALUE', axis=1, inplace=True)
    df2.drop('Assignment', axis=1, inplace=True)
    df2.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df2 = df2[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'CapitalCost']
    df = df.reset_index(drop=True)
    df2 = df2.reset_index(drop=True)
    df = df.append(df2, ignore_index=True)

    #OAR
    df483 = technologies_cf
    Tech_list198 = df483['technology'].tolist()
    Value_list198 = df483['output'].tolist()
    Fuel_list198 = df483['output_fuel'].tolist()
    df3 = df.loc[df['PARAM'] == 'OutputActivityRatio']

    Tech_list3 = df3['TECHNOLOGY'].tolist()
    Tech_list3d = []

    for i in Tech_list3:
        if i not in Tech_list3d:
            Tech_list3d.append(i)

    Fuel_list3 = df3['FUEL'].tolist()
    Fuel_list3d = []

    for j in Fuel_list3:
        if j not in Fuel_list3d:
            Fuel_list3d.append(j)

    Year_list3 = df3['YEAR'].tolist()
    Year_list3d = []

    for k in Year_list3:
        if k not in Year_list3d:
            Year_list3d.append(k)


    MO_list3 = df3['MODE_OF_OPERATION'].tolist()
    MO_list3d = []

    for l in MO_list3:
        if l not in MO_list3d:
            MO_list3d.append(l)

    maxcounter2 = len(MO_list3d) * len(Year_list3d)
    Assign3 = []
    Assign3f = []
    Assign3t = []
    Assign3m = []
    Assign3y = []
    Counter = []
    CounterY = []

    for j in range(0,len(Tech_list198)):
        a3 = Value_list198[j]
        b3 = Tech_list198[j]
        c3 = Fuel_list198[j]      

        for x in Fuel_list3d:
            for w in MO_list3d:
                for y in Tech_list3d:
                     for z in Year_list3d:
                        Counterstring = str(str(x) + str(y))
                        if (b3) in y and (c3) in x and CounterY.count(Counterstring) < maxcounter2:
                            CounterY.append(Counterstring)
                            #print(str(str(x) + str(y)))
                            Assign3.append(a3)
                            Assign3f.append(x)
                            Assign3m.append(w)
                            Assign3t.append(y)
                            Assign3y.append(z)
                        elif(b3 not in y and c3 not in x) and (x not in Tech_list198 and y not in Fuel_list198) and (Counter.count(Counterstring) < maxcounter2):      
                            #print(str(str(x) + str(y)))
                            Assign3.append(0)
                            Assign3f.append(x)
                            Assign3m.append(w)
                            Assign3t.append(y)
                            Assign3y.append(z)
                        elif(b3 in y and c3 not in x) and (x not in Tech_list198 and y not in Fuel_list198) and Counter.count(Counterstring) < maxcounter2:
                            #print(str(str(x) + str(y)))
                            Assign3.append(0)
                            Assign3f.append(x)
                            Assign3m.append(w)
                            Assign3t.append(y)
                            Assign3y.append(z)
                        elif(b3 not in y and c3 in x) and (Fuel_list198.count(y) == 1) and (x not in Tech_list198) and (y not in Fuel_list198) and Counter.count(Counterstring) < maxcounter2:
                            #print(str(str(x) + str(y)))
                            Assign3.append(0)
                            Assign3f.append(x)
                            Assign3m.append(w)
                            Assign3t.append(y)
                            Assign3y.append(z)
                        Counter.append(Counterstring)
    len(Assign3)
    df3['Assignment'] = Assign3
    df3['Assignmentf'] = Assign3f
    df3['Assignmentm'] = Assign3m
    df3['Assignmentt'] = Assign3t
    df3['Assignmenty'] = Assign3y
    df3
    sum_column = df3["Assignment"] + df3["VALUE"]
    df3["SUM"] = sum_column
    df3.drop('VALUE', axis=1, inplace=True)
    df3.drop('TECHNOLOGY', axis=1, inplace=True)
    df3.drop('MODE_OF_OPERATION', axis=1, inplace=True)
    df3.drop('YEAR', axis=1, inplace=True)
    df3.drop('FUEL', axis=1, inplace=True)
    df3.drop('Assignment', axis=1, inplace=True)
    df3.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df3.rename(columns={'Assignmentf': 'FUEL'}, inplace=True)
    df3.rename(columns={'Assignmentm': 'MODE_OF_OPERATION'}, inplace=True)
    df3.rename(columns={'Assignmentt': 'TECHNOLOGY'}, inplace=True)
    df3.rename(columns={'Assignmenty': 'YEAR'}, inplace=True)
    df3 = df3[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df3 = df3.reset_index(drop=True)
    df3
    df = df.loc[df['PARAM'] != 'OutputActivityRatio']
    df = df.reset_index(drop=True)
    df = df.append(df3, ignore_index=True)
    df

    #IAR
    df482 = technologies_cf
    Tech_list197 = df482['technology'].tolist()
    Value_list197 = df482['input'].tolist()
    Fuel_list197 = df482['input_fuel'].tolist()
    df4 = df.loc[df['PARAM'] == 'InputActivityRatio']


    Tech_list4 = df4['TECHNOLOGY'].tolist()
    Tech_list4d = []

    for i in Tech_list4:
        if i not in Tech_list4d:
            Tech_list4d.append(i)

    Fuel_list4 = df4['FUEL'].tolist()
    Fuel_list4d = []

    for j in Fuel_list4:
        if j not in Fuel_list4d:
            Fuel_list4d.append(j)

    Year_list4 = df4['YEAR'].tolist()
    Year_list4d = []

    for k in Year_list4:
        if k not in Year_list4d:
            Year_list4d.append(k)


    MO_list4 = df4['MODE_OF_OPERATION'].tolist()
    MO_list4d = []

    for l in MO_list4:
        if l not in MO_list4d:
            MO_list4d.append(l)

    maxcounter1 = len(MO_list4d) * len(Year_list4d)

    Assign4 = []
    Assign4f = []
    Assign4t = []
    Assign4m = []
    Assign4y = []
    Counter = []

    for j in range(0,len(Tech_list197)):

        a4 = Value_list197[j]
        b4 = Tech_list197[j]
        c4 = Fuel_list197[j]
        #Counterstring = str(str(b4) + str(c4))


        for x in Fuel_list4d:
            for w in MO_list4d:
                for y in Tech_list4d:
                     for z in Year_list4d:   
                        Counterstring = str(str(x) + str(y))    
                        if b4 in y and c4 in x: 
                            Assign4.append(a4)
                            Assign4f.append(x)
                            Assign4m.append(w)
                            Assign4t.append(y)
                            Assign4y.append(z)
                        elif(b4 not in y and c4 not in x) and Counter.count(Counterstring) < maxcounter1:      
                            # print(str(str(x) + str(y)))
                            Assign4.append(0)
                            Assign4f.append(x)
                            Assign4m.append(w)
                            Assign4t.append(y)
                            Assign4y.append(z)
                        elif(b4 in y and c4 not in x) and Counter.count(Counterstring) < maxcounter1:
                            Assign4.append(0)
                            Assign4f.append(x)
                            Assign4m.append(w)
                            Assign4t.append(y)
                            Assign4y.append(z)
                        elif(b4 not in y and c4 in x) and (Fuel_list198.count(y) == 1) and Counter.count(Counterstring) < maxcounter2:
                            #print(str(str(x) + str(y)))
                            Assign4.append(0)
                            Assign4f.append(x)
                            Assign4m.append(w)
                            Assign4t.append(y)
                            Assign4y.append(z)
                        Counter.append(Counterstring)
    len(Assign4)
    df4['Assignment'] = Assign4
    df4['Assignmentf'] = Assign4f
    df4['Assignmentm'] = Assign4m
    df4['Assignmentt'] = Assign4t
    df4['Assignmenty'] = Assign4y
    sum_column = df4["Assignment"] + df4["VALUE"]
    df4["SUM"] = sum_column
    df4.drop('VALUE', axis=1, inplace=True)
    df4.drop('TECHNOLOGY', axis=1, inplace=True)
    df4.drop('MODE_OF_OPERATION', axis=1, inplace=True)
    df4.drop('YEAR', axis=1, inplace=True)
    df4.drop('FUEL', axis=1, inplace=True)
    df4.drop('Assignment', axis=1, inplace=True)
    df4.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df4.rename(columns={'Assignmentf': 'FUEL'}, inplace=True)
    df4.rename(columns={'Assignmentm': 'MODE_OF_OPERATION'}, inplace=True)
    df4.rename(columns={'Assignmentt': 'TECHNOLOGY'}, inplace=True)
    df4.rename(columns={'Assignmenty': 'YEAR'}, inplace=True)
    df4 = df4[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df4 = df4.reset_index(drop=True)
    df = df.loc[df['PARAM'] != 'InputActivityRatio']
    df = df.reset_index(drop=True)
    df = df.append(df4, ignore_index=True)


    #CFCAPITALCOSTS
    import itertools
    df482 = technologies_cf
    Tech_list197 = df482['technology'].tolist()
    Value_list197 = df482['turnkey_a'].tolist()
    Assign5 = []
    df5 = df.loc[df['PARAM'] == 'CapitalCost']
    df5
    Tech_list5 = df5['TECHNOLOGY'].tolist()
    Tech_list5

    Year_list5 = df5['YEAR'].tolist()
    Year_list5d = []

    for i in Year_list5:
        if i not in Year_list5d:
            Year_list5d.append(i)

    for j in range(0,len(Tech_list197)):

        a5 =  Value_list197[j]

        b5 = Tech_list197[j]

        for y in Tech_list5:
                if str(b5) in y:
                    Assign5.append(a5)
                else:
                    Assign5.append(0)
    Assign5             
    chunked_list = list()
    chunk_size = len(Year_list5d)
    for i in range(0, len(Assign5), chunk_size):
        chunked_list.append(Assign5[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign5 = list(itertools.chain(*chunked_list1))
    Assign5
    df5['Assignment'] = Assign5
    sum_column = df5["Assignment"] + df5["VALUE"]
    df5["SUM"] = sum_column
    df5.drop('VALUE', axis=1, inplace=True)
    df5.drop('Assignment', axis=1, inplace=True)
    df5.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df5 = df5[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'CapitalCost']
    df = df.reset_index(drop=True)
    df5 = df5.reset_index(drop=True)
    df = df.append(df5, ignore_index=True)

    #CFFIXEDCOSTS
    df481 = technologies_cf
    Tech_list196 = df481['technology'].tolist()
    Value_list196 = df481['om_fix'].tolist()
    Assign6 = []
    df6 = df.loc[df['PARAM'] == 'FixedCost']

    Tech_list6 = df6['TECHNOLOGY'].tolist()
    Tech_list6

    Year_list6 = df6['YEAR'].tolist()
    Year_list6d = []

    for i in Year_list6:
        if i not in Year_list6d:
            Year_list6d.append(i)

    for j in range(0,len(Tech_list196)):

        a6 =  Value_list196[j]

        b6 = Tech_list196[j]

        for y in Tech_list6:
                if str(b6) in y:
                    Assign6.append(a6)
                else:
                    Assign6.append(0)

    chunked_list = list()
    chunk_size = len(Year_list6d)
    for i in range(0, len(Assign6), chunk_size):
        chunked_list.append(Assign6[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign6 = list(itertools.chain(*chunked_list1))
    df6['Assignment'] = Assign6
    sum_column = df6["Assignment"] + df6["VALUE"]
    df6["SUM"] = sum_column
    df6.drop('VALUE', axis=1, inplace=True)
    df6.drop('Assignment', axis=1, inplace=True)
    df6.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df6 = df6[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'FixedCost']
    df = df.reset_index(drop=True)
    df6 = df6.reset_index(drop=True)
    df = df.append(df6, ignore_index=True)


    #CFMAXCAPACITY
    df480 = technologies_cf
    Tech_list196 = df480['technology'].tolist()
    Tech_list196
    Value_list196 = df480['max_capacity'].tolist()
    Assign7 = []
    df7 = df.loc[df['PARAM'] == 'TotalAnnualMaxCapacity']

    Tech_list7 = df7['TECHNOLOGY'].tolist()
    Tech_list7

    Year_list7 = df7['YEAR'].tolist()
    Year_list7d = []

    for i in Year_list7:
        if i not in Year_list7d:
            Year_list7d.append(i)

    for j in range(0,len(Tech_list196)):

        a7 = -99999 + Value_list196[j]
        b7 = Tech_list196[j]

        for y in Tech_list7:
                if str(b7) in y:
                    Assign7.append(a7)
                else:
                    Assign7.append(0)

    chunked_list = list()
    chunk_size = len(Year_list7d)
    for i in range(0, len(Assign7), chunk_size):
        chunked_list.append(Assign7[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign7 = list(itertools.chain(*chunked_list1))
    df7['Assignment'] = Assign7
    sum_column = df7["Assignment"] + df7["VALUE"]
    df7["SUM"] = sum_column
    df7.drop('VALUE', axis=1, inplace=True)
    df7.drop('Assignment', axis=1, inplace=True)
    df7.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df7 = df7[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'TotalAnnualMaxCapacity']
    df = df.reset_index(drop=True)
    df7 = df7.reset_index(drop=True)
    df = df.append(df7, ignore_index=True)

    #CFVARCOST
    df490 = technologies_cf
    Tech_list198 = df490['technology'].tolist()
    Value_list198 = df490['om_var'].tolist()
    Assign7 = []
    df8 = df.loc[df['PARAM'] == 'VariableCost']

    Tech_list8 = df8['TECHNOLOGY'].tolist()
    Tech_list8d = []

    for i in Tech_list8:
        if i not in Tech_list8d:
            Tech_list8d.append(i)


    Year_list8 = df8['YEAR'].tolist()
    Year_list8d = []

    for k in Year_list8:
        if k not in Year_list8d:
            Year_list8d.append(k)


    MO_list8 = df8['MODE_OF_OPERATION'].tolist()
    MO_list8d = []
    Assign8 = []

    for l in MO_list8:
        if l not in MO_list8d:
            MO_list8d.append(l)

    for j in range(0,len(Tech_list198)):

        a8 = Value_list198[j]
        b8 = Tech_list198[j]

        for w in MO_list8d:
            for y in Tech_list8d:
                for z in Year_list8d:
                        if (b8) in y :  
                            Assign8.append(a8)
                        else:
                            Assign8.append(0)    

    Assign8
    chunked_list = list()
    chunk_size = len(Year_list8d)
    for i in range(0, len(Assign8), chunk_size):
        chunked_list.append(Assign8[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()

    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1
    Assign8 = list(itertools.chain(*chunked_list1))
    df8['Assignment'] = Assign8
    sum_column = df8["Assignment"] + df8["VALUE"]
    df8["SUM"] = sum_column
    df8.drop('VALUE', axis=1, inplace=True)
    df8.drop('Assignment', axis=1, inplace=True)
    df8.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df8 = df8[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'VariableCost']
    df = df.reset_index(drop=True)
    df8 = df8.reset_index(drop=True)
    df = df.append(df8, ignore_index=True)


    #EmissionsAR
    df491 = technologies_cf
    EM_list199 = df491['emissions']
    Value_list199 = df491['emissions_factor'].tolist()
    Tech_list199 = df491['technology'].tolist()
    Assign9 = []
    df9 = df.loc[df['PARAM'] == 'EmissionActivityRatio']
    Tech_list9 = df9['TECHNOLOGY'].tolist()
    Tech_list9d = []

    for i in Tech_list9:
        if i not in Tech_list9d:
            Tech_list9d.append(i)

    Emission_list9 = df9['EMISSION'].tolist()
    Emission_list9d = []

    for j in Emission_list9:
        if j not in Emission_list9d:
            Emission_list9d.append(j)

    Year_list9 = df9['YEAR'].tolist()
    Year_list9d = []

    for k in Year_list9:
        if k not in Year_list9d:
            Year_list9d.append(k)


    MO_list9 = df9['MODE_OF_OPERATION'].tolist()
    MO_list9d = []

    for l in MO_list9:
        if l not in MO_list9d:
            MO_list9d.append(l)

    for j in range(0,len(Tech_list198)):

        a9 = Value_list199[j]
        b9 = Tech_list199[j]
        c9 = EM_list199[j]

        for x in Emission_list9d:
            for w in MO_list9d:
                for y in Tech_list9d:
                    for z in Year_list9d:
                        if (b9) in y and c9 in x:  
                            Assign9.append(a9)
                        else:
                            Assign9.append(0)    

    Assign9
    len(Assign9)
    chunked_list = list()
    chunk_size = len(Year_list9d)
    for i in range(0, len(Assign9), chunk_size):
        chunked_list.append(Assign9[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign9 = list(itertools.chain(*chunked_list1))
    Assign9
    len(Assign9)
    df9['Assignment'] = Assign9
    sum_column = df9["Assignment"] + df9["VALUE"]
    df9["SUM"] = sum_column
    df9
    df9.drop('VALUE', axis=1, inplace=True)
    df9.drop('Assignment', axis=1, inplace=True)
    df9.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df9 = df9[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'EmissionActivityRatio']
    df = df.reset_index(drop=True)
    df9 = df9.reset_index(drop=True)
    df = df.append(df9, ignore_index=True)

    #SpecifiedAnnualDemand
    df472 = specified_annual_demand_cf
    Fuel_list177 = df472['fuel'].tolist()
    Value_list177 = df472['value'].tolist()
    Assign10 = []
    df10 = df.loc[df['PARAM'] == 'SpecifiedAnnualDemand']
    df10
    Fuel_list10 = df10['FUEL'].tolist()
    Year_list10 = df10['YEAR'].tolist()
    Year_list10d = []
    for i in Year_list10:
        if i not in Year_list10d:
            Year_list10d.append(i)
    for j in range(0,len(Fuel_list177)):

        a10 = 0.001 + Value_list177[j]
        b10 = Fuel_list177[j]

        for y in Fuel_list10:
                if b10 in y:
                    Assign10.append(a10)
                else:
                    Assign10.append(0)
    Assign10

    chunked_list = list()
    chunk_size = len(Year_list10d)
    for i in range(0, len(Assign10), chunk_size):
        chunked_list.append(Assign10[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()

    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign10 = list(itertools.chain(*chunked_list1))
    # a = len(df10) - len(Assign101)
    # listdummy = []
    # for i in range (1,a+1):
    #     listdummy.append(0)
    # listdummy
    # Assign10 = listdummy + Assign101
    # len(Assign10)
    df10['Assignment'] = Assign10
    sum_column = df10["Assignment"] + df10["VALUE"]
    df10["SUM"] = sum_column
    df10.drop('VALUE', axis=1, inplace=True)
    df10.drop('Assignment', axis=1, inplace=True)
    df10.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df10 = df10[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'SpecifiedAnnualDemand']
    df = df.reset_index(drop=True)
    df10 = df10.reset_index(drop=True)
    df = df.append(df10, ignore_index=True)

    #SpecifiedDemandProfile
    import numpy as np
    #Profile preparation
    df499 = specified_demand_profile_cf
    df499.columns
    Fuel_list177 = df499.columns.tolist()
    Fuel_list177
    df11 = df.loc[df['PARAM'] == 'SpecifiedDemandProfile']
    Fuel_list11 = df11['FUEL'].tolist()
    Fuel_list11d = []
    Counter = []
    for j in Fuel_list11:
        if j not in Fuel_list11d:
            Fuel_list11d.append(j)


    TS_list11 = df11['TIMESLICE'].tolist()
    TS_list11d = []

    for j in TS_list11:
        if j not in TS_list11d:
            TS_list11d.append(j)

    Year_list11 = df11['YEAR'].tolist()
    Year_list11d = []

    for k in Year_list11:
        if k not in Year_list11d:
            Year_list11d.append(k)

    maxcounter11 = len(TS_list11d) * len(Year_list11d)
    maxcounter11
    Assign11 = []
    Assign11f = []
    Assign11t = []
    Assign11y = []
    for j in range(0,len(Fuel_list177)):
        df1 = pd.DataFrame(df499[str(Fuel_list177[j])])
        assign = []
        Timeslice = 48
        split = (Timeslice / 24)
        Marker = 8761 / (split)
        assign99 = []

        for k in range(1,8761):
            i = (k / Marker) + 1
            assign99.append(int(i))

        df1['Marker'] = assign99


        assign999 = []
        for l in range(1,366):
            for i in range (1,25):
                assign999.append(int(i))

        df1['HourMarker'] = assign999
        table = pd.pivot_table(df1,index=['HourMarker'],columns=['Marker'],values=[str(Fuel_list177[j])],aggfunc=np.sum)

        table.columns = table.columns.droplevel(0)
        table.index.name = None

        cols = [table[col].squeeze() for col in table]
        cols = pd.concat(cols, ignore_index=True)
        cols

        b11 = Fuel_list177[j]

        for x in Fuel_list11d:
            for y in TS_list11d:
                for z in Year_list11d:
                    Counterstring = str(x)   
                    if b11 in x: 
                            Assign11.append(cols[(int(y))-1])
                            Assign11f.append(x)
                            Assign11t.append(y)
                            Assign11y.append(z)
                    elif(b11 not in x) and ('sink' not in x)  and Counter.count(Counterstring) < maxcounter11:      
                            # print(str(str(x) + str(y)))
                            Assign11.append(0)
                            Assign11f.append(x)
                            Assign11t.append(y)
                            Assign11y.append(z)
                    Counter.append(Counterstring) 

    Assign11
    len(Assign11)
    df11['Assignment'] = Assign11
    df11['Assignmentf'] = Assign11f
    df11['Assignmentt'] = Assign11t
    df11['Assignmenty'] = Assign11y
    sum_column = df11["Assignment"] + df11["VALUE"]
    df11["SUM"] = sum_column
    df11.drop('VALUE', axis=1, inplace=True)
    df11.drop('TIMESLICE', axis=1, inplace=True)
    df11.drop('YEAR', axis=1, inplace=True)
    df11.drop('FUEL', axis=1, inplace=True)
    df11.drop('Assignment', axis=1, inplace=True)
    df11.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df11.rename(columns={'Assignmentf': 'FUEL'}, inplace=True)
    df11.rename(columns={'Assignmentt': 'TIMESLICE'}, inplace=True)
    df11.rename(columns={'Assignmenty': 'YEAR'}, inplace=True)
    df11 = df11[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df11 = df11.reset_index(drop=True)
    df11
    df = df.loc[df['PARAM'] != 'SpecifiedDemandProfile']
    df = df.reset_index(drop=True)
    df = df.append(df11, ignore_index=True)


    #CapacityFactor
    import numpy as np
    import pandas as pd
    df500 = capacity_factor_cf
    Tech_list177 = df500.columns.tolist()
    Tech_list177

    #Profile prepearation

    df12 = df.loc[df['PARAM'] == 'CapacityFactor']


    Tech_list12 = df12['TECHNOLOGY'].tolist()
    Tech_list12d = []

    for i in Tech_list12:
        if i not in Tech_list12d:
            Tech_list12d.append(i)
    Tech_list12d        
    TS_list12 = df12['TIMESLICE'].tolist()
    TS_list12d = []

    for l in TS_list12:
        if l not in TS_list12d:
            TS_list12d.append(l)

    Year_list12 = df12['YEAR'].tolist()
    Year_list12d = []

    for k in Year_list12:
        if k not in Year_list12d:
            Year_list12d.append(k)

    maxcounter12 = len(TS_list12d) * len(Year_list12d)
    maxcounter12
    Assign12 = []
    Assign12ts = []
    Assign12t = []
    Assign12y = []
    assign1 = []
    Counter = []
    for j in range(0,len(Tech_list177)): 
        df2 =  pd.DataFrame(df500[str(Tech_list177[j])])
        Timeslice1 = 48
        split1 = (Timeslice1 / 24)
        Marker1 = 8761 / (split1)
        assign991 = []

        for l in range(1,8761):
                i = (l / Marker1) + 1
                assign991.append(int(i))

        df2['Marker'] = assign991
        assign9991 = []
        for k in range(1,366):
            for i in range (1,25):
                assign9991.append(int(i))

        df2['HourMarker'] = assign9991
        table1 = pd.pivot_table(df2,index=['HourMarker'],columns=['Marker'],values=[str(Tech_list177[j])],aggfunc=np.mean)

        table1.columns = table1.columns.droplevel(0)
        table1.index.name = None

        cols1 = [table1[col].squeeze() for col in table1]
        cols1 = pd.concat(cols1, ignore_index=True)

    # Writing dataframe

        b12 = str(Tech_list177[j])
        a12 = -1

        for x in Tech_list12d:
            for y in TS_list12d:
                for z in Year_list12d:
                    Counterstring = str(x)   
                    if b12 in x: 
                            Assign12.append(cols1[(int(y))-1] + a12)
                            Assign12t.append(x)
                            Assign12ts.append(y)
                            Assign12y.append(z)
                    elif(b12 not in x) and (x not in Tech_list177) and Counter.count(Counterstring) < maxcounter12:      
                            Assign12.append(0)
                            Assign12t.append(x)
                            Assign12ts.append(y)
                            Assign12y.append(z)
                    Counter.append(Counterstring)     

    Assign12
    len(df12)
    df12['Assignment'] = Assign12
    df12['Assignmentt'] = Assign12t
    df12['Assignmentts'] = Assign12ts
    df12['Assignmenty'] = Assign12y
    sum_column = df12["Assignment"] + df12["VALUE"]
    df12["SUM"] = sum_column
    df12.drop('VALUE', axis=1, inplace=True)
    df12.drop('TIMESLICE', axis=1, inplace=True)
    df12.drop('TECHNOLOGY', axis=1, inplace=True)
    df12.drop('YEAR', axis=1, inplace=True)
    df12.drop('Assignment', axis=1, inplace=True)
    df12.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df12.rename(columns={'Assignmentt': 'TECHNOLOGY'}, inplace=True)
    df12.rename(columns={'Assignmentts': 'TIMESLICE'}, inplace=True)
    df12.rename(columns={'Assignmenty': 'YEAR'}, inplace=True)
    df12 = df12[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df12 = df12.reset_index(drop=True)
    df12
    df = df.loc[df['PARAM'] != 'CapacityFactor']
    df = df.reset_index(drop=True)
    df = df.append(df12, ignore_index=True)
    df

    #PLATFORMAVAILABILITYFACTOR
    df472 = platform_technologies
    Tech_list173 = df472['technology'].tolist()
    Value_list173 = df472['availability_factor'].tolist()
    Assign13 = []
    df13 = df.loc[df['PARAM'] == 'AvailabilityFactor']
    Tech_list13 = df13['TECHNOLOGY'].tolist()

    Year_list13 = df13['YEAR'].tolist()
    Year_list13d = []
    for i in Year_list13:
        if i not in Year_list13d:
            Year_list13d.append(i)
    for j in range(0,len(Tech_list173)):

        a13 = -1 + int(Value_list173[j])
        Tech_list13
        b13 = Tech_list173[j]
        for y in Tech_list13:
                if str(b13) in y:
                    Assign13.append(a13)
                else:
                    Assign13.append(0)

                    chunked_list = list()
    chunk_size = len(Year_list13d)
    for i in range(0, len(Assign13), chunk_size):
        chunked_list.append(Assign13[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()

    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign13 = list(itertools.chain(*chunked_list1))

    Assign13
    len(Assign13)
    df13['Assignment'] = Assign13
    sum_column = df13["Assignment"] + df13["VALUE"]
    df13["SUM"] = sum_column
    df13.drop('VALUE', axis=1, inplace=True)
    df13.drop('Assignment', axis=1, inplace=True)
    df13.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df13 = df13[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'AvailabilityFactor']
    df = df.reset_index(drop=True)
    df13 = df13.reset_index(drop=True)
    df = df.append(df13, ignore_index=True)

    #PLATFORMCAPITALCOSTSTORAGE
    df475 = platform_storages
    Sto_list175 = df475['storage'].tolist()

    Value_list175 = df475['capital_cost_storage'].tolist()

    Assign14 = []

    df14 = df.loc[df['PARAM'] == 'CapitalCostStorage']

    Sto_list14 = df14['STORAGE'].tolist()
    Sto_list14

    Year_list14 = df14['YEAR'].tolist()
    Year_list14d = []

    for i in Year_list14:
        if i not in Year_list14d:
            Year_list14d.append(i)

    for j in range(0,len(Sto_list175)):

        a14 = Value_list175[j]

        b14 = Sto_list175[j]

        for y in Sto_list14:
                if b14 in y:
                    Assign14.append(a14)
                else:
                    Assign14.append(0)

    Assign14                
    chunked_list = list()
    chunk_size = len(Year_list14d)
    for i in range(0, len(Assign14), chunk_size):
        chunked_list.append(Assign14[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign14 = list(itertools.chain(*chunked_list1))
    df14['Assignment'] = Assign14
    sum_column = df14["Assignment"] + df14["VALUE"]
    df14["SUM"] = sum_column
    df14.drop('VALUE', axis=1, inplace=True)
    df14.drop('Assignment', axis=1, inplace=True)
    df14.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df14 = df14[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'CapitalCostStorage']
    df = df.reset_index(drop=True)
    df14 = df14.reset_index(drop=True)
    df = df.append(df14, ignore_index=True)

    #PLATFORMDISCOUNTRATETECH
    df472 = platform_technologies
    Tech_list173 = df472['technology'].tolist()

    Value_list173 = df472['discount_rate_tech'].tolist()
    Assign15 = []
    df15 = df.loc[df['PARAM'] == 'DiscountRateTech']

    Year_list15 = df15['YEAR'].tolist()
    Year_list15d = []

    for i in Year_list15:
        if i not in Year_list15d:
            Year_list15d.append(i)

    for j in range(0,len(Tech_list173)):

        a15 = -0.05 + Value_list173[j]
        Tech_list15 = df15['TECHNOLOGY'].tolist()
        Tech_list15
        b15 = Tech_list173[j]

        Tech_list15 = df15['TECHNOLOGY'].tolist()

        for y in Tech_list15:
            if str(b15) in y:
                Assign15.append(a15)
            else:
                Assign15.append(0)

            chunked_list = list()
    chunk_size = len(Year_list15d)
    for i in range(0, len(Assign15), chunk_size):
        chunked_list.append(Assign15[i:i+chunk_size])
        chunked_list

    chunked_list1 = list()

    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
            chunked_list1

    Assign15 = list(itertools.chain(*chunked_list1))

    Assign15
    len(Assign15)
    df15['Assignment'] = Assign15
    sum_column = df15["Assignment"] + df15["VALUE"]
    df15["SUM"] = sum_column
    df15.drop('VALUE', axis=1, inplace=True)
    df15.drop('Assignment', axis=1, inplace=True)
    df15.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df15 = df15[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'DiscountRateTech']
    df = df.reset_index(drop=True)
    df15 = df15.reset_index(drop=True)
    df = df.append(df15, ignore_index=True)


    ##PLATFORMDISCOUNTRATESTO
    df468 = platform_storages
    Sto_list170 = df468['storage'].tolist()

    Value_list170 = df468['dicount_rate_sto'].tolist()

    Assign16 = []

    df16 = df.loc[df['PARAM'] == 'DiscountRateSto']

    Sto_list16 = df16['STORAGE'].tolist()
    Sto_list16

    Year_list16 = df16['YEAR'].tolist()
    Year_list16d = []

    for i in Year_list16:
        if i not in Year_list16d:
            Year_list16d.append(i)

    for j in range(0,len(Sto_list170)):

        a16 = Value_list170[j]

        b16 = Sto_list170[j]

        for y in Sto_list16:
                if b16 in y and (a16!= 0.001):
                    Assign16.append(-0.05 + a16)
                elif b16 in y and (a16 == 0.001):
                    Assign16.append(a16)
                else:
                    Assign16.append(0)

    Assign16                
    chunked_list = list()
    chunk_size = len(Year_list16d)
    for i in range(0, len(Assign16), chunk_size):
        chunked_list.append(Assign16[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign16 = list(itertools.chain(*chunked_list1))
    df16['Assignment'] = Assign16
    sum_column = df16["Assignment"] + df16["VALUE"]
    df16["SUM"] = sum_column
    df16.drop('VALUE', axis=1, inplace=True)
    df16.drop('Assignment', axis=1, inplace=True)
    df16.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df16 = df16[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'DiscountRateSto']
    df = df.reset_index(drop=True)
    df16 = df16.reset_index(drop=True)
    df = df.append(df16, ignore_index=True)

    #PLATFORMCAPACITYTOACTIVITYUNIT
    df471 = platform_technologies
    Tech_list113 = df471['technology'].tolist()

    Value_list113 = df471['capacity_to_activity'].tolist()
    Assign17 = []
    df17 = df.loc[df['PARAM'] == 'CapacityToActivityUnit']
    df17
    for j in range(0,len(Tech_list113)):

        a17 = Value_list113[j]
        Tech_list17 = df17['TECHNOLOGY'].tolist()
        Tech_list17
        b17 = Tech_list113[j]

        Tech_list17 = df17['TECHNOLOGY'].tolist()
        Tech_list17d = []

        for i in Tech_list17:
            if i not in Tech_list17d:
                Tech_list17d.append(i)

        for y in Tech_list17d:
                    if b17 in y and (a17!= 0.001):
                        Assign17.append(-8760 + a17)
                    elif b17 in y and (a17 == 0.001):
                        Assign17.append(a17)
                    else:
                        Assign17.append(0)
    Assign17 = Assign17[::int(len(Tech_list113)+1)]
    Assign17
    len(Assign17)
    df17['Assignment'] = Assign17
    sum_column = df17["Assignment"] + df17["VALUE"]
    df17["SUM"] = sum_column
    df17.drop('VALUE', axis=1, inplace=True)
    df17.drop('Assignment', axis=1, inplace=True)
    df17.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df17 = df17[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'CapacityToActivityUnit']
    df = df.reset_index(drop=True)
    df17 = df17.reset_index(drop=True)
    df = df.append(df17, ignore_index=True)

    #PLATFORMANNUALEMISSIONLIMIT

    df469 = platform_annual_emission_limit
    EM_list170 = df469['emission'].tolist()
    EM_list170
    Value_list170 = df469['annual_emission_limit'].tolist()

    Assign18 = []

    df18 = df.loc[df['PARAM'] == 'AnnualEmissionLimit']

    EM_list18 = df18['EMISSION'].tolist()

    Year_list18 = df18['YEAR'].tolist()
    Year_list18d = []

    for i in Year_list18:
        if i not in Year_list18d:
            Year_list18d.append(i)

    for j in range(0,len(EM_list170)):

        a18 = Value_list170[j]

        b18 = EM_list170[j]

        for y in EM_list18:
                if b18 in y and (a18!= 0.001):
                    Assign18.append(-99999 + a18)
                elif b18 in y and (a17 == 0.001):
                    Assign18.append(a17)
                else:
                    Assign18.append(0)

    Assign18                
    chunked_list = list()
    chunk_size = len(Year_list18d)
    for i in range(0, len(Assign18), chunk_size):
        chunked_list.append(Assign18[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign18 = list(itertools.chain(*chunked_list1))
    df18['Assignment'] = Assign18
    sum_column = df18["Assignment"] + df18["VALUE"]
    df18["SUM"] = sum_column
    df18.drop('VALUE', axis=1, inplace=True)
    df18.drop('Assignment', axis=1, inplace=True)
    df18.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df18 = df18[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'AnnualEmissionLimit']
    df = df.reset_index(drop=True)
    df18 = df18.reset_index(drop=True)
    df = df.append(df18, ignore_index=True)
    df

    #PLATFORMOPERATIONALLIFESTO
    df468 = platform_storages
    Sto_list170 = df468['storage'].tolist()

    Value_list170 = df468['operational_life_sto'].tolist()

    Assign19 = []

    df19 = df.loc[df['PARAM'] == 'OperationalLifeStorage']

    Sto_list19 = df19['STORAGE'].tolist()
    Sto_list19

    Year_list19 = df19['YEAR'].tolist()
    Year_list19d = []

    for i in Year_list19:
        if i not in Year_list19d:
            Year_list19d.append(i)

    for j in range(0,len(Sto_list170)):

        a19 = Value_list170[j]

        b19 = Sto_list170[j]

        for y in Sto_list19:
                if b19 in y and (a19 != 0.001):
                    Assign19.append(-99 + a19)
                elif b19 in y and (a19 == 0.001):
                    Assign19.append(a17)
                else:
                    Assign19.append(0)

    Assign19                
    chunked_list = list()
    chunk_size = len(Year_list19d)
    for i in range(0, len(Assign19), chunk_size):
        chunked_list.append(Assign19[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()
    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign19 = list(itertools.chain(*chunked_list1))
    df19['Assignment'] = Assign19
    sum_column = df19["Assignment"] + df19["VALUE"]
    df19["SUM"] = sum_column
    df19.drop('VALUE', axis=1, inplace=True)
    df19.drop('Assignment', axis=1, inplace=True)
    df19.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df19 = df19[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'OperationalLifeStorage']
    df = df.reset_index(drop=True)
    df19 = df19.reset_index(drop=True)
    df = df.append(df19, ignore_index=True)


    #PLATFORMSTOMAXDISCHARGERATE
    df469 = platform_storages
    Sto_list129 = df469['storage'].tolist()

    Value_list129 = df469['storage_max_discharge'].tolist()

    Assign20 = []

    df20 = df.loc[df['PARAM'] == 'StorageMaxDischargeRate']

    Sto_list20 = df20['STORAGE'].tolist()
    Sto_list20

    Year_list20 = df20['YEAR'].tolist()
    Year_list20d = []

    for i in Year_list20:
        if i not in Year_list20d:
            Year_list20d.append(i)

    for j in range(0,len(Sto_list129)):

        a20 = Value_list129[j]

        b20 = Sto_list129[j]

        for y in Sto_list20:
                if b20 in y and (a20!= 0.001):
                    Assign20.append(-99999 + a20)
                elif b20 in y and (a20 == 0.001):
                    Assign20.append(a20)
                else:
                    Assign20.append(0)

    Assign20                
    chunked_list = list()
    chunk_size = len(Year_list20d)
    for i in range(0, len(Assign20), chunk_size):
        chunked_list.append(Assign20[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign20 = list(itertools.chain(*chunked_list1))
    df20['Assignment'] = Assign20
    sum_column = df20["Assignment"] + df20["VALUE"]
    df20["SUM"] = sum_column
    df20.drop('VALUE', axis=1, inplace=True)
    df20.drop('Assignment', axis=1, inplace=True)
    df20.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df20 = df20[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'StorageMaxDischargeRate']
    df = df.reset_index(drop=True)
    df20 = df20.reset_index(drop=True)
    df = df.append(df20, ignore_index=True)
    df

    #PLATFORMSTOMAXCHARGERATE
    df467 = platform_storages
    Sto_list128 = df467['storage'].tolist()

    Value_list128 = df467['storage_max_discharge'].tolist()

    Assign21 = []

    df21 = df.loc[df['PARAM'] == 'StorageMaxChargeRate']

    Sto_list21 = df21['STORAGE'].tolist()
    Sto_list21

    Year_list21 = df21['YEAR'].tolist()
    Year_list21d = []

    for i in Year_list21:
        if i not in Year_list21d:
            Year_list21d.append(i)

    for j in range(0,len(Sto_list128)):

        a21 = Value_list128[j]

        b21 = Sto_list128[j]

        for y in Sto_list21:
                if b21 in y and (a21 != 0.001):
                    Assign21.append(-99999 + a21)
                elif b21 in y and (a21 == 0.001):
                    Assign21.append(a21)
                else:
                    Assign21.append(0)

    Assign21                
    chunked_list = list()
    chunk_size = len(Year_list21d)
    for i in range(0, len(Assign21), chunk_size):
        chunked_list.append(Assign21[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign21 = list(itertools.chain(*chunked_list1))
    df21['Assignment'] = Assign21
    sum_column = df21["Assignment"] + df21["VALUE"]
    df21["SUM"] = sum_column
    df21.drop('VALUE', axis=1, inplace=True)
    df21.drop('Assignment', axis=1, inplace=True)
    df21.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df21 = df21[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'StorageMaxChargeRate']
    df = df.reset_index(drop=True)
    df21 = df21.reset_index(drop=True)
    df = df.append(df21, ignore_index=True)
    df

    #PLATFORMStorageL2D
    df466 = platform_storages
    Sto_list127= df466['storage'].tolist()

    Value_list127= df466['l2d'].tolist()

    Assign22 = []

    df22 = df.loc[df['PARAM'] == 'StorageL2D']

    Sto_list22 = df22['STORAGE'].tolist()
    Sto_list22

    Year_list22 = df22['YEAR'].tolist()
    Year_list22d = []

    for i in Year_list22:
        if i not in Year_list22d:
            Year_list22d.append(i)

    for j in range(0,len(Sto_list127)):

        a22 = Value_list127[j]

        b22 = Sto_list127[j]

        for y in Sto_list22:
                if b22 in y:
                    Assign22.append(a22)
                else:
                    Assign22.append(0)

    Assign22                
    chunked_list = list()
    chunk_size = len(Year_list22d)
    for i in range(0, len(Assign22), chunk_size):
        chunked_list.append(Assign22[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign22 = list(itertools.chain(*chunked_list1))
    df22['Assignment'] = Assign22
    sum_column = df22["Assignment"] + df22["VALUE"]
    df22["SUM"] = sum_column
    df22.drop('VALUE', axis=1, inplace=True)
    df22.drop('Assignment', axis=1, inplace=True)
    df22.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df22 = df22[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'StorageL2D']
    df = df.reset_index(drop=True)
    df22 = df22.reset_index(drop=True)
    df = df.append(df22, ignore_index=True)
    df


    #PLATFORMStoragetagheating
    df465 = platform_storages
    Sto_list126 = df465['storage'].tolist()

    Value_list126 = df465['tag_heating'].tolist()

    Assign23 = []

    df23 = df.loc[df['PARAM'] == 'Storagetagheating']

    Sto_list23 = df23['STORAGE'].tolist()
    Sto_list23

    Year_list23 = df23['YEAR'].tolist()
    Year_list23d = []

    for i in Year_list23:
        if i not in Year_list23d:
            Year_list23d.append(i)

    for j in range(0,len(Sto_list126)):

        a23 = Value_list126[j]

        b23 = Sto_list126[j]

        for y in Sto_list23:
                if b23 in y:
                    Assign23.append(a23)
                else:
                    Assign23.append(0)

    Assign23                
    chunked_list = list()
    chunk_size = len(Year_list23d)
    for i in range(0, len(Assign23), chunk_size):
        chunked_list.append(Assign23[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign23 = list(itertools.chain(*chunked_list1))
    df23['Assignment'] = Assign23
    sum_column = df23["Assignment"] + df23["VALUE"]
    df23["SUM"] = sum_column
    df23.drop('VALUE', axis=1, inplace=True)
    df23.drop('Assignment', axis=1, inplace=True)
    df23.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df23 = df23[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'Storagetagheating']
    df = df.reset_index(drop=True)
    df23 = df23.reset_index(drop=True)
    df = df.append(df23, ignore_index=True)
    df

    #PLATFORMStoragetagcooling
    df464 = platform_storages
    Sto_list125 = df464['storage'].tolist()

    Value_list125 = df464['tag_cooling'].tolist()

    Assign24 = []

    df24 = df.loc[df['PARAM'] == 'Storagetagcooling']
    df24
    Sto_list24 = df24['STORAGE'].tolist()
    Sto_list24

    Year_list24 = df24['YEAR'].tolist()
    Year_list24d = []

    for i in Year_list24:
        if i not in Year_list24d:
            Year_list24d.append(i)

    for j in range(0,len(Sto_list125)):

        a24 = Value_list125[j]

        b24 = Sto_list125[j]

        for y in Sto_list24:
                if b24 in y:
                    Assign24.append(a24)
                else:
                    Assign24.append(0)

    Assign24                
    chunked_list = list()
    chunk_size = len(Year_list24d)
    for i in range(0, len(Assign24), chunk_size):
        chunked_list.append(Assign24[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign24 = list(itertools.chain(*chunked_list1))
    df24['Assignment'] = Assign24
    sum_column = df24["Assignment"] + df24["VALUE"]
    df24["SUM"] = sum_column
    df24.drop('VALUE', axis=1, inplace=True)
    df24.drop('Assignment', axis=1, inplace=True)
    df24.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df24 = df24[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'Storagetagcooling']
    df = df.reset_index(drop=True)
    df24 = df24.reset_index(drop=True)
    df = df.append(df24, ignore_index=True)
    df

    #PLATFORMStorageReturnTemperature
    df463 = platform_storages
    Sto_list124 = df463['storage'].tolist()

    Value_list124 = df463['storage_return_temp'].tolist()

    Assign25 = []

    df25 = df.loc[df['PARAM'] == 'StorageReturnTemperature']

    Sto_list25 = df25['STORAGE'].tolist()
    Sto_list25

    Year_list25 = df25['YEAR'].tolist()
    Year_list25d = []

    for i in Year_list25:
        if i not in Year_list25d:
            Year_list25d.append(i)

    for j in range(0,len(Sto_list124)):

        a25 = Value_list124[j]

        b25 = Sto_list124[j]

        for y in Sto_list25:
                if b25 in y and a25!= 0.001:
                    Assign25.append(-55 + a25)
                elif b25 in y and a25 == 0.001:
                    Assign25.append(a25)           
                else:
                    Assign25.append(0)

    Assign25                
    chunked_list = list()
    chunk_size = len(Year_list25d)
    for i in range(0, len(Assign25), chunk_size):
        chunked_list.append(Assign25[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign25 = list(itertools.chain(*chunked_list1))
    df25['Assignment'] = Assign25
    sum_column = df25["Assignment"] + df25["VALUE"]
    df25["SUM"] = sum_column
    df25.drop('VALUE', axis=1, inplace=True)
    df25.drop('Assignment', axis=1, inplace=True)
    df25.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df25 = df25[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'StorageReturnTemperature']
    df = df.reset_index(drop=True)
    df25 = df25.reset_index(drop=True)
    df = df.append(df25, ignore_index=True)
    df

    #PLATFORMStorageFlowTemperature
    df462 = platform_storages
    Sto_list123 = df462['storage'].tolist()

    Value_list123 = df462['storage_supply_temp'].tolist()

    Assign26 = []

    df26 = df.loc[df['PARAM'] == 'StorageFlowTemperature']

    Sto_list26 = df26['STORAGE'].tolist()
    Sto_list26

    Year_list26 = df26['YEAR'].tolist()
    Year_list26d = []

    for i in Year_list26:
        if i not in Year_list26d:
            Year_list26d.append(i)

    for j in range(0,len(Sto_list123)):

        a26 = Value_list123[j]

        b26 = Sto_list123[j]

        for y in Sto_list26:
                if b26 in y and a26 != 0.001:
                    Assign26.append(-85 + a26)
                elif b26 in y and a26 == 0.001:
                    Assign26.append(a26)
                else:
                    Assign26.append(0)
    Assign26                
    chunked_list = list()
    chunk_size = len(Year_list26d)
    for i in range(0, len(Assign26), chunk_size):
        chunked_list.append(Assign26[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign26 = list(itertools.chain(*chunked_list1))
    df26['Assignment'] = Assign26
    sum_column = df26["Assignment"] + df26["VALUE"]
    df26["SUM"] = sum_column
    df26.drop('VALUE', axis=1, inplace=True)
    df26.drop('Assignment', axis=1, inplace=True)
    df26.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df26 = df26[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'StorageFlowTemperature']
    df = df.reset_index(drop=True)
    df26 = df26.reset_index(drop=True)
    df = df.append(df26, ignore_index=True)

    #PLATFORMStorageAmbientTemperature
    df461 = platform_storages
    Sto_list122 = df461['storage'].tolist()

    Value_list122 = df461['storage_ambient_temp'].tolist()
    Value_list122
    Assign27 = []

    df27 = df.loc[df['PARAM'] == 'StorageAmbientTemperature']

    Sto_list27 = df27['STORAGE'].tolist()
    Sto_list27

    Year_list27 = df27['YEAR'].tolist()
    Year_list27d = []

    for i in Year_list27:
        if i not in Year_list27d:
            Year_list27d.append(i)

    for j in range(0,len(Sto_list122)):

        a27 = Value_list122[j]

        b27 = Sto_list122[j]

        for y in Sto_list27:
                if b27 in y and a27!= 0.001:
                    Assign27.append(-15 + a27)
                elif b27 in y and a27 == 0.001:
                    Assign27.append(a27)            
                else:
                    Assign27.append(0)

    Assign27                
    chunked_list = list()
    chunk_size = len(Year_list27d)
    for i in range(0, len(Assign27), chunk_size):
        chunked_list.append(Assign27[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign27 = list(itertools.chain(*chunked_list1))
    df27['Assignment'] = Assign27
    sum_column = df27["Assignment"] + df27["VALUE"]
    df27["SUM"] = sum_column
    df27.drop('VALUE', axis=1, inplace=True)
    df27.drop('Assignment', axis=1, inplace=True)
    df27.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df27 = df27[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'StorageAmbientTemperature']
    df = df.reset_index(drop=True)
    df27 = df27.reset_index(drop=True)
    df = df.append(df27, ignore_index=True)
    df

    #PLATFORMResidualCapacity
    df460 = platform_technologies
    Tech_list121 = df460['technology'].tolist()

    Value_list121 = df460['residual_capacity'].tolist()
    Value_list121
    df28 = df.loc[df['PARAM'] == 'ResidualCapacity']
    Assign28 = []

    Tech_list28 = df28['TECHNOLOGY'].tolist()
    Tech_list28

    Year_list28 = df28['YEAR'].tolist()
    Year_list28d = []

    for i in Year_list28:
        if i not in Year_list28d:
            Year_list28d.append(i)

    for j in range(0,len(Tech_list121)):

        a28 = Value_list121[j]

        b28 = Tech_list121[j]

        for y in Tech_list28:
                if b28 in y:
                    Assign28.append(a28)
                else:
                    Assign28.append(0)

    Assign28                
    chunked_list = list()
    chunk_size = len(Year_list28d)
    for i in range(0, len(Assign28), chunk_size):
        chunked_list.append(Assign28[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign28 = list(itertools.chain(*chunked_list1))
    df28['Assignment'] = Assign28
    sum_column = df28["Assignment"] + df28["VALUE"]
    df28["SUM"] = sum_column
    df28.drop('VALUE', axis=1, inplace=True)
    df28.drop('Assignment', axis=1, inplace=True)
    df28.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df28 = df28[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'ResidualCapacity']
    df = df.reset_index(drop=True)
    df28 = df28.reset_index(drop=True)
    df = df.append(df28, ignore_index=True)

    #PLATFORMResidualStorageCapacity
    df459 = platform_storages
    Sto_list119 = df459['storage'].tolist()

    Value_list119 = df459['residual_storage_capacity'].tolist()
    Value_list119
    Assign29 = []

    df29 = df.loc[df['PARAM'] == 'ResidualStorageCapacity']

    Sto_list29 = df29['STORAGE'].tolist()
    Sto_list29

    Year_list29 = df29['YEAR'].tolist()
    Year_list29d = []

    for i in Year_list29:
        if i not in Year_list29d:
            Year_list29d.append(i)

    for j in range(0,len(Sto_list119)):

        a29 = Value_list119[j]

        b29 = Sto_list119[j]

        for y in Sto_list29:
                if b29 in y:
                    Assign29.append(a29)
                else:
                    Assign29.append(0)

    Assign29                
    chunked_list = list()
    chunk_size = len(Year_list29d)
    for i in range(0, len(Assign29), chunk_size):
        chunked_list.append(Assign29[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign29 = list(itertools.chain(*chunked_list1))
    df29['Assignment'] = Assign29
    sum_column = df29["Assignment"] + df29["VALUE"]
    df29["SUM"] = sum_column
    df29.drop('VALUE', axis=1, inplace=True)
    df29.drop('Assignment', axis=1, inplace=True)
    df29.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df29 = df29[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'ResidualStorageCapacity']
    df = df.reset_index(drop=True)
    df29 = df29.reset_index(drop=True)
    df = df.append(df29, ignore_index=True)


    #PLATFORMStorageMaxCapacity
    df458 = platform_storages
    Sto_list119 = df458['storage'].tolist()
    Value_list119 = df458['max_storage_capacity'].tolist()
    Assign30 = []
    df30 = df.loc[df['PARAM'] == 'StorageMaxCapacity']
    Sto_list31 = df30['STORAGE'].tolist()
    Sto_list31d = []

    for i in Sto_list31:
        if i not in Sto_list31d:
            Sto_list31d.append(i)

    for j in range(0,len(Sto_list119)):

        a30 = Value_list119[j]

        b30 = Sto_list119[j]

        for y in Sto_list31d:
                if b30 in y and a30!= 0.001:
                    Assign30.append(-99999 + a30)
                elif b30 in y and a30 == 0.001:
                    Assign30.append(a30)               
                else:
                    Assign30.append(0)
    Assign30                
    Assign30 = Assign30[::int(len(Sto_list119)+1)]
    Assign30
    len(Assign30)
    df30['Assignment'] = Assign30
    sum_column = df30["Assignment"] + df30["VALUE"]
    df30["SUM"] = sum_column
    df30.drop('VALUE', axis=1, inplace=True)
    df30.drop('Assignment', axis=1, inplace=True)
    df30.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df30 = df30[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'StorageMaxCapacity']
    df = df.reset_index(drop=True)
    df30 = df30.reset_index(drop=True)
    df = df.append(df30, ignore_index=True)
    df


    #PLATFORMStorageLevelStart
    df457 = platform_storages
    Sto_list118 = df457['storage'].tolist()
    Value_list118 = df457['storage_level_start'].tolist()
    Assign31 = []
    df31 = df.loc[df['PARAM'] == 'StorageLevelStart']
    Sto_list31 = df31['STORAGE'].tolist()
    Sto_list31d = []
    for i in Sto_list31:
        if i not in Sto_list31d:
            Sto_list31d.append(i)

    for j in range(0,len(Sto_list118)):

        a31 = Value_list118[j]

        b31 = Sto_list118[j]

        for y in Sto_list31d:
                if b31 in y:
                    Assign31.append(a31)
                else:
                    Assign31.append(0)
    Assign31                
    Assign31 = Assign31[::int(len(Sto_list118)+1)]
    Assign31
    len(Assign31)
    df31['Assignment'] = Assign31
    sum_column = df31["Assignment"] + df31["VALUE"]
    df31["SUM"] = sum_column
    df31.drop('VALUE', axis=1, inplace=True)
    df31.drop('Assignment', axis=1, inplace=True)
    df31.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df31 = df31[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'StorageLevelStart']
    df = df.reset_index(drop=True)
    df31 = df31.reset_index(drop=True)
    df = df.append(df31, ignore_index=True)


    #PLATFORMStorageUvalue
    df456 = platform_storages
    Sto_list117 = df456['storage'].tolist()

    Value_list117 = df456['u_value'].tolist()
    Value_list117
    Assign32 = []

    df32 = df.loc[df['PARAM'] == 'StorageUvalue']

    Sto_list32 = df32['STORAGE'].tolist()
    Sto_list32

    Year_list32 = df32['YEAR'].tolist()
    Year_list32d = []

    for i in Year_list32:
        if i not in Year_list32d:
            Year_list32d.append(i)

    for j in range(0,len(Sto_list117)):

        a32 = Value_list117[j]

        b32 = Sto_list117[j]

        for y in Sto_list32:
                if b32 in y and a32!= 0.001:
                    Assign32.append(-0.22 + a32)
                elif b32 in y and a32 == 0.001:
                    Assign32.append(a32)           
                else:
                    Assign32.append(0)

    Assign32                
    chunked_list = list()
    chunk_size = len(Year_list32d)
    for i in range(0, len(Assign32), chunk_size):
        chunked_list.append(Assign32[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign32 = list(itertools.chain(*chunked_list1))
    df32['Assignment'] = Assign32
    sum_column = df32["Assignment"] + df32["VALUE"]
    df32["SUM"] = sum_column
    df32.drop('VALUE', axis=1, inplace=True)
    df32.drop('Assignment', axis=1, inplace=True)
    df32.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df32 = df32[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'StorageUvalue']
    df = df.reset_index(drop=True)
    df32 = df32.reset_index(drop=True)
    df = df.append(df32, ignore_index=True)
    df

    #PLATFORMTechnologyFromStorage
    import itertools
    df485 = platform_technology_to_storage
    Tech_list113 = df485['technology'].tolist()
    Value_list113 = df485['technologyfromstorage'].tolist()
    Sto_list113 = df485['storage'].tolist()

    df33 = df.loc[df['PARAM'] == 'TechnologyFromStorage']
    df33

    Assign33 = []


    Tech_list33 = df33['TECHNOLOGY'].tolist()
    Tech_list33d = []

    for i in Tech_list33:
        if i not in Tech_list33d:
            Tech_list33d.append(i)

    Tech_list33d
    Sto_list33 = df33['STORAGE'].tolist()
    Sto_list33
    Sto_list33d = []

    for j in Sto_list33:
        if j not in Sto_list33d:
            Sto_list33d.append(j)


    MO_list33 = df33['MODE_OF_OPERATION'].tolist()
    MO_list33d = []

    for l in MO_list33:
        if l not in MO_list33d:
            MO_list33d.append(l)

    for w in MO_list33d:
        for k in range(0,len(Tech_list113)):
            a33 = Value_list113[k]
            b33 = Tech_list113[k]
            c33 = Sto_list113[k]
            for x in Sto_list33d:
                for y in Tech_list33d:
                    if (b33) in y and (c33) in x: 
                        Assign33.append(a33)
                    else:
                        Assign33.append(0)

    Assign33

    chunked_list33 = list()
    chunk_size33 = len(Tech_list113)
    for i in range(0, len(Assign33), chunk_size33):
        chunked_list33.append(Assign33[i:i+chunk_size33])
    chunked_list33

    chunked_list331 = list()

    for k in range(0, len(chunked_list33)):
        O = sum(chunked_list33[k])
        if O != 0:
            chunked_list331.append(chunked_list33[k]) 

    chunked_list331
    Assign33 = list(itertools.chain(*chunked_list331))
    Assign33


    df33['Assignment'] = Assign33
    sum_column = df33["Assignment"] + df33["VALUE"]
    df33["SUM"] = sum_column
    df33.drop('VALUE', axis=1, inplace=True)
    df33.drop('Assignment', axis=1, inplace=True)
    df33.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df33 = df33[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df33.head(50)
    df = df.loc[df['PARAM'] != 'TechnologyFromStorage']
    df = df.reset_index(drop=True)
    df33 = df33.reset_index(drop=True)
    df = df.append(df33, ignore_index=True)

    #PLATFORMTechnologyToStorage
    import itertools
    df484 = platform_technology_to_storage
    Tech_list112 = df484['technology'].tolist()
    Value_list112 = df484['technologytostorage'].tolist()
    Sto_list112 = df484['storage'].tolist()

    df34 = df.loc[df['PARAM'] == 'TechnologyToStorage']
    df34

    Assign34 = []


    Tech_list34 = df34['TECHNOLOGY'].tolist()
    Tech_list34d = []

    for i in Tech_list34:
        if i not in Tech_list34d:
            Tech_list34d.append(i)

    Tech_list34d
    Sto_list34 = df34['STORAGE'].tolist()
    Sto_list34
    Sto_list34d = []

    for j in Sto_list34:
        if j not in Sto_list34d:
            Sto_list34d.append(j)


    MO_list34 = df34['MODE_OF_OPERATION'].tolist()
    MO_list34d = []

    for l in MO_list34:
        if l not in MO_list34d:
            MO_list34d.append(l)


    for w in MO_list34d:
        for k in range(0,len(Tech_list112)):
            a34 = Value_list112[k]
            b34 = Tech_list112[k]
            c34 = Sto_list112[k]
            for x in Sto_list34d:
                for y in Tech_list34d:
                    if (b34) in y and (c34) in x: 
                        Assign34.append(a34)
                    else:
                        Assign34.append(0)

    Assign34

    chunked_list = list()
    chunk_size = len(Tech_list112)
    for i in range(0, len(Assign34), chunk_size):
        chunked_list.append(Assign34[i:i+chunk_size])
    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 

    chunked_list1
    Assign34 = list(itertools.chain(*chunked_list1))
    Assign34


    df34['Assignment'] = Assign34
    sum_column = df34["Assignment"] + df34["VALUE"]
    df34["SUM"] = sum_column
    df34
    df34.drop('VALUE', axis=1, inplace=True)
    df34.drop('Assignment', axis=1, inplace=True)
    df34.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df34 = df34[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'TechnologyToStorage']
    df = df.reset_index(drop=True)
    df34 = df34.reset_index(drop=True)
    df = df.append(df34, ignore_index=True)

    #PLATFORMTotalAnnualMaxCapacityInvestment
    df454 = platform_technologies
    Tech_list117 = df454['technology'].tolist()
    Tech_list117
    Value_list117 = df454['max_capacity_investment'].tolist()
    Assign35 = []
    df35 = df.loc[df['PARAM'] == 'TotalAnnualMaxCapacityInvestment']

    Tech_list35 = df35['TECHNOLOGY'].tolist()
    Tech_list35

    Year_list35 = df35['YEAR'].tolist()
    Year_list35d = []

    for i in Year_list35:
        if i not in Year_list35d:
            Year_list35d.append(i)

    for j in range(0,len(Tech_list117)):

        a35 = int(Value_list117[j])

        b35 = Tech_list117[j]

        for y in Tech_list35:
                if b35 in y and a35!= 0.001:
                    Assign35.append(-99999 + a35)
                elif b35 in y and a35 == 0.001:
                    Assign35.append(a35)
                else:
                    Assign35.append(0)

    chunked_list = list()
    chunk_size = len(Year_list35d)
    for i in range(0, len(Assign35), chunk_size):
        chunked_list.append(Assign35[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign35 = list(itertools.chain(*chunked_list1))
    df35['Assignment'] = Assign35
    sum_column = df35["Assignment"] + df35["VALUE"]
    df35["SUM"] = sum_column
    df35.drop('VALUE', axis=1, inplace=True)
    df35.drop('Assignment', axis=1, inplace=True)
    df35.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df35 = df35[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'TotalAnnualMaxCapacityInvestment']
    df = df.reset_index(drop=True)
    df35 = df35.reset_index(drop=True)
    df = df.append(df35, ignore_index=True)
    df

    #PLATFORMTotalAnnualMinCapacity
    df420 = platform_technologies
    Tech_list116 = df420['technology'].tolist()
    Tech_list116
    Value_list116 = df420['min_capacity'].tolist()
    Assign36 = []
    df36 = df.loc[df['PARAM'] == 'TotalAnnualMinCapacity']

    Tech_list36 = df36['TECHNOLOGY'].tolist()
    Tech_list36

    Year_list36 = df36['YEAR'].tolist()
    Year_list36d = []

    for i in Year_list36:
        if i not in Year_list36d:
            Year_list36d.append(i)

    for j in range(0,len(Tech_list116)):

        a36 =  int(Value_list116[j])

        b36 = Tech_list116[j]

        for y in Tech_list36:
                if str(b36) in y and (int(Value_list116[j]) > 0):
                    Assign36.append(a36)
                else:
                    Assign36.append(0)

    chunked_list = list()
    chunk_size = len(Year_list36d)
    for i in range(0, len(Assign36), chunk_size):
        chunked_list.append(Assign36[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign36 = list(itertools.chain(*chunked_list1))
    df36['Assignment'] = Assign36
    sum_column = df36["Assignment"] + df36["VALUE"]
    df36["SUM"] = sum_column
    df36.drop('VALUE', axis=1, inplace=True)
    df36.drop('Assignment', axis=1, inplace=True)
    df36.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df36 = df36[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'TotalAnnualMinCapacity']
    df = df.reset_index(drop=True)
    df36 = df36.reset_index(drop=True)
    df = df.append(df36, ignore_index=True)

    #PLATFORMTotalAnnualMinCapacityInvestment
    df466 = platform_technologies
    Tech_list115 = df466['technology'].tolist()
    Tech_list115
    Value_list115 = df466['min_capacity_investment'].tolist()
    Assign37 = []
    df37 = df.loc[df['PARAM'] == 'TotalAnnualMinCapacityInvestment']

    Tech_list37 = df37['TECHNOLOGY'].tolist()
    Tech_list37

    Year_list37 = df37['YEAR'].tolist()
    Year_list37d = []

    for i in Year_list37:
        if i not in Year_list37d:
            Year_list37d.append(i)

    for j in range(0,len(Tech_list115)):

        a37 =  int(Value_list115[j])

        b37 = Tech_list115[j]

        for y in Tech_list37:
                if str(b37) in y and (int(Value_list115[j]) > 0):
                    Assign37.append(a37)
                else:
                    Assign37.append(0)

    chunked_list = list()
    chunk_size = len(Year_list37d)
    for i in range(0, len(Assign37), chunk_size):
        chunked_list.append(Assign37[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign37 = list(itertools.chain(*chunked_list1))
    df37['Assignment'] = Assign37
    sum_column = df37["Assignment"] + df37["VALUE"]
    df37["SUM"] = sum_column
    df37.drop('VALUE', axis=1, inplace=True)
    df37.drop('Assignment', axis=1, inplace=True)
    df37.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df37 = df37[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'TotalAnnualMinCapacityInvestment']
    df = df.reset_index(drop=True)
    df37 = df37.reset_index(drop=True)
    df = df.append(df37, ignore_index=True)
    df

    #PLATFORMTotalTechnologyAnnualActivityLowerLimit
    df478 = platform_technologies
    Tech_list115 = df478['technology'].tolist()
    Tech_list115
    Value_list115 = df478['annual_activity_lower_limit'].tolist()
    Assign38 = []
    df38 = df.loc[df['PARAM'] == 'TotalTechnologyAnnualActivityLowerLimit']

    Tech_list38 = df38['TECHNOLOGY'].tolist()
    Tech_list38

    Year_list38 = df38['YEAR'].tolist()
    Year_list38d = []

    for i in Year_list38:
        if i not in Year_list38d:
            Year_list38d.append(i)

    for j in range(0,len(Tech_list115)):

        a38 =  int(Value_list115[j])

        b38 = Tech_list115[j]

        for y in Tech_list38:
                if str(b38) in y and (int(Value_list115[j]) > 0):
                    Assign38.append(a38)
                else:
                    Assign38.append(0)

    chunked_list = list()
    chunk_size = len(Year_list38d)
    for i in range(0, len(Assign38), chunk_size):
        chunked_list.append(Assign38[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign38 = list(itertools.chain(*chunked_list1))
    df38['Assignment'] = Assign38
    sum_column = df38["Assignment"] + df38["VALUE"]
    df38["SUM"] = sum_column
    df38.drop('VALUE', axis=1, inplace=True)
    df38.drop('Assignment', axis=1, inplace=True)
    df38.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df38 = df38[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'TotalTechnologyAnnualActivityLowerLimit']
    df = df.reset_index(drop=True)
    df38 = df38.reset_index(drop=True)
    df = df.append(df38, ignore_index=True)

    #PLATFORMTotalTotalTechnologyAnnualActivityUpperLimit
    df471 = platform_technologies
    Tech_list114 = df471['technology'].tolist()
    Tech_list114
    Value_list114 = df471['annual_activity_upper_limit'].tolist()
    Assign39 = []
    df39 = df.loc[df['PARAM'] == 'TotalTechnologyAnnualActivityUpperLimit']
    c39 = -99999

    Tech_list39 = df39['TECHNOLOGY'].tolist()
    Tech_list39

    Year_list39 = df39['YEAR'].tolist()
    Year_list39d = []

    for i in Year_list39:
        if i not in Year_list39d:
            Year_list39d.append(i)

    for j in range(0,len(Tech_list114)):

        a39 =  c39 + int(Value_list114[j])

        b39 = Tech_list114[j]

        for y in Tech_list39:
                if b39 in y and a39 != 0.001:
                    Assign39.append(-99999 + a39)
                elif b39 in y and a39 == 0.001:
                    Assign39.append(a39)
                else:
                    Assign39.append(0)

    chunked_list = list()
    chunk_size = len(Year_list39d)
    for i in range(0, len(Assign39), chunk_size):
        chunked_list.append(Assign39[i:i+chunk_size])
    chunked_list

    chunked_list1 = list()


    for k in range(0, len(chunked_list)):
        O = sum(chunked_list[k])
        if O != 0:
            chunked_list1.append(chunked_list[k]) 
    chunked_list1

    Assign39 = list(itertools.chain(*chunked_list1))
    df39['Assignment'] = Assign39
    sum_column = df39["Assignment"] + df39["VALUE"]
    df39["SUM"] = sum_column
    df39.drop('VALUE', axis=1, inplace=True)
    df39.drop('Assignment', axis=1, inplace=True)
    df39.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df39 = df39[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'TotalTechnologyAnnualActivityUpperLimit']
    df = df.reset_index(drop=True)
    df39 = df39.reset_index(drop=True)
    df = df.append(df39, ignore_index=True)

    #PLATFORMTotalTotalTechnologyModelPeriodActivityLowerLimit
    df405 = platform_technologies
    Tech_list113 = df405['technology'].tolist()

    Value_list113 = df405['model_period_activity_lower_limit'].tolist()
    Assign40 = []
    df40 = df.loc[df['PARAM'] == 'TotalTechnologyModelPeriodActivityLowerLimit']

    for j in range(0,len(Tech_list113)):

        a40 = int(Value_list113[j])
        Tech_list40 = df40['TECHNOLOGY'].tolist()
        Tech_list40
        b40 = Tech_list113[j]

        Tech_list40 = df40['TECHNOLOGY'].tolist()
        Tech_list40d = []

        for i in Tech_list40:
            if i not in Tech_list40d:
                Tech_list40d.append(i)

        for y in Tech_list40d:
                if str(b40) in y and (int(Value_list113[j]) > 0):
                    Assign40.append(a40)
                else:
                    Assign40.append(0)
    Assign40 = Assign40[::int(len(Tech_list113)+1)]
    Assign40
    len(Assign40)
    df40['Assignment'] = Assign40
    sum_column = df40["Assignment"] + df40["VALUE"]
    df40["SUM"] = sum_column
    df40.drop('VALUE', axis=1, inplace=True)
    df40.drop('Assignment', axis=1, inplace=True)
    df40.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df40 = df40[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'TotalTechnologyModelPeriodActivityLowerLimit']
    df = df.reset_index(drop=True)
    df40 = df40.reset_index(drop=True)
    df = df.append(df40, ignore_index=True)

    #PLATFORMTotalTotalTechnologyModelPeriodActivityUpperLimit
    df429 = platform_technologies
    Tech_list111 = df429['technology'].tolist()
    Tech_list111
    Value_list111 = df429['model_period_activity_upper_limit'].tolist()
    Assign41 = []
    df41 = df.loc[df['PARAM'] == 'TotalTechnologyModelPeriodActivityUpperLimit']

    for j in range(0,len(Tech_list111)):

        a41 =  Value_list111[j]
        Tech_list41 = df41['TECHNOLOGY'].tolist()
        Tech_list41
        b41 = Tech_list111[j]

        Tech_list41 = df41['TECHNOLOGY'].tolist()
        Tech_list41d = []

        for i in Tech_list41:
            if i not in Tech_list41d:
                Tech_list41d.append(i)

        for y in Tech_list41d:
                if b41 in y and a41 != 0.001:
                    Assign41.append(-99999 + a41)
                elif b41 in y and a41 == 0.001:
                    Assign41.append(a41)
                else:
                    Assign41.append(0)
    Assign41 = Assign41[::int(len(Tech_list111)+1)]
    Assign41
    len(Assign41)
    df41['Assignment'] = Assign41
    sum_column = df41["Assignment"] + df41["VALUE"]
    df41["SUM"] = sum_column
    df41.drop('VALUE', axis=1, inplace=True)
    df41.drop('Assignment', axis=1, inplace=True)
    df41.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df41 = df41[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df = df.loc[df['PARAM'] != 'TotalTechnologyModelPeriodActivityUpperLimit']
    df = df.reset_index(drop=True)
    df41 = df41.reset_index(drop=True)
    df = df.append(df41, ignore_index=True)
    df

    #PLATFORMYearSplit
    import numpy as np
    df41 = df.loc[df['PARAM'] == 'YearSplit']
    Timeslice = len(sets_df['TIMESLICE'])
    a41 = 1 / Timeslice

    TS_list41 = df41['TIMESLICE'].tolist()
    TS_list41d = []

    for j in TS_list41:
        if j not in TS_list41d:
            TS_list41d.append(j)

    Year_list41 = df41['YEAR'].tolist()
    Year_list41d = []

    for k in Year_list41:
        if k not in Year_list41d:
            Year_list41d.append(k)


    Assign41 = []



    for y in TS_list41d:
        for z in Year_list41d: 
                    Assign41.append(a41)    

    Assign41
    len(df41)
    df41['Assignment'] = Assign41
    sum_column = df41["Assignment"] + df41["VALUE"]
    df41["SUM"] = sum_column
    df41.drop('VALUE', axis=1, inplace=True)
    df41.drop('Assignment', axis=1, inplace=True)
    df41.rename(columns={'SUM': 'VALUE'}, inplace=True)
    df41 = df41[['PARAM', 'VALUE', 'REGION', 'REGION2','DAYTYPE', 'EMISSION', 'FUEL', 'DAILYTIMEBRACKET', 'SEASON', 'TIMESLICE','STORAGE', 'MODE_OF_OPERATION', 'TECHNOLOGY', 'YEAR']]
    df41[df41['FUEL'] == str('SINK1DEMAND')]
    df = df.loc[df['PARAM'] != 'YearSplit']
    df = df.reset_index(drop=True)
    df41 = df41.reset_index(drop=True)
    df = df.append(df41, ignore_index=True)
    
    return df