

# AutoEGFN

We provide a computer-aided proof tool called AutoEGFN to determine the number of rounds sufficient for PRP and SPRP security for various variants of EGFN. This tool is constructed by calculating three parameters: $r_1$, $r_2$, and $r_3$.
To show the effectiveness of AutoEGFN, we have applied it to multiple structures such as Type-1/2, Type 1.x, SH/TH GFN, SM10's GFN, Nyberg's GFN, and BMT's EGFN.

The naming convention of files: structure-di-rj.xxx

structure: the name of the structure;

i: branch numbers, such as $4$, $6$, $8$;

j: representing the parameters $r_1$, $r_2$, or $r_3$;

xxx: file suffix.

### file structures
```
filetree
├── README.md
├── /DDGP22/
├── /DFLM19/
├── /EGFN/
├── /Nyberg GFN/
├── /SH GFN and TH GFN/
├── /SM10 GFN/
├── /Type 1.x/
├── /Type-1/
└── /Type-2/
├── /YI11 Type-1/
```

### Required softwares

1. STP (version 2.3.3), z3 (version 4.15.4)
2. Python 3.11.3
3. SageMath 9.3

### Run command

1. Calculate $r_1$ and $r_3$:
The variable that needs to be modified in the "structure-di-rj.py" file is 'target' defined in the "main" function.

```sh
cd ./EGFN
python3 egfn-d4-r1.py
```

The output is the solution searched by STP solver in each round. If no solution is found in the r-th round, then output variable is $max-r_1 = r-1$ or $max-r_3 = r-1$.



2. Calculate $r_2$:
The variable that needs to be modified in the "structure-di-r2.ipynb" file is 'round_number' defined in the first line, which defines the round numbers.

```sh
Open SageMath 9.3 Notebook
Enter the folder EGFN
run egfn-d4-r2.ipynb
```

The output is the matrix and the rank of the output ciphertext with respect to the round functions in 'round_number'-th round. If the matrix is full rank, we have $r_2 =$ round_number.


### Notion
Since the running time of the program falls within an acceptable range, we only included the code for running with stp in the provided program. During the program's execution, corresponding smt files will be generated (the "remove_file" function needs to be deactivated). Therefore, other solvers can be used to run these smt files for solving.
