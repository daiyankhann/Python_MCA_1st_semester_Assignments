Total_Population = 80000

Percentage_of_men = 52

Percentage_of_total_literacy = 48

Percentage_of_literate_men = 35

Total_men = (Percentage_of_men / 100) * Total_Population

Total_women = Total_Population - Total_men

Total_literate_people = (Percentage_of_total_literacy / 100) * Total_Population

Literate_men = (Percentage_of_literate_men / 100) * Total_Population

Literate_women = Total_literate_people - Literate_men

Illiterate_men = Total_men - Literate_men

Illiterate_women = Total_women - Literate_women

print(f"Number of Illiterate men: {Illiterate_men}")

print(f"Number of Illiterate women: {Illiterate_women}")
