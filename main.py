import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
import plotly
import plotly.graph_objs as go
import json
import requests
import re
import sklearn
import networkx as nx
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_predict



with st.echo(code_location='below'):
    st.title("Социально-экономические показатели стран")
    def print_hello(name="world"):
        st.write(f"## Привет, {name}!")
    name = st.text_input("Your name", key="name", value="Anonymous")
    print_hello(name)
    st.subheader("В этом проекте мы рассмотрим динамику некоторых экономических и социальных характеристик стран, а также посмотрим, как эти показатели взаимодействуют между собой")
    st.caption('Часть кода с поиском информации доступна по ссылке ниже:')
    st.markdown("https://github.com/soceconproj/firstpart/tree/main")
    st.subheader('Здесь представлена таблица, в которой можно увидеть основную информацию о странах в последние годы')
    first_df = pd.DataFrame({'Country': {0: 'Albania', 1: 'Algeria', 2: 'Angola', 3: 'Argentina', 4: 'Armenia', 5: 'Austria', 6: 'Azerbaijan', 7: 'Bangladesh', 8: 'Belarus', 9: 'Belgium', 10: 'Belize', 11: 'Bhutan', 12: 'Bolivia', 13: 'Bosnia and Herzegovina', 14: 'Botswana', 15: 'Brazil', 16: 'Bulgaria', 17: 'Burundi', 18: 'Cabo Verde', 19: 'Canada', 20: 'Central African Republic', 21: 'Chile', 22: 'China', 23: 'Colombia', 24: 'Comoros', 25: 'Croatia', 26: 'Cyprus', 27: 'Democratic Republic of the Congo', 28: 'Denmark', 29: 'Djibouti', 30: 'Dominican Republic', 31: 'Ecuador', 32: 'Egypt', 33: 'El Salvador', 34: 'Estonia', 35: 'Eswatini', 36: 'Ethiopia', 37: 'Fiji', 38: 'Finland', 39: 'France', 40: 'Georgia', 41: 'Germany', 42: 'Ghana', 43: 'Guatemala', 44: 'Guinea', 45: 'Guyana', 46: 'Haiti', 47: 'Honduras', 48: 'Hungary', 49: 'Iceland', 50: 'India', 51: 'Indonesia', 52: 'Iran', 53: 'Iraq', 54: 'Ireland', 55: 'Israel', 56: 'Italy', 57: 'Jamaica', 58: 'Japan', 59: 'Jordan', 60: 'Kazakhstan', 61: 'Kenya', 62: 'Kyrgyzstan', 63: 'Laos', 64: 'Latvia', 65: 'Lebanon', 66: 'Lesotho', 67: 'Liberia', 68: 'Lithuania', 69: 'Luxembourg', 70: 'Madagascar', 71: 'Malawi', 72: 'Malaysia', 73: 'Maldives', 74: 'Malta', 75: 'Mauritania', 76: 'Mauritius', 77: 'Mexico', 78: 'Mongolia', 79: 'Montenegro', 80: 'Mozambique', 81: 'Myanmar', 82: 'Namibia', 83: 'Nepal', 84: 'Netherlands', 85: 'Nicaragua', 86: 'North Macedonia', 87: 'Norway', 88: 'Pakistan', 89: 'Panama', 90: 'Papua New Guinea', 91: 'Paraguay', 92: 'Peru', 93: 'Philippines', 94: 'Poland', 95: 'Portugal', 96: 'South Korea', 97: 'Moldova', 98: 'Romania', 99: 'Rwanda', 100: 'Samoa', 101: 'Samoa', 102: 'Serbia', 103: 'Sierra Leone', 104: 'Slovakia', 105: 'Slovenia', 106: 'Solomon Islands', 107: 'South Africa', 108: 'Spain', 109: 'Sri Lanka', 110: 'Sudan', 111: 'Suriname', 112: 'Sweden', 113: 'Switzerland', 114: 'Tajikistan', 115: 'Thailand', 116: 'Tonga', 117: 'Trinidad and Tobago', 118: 'Tunisia', 119: 'Uganda', 120: 'Ukraine', 121: 'United Arab Emirates', 122: 'United Kingdom', 123: 'Tanzania', 124: 'United States', 125: 'Uruguay', 126: 'Uzbekistan', 127: 'Vanuatu', 128: 'Vietnam', 129: 'Zambia', 130: 'Zimbabwe'}, 'Region': {0: 'European Region', 1: 'African Region', 2: 'African Region', 3: 'Region of the Americas', 4: 'European Region', 5: 'European Region', 6: 'European Region', 7: 'South-East Asia Region', 8: 'European Region', 9: 'European Region', 10: 'Region of the Americas', 11: 'South-East Asia Region', 12: 'Region of the Americas', 13: 'European Region', 14: 'African Region', 15: 'Region of the Americas', 16: 'European Region', 17: 'African Region', 18: 'African Region', 19: 'Region of the Americas', 20: 'African Region', 21: 'Region of the Americas', 22: 'Western Pacific Region', 23: 'Region of the Americas', 24: 'African Region', 25: 'European Region', 26: 'European Region', 27: 'African Region', 28: 'European Region', 29: 'Eastern Mediterranean Region', 30: 'Region of the Americas', 31: 'Region of the Americas', 32: 'Eastern Mediterranean Region', 33: 'Region of the Americas', 34: 'European Region', 35: 'African Region', 36: 'African Region', 37: 'Western Pacific Region', 38: 'European Region', 39: 'European Region', 40: 'European Region', 41: 'European Region', 42: 'African Region', 43: 'Region of the Americas', 44: 'African Region', 45: 'Region of the Americas', 46: 'Region of the Americas', 47: 'Region of the Americas', 48: 'European Region', 49: 'European Region', 50: 'South-East Asia Region', 51: 'South-East Asia Region', 52: 'Eastern Mediterranean Region', 53: 'Eastern Mediterranean Region', 54: 'European Region', 55: 'European Region', 56: 'European Region', 57: 'Region of the Americas', 58: 'Western Pacific Region', 59: 'Eastern Mediterranean Region', 60: 'European Region', 61: 'African Region', 62: 'European Region', 63: 'Western Pacific Region', 64: 'European Region', 65: 'Eastern Mediterranean Region', 66: 'African Region', 67: 'African Region', 68: 'European Region', 69: 'European Region', 70: 'African Region', 71: 'African Region', 72: 'Western Pacific Region', 73: 'South-East Asia Region', 74: 'European Region', 75: 'African Region', 76: 'African Region', 77: 'Region of the Americas', 78: 'Western Pacific Region', 79: 'European Region', 80: 'African Region', 81: 'South-East Asia Region', 82: 'African Region', 83: 'South-East Asia Region', 84: 'European Region', 85: 'Region of the Americas', 86: 'European Region', 87: 'European Region', 88: 'Eastern Mediterranean Region', 89: 'Region of the Americas', 90: 'Western Pacific Region', 91: 'Region of the Americas', 92: 'Region of the Americas', 93: 'Western Pacific Region', 94: 'European Region', 95: 'European Region', 96: 'Western Pacific Region', 97: 'European Region', 98: 'European Region', 99: 'African Region', 100: 'Western Pacific Region', 101: 'Western Pacific Region', 102: 'European Region', 103: 'African Region', 104: 'European Region', 105: 'European Region', 106: 'Western Pacific Region', 107: 'African Region', 108: 'European Region', 109: 'South-East Asia Region', 110: 'Eastern Mediterranean Region', 111: 'Region of the Americas', 112: 'European Region', 113: 'European Region', 114: 'European Region', 115: 'South-East Asia Region', 116: 'Western Pacific Region', 117: 'Region of the Americas', 118: 'Eastern Mediterranean Region', 119: 'African Region', 120: 'European Region', 121: 'Eastern Mediterranean Region', 122: 'European Region', 123: 'African Region', 124: 'Region of the Americas', 125: 'Region of the Americas', 126: 'European Region', 127: 'Western Pacific Region', 128: 'Western Pacific Region', 129: 'African Region', 130: 'African Region'}, 'Population(2020)': {0: '2,837,849.00', 1: '43,851,043.00', 2: '32,866,268.00', 3: '45,376,763.00', 4: '2,963,234.00', 5: '8,916,864.00', 6: '10,093,121.00', 7: '164,689,383.00', 8: '9,379,952.00', 9: '11,544,241.00', 10: '397,621.00', 11: '771,612.00', 12: '11,673,029.00', 13: '3,280,815.00', 14: '2,351,625.00', 15: '212,559,409.00', 16: '6,934,015.00', 17: '11,890,781.00', 18: '555,988.00', 19: '38,037,204.00', 20: '4,829,764.00', 21: '19,116,209.00', 22: '1,410,929,362.00', 23: '50,882,884.00', 24: '869,595.00', 25: '4,047,680.00', 26: '1,207,361.00', 27: '89,561,404.00', 28: '5,831,404.00', 29: '988,002.00', 30: '10,847,904.00', 31: '17,643,060.00', 32: '102,334,403.00', 33: '6,486,201.00', 34: '1,329,479.00', 35: '1,160,164.00', 36: '114,963,583.00', 37: '896,444.00', 38: '5,529,543.00', 39: '67,379,908.00', 40: '3,722,716.00', 41: '83,160,871.00', 42: '31,072,945.00', 43: '16,858,333.00', 44: '13,132,792.00', 45: '786,559.00', 46: '11,402,533.00', 47: '9,904,608.00', 48: '9,750,149.00', 49: '366,463.00', 50: '1,380,004,385.00', 51: '273,523,621.00', 52: '83,992,953.00', 53: '40,222,503.00', 54: '4,985,674.00', 55: '9,215,100.00', 56: '59,449,527.00', 57: '2,961,161.00', 58: '125,836,021.00', 59: '10,203,140.00', 60: '18,754,440.00', 61: '53,771,300.00', 62: '6,579,900.00', 63: '7,275,556.00', 64: '1,900,449.00', 65: '6,825,442.00', 66: '2,142,252.00', 67: '5,057,677.00', 68: '2,794,885.00', 69: '630,419.00', 70: '27,691,019.00', 71: '19,129,955.00', 72: '32,365,998.00', 73: '540,542.00', 74: '515,332.00', 75: '4,649,660.00', 76: '1,265,740.00', 77: '128,932,753.00', 78: '3,278,292.00', 79: '621,306.00', 80: '31,255,435.00', 81: '54,409,794.00', 82: '2,540,916.00', 83: '29,136,808.00', 84: '17,441,500.00', 85: '6,624,554.00', 86: '2,072,531.00', 87: '5,379,475.00', 88: '220,892,331.00', 89: '4,314,768.00', 90: '8,947,027.00', 91: '7,132,530.00', 92: '32,971,846.00', 93: '109,581,085.00', 94: '37,899,070.00', 95: '10,297,081.00', 96: '51,836,239.00', 97: '2,620,495.00', 98: '19,257,520.00', 99: '12,952,209.00', 100: '198,410.00', 101: '198,410.00', 102: '6,899,126.00', 103: '7,976,985.00', 104: '5,458,827.00', 105: '2,102,419.00', 106: '686,878.00', 107: '59,308,690.00', 108: '47,363,419.00', 109: '21,919,000.00', 110: '43,849,269.00', 111: '586,634.00', 112: '10,353,442.00', 113: '8,636,561.00', 114: '9,537,642.00', 115: '69,799,978.00', 116: '105,697.00', 117: '1,399,491.00', 118: '11,818,618.00', 119: '45,741,000.00', 120: '44,134,693.00', 121: '9,890,400.00', 122: '67,215,293.00', 123: '59,734,213.00', 124: '331,501,080.00', 125: '3,473,727.00', 126: '34,232,050.00', 127: '307,150.00', 128: '97,338,583.00', 129: '18,383,956.00', 130: '14,862,927.00'}, 'Political Freedom': {0: 'Partly Free', 1: 'Not Free', 2: 'Not Free', 3: 'Free', 4: 'Partly Free', 5: 'Free', 6: 'Not Free', 7: 'Partly Free', 8: 'Not Free', 9: 'Free', 10: 'Free', 11: 'Partly Free', 12: 'Partly Free', 13: 'Partly Free', 14: 'Free', 15: 'Free', 16: 'Free', 17: 'Not Free', 18: 'Free', 19: 'Free', 20: 'Not Free', 21: 'Free', 22: 'Not Free', 23: 'Partly Free', 24: 'Partly Free', 25: 'Free', 26: 'Free', 27: 'Not Free', 28: 'Free', 29: 'Not Free', 30: 'Partly Free', 31: 'Free', 32: 'Not Free', 33: 'Partly Free', 34: 'Free', 35: 'Not Free', 36: 'Not Free', 37: 'Partly Free', 38: 'Free', 39: 'Free', 40: 'Partly Free', 41: 'Free', 42: 'Free', 43: 'Partly Free', 44: 'Not Free', 45: 'Free', 46: 'Not Free', 47: 'Partly Free', 48: 'Partly Free', 49: 'Free', 50: 'Partly Free', 51: 'Partly Free', 52: 'Not Free', 53: 'Not Free', 54: 'Free', 55: 'Free', 56: 'Free', 57: 'Free', 58: 'Free', 59: 'Not Free', 60: 'Not Free', 61: 'Partly Free', 62: 'Not Free', 63: 'Not Free', 64: 'Free', 65: 'Partly Free', 66: 'Partly Free', 67: 'Partly Free', 68: 'Free', 69: 'Free', 70: 'Partly Free', 71: 'Partly Free', 72: 'Partly Free', 73: 'Partly Free', 74: 'Free', 75: 'Partly Free', 76: 'Free', 77: 'Partly Free', 78: 'Free', 79: 'Partly Free', 80: 'Partly Free', 81: 'Not Free', 82: 'Free', 83: 'Partly Free', 84: 'Free', 85: 'Not Free', 86: 'Partly Free', 87: 'Free', 88: 'Partly Free', 89: 'Free', 90: 'Partly Free', 91: 'Partly Free', 92: 'Free', 93: 'Partly Free', 94: 'Free', 95: 'Free', 96: 'Free', 97: 'Partly Free', 98: 'Free', 99: 'Not Free', 100: 'Free', 101: 'Free', 102: 'Partly Free', 103: 'Partly Free', 104: 'Free', 105: 'Free', 106: 'Free', 107: 'Free', 108: 'Free', 109: 'Partly Free', 110: 'Not Free', 111: 'Free', 112: 'Free', 113: 'Free', 114: 'Not Free', 115: 'Not Free', 116: 'Free', 117: 'Free', 118: 'Partly Free', 119: 'Not Free', 120: 'Partly Free', 121: 'Not Free', 122: 'Free', 123: 'Partly Free', 124: 'Free', 125: 'Free', 126: 'Not Free', 127: 'Free', 128: 'Not Free', 129: 'Partly Free', 130: 'Not Free'}, 'Central bank': {0: 'Bank of Albania', 1: 'Bank of Algeria', 2: 'National Bank of Angola', 3: 'Central Bank of Argentina', 4: 'Central Bank of Armenia', 5: 'Oesterreichische Nationalbank', 6: 'Central Bank of Azerbaijan', 7: 'Bangladesh Bank', 8: 'National Bank of the Republic of Belarus', 9: 'National Bank of Belgium', 10: 'Central Bank of Belize', 11: 'Bank of Bhutan', 12: 'Central Bank of Bolivia', 13: 'Central Bank of Bosnia and Herzegovina', 14: 'Bank of Botswana', 15: 'Central Bank of Brazil', 16: 'Bulgarian National Bank', 17: 'Bank of the Republic of Burundi', 18: 'Bank of Cape Verde', 19: 'Bank of Canada', 20: 'Bank of Central African States', 21: 'Central Bank of Chile', 22: "People's Bank of China", 23: 'Bank of the Republic (Colombia)', 24: 'Central Bank of the Comoros', 25: 'Croatian National Bank', 26: 'Central Bank of Cyprus', 27: 'Central Bank of the Congo', 28: 'Danmarks Nationalbank', 29: 'Central Bank of Djibouti', 30: 'Central Bank of the Dominican Republic', 31: 'Central Bank of Ecuador', 32: 'Central Bank of Egypt', 33: 'Central Reserve Bank of El Salvador', 34: 'Bank of Estonia', 35: 'Central Bank of Eswatini', 36: 'National Bank of Ethiopia', 37: 'Reserve Bank of Fiji', 38: 'Bank of Finland', 39: 'Bank of France', 40: 'National Bank of Georgia', 41: 'Deutsche Bundesbank', 42: 'Bank of Ghana', 43: 'Bank of Guatemala', 44: 'Central Bank of the Republic of Guinea', 45: 'Bank of Guyana', 46: 'Bank of the Republic of Haiti', 47: 'Central Bank of Honduras', 48: 'Hungarian National Bank', 49: 'Central Bank of Iceland', 50: 'Reserve Bank of India', 51: 'Bank Indonesia', 52: 'Central Bank of Iran', 53: 'Central Bank of Iraq', 54: 'Central Bank of Ireland', 55: 'Bank of Israel', 56: 'Bank of Italy', 57: 'Bank of Jamaica', 58: 'Bank of Japan', 59: 'Central Bank of Jordan', 60: 'National Bank of Kazakhstan', 61: 'Central Bank of Kenya', 62: 'National Bank of the Kyrgyz Republic', 63: 'Bank of the Lao P.D.R.', 64: 'Bank of Latvia', 65: 'Banque du Liban', 66: 'Central Bank of Lesotho', 67: 'Central Bank of Liberia', 68: 'Bank of Lithuania', 69: 'Central Bank of Luxembourg', 70: 'Central Bank of Madagascar', 71: 'Reserve Bank of Malawi', 72: 'Central Bank of Malaysia', 73: 'Maldives Monetary Authority', 74: 'Central Bank of Malta', 75: 'Central Bank of Mauritania', 76: 'Bank of Mauritius', 77: 'Bank of Mexico', 78: 'Bank of Mongolia', 79: 'Central Bank of Montenegro', 80: 'Bank of Mozambique', 81: 'Central Bank of Myanmar', 82: 'Bank of Namibia', 83: 'Nepal Rastra Bank', 84: 'De Nederlandsche Bank', 85: 'Central Bank of Nicaragua', 86: 'National Bank of North Macedonia', 87: 'Norges Bank', 88: 'State Bank of Pakistan', 89: 'National Bank of Panama', 90: 'Bank of Papua New Guinea', 91: 'Central Bank of Paraguay', 92: 'Central Reserve Bank of Peru', 93: 'Bangko Sentral ng Pilipinas', 94: 'National Bank of Poland', 95: 'Banco de Portugal', 96: 'Bank of Korea', 97: 'National Bank of Moldova', 98: 'National Bank of Romania', 99: 'National Bank of Rwanda', 100: 'Central Bank of Samoa', 101: 'Central Bank of Samoa', 102: 'National Bank of Serbia', 103: 'Bank of Sierra Leone', 104: 'National Bank of Slovakia', 105: 'Bank of Slovenia', 106: 'Central Bank of Solomon Islands', 107: 'South African Reserve Bank', 108: 'Bank of Spain', 109: 'Central Bank of Sri Lanka', 110: 'Central Bank of Sudan', 111: 'Central Bank of Suriname', 112: 'Sveriges riksbank', 113: 'Swiss National Bank', 114: 'National Bank of Tajikistan', 115: 'Bank of Thailand', 116: 'National Reserve Bank of Tonga', 117: 'Central Bank of Trinidad and Tobago', 118: 'Central Bank of Tunisia', 119: 'Bank of Uganda', 120: 'National Bank of Ukraine', 121: 'Central Bank of the United Arab Emirates', 122: 'Bank of England', 123: 'Bank of Tanzania', 124: 'Federal Reserve', 125: 'Central Bank of Uruguay', 126: 'Central Bank of Uzbekistan', 127: 'Reserve Bank of Vanuatu', 128: 'State Bank of Vietnam', 129: 'Bank of Zambia', 130: 'Reserve Bank of Zimbabwe'}, 'Annual GDP(2020)': {0: '$14,370,506,253.33', 1: '$191,310,679,011.58', 2: '$95,012,860,718.09', 3: '$394,446,952,845.24', 4: '$12,932,478,333.25', 5: '$419,186,307,716.41', 6: '$56,548,148,736.78', 7: '$214,962,354,031.80', 8: '$62,765,583,662.61', 9: '$512,638,453,020.10', 10: '$1,424,667,367.43', 11: '$2,320,776,085.79', 12: '$27,378,912,014.67', 13: '$19,937,655,682.32', 14: '$17,182,153,843.96', 15: '$2,268,471,792,918.29', 16: '$60,566,782,151.68', 17: '$2,406,361,756.15', 18: '$1,831,266,583.24', 19: '$1,847,703,996,298.69', 20: '$1,823,368,094.29', 21: '$268,586,104,417.70', 22: '$11,785,004,404,054.60', 23: '$367,803,698,280.80', 24: '$1,249,193,741.79', 25: '$61,535,031,999.34', 26: '$27,215,033,806.18', 27: '$37,052,362,500.45', 28: '$372,510,633,673.23', 29: '$1,128,611,700.36', 30: '$80,162,653,484.64', 31: '$81,657,668,887.57', 32: '$312,970,401,488.28', 33: '$21,271,473,583.31', 34: '$26,836,307,024.55', 35: '$5,441,352,066.52', 36: '$71,633,249,861.68', 37: '$3,413,841,317.66', 38: '$264,721,217,422.86', 39: '$2,730,750,828,276.00', 40: '$17,376,552,815.60', 41: '$3,751,241,122,769.96', 42: '$57,430,579,781.17', 43: '$55,020,023,100.39', 44: '$12,607,200,647.36', 45: '$6,875,438,717.59', 46: '$13,549,581,658.19', 47: '$19,913,659,065.44', 48: '$163,260,617,185.90', 49: '$17,452,945,287.57', 50: '$2,706,600,821,780.82', 51: '$1,179,530,430,084.12', 52: '$499,220,291,211.40', 53: '$198,178,215,337.42', 54: '$406,056,411,411.57', 55: '$311,691,762,137.65', 56: '$1,959,439,492,411.70', 57: '$12,904,621,963.64', 58: '$6,187,013,947,904.92', 59: '$33,075,085,064.60', 60: '$207,705,575,979.18', 61: '$64,860,101,745.44', 62: '$6,593,004,560.64', 63: '$13,355,463,610.38', 64: '$30,808,562,938.41', 65: '$31,648,904,715.41', 66: '$2,330,681,471.61', 67: '$2,475,775,658.93', 68: '$51,396,658,841.03', 69: '$67,942,997,440.60', 70: '$12,705,052,902.85', 71: '$10,080,189,306.15', 72: '$376,654,485,569.54', 73: '$3,061,254,072.17', 74: '$13,664,504,216.41', 75: '$7,829,358,659.45', 76: '$11,737,008,576.10', 77: '$1,201,954,407,872.70', 78: '$13,288,991,441.97', 79: '$4,533,984,453.54', 80: '$17,648,220,319.52', 81: '$80,424,462,199.73', 82: '$13,499,756,302.60', 83: '$24,262,542,367.97', 84: '$925,798,523,585.04', 85: '$11,406,278,011.48', 86: '$11,189,794,856.65', 87: '$488,911,512,109.46', 88: '$258,078,002,937.57', 89: '$41,470,466,792.07', 90: '$20,996,892,564.14', 91: '$36,824,961,033.39', 92: '$187,457,171,746.57', 93: '$326,553,366,228.05', 94: '$643,085,265,147.75', 95: '$234,654,414,142.89', 96: '$1,468,558,788,293.07', 97: '$9,197,982,945.48', 98: '$224,969,765,141.55', 99: '$10,996,880,113.03', 100: '$522,466,367.71', 101: '$741,709,517.63', 102: '$49,721,665,328.75', 103: '$3,737,165,032.25', 104: '$109,111,285,633.98', 105: '$54,097,609,433.22', 106: '$1,121,317,739.21', 107: '$400,228,939,387.24', 108: '$1,401,623,069,102.21', 109: '$84,293,528,650.46', 110: '$85,064,646,217.92', 111: '$4,146,483,053.33', 112: '$580,499,441,330.26', 113: '$692,095,426,032.17', 114: '$10,940,424,058.73', 115: '$425,391,280,429.98', 116: '$455,079,252.29', 117: '$19,183,685,986.99', 118: '$47,084,697,907.18', 119: '$43,828,692,209.54', 120: '$130,072,807,270.76', 121: '$404,700,030,660.31', 122: '$2,628,312,650,645.44', 123: '$56,593,929,840.20', 124: '$17,709,432,714,644.80', 125: '$46,654,650,902.33', 126: '$84,121,862,780.94', 127: '$780,029,849.65', 128: '$206,694,203,923.45', 129: '$28,648,141,585.54', 130: '$15,737,548,231.72'}, 'GDP per capita (2020)': {0: '$13,192', 1: '$10,735', 2: '$6,110', 3: '$19,691', 4: '$12,620', 5: '$51,858', 6: '$13,727', 7: '$4,871', 8: '$19,187', 9: '$48,770', 10: '$6,122', 11: '$10,551', 12: '$7,845', 13: '$14,509', 14: '$14,655', 15: '$14,064', 16: '$22,379', 17: '$731', 18: '$6,045', 19: '$46,064', 20: '$936', 21: '$23,325', 22: '$16,316', 23: '$13,449', 24: '$2,989', 25: '$27,077', 26: '$38,816', 27: '$1,082', 28: '$55,820', 29: '$5,481', 30: '$17,003', 31: '$10,329', 32: '$11,951', 33: '$7,983', 34: '$35,257', 35: '$8,405', 36: '$2,297', 37: '$11,451', 38: '$47,154', 39: '$42,321', 40: '$13,966', 41: '$51,423', 42: '$5,446', 43: '$8,393', 44: '$2,671', 45: '$18,680', 46: '$2,934', 47: '$5,138', 48: '$31,098', 49: '$52,376', 50: '$6,166', 51: '$11,445', 52: '$12,644', 53: '$9,012', 54: '$90,789', 55: '$39,056', 56: '$39,073', 57: '$8,761', 58: '$40,232', 59: '$9,817', 60: '$25,363', 61: '$4,340', 62: '$4,715', 63: '$7,811', 64: '$30,100', 65: '$11,488', 66: '$2,317', 67: '$1,392', 68: '$37,107', 69: '$112,557', 70: '$1,464', 71: '$1,509', 72: '$26,472', 73: '$12,744', 74: '$39,980', 75: '$5,110', 76: '$19,463', 77: '$17,852', 78: '$11,724', 79: '$18,259', 80: '$1,230', 81: '$4,857', 82: '$8,815', 83: '$3,800', 84: '$54,324', 85: '$5,280', 86: '$15,931', 87: '$63,548', 88: '$4,563', 89: '$25,390', 90: '$4,064', 91: '$12,390', 92: '$11,261', 93: '$7,954', 94: '$32,399', 95: '$31,962', 96: '$42,336', 97: '$12,324', 98: '$28,871', 99: '$2,099', 100: '$6,417', 101: '$6,417', 102: '$18,255', 103: '$1,637', 104: '$30,510', 105: '$37,051', 106: '$2,483', 107: '$12,666', 108: '$36,211', 109: '$12,537', 110: '$3,927', 111: '$15,865', 112: '$50,923', 113: '$68,755', 114: '$3,658', 115: '$17,285', 116: '$6,347', 117: '$23,722', 118: '$10,260', 119: '$2,175', 120: '$12,376', 121: '$63,299', 122: '$42,676', 123: '$2,635', 124: '$59,920', 125: '$21,608', 126: '$7,332', 127: '$2,854', 128: '$8,200', 129: '$3,278', 130: '$3,353'}, 'Daily median income(2019)': {0: '$7.57', 1: '$8.01', 2: '$1.84', 3: '$13.78', 4: '$5.87', 5: '$50.10', 6: '$17.46', 7: '$3.74', 8: '$19.03', 9: '$45.60', 10: '$5.08', 11: '$7.97', 12: '$10.24', 13: '$20.11', 14: '$4.56', 15: '$12.75', 16: '$18.63', 17: '$1.11', 18: '$7.38', 19: '$51.58', 20: '$1.17', 21: '$17.62', 22: '$11.24', 23: '$8.84', 24: '$3.92', 25: '$21.75', 26: '$37.94', 27: '$1.26', 28: '$49.27', 29: '$4.24', 30: '$11.70', 31: '$9.43', 32: '$4.01', 33: '$9.06', 34: '$31.98', 35: '$3.11', 36: '$3.08', 37: '$7.97', 38: '$45.79', 39: '$45.60', 40: '$6.21', 41: '$47.86', 42: '$5.47', 43: '$6.27', 44: '$2.96', 45: '$9.32', 46: '$3.56', 47: '$5.66', 48: '$23.48', 49: '$53.88', 50: '$3.40', 51: '$5.24', 52: '$10.46', 53: '$5.62', 54: '$44.78', 55: '$31.23', 56: '$36.73', 57: '$7.85', 58: '$41.54', 59: '$8.95', 60: '$11.04', 61: '$2.65', 62: '$5.34', 63: '$3.90', 64: '$24.21', 65: '$17.70', 66: '$3.13', 67: '$1.94', 68: '$25.76', 69: '$63.75', 70: '$1.12', 71: '$1.40', 72: '$24.35', 73: '$16.26', 74: '$41.37', 75: '$5.00', 76: '$11.21', 77: '$9.04', 78: '$8.35', 79: '$14.11', 80: '$1.50', 81: '$5.67', 82: '$4.97', 83: '$4.25', 84: '$48.02', 85: '$7.38', 86: '$11.25', 87: '$62.14', 88: '$3.81', 89: '$17.48', 90: '$3.14', 91: '$12.15', 92: '$10.31', 93: '$4.98', 94: '$15.94', 95: '$25.15', 96: '$39.87', 97: '$9.02', 98: '$16.59', 99: '$1.93', 100: '$7.79', 101: '$7.79', 102: '$12.60', 103: '$2.17', 104: '$24.14', 105: '$35.67', 106: '$2.94', 107: '$4.32', 108: '$32.24', 109: '$6.63', 110: '$3.39', 111: '2018 $6.44', 112: '$48.82', 113: '$58.08', 114: '$6.55', 115: '$12.18', 116: '$8.18', 117: '$18.19', 118: '$9.43', 119: '$2.33', 120: '$13.26', 121: '$84.89', 122: '$41.40', 123: '$1.98', 124: '$57.21', 125: '$20.36', 126: '$3.74', 127: '$3.68', 128: '$9.30', 129: '$1.51', 130: '$2.36'}, 'Foreign direct investment, net inflows (% of GDP)': {0: '7.86%', 1: '0.81%', 2: '-4.58%', 3: '1.50%', 4: '1.86%', 5: '-1.82%', 6: '3.12%', 7: '0.63%', 8: '1.98%', 9: '-5.43%', 10: '4.74%', 11: '0.51%', 12: '-0.53%', 13: '1.93%', 14: '1.42%', 15: '3.68%', 16: '3.03%', 17: '0.03%', 18: '13.52%', 19: '2.59%', 20: '1.15%', 21: '4.51%', 22: '1.31%', 23: '4.43%', 24: '0.32%', 25: '1.93%', 26: '103.93%', 27: '1.45%', 28: '-2.14%', 29: '5.26%', 30: '3.18%', 31: '0.89%', 32: '2.97%', 33: '2.59%', 34: '9.41%', 35: '2.86%', 36: '2.62%', 37: '5.86%', 38: '5.86%', 39: '1.88%', 40: '7.67%', 41: '1.75%', 42: '5.77%', 43: '1.52%', 44: '0.33%', 45: '32.76%', 46: '0.52%', 47: '3.81%', 48: '56.37%', 49: '-2.42%', 50: '1.76%', 51: '2.23%', 52: '0.58%', 53: '-1.38%', 54: '-11.70%', 55: '4.83%', 56: '1.56%', 57: '4.20%', 58: '0.79%', 59: '1.85%', 60: '1.83%', 61: '1.40%', 62: '3.14%', 63: '4.14%', 64: '3.11%', 65: '4.28%', 66: '4.97%', 67: '2.82%', 68: '2.88%', 69: '-16.06%', 70: '3.34%', 71: '0.91%', 72: '2.50%', 73: '17.04%', 74: '27.97%', 75: '-11.62%', 76: '3.36%', 77: '2.32%', 78: '17.46%', 79: '7.55%', 80: '14.26%', 81: '2.17%', 82: '-1.40%', 83: '0.54%', 84: '3.93%', 85: '3.99%', 86: '4.38%', 87: '4.21%', 88: '0.80%', 89: '8.82%', 90: '1.35%', 91: '1.57%', 92: '3.89%', 93: '2.30%', 94: '2.42%', 95: '4.31%', 96: '0.59%', 97: '4.19%', 98: '2.95%', 99: '3.71%', 100: '0.12%', 101: '0.12%', 102: '8.29%', 103: '8.31%', 104: '2.20%', 105: '3.16%', 106: '2.09%', 107: '1.46%', 108: '1.06%', 109: '0.90%', 110: '2.56%', 111: '1.72%', 112: '3.13%', 113: '5.10%', 114: '2.56%', 115: '0.88%', 116: '0.34%', 117: '0.79%', 118: '2.07%', 119: '3.60%', 120: '3.79%', 121: '3.27%', 122: '0.08%', 123: '1.62%', 124: '1.64%', 125: '2.13%', 126: '4.01%', 127: '3.74%', 128: '6.15%', 129: '2.35%', 130: '1.65%'}, 'Unemployment rate(2021)': {0: '11.82%', 1: '12.70%', 2: '8.53%', 3: '10.90%', 4: '20.90%', 5: '6.30%', 6: '6.58%', 7: '5.23%', 8: '4.74%', 9: '6.42%', 10: '8.22%', 11: '4.33%', 12: '8.51%', 13: '15.22%', 14: '24.72%', 15: '14.40%', 16: '5.42%', 17: '1.79%', 18: '15.42%', 19: '7.51%', 20: '6.57%', 21: '9.13%', 22: '4.82%', 23: '14.34%', 24: '9.45%', 25: '8.68%', 26: '6.13%', 27: '5.43%', 28: '4.80%', 29: '28.39%', 30: '8.50%', 31: '6.43%', 32: '9.33%', 33: '5.94%', 34: '6.33%', 35: '25.76%', 36: '3.69%', 37: '5.24%', 38: '7.53%', 39: '8.06%', 40: '10.66%', 41: '3.54%', 42: '4.70%', 43: '3.57%', 44: '6.34%', 45: '16.42%', 46: '15.73%', 47: '8.51%', 48: '4.12%', 49: '5.40%', 50: '5.98%', 51: '4.41%', 52: '11.46%', 53: '14.19%', 54: '6.63%', 55: '5.05%', 56: '9.83%', 57: '9.18%', 58: '2.80%', 59: '19.25%', 60: '4.90%', 61: '5.74%', 62: '9.10%', 63: '1.26%', 64: '7.60%', 65: '14.49%', 66: '24.60%', 67: '4.09%', 68: '7.90%', 69: '5.23%', 70: '2.59%', 71: '7.02%', 72: '4.61%', 73: '6.08%', 74: '3.50%', 75: '11.46%', 76: '7.41%', 77: '4.38%', 78: '7.08%', 79: '18.49%', 80: '3.98%', 81: '2.17%', 82: '21.68%', 83: '5.05%', 84: '4.01%', 85: '5.96%', 86: '16.20%', 87: '4.99%', 88: '4.35%', 89: '12.09%', 90: '2.75%', 91: '7.21%', 92: '4.83%', 93: '2.41%', 94: '3.37%', 95: '6.65%', 96: '3.53%', 97: '3.96%', 98: '5.17%', 99: '1.61%', 100: '9.84%', 101: '9.84%', 102: '11.81%', 103: '5.33%', 104: '6.74%', 105: '4.42%', 106: '1.03%', 107: '33.56%', 108: '14.73%', 109: '5.39%', 110: '19.81%', 111: '10.06%', 112: '8.66%', 113: '5.32%', 114: '7.75%', 115: '1.42%', 116: '3.97%', 117: '4.80%', 118: '16.82%', 119: '2.94%', 120: '8.88%', 121: '3.36%', 122: '4.53%', 123: '2.65%', 124: '5.46%', 125: '10.45%', 126: '7.16%', 127: '2.18%', 128: '2.17%', 129: '13.03%', 130: '5.17%'}})
    first_df.dropna()
    regions = pd.DataFrame({
       'first column': ['African Region', 'Eastern Mediterranean Region', 'European Region','Region of the Americas',
        'South-East Asia Region','Western Pacific Region'],
         'second column': [1, 2, 3, 4, 5, 6]})
    option = st.selectbox(
            'Выберите регион:', regions['first column'])
    df_selection = first_df[lambda x: x["Region"] == option]
    st.dataframe(df_selection)
    st.subheader("Сначала давайте посмотрим, как соотносятся ВВП на душу населения и чистый приток иностранных инвестиций")
    st.caption('Чтобы увидеть значения для каждой страны, наведите курсор на выбранную точку')
    gi = alt.Chart(first_df).mark_circle().encode(
       x='GDP per capita (2020)', y='Foreign direct investment, net inflows (% of GDP)', color='Region', tooltip=['Country', 'Population(2020)', 'GDP per capita (2020)', 'Foreign direct investment, net inflows (% of GDP)'])
    st.altair_chart(gi, use_container_width=True)
    st.caption('Нетрудно заметить, что явной корреляции между этими показателями нет')
    st.subheader("Теперь с помощью геоданных и Plotly посмотрим, в каких странах неравенство доходов выше")
    st.caption('Чтобы увидеть значения для каждой страны, наведите курсор на выбранную страну')
    gini_df= pd.read_csv("https://raw.githubusercontent.com/datasets/gini-index/master/data/gini-index.csv")
    ###FROM https://plotly.com/python/mapbox-county-choropleth/
    gini_dict = dict(
        type='choropleth',
        locations=gini_df['Country Code'],
        z=gini_df['Value'],
        text=gini_df['Country Name'],
        colorbar={'title': 'Gini'})
     ###END FROM
    gini_line = dict(
        title='Gini',
        geo=dict(showframe=False))
    gini_graph = go.Figure(data=[gini_dict], layout=gini_line)
    st.plotly_chart(gini_graph)
    st.subheader("Далее посмотрим на визуализацию некоторых показателей. Для корректного отображения некоторых графиков вам будет необходимо скачать и потом загрузить указанные данные ")
    st.caption('Во-первых, скачайте пожалуйста информацию о годовом ВВП США по следующей ссылке:')
    st.markdown("https://fred.stlouisfed.org/series/GDPA#0")
    file_1 = st.file_uploader("Загрузите первый CSV-файл")
    df_1 = pd.read_csv(file_1)
    st.dataframe(df_1)
    st.caption('Чтобы увидеть значения для каждой даты, наведите курсор на выбранную точку')
    hover = alt.selection_single(
         fields=["DATE"],
         nearest=True,
         on="mouseover",
         empty="none",)
    graph_gdp = (alt.Chart(df_1, title="US annual GDP").mark_line().encode(x="DATE",y="GDPA"))
    ###FROM https://docs.streamlit.io/library/api-reference/charts/st.altair_chart:
    points = graph_gdp.transform_filter(hover).mark_circle(size=65)
    tooltips = (alt.Chart(df_1).mark_rule().encode(x="DATE",y="GDPA", opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
         tooltip=[alt.Tooltip("DATE"), alt.Tooltip("GDPA", title="Annual GDP")],).add_selection(hover))
    chart = (graph_gdp + points + tooltips).interactive()
    ###END FROM
    st.altair_chart(chart,use_container_width=True)
    file_2 = st.file_uploader("Загрузите CSV-файл")
    df_2 = pd.read_csv(file_2)
    st.dataframe(df_2)
    st.caption('Аналогично, чтобы увидеть значения для каждой даты, наведите курсор на выбранную точку')
    hover_1 = alt.selection_single(
          fields=["DATE"],
          nearest=True,
          on="mouseover",
          empty="none")
    graph_un = (alt.Chart(df_2, title="US unemployment rate").mark_line().encode(x="DATE",y="UNRATE"))
    ##FROM https://docs.streamlit.io/library/api-reference/charts/st.altair_chart:
    points_1 = graph_un.transform_filter(hover_1).mark_circle(size=65)
    tooltips_1 = (alt.Chart(df_2).mark_rule().encode(x="DATE",y="UNRATE", opacity=alt.condition(hover_1, alt.value(0.3), alt.value(0)),
    tooltip=[alt.Tooltip("DATE"), alt.Tooltip("UNRATE", title="Unemployment rate")],).add_selection(hover_1))
    chart_u = (graph_un + points_1 + tooltips_1).interactive()
    ###END FROM
    st.altair_chart(chart_u,use_container_width=True)
    st.subheader("Сегодня, помимо ВВП на душу населения, все чаще используется понятие индекса человеческого счастья, чтобы сравнить благосостояние людей между странами. По представленным ниже данным построим регрессию для индекса человеческого счастья в 2019 году")
    st.caption('Чтобы отсортировать значения показателя по убыванию или возрастанию, нажмите на название столбца')
    happy_df= pd.read_csv("https://raw.githubusercontent.com/choudharynisha/predicting-world-happiness/main/data/2019.csv")
    del happy_df['Overall rank']
    st.dataframe(happy_df)
    st.subheader("Выведем значения коэффициентов корреляции:")
    corr_df =happy_df.corr()
    st.dataframe(corr_df)
    gr_1 = alt.Chart(happy_df).mark_circle().encode(
          x='GDP per capita', y='Score', color='Country or region', tooltip=['Country or region', 'GDP per capita', 'Score'])
    st.altair_chart(gr_1, use_container_width=True)
    gr_2 = alt.Chart(happy_df).mark_circle().encode(
          x='Social support', y='Score', color='Country or region', tooltip=['Country or region', 'Social support', 'Score'])
    st.altair_chart(gr_2, use_container_width=True)
    gr_3 = alt.Chart(happy_df).mark_circle().encode(
          x='Perceptions of corruption', y='Score', color='Country or region', tooltip=['Country or region', 'Perceptions of corruption', 'Score'])
    st.altair_chart(gr_3, use_container_width=True)
    st.subheader("Давайте построим линейную регрессию на основе этих данных. Найдем коэффициенты модели:")
    new_df = happy_df.drop(['Score','Country or region'],axis=1)
    model = LinearRegression()
    model.fit(new_df, happy_df["Score"])
    coefficients= model.coef_
    st.text(coefficients)
    pred_scores = cross_val_predict(model, new_df, happy_df["Score"], cv=10)
          fig, ax = plt.subplots()
    ###FROM https://scikit-learn.org/stable/auto_examples/ensemble/plot_stack_predictors.html#sphx-glr-auto-examples-ensemble-plot-stack-predictors-py:
    ax.scatter(happy_df["Score"], pred_scores, edgecolors=(0, 0, 0))
    ax.plot([happy_df["Score"].min(), happy_df["Score"].max()], [happy_df["Score"].min(), happy_df["Score"].max()], "k--", lw=4)
    ###END FROM
    ax.set_xlabel("Measured scores")
    ax.set_ylabel("Predicted scores")
    st.pyplot(fig)
    st.subheader("Немного работы с графами:")
    st.caption('Например, графы могут использоваться для визуализации торговых связей между странами. Давайте рассмотрим это на примере нескольких стран')
    st.caption('Данные были взяты со страницы ниже:')
    st.markdown("https://oec.world/")
    exp_df= pd.DataFrame({'Ex_country': ['United Kingdom', 'United Kingdom', 'United Kingdom','Switzerland','Switzerland','Switzerland','Switzerland','Switzerland','Germany','Germany','Germany','Germany','China','China','China','Japan','Japan','United States','United States','United States','France','France','France','Italy','Italy','Italy','Italy','Italy'], 'Imp_country': ['United States', 'Germany', 'France','United States','Germany','China','United Kingdom','France','United States','China','France','United Kingdom','United States','Japan','Germany','China','United States','China','Japan','Germany','Germany','United States','Italy','Germany','France','United States','Switzerland','United Kingdom'], 'Export(billion dollars)': [51.7,39.9,22.4,62,49.2,17.3,14.5,16.3,116,106,101,74.4,438,151,112,133,112,122,63.1,59.2,65.2,36.7,36,62.1,49.5,47.9,25.1,25]})
    pd.pivot_table(exp_df,index=["Ex_country", "Imp_country"])
    exp_df
    G = nx.MultiDiGraph()
    G.add_node("Italy")
    G.add_node("Germany")
    G.add_node("France")
    G.add_node("United States")
    G.add_node("United Kingdom")
    G.add_node("Switzerland")
    G.add_node("China")
    G.add_node("Japan")
    G.add_edges_from([("China", "United States"),("China", "Japan"),("China", "Germany"),("United States", "China"),("United States", "Japan"),
           ("United States", "Germany"),("Germany", "United States"),("Germany", "China"),("Germany", "France"),("Germany", "United Kingdom"),
           ("France", "Germany"),("France", "United States"),("France", "Italy"),("Italy", "Germany"),("Italy", "France"),("Italy", "United States"),
           ("Italy", "Switzerland"),("Italy", "United Kingdom"),("United Kingdom", "Germany"),("United Kingdom", "France"),("United Kingdom", "United States"),
           ("Japan", "United States"),("Japan", "China"),("Switzerland", "United States"),("Switzerland", "China"),("Switzerland", "France"),("Switzerland", "Germany"),("Switzerland", "United Kingdom")])
    fig_ex, ax = plt.subplots()
    pos = nx.kamada_kawai_layout(G)
    nx.draw(G,pos, with_labels=True,alpha=1, edge_color="r",arrows=True, arrowsize=21,node_color='w')
    st.pyplot(fig_ex)
    st.subheader("Регулярные выражения:")
    st.caption('Например, можно использовать этот метод, когда в статье или тексте используется много незнакомых вам аббревиатур. С помощью регулярных выражений вы сможете собрать список этих аббревиатур')
    st.caption('Для примера рассмотрим фрагмент этой статьи:')
    st.markdown("https://www.imf.org/en/Topics/imf-and-covid19/Policy-Responses-to-COVID-19")
    text = 'Vaccination of another 28 percent of population is expected to be funded by World Bank and ADB grants. The authorities rolled out 0.8 percent of GDP social assistance under the World Bank-funded REACH program in 2020. The Bank of Albania announced it had set up a €400 million repo line with the ECB. Imports of pharmaceutical products used in the fight against Covid-19 were temporarily exonerated from VAT. In terms of spending measures, a SFL enacted on June 4, 2020 included provisions amounting to DZD 70 bn dinars to mitigate the health and economic impacts of the COVID-19 crisis. '
    st.caption(text)
    abbr_1 = re.findall(" [A-Z][A-Z][A-Z] ", text)
    abbr_2 = re.findall(" [A-Z][A-Z][A-Z]\.", text)
    abbr = abbr_1+abbr_2
    st.caption('Получим следующий список аббревиатур:')
    st.text(abbr)
    st.text('ADB - Asina Development Bank')
    st.text('GDP - Gross domestic product')
    st.text('SFL - Supplementary finance law')
    st.text('DZD - Algerian dinar')
    st.text('ECB - European Central Bank')
    st.text('VAT - Value-added tax')
