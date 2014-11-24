
    function point_it(cvs_id, event){
        //pos_x = event.offsetX?(event.offsetX):event.pageX-document.getElementById(cvs_id).offsetLeft;
        //pos_y = event.offsetY?(event.offsetY):event.pageY-document.getElementById(cvs_id).offsetTop;
        //pos_x = event.clientX?(event.clientX):event.pageX-document.getElementById(cvs_id).clientLeft;
        //pos_y = event.clientY?(event.clientY):event.pageY-document.getElementById(cvs_id).clientTop;
        //var pos = getMousePos(document.getElementById(cvs_id),event);
        //pos_x = pos.x;
        //pos_y = pos.y;
        var canvas = document.getElementById(cvs_id);
        var rect = canvas.getBoundingClientRect();
        var pos_x = event.clientX - rect.left;
        var pos_y = event.clientY - rect.top;
        var ctx = canvas.getContext("2d");
        ctx.strokeStyle="#FF0000"
        ctx.beginPath();
        ctx.arc(pos_x,pos_y,6,0,2*Math.PI);
        ctx.stroke();
        draw_line(cvs_id,ctx,pos_x,pos_y);
    }
    lrunning = 1;
    rrunning = 1;
    start_x = 0;
    start_y = 0;

    function draw_line(cvs_id,ctx,x,y){
        x = Math.round(x);
        y = Math.round(y);
        if(cvs_id=="mycanvas")
        switch(lrunning){
            case 1:
              start_x = x;
              start_y = y;
              lrunning = 2;
              break;
            case 2:
              ctx.beginPath();
              ctx.moveTo(start_x,start_y);
              ctx.lineTo(x,y);
              ctx.stroke();
              lrunning = 1;
              document.getElementById("coords").value = "("+start_x.toString()+","+start_y.toString()+"); ("+x.toString()+","+y.toString()+")";
              break;
        }
        else
         switch(rrunning){
            case 1:
              start_x = x;
              start_y = y;
              rrunning = 2;
              break;
            case 2:
              ctx.beginPath();
              ctx.moveTo(start_x,start_y);
              ctx.lineTo(x,y);
              ctx.stroke();
              rrunning = 1;
              document.getElementById("test_coords").value = "("+start_x.toString()+","+start_y.toString()+"); ("+x.toString()+","+y.toString()+")";
              break;
        }
    }
    
    var current_img = "";
    
    function showOldImg(){
        var canvas = document.getElementById("mycanvas")
        canvas.width = canvas.width;
        var ctx = canvas.getContext("2d");
        var img = new Image();
        img.onload = function(){
          ctx.drawImage(img,0,0,300,230);
      }
      img.src = current_img;
      document.getElementById("coords").value="";
    }

    function loadNewImg(){
        var canvas = document.getElementById("mycanvas");
        canvas.width = canvas.width;
        var ctx = canvas.getContext("2d");
        var url = "http://www.vision.caltech.edu/Image_Datasets/Caltech256/images/";
        var cates = ["003.backpack","007.bat","012.binoculars","013.birdbath","018.bowling-pin","017.bowling-ball","022.buddha-101","024.butterfly","026.cake","032.cartman","036.chandelier-101","038.chimp","040.cockroach","046.computer-monitor","047.computer-mouse","051.cowboy-hat","052.crab-101","056.dog","054.diamond-ring","061.dumb-bell","062.eiffel-tower","063.electric-guitar-101","064.elephant-101","066.ewer-101","067.eyeglasses","080.frog","081.frying-pan","084.giraffe","085.goat","100.hawksbill-101","101.head-phones","110.hourglass","111.house-fly","112.human-skeleton","119.jesus-christ","120.joy-stick","121.kangaroo-101","122.kayak","124.killer-whale","126.ladder","131.lightbulb","132.light-house","134.llama-101","136.mandolin","140.menorah-101","141.microscope","143.minaret","144.minotaur","150.octopus","147.mushroom","151.ostrich","152.owl","153.palm-pilot","154.palm-tree","157.pci-card","158.penguin","165.pram","167.pyramid","168.raccoon","174.rotary-phone","177.saturn","179.scorpion-101","180.screwdriver","182.self-propelled-lawn-mower","183.sextant","185.skateboard","195.soda-can","197.speed-boat","198.spider","199.spoon","202.steering-wheel","203.stirrups","205.superman","209.sword","210.syringe","212.teapot","213.teddy-bear","214.teepee","216.tennis-ball","218.tennis-racket","219.theodolite","220.toaster","221.tomato","222.tombstone","223.top-hat","225.tower-pisa","226.traffic-light","228.triceratops","230.trilobite-101","231.tripod","232.t-shirt","235.umbrella-101","236.unicorn","239.washing-machine","240.watch-101","243.welding-mask","246.wine-bottle","250.zebra","253.faces-easy-101","254.greyhound","256.toad",];
       //var cates = ["003.backpack","007.bat","012.binoculars","013.birdbath","018.bowling-pin","017.bowling-ball","022.buddha-101","024.butterfly","026.cake","032.cartman","036.chandelier-101","038.chimp","040.cockroach","046.computer-monitor","047.computer-mouse","051.cowboy-hat","052.crab-101","056.dog","054.diamond-ring","061.dumb-bell","067.eyeglasses","101.head-phones"];
        var i = Math.floor(Math.random()*cates.length);
        var j = Math.floor(1+Math.random()*90).toString();
        var name = "";
        switch(j.length){
            case 1:
              name = name + "000" + j;
              break;
            case 2:
              name = name + "00" + j;
              break;
            case 3:
                name = name + "0" + j;
                break;
            }
        var img_name = cates[i]+"/"+cates[i].split(".")[0]+"_"+name+".jpg";
        var img = new Image();
        img.onload = function(){
          ctx.drawImage(img,0,0,300,230);
        }
        current_img = url+img_name;
        img.src = current_img;
        document.getElementById("imgname").value = img_name;
        showImgFromDB();
        }
    
    function showImgFromDB(){
       var cvs = document.getElementById("test_canvas");
       cvs.width = cvs.width;
       var ctx = cvs.getContext("2d");
       var url = "http://www.vision.caltech.edu/Image_Datasets/Caltech256/images/";
       var test_cate = document.getElementById("test_cate").value;
       var test_imgname = document.getElementById("test_imgname").value;
       var test_sympoints = document.getElementById("test_sympoints").value;
       var testimg = new Image();
       testimg.onload = function(){
           ctx.drawImage(testimg,0,0,300,230);
           }
       testimg.src = url+test_cate+"/"+test_imgname;
       document.getElementById('test_coords').value="";
        }

    function reload(){
        window.location.href = "http://sundance.ist.psu.edu:8080/symcaptcha/";
        }

    function randomRGB(){
        var col = "rgb("+Math.floor(Math.random()*255).toString()+","+Math.floor(Math.random()*255).toString()+","+Math.floor(Math.random()*255).toString()+")";
        document.getElementById("div_result0").style.color = col;
        alert("qqqqq");
    }

