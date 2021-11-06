df_c_ACC <- read_csv("Desktop/oddball-analysis/data/df_c_ACC.csv", 
                          col_types = cols(...1 = col_skip()))
df_d_ACC <- read_csv("Desktop/oddball-analysis/data/df_d_ACC.csv", 
                          col_types = cols(...1 = col_skip()))
t.test(df_c_ACC,df_d_ACC, var.equal = T)
d = 0.012277*sqrt((length(df_c_ACC)+length(df_d_ACC))/length(df_c_ACC)*length(df_d_ACC))
print(d)
