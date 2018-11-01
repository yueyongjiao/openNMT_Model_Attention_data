import os
import sys

path = sys.argv[1]
print path
#beam_l = ['base_beam_1pre.e30', 'cover1_beam_1pre.e30', 'cover5_beam_1pre.e30', 'cover10_beam_1pre.e30', 'coverw_beam_1pre.e30']
beam_l = ['coverw_beam1_pre.e30','cover5_beam1_pre.e30','cover10_beam1_pre.e30']
fw = open(path + '/rouge_score', 'w')
for beam in beam_l:
    fw.write('=' * 50 + '\n')
    # print one_file
    s = 'python to_id.py ' + path + '/' + beam
    # print s
    os.system(s)
    s = 'python test_rouge.py -c ' + path + '/' + beam + '_id -r 725_target_id'
    # print s
    res = os.popen(s)
    x = res.read()
    fw.write(beam + '\t' + x + '\n')
    fw.flush()
    res.close()
fw.close()

