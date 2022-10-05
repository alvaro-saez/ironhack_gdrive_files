#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 
import re


# In[ ]:


def cat_var(df, cols):
    '''
    Return: a Pandas dataframe object with the following columns:
        - "categorical_variable" => every categorical variable include as an input parameter (string).
        - "number_of_possible_values" => the amount of unique values that can take a given categorical variable (integer).
        - "values" => a list with the posible unique values for every categorical variable (list).

    Input parameters:
        - df -> Pandas dataframe object: a dataframe with categorical variables.
        - cols -> list object: a list with the name (string) of every categorical variable to analyse.
    '''
    cat_list = []
    for col in cols:
        cat = df[col].unique()
        cat_num = len(cat)
        cat_dict = {"categorical_variable":col,
                    "number_of_possible_values":cat_num,
                    "values":cat}
        cat_list.append(cat_dict)
    df = pd.DataFrame(cat_list).sort_values(by="number_of_possible_values", ascending=False)
    return df.reset_index(drop=True)


# In[ ]:


def row_filter(df, columns_name, value_of_the_cell):
    '''
    Return: a Pandas dataframe object where columns have been filtered by a set of values from a given column (categorical variable). 
            The resulting dataframe will be sorted descending from highest to lowest amount of deaths and the index column will be reset.

    Input parameters:
        - df -> Pandas dataframe object: a dataframe with categorical variables.
        - columns_name -> string: a string with the name of a categorical variable (e.g.: 'Sexo' or ['Sexo', 'Gender']).
        - value_of_the_cell -> list object: a list of values (string) which rows will be INCLUDED into the returned dataframe (e.g.: ['Hombres', 'Mujeres'])
    '''
    df = df[df[columns_name].isin(value_of_the_cell)].sort_values(by='Total', ascending=False)
    return df.reset_index(drop=True)


# In[ ]:


def nrow_filter(df, columns_name, value_of_the_cell):
    '''
    Return: a Pandas dataframe object where columns have been filtered by a set of values from a given column (categorical variable). 
            The resulting dataframe will be sorted descending from highest to lowest amount of deaths and the index column will be reset.

    Input parameters:
        - df -> Pandas dataframe object: a dataframe with categorical variables.
        - columns_name -> string: a string with the name of a categorical variable (e.g.: 'Sexo' or ['Sexo', 'Gender']).
        - value_of_the_cell -> list object: a list of values (string) which rows will be EXCLUDED into the returned dataframe (e.g.: ['Hombres', 'Mujeres'])
    '''
    df = df[~df[columns_name].isin(value_of_the_cell)].sort_values(by='Total', ascending=False)
    return df.reset_index(drop=True)


# In[ ]:


def groupby_formula(df, columns_name_to_be_aggruped, agg_var='Total', sort_var='Total', formula):
    '''
    Return: a Pandas dataframe object where rows have been gruped by a given group of columns (categorical variables). 
            The resulting dataframe will be sorted descending from highest to lowest amount of deaths and the index column will be reset.

    Input parameters:
        - df -> Pandas dataframe object: a dataframe with categorical variables and an aggregation variable.
        - columns_name_to_be_aggruped -> list object: a list of values with the name of a group of categorical variables (e.g.: ['Sexo', 'Edad']).
        - agg_var -> string: a string with the name of the variable to be aggregated. In this case the variable 'Total' (number of deaths) is set as default.
        - sort_var -> string: a string with the name of the variable to sort the dataframe by. In this case the variable 'Total' (number of deaths) is set as default.
        - formula -> ejemplo "sum"
    '''
    df = df.groupby(columns_name_to_be_aggruped, as_index=False).agg({agg_var:formula})
    df = df.sort_values(by=sort_var, ascending=False)
    return df.reset_index(drop=True)


# In[ ]:


def pivot_table(df, col, x_axis, value='Total'):
    '''
    Return: a Pandas dataframe object where categorical variable values have been pivoted. 
            The resulting dataframe index column will be reset.

    Input parameters:
        - df -> Pandas dataframe object: a dataframe with categorical variables and an aggregation variable.
        - col -> string: a string with the name of a categorical variable to be pivoted (e.g.: 'cause_code').
        - x_axis -> string: a string with the name of a categorical variable to represent the x-axis (e.g.: 'Periodo').
        - value -> string: string: a string with the name of the variable to be aggregated. In this case the variable 'Total' (number of deaths) is set as default.
    '''
    df = df.pivot_table(values=value,
                        columns=col,
                        index=x_axis,
                        aggfunc='sum')
    return df.reset_index()

