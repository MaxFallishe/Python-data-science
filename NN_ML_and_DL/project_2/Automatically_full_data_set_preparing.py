#link - https://github.com/ageron/handson-ml/blob/master/02_end_to_end_machine_learning_project.ipynb

#If the data is not displayed, then it's worth trying to add print ()
#Example: test_set.head() - isn't displayed,    print(test_set.head()) - displayed

#If the graph is not built then you need to add plt.show ()
#Example: line 102 and 103 


#If yo can't save the graphic try to use plt.savefig() instead save_fig()
#Example line 157 - 167
import os
import tarfile
from six.moves import urllib



DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

fetch_housing_data()

import pandas as pd

pd.set_option('display.expand_frame_repr', False)  #чтобы показывались все столбцы


def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

housing = load_housing_data()

#при повторении затести эти строки
#housing.head() - верхние 5 cтрок

#housing.info() - краткое описание данных, а именно общего числа строк, тип и количества ненулевых значения

#housing.describe() - отображает сводку о числовых атрибутах


import matplotlib.pyplot as plt

#housing.hist(bins=50, figsize=(20,15))
#plt.show()


#Test dataset preparing
#↓↓↓↓↓
import numpy as np

np.random.seed(42)   # to make this notebook's output identical at every run



# For illustration only. Sklearn has train_test_split()
def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


train_set, test_set = split_train_test(housing, 0.2)
print(len(train_set), "train +", len(test_set), "test")   #16512 train + 4128 test


import hashlib

def test_set_check(identifier, test_ratio, hash):
    return hash(np.int64(identifier)).digest()[-1] < 256 * test_ratio

def split_train_test_by_id(data, test_ratio, id_column, hash = hashlib.md5):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio, hash))
    return data.loc[~in_test_set], data.loc[in_test_set]


housing_with_id = housing.reset_index()   # adds an `index` column
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "index")

housing_with_id["id"] = housing["longitude"] * 1000 + housing["latitude"]
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "id")

#print(test_set.head())


from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)

#print(test_set.head())


#housing["median_income"].hist()
#plt.show()


#last line OUT[21]



# Divide by 1.5 to limit the number of income categories# Divide 
housing["income_cat"] = np.ceil(housing["median_income"] / 1.5)
# Label those above 5 as 5
housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)

print(housing["income_cat"].value_counts()) # need print


#housing["income_cat"].hist()
#plt.show()


from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

#print(strat_test_set["income_cat"].value_counts() / len(strat_test_set))

#print(housing["income_cat"].value_counts() / len(housing)



#Сравнивание  рандомной и стратифицированной выборки
#def income_cat_proportions(data):
#    return data["income_cat"].value_counts() / len(data)
#
#train_set, test_set = train_test_split(housing, test_size=0.2, random_state=42)
#
#compare_props = pd.DataFrame({
#    "Overall": income_cat_proportions(housing),
#    "Stratified": income_cat_proportions(strat_test_set),
#    "Random": income_cat_proportions(test_set),
#}).sort_index()
#compare_props["Rand. %error"] = 100 * compare_props["Random"] / compare_props["Overall"] - 100
#compare_props["Strat. %error"] = 100 * compare_props["Stratified"] / compare_props["Overall"] - 100
#print(compare_props)


for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat", axis=1, inplace=True)


#Discover and visualize the data to gain insights#

housing = strat_train_set.copy()

housing.plot(kind="scatter", x="longitude", y="latitude")
plt.savefig("bad_visualization_plot")


housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.1)
plt.savefig("better_visualization_plot")
housing.plot(kind="scatter", x="longitude",  y="latitude", alpha=0.4,
    s=housing["population"]/100, label="population", figsize=(10,7),
    c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,
    sharex=False)

plt.legend()
plt.savefig("housing_prices_scatterplot")


