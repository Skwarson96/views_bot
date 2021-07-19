# views_bot

Script created for fun to prank my colleaue from collage. I wanted increase number of visitors on his github profile. 
Total using the script I did more than 780k of views. During the great fun of watching the counter increasing. I came up with an idea to make time prediction
of single use of the script.


The steps I have taken:
 - So at the begining I made train dataset by: create_dataset.py
 - Then fill these dataset with data by using: collect_train_data.py
 - Then I repeated the previous steps but for test dataset (created by: create_dataset.py and fill by collect_test_data.py)
 - And finally, I analyzed the results in conclusions.py
 
 ## Requirements
In requirements.txt and to change IP adress I use TOR.
I support with these sites:
- https://stackoverflow.com/questions/30286293/make-requests-using-python-over-tor
- https://github.com/umarfarook882/Blog-Views-Bot

 ## How it works
 To single use of these 'project':
 ```
  python3 main.py thread_number iter_1 iter_2
  ```
 - thread_number - is the number of threads you want to use I tested on max 10 threads
 - iter_1 - is how many times you want to make request to site using new single IP adress
 - iter_2 - is how many times you want to make request to site using IP adress selected in the previous step 
 
 ### Example
 Choosing a command:
 ```
 python3 main.py 5 5 2
 ```
 you will use 5 threads and 5 times you will change IP address but every of these IP adresses will be use 2 times. So
 you will be make 50 requests. 
 
 ## Time prediction
 To predict time I compared the action of regressors from sklearn library: RandomForrestRegressor, SVR, DecisionTreeClassifier and LinearRegressor.
 The best of them to these task was DecisionTreeClassifier.
 
<p align="center">
<img src="https://github.com/Skwarson96/views_bot/blob/main/plots_and_imgs/plot_dtr.png" />
</p>
Not counting a few error values caused by breaking the internet connection prediction on plot looks good. 

## Best parameters
On my laptop and my internet connection the best number of threads is between 7-9. iter_1 and iter_2 parameters should be not to high, for me its about 20 for iter_1 
and 2-3 for iter_2. For these parameters number of requests per second is the greatest and number of true requests is closest to planned number. 
Because the greater the values of these parameters, the greater the difference between the number of planned requests and the number of true requests.
<p align="center">
<img src="https://github.com/Skwarson96/views_bot/blob/main/plots_and_imgs/req_time_ratio.png" />
</p>

<p align="center">
<img src="https://github.com/Skwarson96/views_bot/blob/main/plots_and_imgs/threads_ratio_scatter.png" />
</p>


I only tested it on one site, I don't know if it will work for others sites. Remember you use it at your own risk.
