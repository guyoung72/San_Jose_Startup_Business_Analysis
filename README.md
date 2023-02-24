# 🗺️Unlaunched Startup Project

Our team is planning to launch a local startup in San Jose by May 2023. I won't tell what exactly the startup is about, but I can say it is a consumer service startup.

I am doing the analytics work for them so they can reach their ambitious goals.

## I am helping them out with analytics including:<br>
🗺️ Analyze and visualize potential service areas via Bokeh and Google Maps API<br>
📑 Manage a dataset of +1,000 addresses to target areas by day to advertise the service & product<br>
📈 Communicate with CEO to plan marketing and service operation based on analysis results<br>

I will be using Python Jupyter Notebook for this repo. All address found in the 'data' folder do not represent actual customers' locations. They were selected purely randomly.
<br><br>
Download the interactive map here: https://drive.google.com/file/d/1s_XeUPESZlX9uedfrWVnx5nNeoPoVvnR/view?usp=sharing
<br><br>
<img width="1157" alt="image" src="https://user-images.githubusercontent.com/79275984/221008897-c2112051-246c-4b23-b463-c48267e23314.png">

Above is a image of "Potential_Customers_Map" in my repo. Any information uploaded in this repo will not include actual customer information for privacy purposes (all geographic information uploaded here are not actual customers' addresses).
<br><br>
![Honeycam 2023-02-23 16-55-02](https://user-images.githubusercontent.com/79275984/221065658-4e9e414c-5dd1-4b84-9131-0e388f282893.gif)<br>
Above is a GIF of my selenium web scraper collecting data from our Google Maps address list of potential customers. It automatically scrolls through thousands of addresses and collects only the street addresses and zip codes and puts them into one dataframe. A csv file containing all the addresses is created after the process. If anyone of our team adds or deletes data, this web scraper helps us our dataset keep updated - without having the need of copying and pasting all them into an Excel file by hand.
<br><br>
![170441](https://user-images.githubusercontent.com/79275984/221067216-d1350d11-7099-447a-aa56-6b6d24f2c5e9.jpg)
<br>
After concating addresses into one dataframe, I convert them into geocodes (latitude & longtitudes) using the Google Maps API. The reason of doing so is because using Bokeh & GMaps requires coordinates. I will use Bokeh, an Python data visualization package useful for interactive visualizations (basically it lets users to interact with the data, rather than just being a static graph image).
<br><br>
![image](https://user-images.githubusercontent.com/79275984/221067794-7aeb4f84-7183-483a-8092-e3d73b304f82.png)
<br> (To see the full code, take a look at the file "San Jose Potential Customers.")
<br><br><img width="1157" alt="image" src="https://user-images.githubusercontent.com/79275984/221008897-c2112051-246c-4b23-b463-c48267e23314.png">
