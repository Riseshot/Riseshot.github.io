import csv

reader = csv.reader(open("archinect_survey_results_gps", "rU"), delimiter=',')
writer = csv.writer(open("archinect_survey_results_gps_delimiter.txt", 'w'), delimiter=';')
writer.writerows(reader)

print("Delimiter successfully changed")