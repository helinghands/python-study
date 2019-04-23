import pandas as pd
def getData(file_name):
    data=pd.read_csv(file_name)
    X_parameter=[]
    Y_parameter=[]
    for single_meter_feet,single_price_value in zip(data['sqaure_meter'],data['price']):
        X_parameter.append([float(single_meter_feet)])
        Y_parameter.append(float(single_price_value))
        return X_parameter,Y_parameter
#def linear_model_main(X_parameter,Y_parameter,predict_square_meter):
    #regr = LinearRegression()
