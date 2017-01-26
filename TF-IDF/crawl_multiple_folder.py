import urlKeywordSearch

include_content = True

url_folder_names = ['00_url_Bakery Cake','00_url_Barbeque Grill','00_url_Coffee Shop','00_url_Ice Cream','00_url_Japanese','00_url_Lounge Hotel Restaurant','00_url_Seafood','00_url_Sukiyaki Shabu','00_url_Travel Bureaus']
raw_folder_names = ['01_raw-data_Bakery Cake', '01_raw-data_Barbeque Grill', '01_raw-data_Coffee Shop', '01_raw-data_Ice Cream', '01_raw-data_Japanese', '01_raw-data_Lounge Hotel Restaurant', '01_raw-data_Seafood', '01_raw-data_Sukiyaki Shabu', '01_raw-data_Travel Bureaus']

n_category = min(len(url_folder_names), len(raw_folder_names))
for i in range(n_category):
    url_folder_name = url_folder_names[i]
    raw_folder_name = raw_folder_names[i]

    path_url = './temp-processing-data/'+url_folder_name
    path_raw_data = './temp-processing-data/'+raw_folder_name+'/01_raw-data/'
    path_raw_data_keyword = './temp-processing-data/'+raw_folder_name+'/01_raw-data-keyword/'
    path_raw_data_content = './temp-processing-data/'+raw_folder_name+'/01_raw-data-content/'
    urlKeywordSearch.search(path_url, path_raw_data, path_raw_data_keyword, path_raw_data_content, include_content)