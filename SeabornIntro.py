import pandas as pd
import seaborn.objects as so
import matplotlib as plt
def main():
    penguins = pd.read_csv("https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv")
    penguins.head()
    (
        so.Plot(penguins, x="bill_length_mm", y="bill_depth_mm")
        .add(so.Dot())
    )

    x = (
        so.Plot(penguins, x="species", y="body_mass_g", color="sex") 
        .add(so.Bar(), so.Agg(), so.Dodge())
    )
    y = x.save("Penguins 2")
    

if __name__ == "__main__":
    main()