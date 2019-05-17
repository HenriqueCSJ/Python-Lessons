import pandas as pd

housing = pd.read_csv("cal_housing_clean.csv")

housing.head()

# Separando as variáveis (features) e as respostas

y_val = housing["medianHouseValue"]
x_data = housing.drop("medianHouseValue", axis=1)

x_data
y_val

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x_data, y_val, test_size=0.3, random_state=101)

# Scale the feature data

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(X_train)

X_train = pd.DataFrame(data=scaler.transform(X_train), columns=X_train.columns, index=X_train.index)
X_train

X_test = pd.DataFrame(data=scaler.transform(X_test), columns=X_test.columns, index=X_test.index)

# Create feature columns

housing.columns

import tensorflow as tf

age = tf.feature_column.numeric_column("housingMedianAge")
rooms = tf.feature_column.numeric_column("totalRooms")
bedrooms = tf.feature_column.numeric_column("totalBedrooms")
pop = tf.feature_column.numeric_column("population")
households = tf.feature_column.numeric_column("households")
income = tf.feature_column.numeric_column("medianIncome")

# Agregando todas as features em uma variável
feat_cols = [age, rooms, bedrooms, pop, households, income]
feat_cols

input_func = tf.estimator.inputs.pandas_input_fn(x=X_train,
                                                 y=y_train,
                                                 batch_size=10,
                                                 num_epochs=1000,
                                                 num_threads=4,
                                                 shuffle=True)

model = tf.estimator.DNNRegressor(hidden_units=[4, 6, 6, 4], feature_columns=feat_cols)

model.train(input_fn=input_func, steps=200000)

# Não uso um valor de y porque estou agora prevendo os resultados
# Também preciso apenas de 1 epoch
predic_input_func = tf.estimator.inputs.pandas_input_fn(x=X_test,
                                                       batch_size=10,
                                                       num_epochs=1,
                                                       shuffle=False)

pred_gen = model.predict(predic_input_func)
predictions = list(pred_gen)
predictions

final_preds = []

for pred in predictions:
    final_preds.append(pred["predictions"])

from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, final_preds)**0.5