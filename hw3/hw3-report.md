Dakota Scott, HW3

Idiom: Bar Chart / Mark: Line  ('Maximum Daily Percentage Change vs Company Name')
| Data: Attribute           | Data: Attribute Type  | Encode: Channel |  
| Company Name              | key, categorical      | Color |  
| Percentage Daily Change   | value, quantititative | vertical spatial region (y-axis) |  

Idiom: Line Graph / Mark: Line ('Percentage Daily Change vs Time (year)')
| Data: Attribute           | Data: Attribute Type                  | Encode: Channel |  
| Date                      | key, quantititative (temporal)        | Horizontal spatial region X-axis|  
| Percentage Daily Change   | value, quantititative                 | vertical spatial region (y-axis) |  


Idiom: Scatter plot matrix ("Relationship of daily high and low on daily percentage increase of five different stocks")
| Data: Attribute               | Data: Attribute Type                  | Encode: Channel |  
| Company                       | key, categorical                      | color: corresponding color for each company |  
| Chart information (see below) | value, quantititative                 | vertical spatial region (y-axis) |  
  
Idiom: Scatter Plot / Mark: Dot  ("Comparison of daily high on daily percentage increase for {company}")
| Data: Attribute           | Data: Attribute Type                  | Encode: Channel |  
| Daily High                | key, quantitative                     | horizontal spatial on common scale region (x-axis) |  
| Percentage Daily Change   | value, quantititative                 | vertical spatial region (y-axis) |  
  
Idiom: Scatter Plot / Mark: Dot  ("Comparison of daily low on daily percentage increase for {company}")
| Data: Attribute           | Data: Attribute Type                  | Encode: Channel |  
| Daily Low                 | key, quantitative                     | horizontal spatial on common scale region (x-axis) |  
| Percentage Daily Change   | value, quantititative                 | vertical spatial region (y-axis) |  


Report

In order to try and find the "best" stocks to invest in, there are many ways to calculate the optimality. This exploration attempts to see if corresponding factors such as "Daily low" or "Daily high" correlate well with the daily percentage change (profit percentage for the day on any investments that day). In order to accomplish this assignment, the "all_stocks_5yr.csv" was used for all figures and calculations. It details the daily stock opening price, closing price, high price, low price, and trading volume for all stocks on the market for the past 5 years. 

In order to evaluate the data, the daily percentage change needed to be calculated. This was accomplished by using a percentage change formula of  (daily high - daily low) / (daily low). This accounts for percentage difference of increase for the day. In order to more closely examine the nature of the spikes (relatively high daily percentage changes), the five companies with the highest daily spikes were demonstrated in a bar chart, and were further the data inputs for all further calculations. To display the selection of the top 5 companies, the use of the color channel was used by illustrating the bars representing the companies as green and all other companies using the color red, to demonstrate contrast between the categorical values. Secondly, the daily percent change of the top 5 companies was plotted using a line chart, this included refining the dataset to solely the companies with the top 5 greatest daily spikes recorded. This was a comparison to potentially illustrate the temporal frequency associated with these major spikes. The magnitude of the spike; a quantitative value, was encoded using the vertical spacial region on the y-axis, whereas the temporal data was encoded using the horizontal space on the x-axis. The line chart uses different colors to differentiate between the different companies. Finally, in order to assess relationships between the daily high and low, as well as the daily percentage change, a comparison matrix was created to compare daily percentage of companies with the high or low for the corresponding day. 

In order to recreate Chart 1 from python in excel, I saved the processed information from python to a file. I then opened this file and plotted a line graph by selecting the two corresponding columns. 

In reflection, due to my prior experience, the use of python libraries for data visualization was far easier than the use of Excel. Every menu selection in a gui is still a call to a line of code, I would prefer just to type the line of code.