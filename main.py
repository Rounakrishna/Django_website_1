# def maxSubArray(nums):
#         max_sum = 0
#         n = len(nums)
#         for i in range(n):
#             for j in range(1,i):
                
#         # max_sum = max(max_sum,)
#         return max_sum


# nums = [-2,1,-3,4,-1,2,1,-5,4]
# # print(maxSubArray(nums))

# def bubblesort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0,n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#                 swapped = True
#         if not swapped:
#             break              
#     return arr

# arr = [6,4,8,2,9,1,8]
# # print(bubblesort(arr))

# class employ:
#     company = "apple"
#     def __init__(self,name):
#         self.name = name
#         self.raise_amount = 0.02
#     def showDetail(self):
#         print(f"{self.name},{self.raise_amount},{self.company}")

# emp=employ("krishna")
# emp1=employ("nemat")
# emp.company="Apple_india"
# emp.raise_amount = 23
# emp1.showDetail()
# emp.showDetail()


# def count_leap_years(start_year, end_year):
#     lst = []
#     for year in range(start_year,end_year+1):
#         if year %4 == 0:
#             if year % 100 == 0:
#                 if year % 400 ==0:
#                     lst.append(year)
                
#     return lst
       
# start_year = 2000
# last_year = 2024
# print(count_leap_years(start_year,last_year))

def dayOfYear(date):
        result = date.split("-")
        return int(result[2])

date ="2019-01-09" 
print(dayOfYear(date))