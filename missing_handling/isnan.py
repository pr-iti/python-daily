import numpy as np
# isnan, nan_to_num,isinf
#np.isnan(arr)
arr1 = np.array([10, 20, 30, np.nan, 50, np.nan, 70, 80, np.inf, 800, 900, -np.inf, 23, 45])

# print(arr1)
# print(np.isnan(arr1))

# -------------------  .nan_to_num(arr,nan=value)  -----------------
print(np.nan_to_num(arr1, nan=20, posinf=2000, neginf=9000))

# ---------------------- .isinf ------------
# print(np.isinf(arr1))

# print(np.nan_to_num(arr1,posinf=2000,neginf= 9000,nan =3333))