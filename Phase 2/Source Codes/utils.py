def extract_hour_from_string(s):
    if s and len(s) in [3, 4]:
        return int(s[:-2])
    else:
        return None 

def get_col_data_type(spark_df, type='num'):
    """
    type: string, ['num', 'string']
    """    
    cols_types = spark_df.dtypes
    cols = []
    if type == 'num':
        cols = [col[0] for col in cols_types if col[1] in ['int', 'float']]
    elif type == 'string':
        cols = [col[0] for col in cols_types if col[1] in ['string']]
    else:
        raise ValueError('Please specify either num or string for type arg.')
    return cols

def imputer_method(input_cols, method='mean'):
    if input_cols:
        try:
            return Imputer(
                    inputCols=input_cols,
                    outputCols=input_cols
                    ).setStrategy("mean")
        except:
            raise ValueError('Method has to be mean, median or mode') 
    else:
        raise ValueError('Input col is empty')
    