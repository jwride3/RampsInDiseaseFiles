# RampsInDiseaseFiles
Files for the Ramps in Disease Project in the Ridge Lab

main.py filters by uniqueness and p_value
Its parameters are: 
1 - Text File containing the path names for all the Input files
2 - Output File name
3+ - Each filter word for the phenotype. Need at least 1 but can use more


main2.py starts sorting rsIDs by chromosome
Paramters:
1 - tsv file name containing the filtered traits for that disease found in main.py
2 - The name of the disease to be used to create a folder
