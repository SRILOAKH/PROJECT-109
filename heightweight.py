import pandas as pd
import csv 
import statistics
df=pd.read_csv("data.csv")
height_List=df["Height"].to_list()
weight_List=df["Weight"].to_list()
height_mean=statistics.mean(height_List)
weight_mean=statistics.mean(weight_List)
height_median=statistics.median(height_List)
weight_median=statistics.median(weight_List)
height_mode=statistics.mode(height_List)
weight_mode=statistics.mode(weight_List)
print("mean,median,mode of height is",height_mean,height_median,height_mode)
print("mean,median,mode of weight is",weight_mean,weight_median,weight_mode)
height_deviation=statistics.stdev(height_List)
weight_deviation=statistics.stdev(height_List)
height_first_stdev_start,height_first_stdev_end=height_mean-height_deviation,height_mean+height_deviation
height_second_stdev_start,height_second_stdev_end=height_mean-(2*height_deviation),height_mean+(2*height_deviation)
height_third_stdev_start,height_third_stdev_end=height_mean-(3*height_deviation),height_mean+(3*height_deviation)

weight_first_stdev_start,weight_first_stdev_end=weight_mean-weight_deviation,weight_mean+weight_deviation
weight_second_stdev_start,weight_second_stdev_end=weight_mean-(2*weight_deviation),weight_mean+(2*weight_deviation)
weight_third_stdev_start,weight_third_stdev_end=weight_mean-(3*weight_deviation),weight_mean+(3*weight_deviation)

height_List_of_data_within_1_stdev=[result for result in height_List if result>height_first_stdev_start and result<height_first_stdev_end]
height_List_of_data_within_2_stdev=[result for result in height_List if result>height_second_stdev_start and result<height_second_stdev_end]
height_List_of_data_within_3_stdev=[result for result in height_List if result>height_third_stdev_start and result<height_third_stdev_end]

weight_List_of_data_within_1_stdev=[result for result in weight_List if result>weight_first_stdev_start and result<weight_first_stdev_end]
weight_List_of_data_within_2_stdev=[result for result in weight_List if result>weight_second_stdev_start and result<weight_second_stdev_end]
weight_List_of_data_within_3_stdev=[result for result in weight_List if result>weight_third_stdev_start and result<weight_third_stdev_end]

print("{}% of data for height lies within 1 stdev".format(len(height_List_of_data_within_1_stdev)*100/len(height_List)))
print("{}% of data for height lies within 2 stdev".format(len(height_List_of_data_within_2_stdev)*100/len(height_List)))
print("{}% of data for height lies within 3 stdev".format(len(height_List_of_data_within_3_stdev)*100/len(height_List)))

print("{}% of data for weight lies within 1 stdev".format(len(weight_List_of_data_within_1_stdev)*100/len(weight_List)))
print("{}% of data for weight lies within 2 stdev".format(len(weight_List_of_data_within_2_stdev)*100/len(weight_List)))
print("{}% of data for weight lies within 3 stdev".format(len(weight_List_of_data_within_3_stdev)*100/len(weight_List)))
