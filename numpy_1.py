import numpy as np 

# arryy=np.array([0,1,2,3,4,5])
# print(arryy)

#[0 1 2 3 4 5]

# zeros_array=np.zeros(6)
# print(zeros_array)

# [0. 0. 0. 0. 0. 0.]

# ones_array=np.ones((2,3))
# print(ones_array)

# filled_array=np.full((2,2),7)
# print(filled_array)

# arange_array=np.arange(1,10,2)
# print(arange_array)

# identity_matrix=np.eye(3)
# print(identity_matrix)

# array_2d=np.array([[1,2,3],
#                    [4,5,6]])
# print(array_2d.shape)

# array_size=np.array([[1,2,3],[4,5,6]])
# print(array_size.size)

# array_1d=np.array([1,2,3])
# array_2d=np.array([[1,2],[3,4]])
# array_3d=np.array([[[1,2],[3,4],[5,6],[7,8]]])

# print(array_1d.ndim)
# print(array_2d.ndim)
# print(array_3d.ndim)

# arry=np.array([1,23,4,3,56,43,65])
# print(arry.dtype)

# arry=np.array([1,2.3,4,3,56,43,6.5])
# print(arry.dtype)

# arry=np.array(['dev','gupil','piyush'])
# print(arry.dtype)

# arrry=np.array([1.2,3.4,5.6])
# print(arrry.dtype)
# aarry=arrry.astype(int)
# print(aarry.dtype)


# # calc_array=np.array([2,3,4,5,6])
# # print(calc_array + 2)
# # print(calc_array * 10)
# # print(calc_array  - 2)
# # print(calc_array / 2)

# # calc_array=np.array([2,3,4,5,6])
# # print(np.sum(calc_array))
# # print(np.mean(calc_array))
# # print(np.min(calc_array))
# # print(np.max(calc_array))
# # print(np.std(calc_array))
# # print(np.var(calc_array))

# indx_array=np.array([20,30,40,50,60])
# print(indx_array[0])
# print(indx_array[2])
# print(indx_array[-1])


# slic_array=np.array([10,20,30,40,50,60])
# print(slic_array[0:5])
# print(slic_array[:5])
# print(slic_array[1:4])
# print(slic_array[::2])
# print(slic_array[::-1])


# fancyidx_array=np.array([10,20,30,40,50,60])
# print(fancyidx_array[[0,3,5]])
# print(fancyidx_array[[1,2]])

# boolmask_array=np.array([10,20,30,40,50,60])
# print(boolmask_array[ boolmask_array>=20])

# rray=np.array([10,20,30,40,50,60])
# reshape_arr=rray.reshape(2,3)
# print(reshape_arr)

# arraryy=np.array([[1,2,3],[4,5,6]])
# print(arraryy.ravel())
# print(arraryy.flatten())


# aray=np.array([10,20,30,40,50,60])
# print(aray)
# rearay=np.insert(aray,2,100)
# print(rearay)

# arrayy_2d=np.array([[1,2],[3,4]])
# print(arrayy_2d)
# rearrayy_2d=np.insert(arrayy_2d,2,[5,6],axis=0)
# print(rearrayy_2d)
# rearrayy_2d=np.insert(arrayy_2d,2,[5,6],axis=1)
# print(rearrayy_2d)
# rearrayy_2d=np.insert(arrayy_2d,2,[5,6],axis=None)
# print(rearrayy_2d)

# araay=np.array([10,20,30])
# print(araay)
# rearaay=np.append(araay,[40,50,60])
# print(rearaay)

# array1=np.array([0,1,2])
# array2=np.array([3,4,5])
# new_array=np.concatenate((array1,array2))
# print(new_array)
# new_array=np.concatenate((array1,array2),axis=0)
# print(new_array)

# arra=np.array([0,1,2,3,4,5])
# print(arra)
# new_arra=np.delete(arra,0)
# print(new_arra)

# arra_2d=np.array([[0,1,2],[3,4,5]])
# print(arra_2d)
# new_arra_2d=np.delete(arra_2d,0,axis=None)
# print(new_arra_2d)
# new_arra_2d=np.delete(arra_2d,0,axis=0)
# print(new_arra_2d)
# new_arra_2d=np.delete(arra_2d,0,axis=1)
# print(new_arra_2d)

# aarra1=np.array([0,1,2])
# aarra2=np.array([3,4,5])
# new_aarra1=np.vstack(((aarra1,aarra2)))
# new_aarra2=np.hstack(((aarra1,aarra2)))
# print(new_aarra1)
# print(new_aarra2)

# arrar=np.array([0,1,2,3,4,5])
# print(np.split(arrar,2))




# prices=np.array([100,200,300])
# discount=10
# finalprices=prices-(prices*discount/100)
# print(finalprices)

# arr=np.array([100,200,300])
# result=arr*2
# print(result)



# arr=np.array([[1,2,3,],[4,5,6]])
# arr2=np.array([10,20,30])
# result=arr+arr2
# print(result)




# arr=np.array([[1,2,3,],[4,5,6]])
# arr2=np.array([10,20])
# result=arr+arr2
# print(result)

# arr=np.array([1,2,3])
# arr2=np.array([10,20,30])
# result=arr+arr2
# print(result)




# arr=np.array([4,5,6])
# arr2=np.array([10,20,30])
# result=arr*arr2
# print(result)




# arr2=np.array([10,20,np.nan,30])

# print(np.isnan(arr2))





# arr2=np.array([10,20,23,30])

# print(np.isnan(arr2))


# print(np.nan==np.nan)





# arr2=np.array([10,20,np.nan,23,30,np.nan,np.nan])

# neww=np.nan_to_num(arr2,nan=100)
# print(neww)




# arr2=np.array([10,20,np.nan,23,30,np.nan,np.nan])

# neww=np.nan_to_num(arr2)
# print(neww)



# arr2=np.array([10,20,np.inf,23,30])

# neww=np.isinf(arr2)
# print(neww)






# arr2=np.array([10,np.inf,20,np.nan,23,30,np.inf,np.nan,np.inf])

# neww=np.nan_to_num(arr2,posinf=100,neginf=-100)

# print(neww)