#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import os
import new_bing_search
import urlKeywordSearch
import wordParser_LexTo
import ngrams
import extract_feature
import merge_test_data_to_csv
from collections import defaultdict
import time

MODEL_DIR_PATH = './model/'

INPUT_PATH = './number_input.txt'
NEW_FORMAT_INPUT_PATH = './new_number_input.txt'
UNKNOWN_NUMBER_INPUT_PATH = './unknown_number_input.txt'

# Categories which will be predicted from models
N_MODEL = 4
PREDICTED_CATEGORIES = ['airline', 'accommodation', 'tourism', 'restaurant']

# Target categories
START_CATEGORY_COLUMN_INDEX = 4
CATEGORIES = [
    'airline', 'accommodation', 'tourism', 'restaurant',
    'travel_hotel', 'travel_resorts_bungalows', 'travel_travel_bureaus',
    'travel_bus_lines', 'travel_air_travel_ticket_agencies', 'travel_airline_companies',
    'travel_travel_homestay', 'travel_travel_hotel_reservation_services',
    'travel_travel_museums', 'hotel_lounge', 'thai', 'bakery_cake', 'dessert',
    'chinese', 'japanese', 'seafood', 'sukiyaki_shabu', 'fast_food', 'delivery'
]

def import_yellow_pages_db(file_name_in="./yellowpages.csv"):
    is_first_line = True
    phone_cat = defaultdict(dict)
    with open(file_name_in) as pearl:
        for line in pearl:
            if is_first_line:
                headers = line.split(',', START_CATEGORY_COLUMN_INDEX)
                categories = [cat.strip() for cat in headers[START_CATEGORY_COLUMN_INDEX].split(',')]
                is_first_line = False
                continue
            else:
                row_data = line.split(',', START_CATEGORY_COLUMN_INDEX)
                phone_num = row_data[1].strip().replace("-", "")
                is_category_values = row_data[START_CATEGORY_COLUMN_INDEX].strip().split(',')
                for idx, val in enumerate(is_category_values):
                    if categories[idx] in CATEGORIES:
                        phone_cat[phone_num][categories[idx]] = True if val == '1' else False
    return phone_cat


def load_model(filename_in):
    f = open(filename_in, 'r')
    classifier = pickle.load(f)
    f.close()
    return classifier


def import_test_data(filename='./temp-processing-data/05_merge-csv/test_data.csv'):
    featuresets = []
    mobile_no = []
    with open(filename, 'r') as fin:
        for line in fin:
            num, words = line.split(",", 1)

            # phone_no = num.strip()
            if len(words.strip()) == 0:
                words = dict()
            else:
                words = dict([x.split(':') for x in words.strip().split(' ')])
                words = dict((k, float(v)) for k, v in words.iteritems())

            featuresets.append(words)
            mobile_no.append(num)
    return (mobile_no, featuresets)


def process_data(filename_in='./number_input.txt'):
    new_bing_search.runBingSearch(filename_in)
    urlKeywordSearch.search()
    wordParser_LexTo.parseAllDocuments(path_in='./temp-processing-data/01_raw-data-keyword/')
    ngrams.applyNgramAllDocuments()
    extract_feature.extract_feature()
    merge_test_data_to_csv.mergeResultToCSV()


def check_yellowpages(filename_in, phone_no_cat_db):
    phone_cat = {}
    fout = open(UNKNOWN_NUMBER_INPUT_PATH, 'w')
    with open(filename_in) as pearl:
        for num in pearl:
            num = num.strip()
            if num.replace("-", "") in phone_no_cat_db:
                # print 'phone number : ', num, " >> YELLOW PAGES DATABASE"
                phone_cat[num] = phone_no_cat_db[num.replace("-", "")]
            else:
                fout.write(num+'\n')
    return phone_cat


def change_format_phone(file_name_in, file_name_out):
    fout = open(file_name_out, 'w')
    with open(file_name_in) as pearl:
        for num in pearl:
            num = num.strip()
            if len(num) == 9:
                fout.write(num[0:2]+'-'+num[2:5]+'-'+num[5:9]+'\n')
            elif len(num) == 10:
                fout.write(num[0:3]+'-'+num[3:6]+'-'+num[6:10]+'\n')
            else:
                fout.write(num+'\n')


def predict(filename_in='./number_input.txt', filename_out='./results/result.csv'):
    change_format_phone(filename_in, NEW_FORMAT_INPUT_PATH)

    # Seperate between phone numbers which are (in / not in) yellowpages
    #     and read categories from yellowpages
    phone_no_cat_db = import_yellow_pages_db()
    phone_cat = check_yellowpages(NEW_FORMAT_INPUT_PATH, phone_no_cat_db)

    # Categorize the category of (ONLY) unknown phone number
    process_data(UNKNOWN_NUMBER_INPUT_PATH)
    
    mobile_no, test_data = import_test_data()
    if mobile_no and test_data:
        for model_id in range(1, N_MODEL+1):
            # Load Classification Model
            model_file_name = 'sklearn_model_%02d.pickle' % model_id
            model_file_path = os.path.join(MODEL_DIR_PATH, model_file_name)
            print "Model#%d:" % model_id, model_file_path
            classifier = load_model(model_file_path)

            this_cat_name = PREDICTED_CATEGORIES[model_id - 1]
            for row_i, test_case in enumerate(test_data):
                this_mobile_no = mobile_no[row_i]
                if test_case == {}:
                    phone_cat[this_mobile_no][this_cat_name] = False
                    print 'phone number : ', this_mobile_no, " >> NOT   "
                else:
                    result_class = classifier.predict(test_case)
                    result_class = result_class[0]
                    phone_cat[this_mobile_no][this_cat_name] = True if result_class >= 0.6 else False
                    print 'phone number : ', this_mobile_no, " >>", result_class
    else:
        print "No prediction required."

    # Write Result
    with open(filename_out, 'w') as file_out:
        ## Print the header of target file
        file_out.write('mobile_no,')
        file_out.write(','.join(CATEGORIES))
        file_out.write('\n')

        ## Print the body of target file
        for num_key in phone_cat:
            file_out.write(num_key.replace("-", ""))
            for cat in CATEGORIES:
                if cat in phone_cat[num_key]:
                    file_out.write(',1' if phone_cat[num_key][cat] else ',0')
                else:
                    file_out.write(',0')
            file_out.write('\n')

    print "Success :: Result is saved !"


def run(filename_in=INPUT_PATH, filename_out=None):
    if filename_out is None:
        dt = time.strftime("%Y%m%d_%H-%M", time.localtime())
        filename_out = './results/result'+dt+'.csv'
    predict(filename_in, filename_out)


if __name__ == '__main__':
    run()