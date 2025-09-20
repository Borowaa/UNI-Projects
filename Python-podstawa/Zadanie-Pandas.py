import pandas as pd


def read_data_frame(csv_file, types_row):
    type_map = {
        "INT": "Int64",
        "STRING": str,
        "CAT": "category",
        "BOOL": lambda x: x.strip().lower() in ("yes", "true"),
    }
    df = pd.read_csv(
        csv_file,
        sep=";",
        nrows=types_row,
        header=None,
        dtype=str,
        encoding="ISO-8859-1",
    )
    columns = df.iloc[0].to_list()
    types = df.iloc[1].to_list()
    dtypes = {}
    converters = {}
    for col, t in zip(columns, types):
        if t == "BOOL":
            converters[col] = type_map[t]
        else:
            dtypes[col] = type_map[t]

    df = pd.read_csv(
        csv_file,
        sep=";",
        skiprows=2,
        encoding="ISO-8859-1",
        names=columns,
        dtype=dtypes,
        converters=converters,
    )
    return df


def zadanie_1(file_name):
    df = read_data_frame(file_name, 2)
    print(df[df["Year"] == 2000])


def zadanie_2(file_name):
    df = read_data_frame(file_name, 2)
    df = df.groupby("Director")["Length"].mean()
    print(df)


def zadanie_3(file_name):
    df = read_data_frame(file_name, 2)
    df[["Title", "Director", "Popularity"]].to_csv("movies_copy.csv", index=False)


def zadanie_4(file_name):
    df = read_data_frame(file_name, 2)
    print(
        f"Procentowy udział filmów z nagrodami: {(len(df[df['Awards'] == True])/len(df))*100:.2f}%"
    )


def zadanie_5(file_name):
    df = read_data_frame(file_name, 2)
    print(df[df["Director"].str.contains("kubrick", case=False, na=False)])


def zadanie_6(file_name):
    df = read_data_frame(file_name, 2)
    comedy_sum = df[df["Subject"].str.lower() == "comedy"]["Popularity"].sum()
    print(comedy_sum)


print("Zadanie 1:")
zadanie_1("movies.csv")
print("==============")
print("Zadanie 2:")
zadanie_2("movies.csv")
print("==============")
print("Zadanie 3:")
zadanie_3("movies.csv")
print("==============")
print("Zadanie 4:")
zadanie_4("movies.csv")
print("==============")
print("Zadanie 5:")
zadanie_5("movies.csv")
print("==============")
print("Zadanie 6:")
zadanie_6("movies.csv")