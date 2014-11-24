#! /usr/bin/python
import urllib,os,shutil

cates = ["003.backpack","007.bat","012.binoculars","013.birdbath","018.bowling-pin","017.bowling-ball","022.buddha-101","024.butterfly","026.cake","032.cartman","036.chandelier-101","038.chimp","040.cockroach","046.computer-monitor","047.computer-mouse","051.cowboy-hat","052.crab-101","056.dog","054.diamond-ring","061.dumb-bell","062.eiffel-tower","063.electric-guitar-101","064.elephant-101","066.ewer-101","067.eyeglasses","080.frog","081.frying-pan","084.giraffe","085.goat","100.hawksbill-101","101.head-phones","110.hourglass","111.house-fly","112.human-skeleton","119.jesus-christ","120.joy-stick","121.kangaroo-101","122.kayak","124.killer-whale","126.ladder","131.lightbulb","132.light-house","134.llama-101","136.mandolin","140.menorah-101","141.microscope","143.minaret","144.minotaur","150.octopus","147.mushroom","151.ostrich","152.owl","153.palm-pilot","154.palm-tree","157.pci-card","158.penguin","165.pram","167.pyramid","168.raccoon","174.rotary-phone","177.saturn","179.scorpion-101","180.screwdriver","182.self-propelled-lawn-mower","183.sextant","185.skateboard","195.soda-can","197.speed-boat","198.spider","199.spoon","202.steering-wheel","203.stirrups","205.superman","209.sword","210.syringe","212.teapot","213.teddy-bear","214.teepee","216.tennis-ball","218.tennis-racket","219.theodolite","220.toaster","221.tomato","222.tombstone","223.top-hat","225.tower-pisa","226.traffic-light","228.triceratops","230.trilobite-101","231.tripod","232.t-shirt","235.umbrella-101","236.unicorn","239.washing-machine","240.watch-101","243.welding-mask","246.wine-bottle","250.zebra","253.faces-easy-101","254.greyhound","256.toad",]
url="http://www.vision.caltech.edu/Image_Datasets/Caltech256/images/"

imgs = open(r'cal256.usrlabel').read().strip().split()
dic ={}
for cate in cates:
    dic[cate[:3]]=cate

for img in imgs:
    print img
    if img in os.listdir('imgs'):
        print 'extant'
        shutil.copy2(r'./imgs/'+img,r'./imgs_label/'+img)
        continue
    cate = dic[img[:3]]
    img_url = url+cate+'/'+img
    urllib.urlretrieve(img_url,'./imgs_label/'+img)

