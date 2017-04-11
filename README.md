# spikenn
- problem - find spikes in calcium imaging data
- solution
    - cnn
    - rnn?
    - gan?

# spikefinder-datasets

This README describes how to load the datasets for the spikefinder analysis benchmarking challenge. You probably received this document when downloading a dataset. Visit the [spikefinder](https://github.com/codeneuro/spikefinder) repository for more information on the challenge.

Training datasets are provided with ground truth in CSV format. There are ten training datasets numbered `1-10`, and five testing datasets numbered `1-5`. For each one there is a `calcium` file with calcium flouresence signals, and a `spikes` file with spike rates, both sampled at a common rate of `100 Hz`. The columns of each table are neurons, and the rows are time points. In a given dataset, some neurons will have slightly different numbers of time points than others, this is expected.

Along with the data itself, each download includes example loading scripts in python and matlab, the source code of which is in this reposistory.

To contribute example loading scripts for other languages, just submit a pull request! If there are problems with the loading scripts, create a GitHub issue.

# data sizes
- train/1
0 71986 1 71986 2 35993 3 71985 4 71986 5 71986 6 71986 7 71985 8 71986 9 59717 10 71986 
- train/2
0 35508 1 35508 2 35508 3 35508 4 35508 5 33685 6 35508 7 35508 8 27414 9 35508 10 35508 11 32049 12 35508 13 35508 14 35508 15 35508 16 25709 17 35508 18 21252 19 31077 20 9682 
- train/3
0 53229 1 53229 2 24401 3 20014 4 27003 5 16802 6 53229 7 53229 8 53229 9 53229 10 53229 11 53229 12 53229 
- train/4
0 27763 1 27763 2 27763 3 27763 4 27763 5 27763 
- train/5
0 16919 1 16919 2 16919 3 16919 4 16919 5 16919 6 16919 7 16919 8 16919 
- train/6
0 23998 1 23998 2 5998 3 23998 4 9598 5 23998 6 19198 7 19198 8 23998 
- train/7
0 23973 1 23973 2 23973 3 23973 4 23973 5 23973 6 23973 7 23973 8 23973 9 23973 10 23972 11 23972 12 23970 13 23970 14 23970 15 21715 16 23971 17 23971 18 23971 19 23971 20 23971 21 23971 22 23971 23 23971 24 23971 25 23971 26 23971 27 23971 28 23971 29 23970 30 23970 31 23970 32 23970 33 23970 34 23970 35 23970 36 23970 
- train/8
0 23973 1 11986 2 23973 3 23973 4 23973 5 23973 6 23972 7 23973 8 23973 9 23973 10 23973 11 23973 12 23973 13 23973 14 23973 15 23973 16 23973 17 23973 18 23973 19 23973 20 23973 
- train/9
0 31959 1 15475 2 31959 3 31954 4 31954 5 31959 6 31959 7 31956 8 31956 9 31959 10 31959 11 31959 12 31956 13 23966 14 31957 15 6486 16 31957 17 31957 18 31957 19 31959 
- train/10
0 31994 1 31994 2 31994 3 31964 4 31964 5 31957 6 19496 7 31959 8 10999 9 9698 10 10138 11 18498 12 13179 13 5507 14 31994 15 18757 16 22503 17 31994 18 31994 19 31994 20 31962 21 31962 22 31963 23 31966 24 31965 25 31965 26 31962 
- test/1
0 71984 1 35992 2 71984 3 71984 4 71984 
- test/2
0 77873 1 34667 2 69617 3 9198 4 47674 5 38004 6 47691 7 45558 8 42456 9 26650 
- test/3
0 55769 1 55769 2 55769 3 55769 4 34173 5 26236 
- test/4
0 33280 1 33280 2 30810 
- test/5
0 16919 1 16919 2 16919 3 16919 4 16919 5 1700 6 2501 7 11720 
