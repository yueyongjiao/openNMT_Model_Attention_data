import os
import sys

path = sys.argv[1]
print path
gram_l = [2, 3]

fw = open('score_' + path, 'w')
len_l = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
cov_l = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
for ii in len_l:
    fw.write('=' * 50 + '\n')
    for jj in cov_l:
        one_file = 'pre.e30_len_' + str(ii) + '_cov_' + str(jj)
        print one_file
        s2 = 0
        n2 = 0
        s3 = 0
        n3 = 0
        for n_gram in gram_l:
            f = open(path + '/' + one_file)
            line_num = {}
            num_line = {}
            count = 0
            for line in f:
                line = line.strip().decode('utf8')
                inference = line.replace(' ', '')
                tp = {}
                for i in range(len(inference) - n_gram + 1):
                    a = inference[i:i + n_gram]
                    if a in tp:
                        line_num[inference] = count
                        num_line[count] = inference
                    tp[a] = 1
                count += 1
            f.close()
            if n_gram == 2:
                n2 = len(line_num)
                s2 = len(line_num) * 1.0 / count
            else:
                n3 = len(line_num)
                s3 = len(line_num) * 1.0 / count

            print count
            f.close()
        fw.write(one_file + '\t' + str(n2) + '\t' + str(round(s2, 5)) + '\t' + str(n3) + '\t' + str(round(s3, 5)) + '\n')
fw.close()

