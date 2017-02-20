$(document).on('click', '#btn-json', function() {
    $('#btn-json').addClass('active')
    $('#btn-result').removeClass('active')
    $('.result-visual').addClass('hide')
    $('.result-json').removeClass('hide')

});
$(document).on('click', '#btn-result', function() {
    $('#btn-json').removeClass('active')
    $('#btn-result').addClass('active')
    $('.result-visual').removeClass('hide')
    $('.result-json').addClass('hide')
});

$(document).on('click', '#try-url', function() {
    $('#input-demo-result').val('https://www.wongnai.com/restaurants/1667sR-%E0%B8%81%E0%B9%8B%E0%B8%A7%E0%B8%A2%E0%B8%88%E0%B8%B1%E0%B9%8A%E0%B8%9A%E0%B8%99%E0%B8%B2%E0%B8%A2%E0%B9%80%E0%B8%AD%E0%B9%87%E0%B8%81')
    $('.input-tag').text("URL")
    resizeTextarea()
})

$(document).on('click', '#try-keyword', function() {
    $('#input-demo-result').val('ซอร์เทรล สาทร Bangkok')
    $('.input-tag').text("KEYWORD")
    resizeTextarea()
})

$(document).on('click', '#try-phone', function() {
    $('#input-demo-result').val('02-690-1888')
    $('.input-tag').text("PHONE")
    resizeTextarea()
})

$(document).on('click', '#try-text', function() {
    $('#input-demo-result').val(`Krua Dok Mai Kao has regularly been packed out since it opened back in 2004, the brainchild of a savvy owner who saw the shortage of proper standalone restaurants in the Pathumwan neighborhood. Every day, office workers and families gather at the bright and airy two-story establishment, where bare concrete pillars stretch to the high ceilings amid a homey sprawl of marble tables, wooden seats and old-style armchairs. The menu has long been renowned for its international fare and bakery goods, which we feel masks the fact that the Thai offerings here lack authentic flavors. While popular dishes like the ham and cheese spring rolls (B105), baked baby clams with butter and garlic sauce served with French bread (B145) and spicy fried crispy cat fish with salted egg (B135) are all solid enough, others seem to be overloaded with sugar. The tom yam talay haeng (seafood with spicy sauce, B155) misses the point of the traditional recipe altogether, with the sweet notes totally overpowering the sour and spicy. It’s a similar story with the yam hed khem thong (spicy golden mushroom and shrimp salad, B95), which looks impressive but is all too saccharine and completely lacking in any tart lime, and the tom yum moo toon (spicy pork stew with herbs, B135/155), which is more a sweet soup than a spicy stew. That said, the kitchen is pretty quick and uses fresh ingredients, even if these aren’t always utilized to their full-flavored potential. In any case, the bakery is without a doubt the place’s strongest suit, serving a variety of delights where excessive sweetness is a good thing, like the tiramisu cake (B105) and Thai tea crepe cake (B105). If you’re stuck in this rather limited neighborhood for dining then Krua Dok Mai Kao isn’t a bad option, though limited parking and slightly slow service when they’re busy don’t exactly help. Just be prepared for a sugar rush whatever you decide to order. Corkage B300 (wine only). - See more at: http://bk.asia-city.com/restaurants/bangkok-restaurant-reviews/krua-dok-mai-kao#sthash.mwMtxT3B.dpuf`);
    $('.input-tag').text("TEXT")
    resizeTextarea()
})

function resizeTextarea() {
    var observe;
    if (window.attachEvent) {
        observe = function(element, event, handler) {
            element.attachEvent('on' + event, handler);
        };
    } else {
        observe = function(element, event, handler) {
            element.addEventListener(event, handler, false);
        };
    }
    $(document).ready(function() {
        var text = document.getElementById('input-demo-result');

        function resize() {
            text.style.height = 'auto';
            text.style.height = text.scrollHeight + 4 + 'px';
        }
        /* 0-timeout to get the already changed text */
        function delayedResize() {
            window.setTimeout(resize, 0);
        }
        observe(text, 'change', resize);
        observe(text, 'cut', delayedResize);
        observe(text, 'paste', delayedResize);
        observe(text, 'drop', delayedResize);
        observe(text, 'keydown', delayedResize);

        text.focus();
        text.select();
        resize();
    });
    // end auto resize textareaa
}

// auto tag

function isPhoneNumber(inputtxt) {
    var phoneno = /^\+?([0-9]{1,4})\)?[-. ]?([0-9\-]){6,}[0-9]|[0-9]{3,}?[-. ]?[0-9]$/;
    if(phoneno.test(inputtxt)) {
        return true;
    }
    else {
        return false;
    }
}
function isUrl(inputtxt){
    var urlPattern = /^(http[s]?:\/\/){0,1}(www\.){0,1}[a-zA-Z0-9\.\-]+\.[a-zA-Z]{2,5}[\.]{0,1}/;
    if(urlPattern.test(inputtxt)) {
        return true;
    }
    else {
        return false;
    }
}
function autotag(inputtxt){
    var MIN_LEN_TEXT = 50;
    if(inputtxt.trim().length == 0) return "";
    if(isUrl(inputtxt)) return "URL";
    else if(isPhoneNumber(inputtxt)) return "PHONE";
    else if( inputtxt.length < MIN_LEN_TEXT )
        return "KEYWORD"
    else
        return "TEXT"
}
$(document).on('input','#input-demo-first',function(){
    var inputtxt = $('#input-demo-first').val()
    var tag = autotag(inputtxt)
    $('.input-tag').text(tag)
})
$(document).on('input','#input-demo-result',function(){
    var inputtxt = $('#input-demo-result').val()
    var tag = autotag(inputtxt)
    $('.input-tag').text(tag)
})
// end auto tag

// MOCK

var result_keyword = {
    request: {
    input: "ซอร์เทรล สาทร Bangkok",
    type: "keyword",
    api: "analyze",
    version: "1.0.0",
    resolvedPageUrl: [
        "https://th.foursquare.com/v/sortrel-%E0%B8%8B%E0%B8%AD%E0%B8%A3%E0%B9%80%E0%B8%97%E0%B8%A3%E0%B8%A5/4ba267c0f964a5209cf537e3",
        "https://th.tripadvisor.com/Restaurant_Review-g293916-d3692361-Reviews-Sortrel_Restaurant-Bangkok.html",
        "http://www.painaidii.com/business/132857/sortrel-naratiwas-17-10120/lang/th/",
        "http://www.sortrel.co.th/sathorn_home.html",
        "http://www.painaidii.com/review/10509/sortrel-naratiwas-17-10120/lang/th/",
        "http://www.bumres.com/index.php?route=restaurant/information&restaurant_id=6415",
        "http://www.thaihometown.com/condo/655781",
        "https://th.tripadvisor.com/ShowUserReviews-g293916-d3692361-r332596219-Sortrel_Restaurant-Bangkok.html",
        "http://www.opensnap.com/th/bangkok/p-ซอร์เทรล-ทุ่งมหาเมฆ-อาหารเมดิเตอร์เรเนียน-พิซซ่า-พาสต้า-กุ้งแช่นำปลา-p201415298",
        "http://www.gplace.com/4816/à¸‹à¸­à¸£à¹Œà¹€à¸—à¸£à¸¥",
        "https://foursquare.com/user/4107912/list/bangkok",
        "http://www.youtube.com/watch?v=AZ7AjexrbqQ",
        "https://foursquare.com/user/20586472/list/bangkok",
        "http://www.prakardproperty.com/property/show/102327",
        "https://www.dotproperty.co.th/en/2-bedroom-condo-for-sale-in-thung-maha-mek-sathon_235534",
        "https://es.foursquare.com/v/sortrel-%E0%B8%8B%E0%B8%AD%E0%B8%A3%E0%B9%80%E0%B8%97%E0%B8%A3%E0%B8%A5/4ba267c0f964a5209cf537e3",
        "http://www.letsgobikingthailand.com/greenpeaceeng#!",
        "http://www.letsgobikingthailand.com/urban-oasis-specialeng#!",
        "http://www.prakardproperty.com/property/show/56298",
        "http://www.property1click.com/property-109308/",
        "http://www.thaihometown.com/condo/662239",
        "http://www.baanfinder.com/th/property/5398105_rhythm-sathornnarathiwas-floor22-a07",
        "http://www.novabizz.com/p73566/à¸‚à¸²à¸¢-à¸„à¸­à¸™à¹‚à¸”à¸£à¸´à¸—à¸¶à¹ˆà¸¡-à¸ªà¸²à¸—à¸£-à¸™à¸£à¸²à¸˜à¸´à¸§à¸²à¸ª-2-à¸™à¸­à¸™-2-à¸™à¹‰à¸³.html",
        "http://www.apartments.in.th/detail-19771-Rhythm%20Sathorn%20-%20Narathiwas.php",
        "http://www.choowap.co.th/hotel/%E0%B9%82%E0%B8%A3%E0%B8%87%E0%B9%81%E0%B8%A3%E0%B8%A1%E0%B9%80%E0%B8%94%E0%B8%AD%E0%B8%B0-%E0%B8%AA%E0%B8%B8%E0%B9%82%E0%B8%82%E0%B8%97%E0%B8%B1%E0%B8%A2-%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E",
        "http://www.lekkoo.com/location/L.P.N._Tower,_8th_floor,,_216/18_Thanong_Nong_Linchi,_Chongnonsi,_Yannawa,_Bangkok,_Thailand",
        "http://www.choowap.co.th/hotel/%E0%B9%82%E0%B8%A3%E0%B8%87%E0%B9%81%E0%B8%A3%E0%B8%A1%E0%B8%A1%E0%B8%93%E0%B9%80%E0%B8%91%E0%B8%B5%E0%B8%A2%E0%B8%A3-%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E",
        "https://ja.foursquare.com/baidawei/list/bangkok-night-life",
        "https://th.foursquare.com/prapapun_n/list/%E0%B8%95%E0%B8%B0%E0%B8%A5%E0%B8%AD%E0%B8%99%E0%B8%81%E0%B8%99-%E0%B8%95%E0%B8%B0%E0%B8%A5%E0%B8%AD%E0%B8%99%E0%B8%8A%E0%B8%A1-in-thailand",
        "http://th.soidb.com/bangkok/restaurant/list.html?pageNum=15&st%5B%5D=12&sort=date",
        "http://th.soidb.com/bangkok/restaurant/sp-bigc-suksawat.html",
        "http://www.gplace.com/%E0%B8%9A%E0%B8%A3%E0%B8%B4%E0%B8%A9%E0%B8%B1%E0%B8%97-%E0%B9%84%E0%B8%97%E0%B8%A2%E0%B8%A7%E0%B8%B2%E0%B8%9E%E0%B8%A5%E0%B8%B2%E0%B8%8B%E0%B9%88%E0%B8%B2-%E0%B8%88%E0%B8%B3%E0%B8%81%E0%B8%B1%E0%B8%94",
        "http://www.lekkoo.com/location/10_Thanon_Non_Si,_Yannawa,_Bangkok_10120,_Thailand",
        "http://kitkaanyai.com/images/BRT/BRT.pdf",
        "https://ja.foursquare.com/gift_2000/list/nigth-life"
    ]
},
    language: "th",
    result: {
        keywords: [
            "sortel",
            "ร้านอาหาร",
            "sortrel",
            "เช่าคอนโดมิเนียม",
            "foursquare",
            "search",
            "กรุงเทพกรุงเทพ",
            "คอนโดมิเนียมคอนโดมิเนียม",
            "คอนโดสาทร",
            "เช่าคอนโด",
            "thailand"
        ],
        contents: "ซอร์เทรล - th.foursquare.com  ซอร์เทรล, 1122 Naradhiwas Rajanagarindra Rd., สาทร, กรุงเทพมหานคร, @sortel,sortel,sortel  narathivath 17,sortel @ narathivath 17,sortel's,sortel's cottage,sortel@narathivad satorn,sortel@narathivath,sortelnarathivad satorn,sortelnarathivath, ร้านอาหาร, ผับ, สำรองที่, อาหารค่ำร้านอาหาร ซอร์เทรล, กรุงเทพมหานคร (กทม.) - รีวิวร้านอาหาร ...  ร้านอาหาร ซอร์เทรล, กรุงเทพมหานคร (กทม.), ร้านอาหาร, รีวิวร้านอาหาร, อาหาร, ห้องอาหารซอร์เทรล ,นราธิวาส 17 (Sortrel ,Naratiwas 17) - แผนที่ ... sortrel ซอร์เทรล ถ.นราธิวาส 17 สาทร pub&restaurant sathorn ... รีวิว ซอร์เทรล นราธิวาส 17 โดย meepooh 27 | PaiNaiDii.com ซอร์เทรล - Sortrel ร้านอาหาร , ถนนจันทน์, | รีวิว แผนที่ ...  ซอร์เทรล - Sortrel, ร้าน ซอร์เทรล - Sortrel, ซอร์เทรล - Sortrel รีวิว, ซอร์เทรล - Sortrel แผนที่, , , ให้เช่า คอนโด Bangkok Horizon นราธิวาส 14 เดินทางสะดวก ติด ...  คอนโดให้เช่า , ให้เช่าคอนโด , ให้เช่า คอนโด สาทร กรุงเทพมหานคร ,  คอนโด  , คอนโด กรุงเทพมหานคร , ให้เช่า คอนโด กรุงเทพมหานคร , คอนโด 39 ตารางเมตร , คอนโด สาทร , คอนโด สาทร  ให้เช่า คอนโดมิเนียม , คอนโดมิเนียมให้เช่า , คอนโดมิเนียม สาทร กรุงเทพมหานคร , ประกาศให้เช่า คอนโดมิเนียม 1 ห้องนอน 1 ห้องน้ำ , คอนโดมิเนียมประกาศให้เช่า , ให้เช่าคอนโดมิเนียม  , คอนโดมิเนียม พื้นที่ 39.00 ตารางเมตร , ให้เช่าคอนโดมิเนียม , คอนโดมิเนียมสำหรับให้เช่า , คอนโดมิเนียม 39.00 ตารางเมตร , คอนโดมิเนียม  , คอนโดมิเนียม 1 ห้องนอน 1 ห้องน้ำมีเฟรนช์ฟรายด์ฟรีให้ทอดเอง - ร้านอาหาร ซอร์เทรล  ร้านอาหาร ซอร์เทรล, กรุงเทพมหานคร (กทม.), ไทย, มีเฟรนช์ฟรายด์ฟรีให้ทอดเองกุ้งแช่นำปลา - ซอร์เทรล - จัดเลี้ยงเป็นกลุ่ม - ทุ่งมหาเมฆ ...  กรุงเทพและปริมลฑล,ซอร์เทรล,ทุ่งมหาเมฆ,จัดเลี้ยงเป็นกลุ่ม,กุ้งแช่นำปลา,OpenSnap,กรุงเทพและปริมลฑล,ร้านอาหาร,รูปอาหาร,เมนูอร่อย,เมนูแนะนำ,ส่วนลดร้านอาหาร,โปรโมชั่นร้านอาหาร,แชะชิมแชร์ซอร์เทรล อาหารซอร์เทรล ซอร์เทรลอร่อย เมนูซอร์เทรล แนะนำซอร ...  ซอร์เทรล, อาหาร, อร่อย, เมนู, เผา, ย่าง, ทอด, ทะเล, ตามสั่ง, ข้าว, ก๋วยเตี๋ยว, แนะนำอาหารซอร์เทรล, ซอร์เทรลอร่อย, เมนูซอร์เทรลBangkok - foursquare.com  Foursquare,foursq,4sq,check-in,badges,explore,recommendation,local,review,tip,restaurant,bar,coffee,park,New York,San Francisco,Chicago,London,sushi,pizza,cocktails,vacation,food,search,citiesบรรยากาศร้าน Sortrel (ซอร์เทรล) นราธิวาสราชนครินทร์ 17 ...  บรรยากาศร้าน Sortrel, ร้านเลิศรส, ร้าน Sortrel อยู่ไหน, รีวิวร้าน Sortrel, ร้านน่านั่งสีลม, ร้านน่านั่งพระราม 3, ร้านเหล้า นราธิวาส, ร้านนั่งชิวล์ ซอยนราธิวา...Bangkok - foursquare.com  Foursquare,foursq,4sq,check-in,badges,explore,recommendation,local,review,tip,restaurant,bar,coffee,park,New York,San Francisco,Chicago,London,sushi,pizza,cocktails,vacation,food,search,citiesขาย คอนโดริทึ่ม สาทร-นราธิวาส 2 นอน 2 น้ำ - กรุงเทพมหานคร ...  ขายคอนโด กรุงเทพมหานคร สาทร คอนโดริทึ่ม สาทร-นราธิวาส ตรงข้าม ซิตี้ วีว่า เดินทางสะดวก ติด BRT อาคารสงเคราะห์ 120 เมตร\r พื้นที่ 54.9 ตรม 2 ห้องนอน 2 ห้องน้ำ ชั้น 24 วิวสวย\r ชื่อโครงการ ริทึ่2 bed condo for sale in Thung Maha Mek, Sathon ฿7,500,000 ...  Thung Maha Mek, Sathon Condo for sale ★ 2 Bedrooms ✓ 60.50 m<sup>2</sup> ✓ 2 Bathrooms Price ฿7,500,000 #235534SORTREL (ซอร์เทรล) - ทุ่งมหาเมฆ - 127 tips de 9788 visitantes  SORTREL, 1122 Naradhiwas Rajanagarindra Rd., สาทร, กรุงเทพมหานคร, @sortel,sortel,sortel  narathivath 17,sortel @ narathivath 17,sortel's,sortel's cottage,sortel@narathivad satorn,sortel@narathivath,sortelnarathivad satorn,sortelnarathivath, Restaurante, Pub, Reservas, CenaLet's go Biking Thailand | Tour packages | Green Peace  Bang Kra Jao, Bang Krachao, Bangkok by bike, Bicycle tour Bangkok, Bike tour Bangkok, Let's go biking, Tempat wisata di bangkok, Tourist attractions in bangkok, What to do in BangkokLet's go Biking Thailand | Tour packages | Urban Oasis Special  Bang Kra Jao, Bang Krachao, Bangkok by bike, Bicycle tour Bangkok, Bike tour Bangkok, Let's go biking, Tempat wisata di bangkok, Tourist attractions in bangkok, What to do in Bangkokขายคอนโด RHYTHM Sathorn-Narathiwas fl24 - กรุงเทพมหานคร ...  ขายคอนโด กรุงเทพมหานคร สาทร อาคารสูง 27 ชั้น จำนวน 1 หลัง \r แบ่งเป็นห้องชุดสำหรับพักอาศัยจำนวน 300 ห้อง\r ห้องชุดสำหรับการพาณิชย์จำนวน 1 ห้อง\r \r สถานที่ใกล้เคียง\r สถานีรถไฟฟ้า : ใกล้บีทีเอสช่ขาย คอนโดริทึ่ม สาทร-นราธิวาส 2 นอน 2 น้ำ - Property1Click.com  ให้เช่า คอนโด rhythm สาทร นราธิวาส 35 ตรม. ชั้น 25 1 นอน ...  คอนโดให้เช่า , ให้เช่าคอนโด , ให้เช่า คอนโด สาทร กรุงเทพมหานคร ,  คอนโด  , คอนโด กรุงเทพมหานคร , ให้เช่า คอนโด กรุงเทพมหานคร , คอนโด 35 ตารางเมตร , คอนโด สาทร , คอนโด สาทร  ให้เช่า คอนโดมิเนียม , คอนโดมิเนียมให้เช่า , คอนโดมิเนียม สาทร กรุงเทพมหานคร , ประกาศให้เช่า คอนโดมิเนียม 1 ห้องนอน 1 ห้องน้ำ , คอนโดมิเนียมประกาศให้เช่า , ให้เช่าคอนโดมิเนียม  , คอนโดมิเนียม พื้นที่ 35.00 ตารางเมตร , ให้เช่าคอนโดมิเนียม , คอนโดมิเนียมสำหรับให้เช่า , คอนโดมิเนียม 35.00 ตารางเมตร , คอนโดมิเนียม  , คอนโดมิเนียม 1 ห้องนอน 1 ห้องน้ำRHYTHM Sathorn-Narathiwas floor22 A07 - BaanFinder.com ขาย คอนโดริทึ่ม สาทร-นราธิวาส 2 นอน 2 น้ำ อสังหาริมทรัพย์ ... คอนโด Rhythm Sathorn - Narathiwas ถนนนราธิวาสราชนครินทร์ ...  Rhythm Sathorn - Narathiwas,¶¹¹¹ÃÒ¸ÔÇÒÊÃÒª¹¤ÃÔ¹·Ãì á¢Ç§·Øè§ÁËÒàÁ¦ à¢µÊÒ·Ã ¡·Á.10102,¡ÃØ§à·¾ ,,N/A,ËÍ¾Ñ¡, Í¾ÒÃì·àÁé¹·ì, ¤Í¹â´, ºéÒ¹àªèÒ, ËéÍ§àªèÒ, Í¾ÒÃì·àÁ¹·ì, áÁ¹ªÑè¹, ÊØ¢ØÁÇÔ·, ÃÑª´Ò, ´Ô¹á´§, ËéÇÂ¢ÇÒ§, ÅÒ´¾ÃéÒÇ, ¾­Òä·, Í¹ØÊÒÇÃÕªÑÂ, ÃÒªà·ÇÕ, à¾ÅÔ¹¨Ôµ, ·Í§ËÅèÍ, ¹Ò¹Ò, ÍâÈ¡, ÊÕÅÁ, ÊÒ·Ã, ÊÒ¸Ã, ÃÒ§¹éÓ, ÊØ·¸ÔÊÒÃ, ¾ËÅâÂ¸Ô¹, ÍÒÃÕÂì, ÊÐ¾Ò¹¤ÇÒÂ, ã¡ÅéÃ¶ä¿¿éÒ, BTS, MRT, à»Ô´ãËÁè, àªèÒ, ãËéàªèÒ, apartment, condo, rent, sale   โรงแรมเดอะ สุโขทัย กรุงเทพ , กรุงเทพฯ - Sukhothai Hotel ...  โรงแรมเดอะ สุโขทัย กรุงเทพ,กรุงเทพฯ,กรุงเทพ,Hotel,Resort,Hotel กรุงเทพ,Resort กรุงเทพ,Booking,Accommodation,ThailandL.P.N. Tower, 8th floor,, 216/18 Thanong Nong Linchi ...  L.P.N. Tower, 8th floor,, 216/18 Thanong Nong Linchi, Chongnonsi, Yannawa, Bangkok, Thailand, local search, local search engine, location based search engine, website to location, latitude longitudeโรงแรมมณเฑียร กรุงเทพ , กรุงเทพฯ - Montien Hotel Bangkok  โรงแรมมณเฑียร กรุงเทพ,กรุงเทพฯ,กรุงเทพ,Hotel,Resort,Hotel กรุงเทพ,Resort กรุงเทพ,Booking,Accommodation,ThailandBangkok Night Life - ja.foursquare.com  Foursquare、foursq、4sq、チェックイン、バッジ、explore、おすすめ、ローカルレビュー、tip、レストラン、バー、コーヒー、公園、ニューヨーク、サンフランシスコ、シカゴ、ロンドン、すし、ピザ、カクテル、バケーション、食べ物、検索、街ตะลอนกิน ตะลอนชิม in Thailand  Foursquare,foursq,4sq,เช็คอิน,ป้าย,สำรวจ,คำแนะนำ,ท้องถิ่น,ความคิดเห็น,คำแนะนำ,ร้านอาหาร,บาร์,กาแฟ,สวน,นิวยอร์ก,ซานฟรานซิสโก,ชิคาโก,ลอนดอน,ซูชิ,พิซซ่า,คอกเทล,วันหยุด,อาหาร,ค้นหา,เมืองกรุงเทพมหานคร - กิน - ร้านอาหาร - รายการ Page 15 [ประเภท ...  รายการ Page 15, ร้านอาหาร, กิน, กรุงเทพมหานคร, ไทยเอส แอนด์ พี - บิ๊กซี สุขสวัสดิ์ [กรุงเทพมหานคร ...  เอส แอนด์ พี - บิ๊กซี สุขสวัสดิ์, เดลี่/เบเกอรี่, ร้านอาหาร, กิน, กรุงเทพมหานคร, ไทยบริษัท ไทยวาพลาซ่า จำกัด  บริษัท ไทยวาพลาซ่า จำกัด,บริษัท,กรุงเทพมหานคร10 Thanon Non Si, Yannawa, Bangkok 10120, Thailand - Map ...  10 Thanon Non Si, Yannawa, Bangkok 10120, Thailand, local search, local search engine, location based search engine, website to location, latitude longitudeNigth Life - ja.foursquare.com  Foursquare、foursq、4sq、チェックイン、バッジ、explore、おすすめ、ローカルレビュー、tip、レストラン、バー、コーヒー、公園、ニューヨーク、サンフランシスコ、シカゴ、ロンドン、すし、ピザ、カクテル、バケーション、食べ物、検索、街"
    },
    category: [
        {
            name: "Accommodation",
            score: "1.0",
            confidence: "Yes"
        },
        {
            name: "Airline",
            score: "8.24013736644e-13",
            confidence: "No"
        },
        {
            name: "Restaurant & Delivery",
            score: "7.96242076485e-18",
            confidence: "No"
        },
        {
            name: "Tourism",
            score: "1.19205234345e-35",
            confidence: "No"
        }
    ]};
var result_url = {
    request: {
    input: "https://www.wongnai.com/restaurants/1667sR-%E0%B8%81%E0%B9%8B%E0%B8%A7%E0%B8%A2%E0%B8%88%E0%B8%B1%E0%B9%8A%E0%B8%9A%E0%B8%99%E0%B8%B2%E0%B8%A2%E0%B9%80%E0%B8%AD%E0%B9%87%E0%B8%81",
    type: "url",
    api: "analyze",
    version: "1.0.0",
    resolvedPageUrl: [
        "https://www.wongnai.com/restaurants/1667sR-%E0%B8%81%E0%B9%8B%E0%B8%A7%E0%B8%A2%E0%B8%88%E0%B8%B1%E0%B9%8A%E0%B8%9A%E0%B8%99%E0%B8%B2%E0%B8%A2%E0%B9%80%E0%B8%AD%E0%B9%87%E0%B8%81"
    ]
},
    language: "th",
    result: {
        keywords: [
            "deal",
            "guay",
            "jab",
            "marketplace",
            "nai",
            "restaurant",
            "wongnai",
            "ก๋วยจั๊บ",
            "ก๋วยเตี๋ยวรีวิว",
            "คูปองวง",
            "จั๊บนาย"
        ],
        contents: "ก๋วยจั๊บนายเอ็ก,Guay Jab Nai X,สัมพันธวงศ์,กรุงเทพมหานคร,ก๋วยเตี๋ยว,รีวิว,เมนูแนะนำ,รูปภาพอาหาร,รูปอาหาร,ร้านเด็ด,ร้านอร่อย,ร้านอาหาร,อาหาร,เส้นทาง,แผนที่,ส่วนลด,คูปอง,วงใน,restaurant,deal,wongnai,marketplace"
    },
    category: [
        {
            name: "Restaurant & Delivery",
            score: "1.0",
            confidence: "Yes"
        },
        {
            name: "Accommodation",
            score: "1.75426668581e-08",
            confidence: "No"
        },
        {
            name: "Airline",
            score: "3.41040544427e-28",
            confidence: "No"
        },
        {
            name: "Tourism",
            score: "7.68875881371e-33",
            confidence: "No"
        }
    ]};
var result_phone = {
    request: {
        input: "02-690-1888",
        type: "phone",
        api: "analyze",
        version: "1.0.0",
        resolvedPageUrl: [
            "https://www.facebook.com/CourtyardMarriottBkk?rf=165324766831122",
            "https://www.facebook.com/media/set/?set=a.481579465215404.110703.138183282888359&type=1",
            "http://www.bkkmenu.com/restaurant/Momo-Cafe",
            "https://th-th.facebook.com/CourtyardMarriottBkk/",
            "https://pantip.com/topic/35886002#!",
            "https://www.bts.co.th/customer/th/02-route-area.aspx",
            "http://www.greenleafthai.org/th/green_hotel/detail.php?ID=2999",
            "https://www.bts.co.th/customer/en/02-route-area.aspx",
            "http://directory.mthai.com/detail/MD11702423.html",
            "http://www.centralbangkok.org/th/event-cate/promotion-th/",
            "http://www.centralbangkok.org/th/cpt_events/sparkling-new-years-eve-dinner-buffet/",
            "https://toeysk.wordpress.com/2013/04/14/130-momo-cafe-courtyard-by-marriott-international-lunch-buffet/",
            "http://travel.truelife.com/detail/38557",
            "http://www.bangkokpost.com/travel/accommodation/26078/courtyard-by-marriott-bangkok",
            "http://www.bangkokair.com/tha/flyerbonus/view/courtyard-awards",
            "http://www.bangkokair.com/tha/flyerbonus/view/earn-points-Courtyard",
            "http://th.soidb.com/bangkok/hotel/courtyard-bangkok.html",
            "http://www.thaihotelnews.com/promotion/details/3235",
            "https://th-th.facebook.com/Quppee/",
            "https://www.thaihoteldeal.com/mobile/promotion/3139?/mobile/promotion/3139",
            "http://www.quppee.com/restaurant/1272--_MoMo_Cafe_",
            "http://m.visitorstothailand.com/docs/pages/page-hotel-bkk-siam.html",
            "http://www.imgrum.net/user/courtyardbangkok/417719161",
            "https://toeysk.wordpress.com/category/buffet/",
            "http://www.maymey.com/archives/tag/chef-table-momo-cafe-courtyard-by-marriott-bangkok/",
            "http://www.ipick.com/bangkok/th/restaurant/30005309",
            "https://www.wongnai.com/restaurants/4352Op-momo-cafe",
            "http://th.soidb.com/bangkok/bar-pub/momo-bar.html",
            "http://www.thaihotelnews.com/promotion/details/3139",
            "http://www.weddingsquare.com/forum_posts.asp?TID=154373",
            "http://www.bangkokhut.com/%e0%b8%9a%e0%b8%b8%e0%b8%9f%e0%b9%80%e0%b8%9f%e0%b8%95%e0%b9%8c%e0%b8%94%e0%b8%b4%e0%b8%99%e0%b9%80%e0%b8%99%e0%b8%ad%e0%b8%a3%e0%b9%8c-momo-cafe-courtyard-by-marriott-bangkok.html",
            "http://www.soidb.com/bangkok/bar-pub/momo-bar.html",
            "http://www.soidb.com/bangkok/spa/mood-m.html",
            "http://www.nationmultimedia.com/travel/Island-in-the-sun-30270348.html",
            "http://www.maymey.com/archives/tag/%e0%b8%a3%e0%b8%b5%e0%b8%a7%e0%b8%b4%e0%b8%a7/",
            "http://at-bangkok.com/seafood-buffet-promotion-momo-caf/",
            "http://www.lookeastmagazine.com/2013/08/dining-specials-august-2013/",
            "http://saleherethailand.com/promotion/food-drink/20-restaurant-past2/",
            "http://www.kbsthailand.com/upload_file/1%20Bangkok%20Summer%20Promotion%20Package%20on%20Mar.%2001,%202016%20-%20Jun.%2030,%202016.pdf",
            "http://baiyokesiam.com/index.php?option=com_content&view=article&id=3&Itemid=20",
            "http://hello2day.com/momo-cafe-international-lunch-buffet-courtyard-by-marriott/",
            "http://eatwithpete.com/momo-cafe-2017/",
            "http://eataroi.com/%e0%b8%9a%e0%b8%b8%e0%b8%9f%e0%b9%80%e0%b8%9f%e0%b9%88%e0%b8%95%e0%b9%8c%e0%b8%a1%e0%b8%b7%e0%b9%89%e0%b8%ad%e0%b8%81%e0%b8%a5%e0%b8%b2%e0%b8%87%e0%b8%a7%e0%b8%b1%e0%b8%99-momo-cafe-%e0%b9%82%e0%b8%a1%e0%b9%82%e0%b8%a1%e0%b9%88%e0%b8%84%e0%b8%b2%e0%b9%80%e0%b8%9f%e0%b9%88-%e0%b8%9a%e0%b8%b8%e0%b8%9f%e0%b9%80%e0%b8%9f%e0%b9%88%e0%b8%95%e0%b9%8c%e0%b9%82%e0%b8%a3%e0%b8%87%e0%b9%81%e0%b8%a3%e0%b8%a1-courtyard-by-marriott-bangkok/",
            "http://www.imgrum.net/tag/courtyardbangkok",
            "http://eataroi.com/%e0%b8%a3%e0%b8%b5%e0%b8%a7%e0%b8%b4%e0%b8%a7-%e0%b8%9a%e0%b8%b8%e0%b8%9f%e0%b9%80%e0%b8%9f%e0%b9%88%e0%b8%95%e0%b9%8c%e0%b8%ad%e0%b8%b2%e0%b8%ab%e0%b8%b2%e0%b8%a3%e0%b8%99%e0%b8%b2%e0%b8%99%e0%b8%b2%e0%b8%8a%e0%b8%b2%e0%b8%95%e0%b8%b4-%e0%b8%a1%e0%b8%b7%e0%b9%89%e0%b8%ad%e0%b9%80%e0%b8%a2%e0%b9%87%e0%b8%99%e0%b8%a7%e0%b8%b1%e0%b8%99%e0%b8%a8%e0%b8%b8%e0%b8%81%e0%b8%a3%e0%b9%8c-%e0%b8%ab%e0%b9%89%e0%b8%ad%e0%b8%87%e0%b8%ad%e0%b8%b2%e0%b8%ab%e0%b8%b2%e0%b8%a3-momo-cafe%e0%b9%82%e0%b8%a3%e0%b8%87%e0%b9%81%e0%b8%a3%e0%b8%a1-courtyard-by-marriott-bangkok/",
            "http://job.hotelier-th.com/job_positionview.php?key=26934",
            "http://www.siksinhot.com/P/368493",
            "https://es-la.facebook.com/CourtyardMarriottBkk/",
            "http://job.hotelier-th.com/job_positionview.php?key=26750",
            "http://www.yummygallery.com/momo-cafe-courtyard-marriott/"
        ]
    },
    language: "th",
    result: {
        keywords: [
            "โรงแรม",
            "courtyard",
            "momo",
            "marriott",
            "cafe",
            "tea",
            "thailand",
            "ร้านอาหาร",
            "news",
            "airline",
            "bar"
        ],
        contents: "Courtyard Bangkok | Facebook Momo Cafe' @ Courtyard by Marriott Bangkok | Facebook Momo Cafe (โมโม คาเฟ่) - BKKMENU.com Courtyard Bangkok | Facebook แวะกินข้าวเที่ยง Lunch Buffet @ MoMo Cafe  ย่านราชดำริมีโรงแรมตั้งอยู่ติดๆ กันหลายแห่ง หนึ่งในนั้น คือ โรงแรมคอร์ทยาร์ด โดย แมริออท กรุงเทพ ที่ตั้งอยู่ภายในซอยมหาดเล็กหลวง 1 ซึ่งเมื่อหลายวันก่อน ฮูกน้อยพเส้นทางให้บริการ : BTSC Smoke-Free Hotel  Smoke-Free HotelCurrent Service Routes - BTSC Courtyard By Marriott Bangkok : เลขที่ 155/1 ...  Courtyard By Marriott Bangkok, Courtyard By Marriott Bangkok แผนที่, Courtyard By Marriott Bangkok เบอร์โทรศัพท์, Courtyard By Marriott Bangkok รีวิว, ท่องเที่ยวและโรงแรม > ที่พัก-โรงแรมโปรโมชั่นพิเศษ - Central Bangkok ร่วมฉลองวันขึ้นปีใหม่ 2558 ที่โมโม่คาเฟ่ - Central Bangkok 130. MoMo Cafe – Courtyard by Marriott [International ...   MomoCafé ที่ตั้ง : โรงแรมคอร์ทยาร์ด แมริออท กรุงเทพฯ (Courtyard by Marriott Bangkok) ซอย มหาดเล็กหลวง 1 ถนนราชดำริกรุงเทพฯ 10330 เบอร์โทรศัพท์ : 02-690-1888 เว็บไซต์ : www.courtyardbangkok.com วัน-เวลาเปิดบริการ : เปิดบริการทุกวัน ตั้งแต่ 6.00 น. – 01.00 น. บรรยากาศจะออกแนวโปร่ง โล่งสบาย ให้ความรู้สึกผ่อนคลาย เหมาะกับมาทานอาหารกลางวันแบบ business lunch ค่ะ ตรงส่วนของไลน์บุฟเฟ่ต์เริ่มด้วยสลัดบาร์ seafood on ice, ceasar salad และซุปค่ะ ส่วนของหวานและชีส ผลไม้ ส่วนอาหารปรุงเสร็จ ฃ อาหารไทย พิซซ่า ปลาดิบ ซูชิ และพวก cold cut ครัวเปิดค่ะ ไอศกรีมและท็อปปิ้ง ส่วนของทานเล่น พวกแซนวิชต่างๆ ถ้าไม่อยากหนักท้องทานบุฟเฟต์ค่ะ…เปิดตัวโฉมใหม่ MoMo Cafe คาเฟ่บรรยากาศสบายๆ สไตล์คนเมือง  ร้านอาหารโรงแรม,momocafe,ร้านอาหารกรุงเทพ,อาหารไทย,อาหารฟิวชั่น,courtyardbymarriottbangkokCourtyard by Marriott Bangkok | Bangkok Post: Travel  Courtyard by Marriott Bangkok, news,breaking news,latest news,current news,world news,national news,business news,Thai newsแลกรางวัลกับโรงแรมคอร์ทยาร์ด โดย แมริออท - บางกอกแอร์เวย์ส  บางกอกแอร์เวย์ส, Bangkok Airways, бангкок эйрвейз, бангкок эйрвейз, バンコクエアウェイズ, Koh Samui, Airline, Thailand Airline, Airline in Thailand, Trat, Krabi, Lampang, Pattaya, Phuket, Samui, Sukhothai, Chiang Mai, Bengaluru, Dhaka, Hong Kong, Kuala Lumpur, Luang Prabang, Malé, Mumbai, Phnom Penh, Siem Reap, Singapore, Yangonโรงแรมคอร์ทยาร์ด โดย แมริออท - บางกอกแอร์เวย์ส  บางกอกแอร์เวย์ส, Bangkok Airways, бангкок эйрвейз, бангкок эйрвейз, バンコクエアウェイズ, Koh Samui, Airline, Thailand Airline, Airline in Thailand, Trat, Krabi, Lampang, Pattaya, Phuket, Samui, Sukhothai, Chiang Mai, Bengaluru, Dhaka, Hong Kong, Kuala Lumpur, Luang Prabang, Malé, Mumbai, Phnom Penh, Siem Reap, Singapore, YangonCourtyard Bangkok [กรุงเทพมหานคร - โรงแรม] - SoiDB ไทย  Courtyard Bangkok, โรงแรม, ที่พัก, กรุงเทพมหานคร, ไทยSpecial Chinese Food Corners at Momo Cafe : www ...  โปรโมชั่นโรงแรม, โปรโมชั่นร้านอาหาร, โปรโมชั่น Courtyard by Marriott Bangkok Quppee | Facebook ข่าวโรงแรม ข่าวโรงแรมไทย ประชาสัมพันธ์โรงแรม โปรโมทโรงแรม ...  ข่าวโรงแรม,ประชาสัมพันธ์โรงแรม,โปรโมทโรงแรม,โปรโมทร้านอาหาร,โปรโมชั่นโรงแรม,โปรโมชั่นร้านอาหาร,โฆษณาโรงแรม,โฆษณาร้านอาหารQuppee - Restaurant - ห้องอาหาร MoMo Cafe ACCOMMODATION IN BANGKOK - Visitors to Thailand Courtyard by Marriott Bangkok (@courtyardbangkok ...  Courtyard by Marriott Bangkok, courtyardbangkokBuffet | toeysk.  Posts about Buffet written by toeyskChef Table. MoMo Café. Courtyard by Marriott Bangkok ... ร้าน MoMo Cafe (Courtyard by Marriott) แผนที่ เบอร์โทร ...  รายละเอียดร้าน MoMo Cafe (Courtyard by Marriott) | นานาชาติ - คาเฟ่ | ปทุมวัน รีวิวพร้อมรูปภาพและเมนูแนะนำร้าน MoMo Cafe (โมโม่คาเฟ่) - Wongnai  MoMo Cafe,โมโม่คาเฟ่,ปทุมวัน,กรุงเทพมหานคร,อาหารนานาชาติ,บุฟเฟ่ต์,รีวิว,เมนูแนะนำ,รูปภาพอาหาร,รูปอาหาร,ร้านเด็ด,ร้านอร่อย,ร้านอาหาร,อาหาร,เส้นทาง,แผนที่,ส่วนลด,คูปอง,วงใน,restaurant,deal,wongnai,marketplaceMoMo Bar [กรุงเทพมหานคร - บาร์/ผับ] - SoiDB ไทย  MoMo Bar, บาร์/ผับ, ไนท์ไลฟ์, กรุงเทพมหานคร, ไทยSparkling New Year's Eve Dinner Buffet - thaihotelnews.com  โปรโมชั่นโรงแรม, โปรโมชั่นร้านอาหาร, โปรโมชั่น Courtyard by Marriott Bangkok แต่งงาน หาสถานที่จัดงานแต่งงานค่ะ - WeddingSquare  แต่งงาน หาสถานที่จัดงานบุฟเฟต์มื้อกลางวัน Momo Cafe Courtyard by Marriott Bangkok  อร่อยไม่ซ้ำระดับอินเตอร์ กับบุฟเฟต์นานาชาติมื้อกลางวัน Momo Cafe CourtyaMoMo Bar [Bangkok - Bar/Pub] - SoiDB Thailand  MoMo Bar, Bar/Pub, Nightlife, Bangkok, ThailandThe Mood@M [Bangkok - Spa] - SoiDB Thailand  The Mood@M, Spa, Wellness, Bangkok, ThailandIsland in the sun - The Nation  Soneva Kiri in Koh Kood is offering a two-night Ever Soneva So Sabai Sabai package ...รีวิว – เมเม่รีวิว: กิน พัก เที่ยว ไอที Gadget Seafood Buffet Promotion at Momo Café  promotionLOOKEAST: Dining Specials - August 2013  Special deals for dining in August 2013*+รวมโปรโมชั่น “วันแม่ ปี 58” จากร้านดัง 20 แห่ง!! (ภาค 2 ... BANGKOK SUMMER PROMOTION PACKAGE Customers List - baiyokesiam.com  Black tea,Green tea,Oolong tea,White tea,Red tea,Herbal tea,Decaf,Organics tea,Caffeine free tea,Ice tea,Fruit tea,Edmond,Rooibosch,Ayurvedaนั่งชิล กินเพลิน อิ่มจนพุงกางกับบุฟเฟ่ต์มื้อกลางวันที่ ...  \t \t\tติดตามเรื่องราวของเราบน Facebook คลิกที่นี่ ได้เลยครับ ^^ Comments commentsชวนชิมบุฟเฟ่ต์ราคาสบายๆ เช้า กลางวัน เย็น ที่ MoMo Café ... รีวิว บุฟเฟ่ต์มื้อกลางวัน Momo Cafe (โมโม่คาเฟ่) บุฟเฟ่ต์ ...  momo cafe,โมโม่คาเฟ่,บุฟเฟ่ต์มื้อกลางวัน,บุฟเฟ่ต์โรงแรมImages tagged with #courtyardbangkok on instagram  courtyardbangkok, instagram, imagesรีวิว บุฟเฟ่ต์อาหารนานาชาติ มื้อเย็นวันศุกร์ ห้องอาหาร ...  momo cafe,โมโม่คาเฟ่,บุฟเฟ่ต์มื้อเย็นวันศุกร์,บุฟเฟ่ต์โรงแรม,dinner,finedine,fridaynight,hangout,marriottGuest Relations Manager Courtyard by Marriott Bangkok ...  thaihoteljob jobs part time careers hospitality industry catering job chef employment career bangkok phuket thailand vacancies vacancy position receptionist positions recruitment work it reservation restaurant spa thaihotelstaff tourism training กรุงเทพ งานโรงแรม งาน ตำแหน่ง ตำแหน่งงานว่าง ท่องเที่ยว ไทย ประเทศไทย รับสมัคร  รับสมัครงาน ร้านอาหาร รีสอร์ท สมัคร สมัครงาน หางาน โรงแรมSpice Market (스파이스마켓)|태국-방콕맛집, 일식/중식/세계음식맛집  태국-방콕맛집,Spice Market (스파이스마켓)맛집,회식,모임,데이트,추천맛집,베스트10Courtyard Bangkok | Facebook F&B Service Supervisor Courtyard by Marriott Bangkok ...  thaihoteljob jobs part time careers hospitality industry catering job chef employment career bangkok phuket thailand vacancies vacancy position receptionist positions recruitment work it reservation restaurant spa thaihotelstaff tourism training กรุงเทพ งานโรงแรม งาน ตำแหน่ง ตำแหน่งงานว่าง ท่องเที่ยว ไทย ประเทศไทย รับสมัคร  รับสมัครงาน ร้านอาหาร รีสอร์ท สมัคร สมัครงาน หางาน โรงแรมMomo Cafe : บุฟเฟ่ต์ซีฟู้ด เนื้อย่างและอาหารนานาชาติ ...  "
    },
    category: [
        {
            name: "Accommodation",
            score: "1.0",
            confidence: "Yes"
        },
        {
            name: "Airline",
            score: "1.55351363851e-05",
            confidence: "No"
        },
        {
            name: "Tourism",
            score: "5.07467858445e-37",
            confidence: "No"
        },
        {
            name: "Restaurant & Delivery",
            score: "5.28872599601e-46",
            confidence: "No"
        }
    ]
};
var result_text = {
    request: {
        input: "Krua Dok Mai Kao has regularly been packed out since it opened back in 2004, the brainchild of a savvy owner who saw the shortage of proper standalone restaurants in the Pathumwan neighborhood. Every day, office workers and families gather at the bright and airy two-story establishment, where bare concrete pillars stretch to the high ceilings amid a homey sprawl of marble tables, wooden seats and old-style armchairs. The menu has long been renowned for its international fare and bakery goods, which we feel masks the fact that the Thai offerings here lack authentic flavors. While popular dishes like the ham and cheese spring rolls (B105), baked baby clams with butter and garlic sauce served with French bread (B145) and spicy fried crispy cat fish with salted egg (B135) are all solid enough, others seem to be overloaded with sugar. The tom yam talay haeng (seafood with spicy sauce, B155) misses the point of the traditional recipe altogether, with the sweet notes totally overpowering the sour and spicy. It’s a similar story with the yam hed khem thong (spicy golden mushroom and shrimp salad, B95), which looks impressive but is all too saccharine and completely lacking in any tart lime, and the tom yum moo toon (spicy pork stew with herbs, B135/155), which is more a sweet soup than a spicy stew. That said, the kitchen is pretty quick and uses fresh ingredients, even if these aren’t always utilized to their full-flavored potential. In any case, the bakery is without a doubt the place’s strongest suit, serving a variety of delights where excessive sweetness is a good thing, like the tiramisu cake (B105) and Thai tea crepe cake (B105). If you’re stuck in this rather limited neighborhood for dining then Krua Dok Mai Kao isn’t a bad option, though limited parking and slightly slow service when they’re busy don’t exactly help. Just be prepared for a sugar rush whatever you decide to order. Corkage B300 (wine only). - See more at: http://bk.asia-city.com/restaurants/bangkok-restaurant-reviews/krua-dok-mai-kao#sthash.mwMtxT3B.dpuf",
        type: "text",
        api: "analyze",
        version: "1.0.0",
        "resolvedPageUrl": []
    },
    language: "th",
    result: {
        keywords: [
            "spicy",
            "dok",
            "kao",
            "krua",
            "mai",
            "bakery",
            "cake",
            "like",
            "limited",
            "neighborhood",
            "restaurants"
        ],
        contents: "Krua Dok Mai Kao has regularly been packed out since it opened back in 2004, the brainchild of a savvy owner who saw the shortage of proper standalone restaurants in the Pathumwan neighborhood. Every day, office workers and families gather at the bright and airy two-story establishment, where bare concrete pillars stretch to the high ceilings amid a homey sprawl of marble tables, wooden seats and old-style armchairs. The menu has long been renowned for its international fare and bakery goods, which we feel masks the fact that the Thai offerings here lack authentic flavors. While popular dishes like the ham and cheese spring rolls (B105), baked baby clams with butter and garlic sauce served with French bread (B145) and spicy fried crispy cat fish with salted egg (B135) are all solid enough, others seem to be overloaded with sugar. The tom yam talay haeng (seafood with spicy sauce, B155) misses the point of the traditional recipe altogether, with the sweet notes totally overpowering the sour and spicy. It’s a similar story with the yam hed khem thong (spicy golden mushroom and shrimp salad, B95), which looks impressive but is all too saccharine and completely lacking in any tart lime, and the tom yum moo toon (spicy pork stew with herbs, B135/155), which is more a sweet soup than a spicy stew. That said, the kitchen is pretty quick and uses fresh ingredients, even if these aren’t always utilized to their full-flavored potential. In any case, the bakery is without a doubt the place’s strongest suit, serving a variety of delights where excessive sweetness is a good thing, like the tiramisu cake (B105) and Thai tea crepe cake (B105). If you’re stuck in this rather limited neighborhood for dining then Krua Dok Mai Kao isn’t a bad option, though limited parking and slightly slow service when they’re busy don’t exactly help. Just be prepared for a sugar rush whatever you decide to order. Corkage B300 (wine only). - See more at: http://bk.asia-city.com/restaurants/bangkok-restaurant-reviews/krua-dok-mai-kao#sthash.mwMtxT3B.dpuf"
    },
    category: [
        {
            name: "Restaurant & Delivery",
            score: "0.999999996133",
            confidence: "Yes"
        },
        {
            name: "Airline",
            score: "7.03625383687e-08",
            confidence: "No"
        },
        {
            name: "Accommodation",
            score: "4.70630024013e-11",
            confidence: "No"
        },
        {
            name: "Tourism",
            score: "1.76289553762e-39",
            confidence: "No"
        }
    ]
};

// END MOCK

function showResult(result){
    setTimeout(function(){
        $('.loading').addClass('hide')
        $('.result').removeClass('hide')
        if (!library)
            var library = {};

        // data = data.replace('\"\"', '\"');
        // var result = JSON.parse(data).data
        // result = result;
        // console.log(result);

        library.json = {
            replacer: function(match, pIndent, pKey, pVal, pEnd) {
                var key = '<span class=json-key>';
                var val = '<span class=json-value>';
                var str = '<span class=json-string>';
                var r = pIndent || '';
                if (pKey)
                    r = r + key + pKey.replace(/[": ]/g, '') + '</span>: ';
                if (pVal)
                    r = r + (pVal[0] == '"' ? str : val) + pVal + '</span>';
                return r + (pEnd || '');
            },
            prettyPrint: function(obj) {
                var jsonLine = /^( *)("[\w]+": )?("[^"]*"|[\w.+-]*)?([,[{])?$/mg;
                return JSON.stringify(obj, null, 3)
                    .replace(/&/g, '&amp;').replace(/\\"/g, '&quot;')
                    .replace(/</g, '&lt;').replace(/>/g, '&gt;')
                    .replace(jsonLine, library.json.replacer);
            }
        };
        $('.json').html(library.json.prettyPrint(result));
        $('#table-result').html(`<thead>
                                                <tr>
                                                    <th style="border-radius: 7px 0 0 0;">#</th>
                                                    <th>Name</th>
                                                    <th>Score</th>
                                                    <th style="border-radius: 0 7px 0 0;">Confident ?</th>
                                                </tr>
                                                </thead>
                                                <tbody>
                                                    <tr></tr>
                                                </tbody>`)
        var hasCat = false;
        result.category.forEach(function (val, index, arr) {
            if(parseFloat(val.score)>0.1){
                $('#table-result tr:last').after(`<tr>
                                                        <th scope="row">`+(index+1)+`</th>
                                                        <td>`+val.name+`</td>
                                                        <td>`+val.score+`</td>
                                                        <td>`+val.confidence+`</td>
                                                    </tr>`);
                hasCat = true
            }
        })
        if(!hasCat){
            result.category.forEach(function (val, index, arr) {
                if(parseFloat(val.score)>0.00001){
                    $('#table-result tr:last').after(`<tr>
                                                        <th scope="row">`+(index+1)+`</th>
                                                        <td>`+val.name+`</td>
                                                        <td>`+val.score+`</td>
                                                        <td>`+val.confidence+`</td>
                                                    </tr>`);
                    hasCat = true
                }
            })
        }
        if(!hasCat){
            $('#table-result tr:last').after(`<tr>
                                                <th scope="row">1</th>
                                                <td>Unknown</td>
                                                <td>-</td>
                                                <td>-</td>
                                            </tr>`);
        }

        $('.important-words').html(`<span class="btn btn-inverse btn-sm btn-tag hide"></span></span>`);
        result.result.keywords.forEach(function (val, index, arr) {
            $('.important-words span:last').after(`<span class="btn btn-inverse btn-sm btn-tag">`+val+`</span></span>`);
        });
    },1500);

}

var input;
$(document).on('click','.btn-analyze1',function(){
    input = $('#input-demo-first').val().trim()
})
$(document).on('click','.btn-analyze2',function(){
    input = $('#input-demo-result').val().trim()
})

$(document).on('click','.btn-analyze',function(){
    if(input.trim().length == 0){
        $('#input-demo-first').val('02-690-1888');
        $('#input-demo-result').val('02-690-1888');
        $('.input-tag').text("PHONE")
        input = '02-690-1888'
    }
    $('.loading').removeClass('hide')
    $('.result').addClass('hide')
    setTimeout(function(){
        var input_type = $('#input-tag2').text()
        if(input.trim() == "02-690-1888"){
            showResult(result_phone)
        } else if(input.trim() == "https://www.wongnai.com/restaurants/1667sR-%E0%B8%81%E0%B9%8B%E0%B8%A7%E0%B8%A2%E0%B8%88%E0%B8%B1%E0%B9%8A%E0%B8%9A%E0%B8%99%E0%B8%B2%E0%B8%A2%E0%B9%80%E0%B8%AD%E0%B9%87%E0%B8%81"){
            showResult(result_url)
        } else if(input.trim() == "ซอร์เทรล สาทร Bangkok"){
            showResult(result_keyword)
        } else if(input.trim() == "Krua Dok Mai Kao has regularly been packed out since it opened back in 2004, the brainchild of a savvy owner who saw the shortage of proper standalone restaurants in the Pathumwan neighborhood. Every day, office workers and families gather at the bright and airy two-story establishment, where bare concrete pillars stretch to the high ceilings amid a homey sprawl of marble tables, wooden seats and old-style armchairs. The menu has long been renowned for its international fare and bakery goods, which we feel masks the fact that the Thai offerings here lack authentic flavors. While popular dishes like the ham and cheese spring rolls (B105), baked baby clams with butter and garlic sauce served with French bread (B145) and spicy fried crispy cat fish with salted egg (B135) are all solid enough, others seem to be overloaded with sugar. The tom yam talay haeng (seafood with spicy sauce, B155) misses the point of the traditional recipe altogether, with the sweet notes totally overpowering the sour and spicy. It’s a similar story with the yam hed khem thong (spicy golden mushroom and shrimp salad, B95), which looks impressive but is all too saccharine and completely lacking in any tart lime, and the tom yum moo toon (spicy pork stew with herbs, B135/155), which is more a sweet soup than a spicy stew. That said, the kitchen is pretty quick and uses fresh ingredients, even if these aren’t always utilized to their full-flavored potential. In any case, the bakery is without a doubt the place’s strongest suit, serving a variety of delights where excessive sweetness is a good thing, like the tiramisu cake (B105) and Thai tea crepe cake (B105). If you’re stuck in this rather limited neighborhood for dining then Krua Dok Mai Kao isn’t a bad option, though limited parking and slightly slow service when they’re busy don’t exactly help. Just be prepared for a sugar rush whatever you decide to order. Corkage B300 (wine only). - See more at: http://bk.asia-city.com/restaurants/bangkok-restaurant-reviews/krua-dok-mai-kao#sthash.mwMtxT3B.dpuf"){
            showResult(result_text)
        } else{
            $.post("/api/analyze",
                {
                    input_value : input,
                    input_type :  input_type
                }
                , function(data, status){
                    $('.loading').addClass('hide')
                    $('.result').removeClass('hide')
                    console.log("Data: " + data + "\nStatus: " + status);

                    if (!library)
                        var library = {};

                    data = data.replace('\"\"', '\"');
                    var result = JSON.parse(data).data

                    library.json = {
                        replacer: function(match, pIndent, pKey, pVal, pEnd) {
                            var key = '<span class=json-key>';
                            var val = '<span class=json-value>';
                            var str = '<span class=json-string>';
                            var r = pIndent || '';
                            if (pKey)
                                r = r + key + pKey.replace(/[": ]/g, '') + '</span>: ';
                            if (pVal)
                                r = r + (pVal[0] == '"' ? str : val) + pVal + '</span>';
                            return r + (pEnd || '');
                        },
                        prettyPrint: function(obj) {
                            var jsonLine = /^( *)("[\w]+": )?("[^"]*"|[\w.+-]*)?([,[{])?$/mg;
                            return JSON.stringify(obj, null, 3)
                                .replace(/&/g, '&amp;').replace(/\\"/g, '&quot;')
                                .replace(/</g, '&lt;').replace(/>/g, '&gt;')
                                .replace(jsonLine, library.json.replacer);
                        }
                    };
                    $('.json').html(library.json.prettyPrint(result));
                    $('#table-result').html(`<thead>
                                                <tr>
                                                    <th style="border-radius: 7px 0 0 0;">#</th>
                                                    <th>Name</th>
                                                    <th>Score</th>
                                                    <th style="border-radius: 0 7px 0 0;">Confident ?</th>
                                                </tr>
                                                </thead>
                                                <tbody>
                                                    <tr></tr>
                                                </tbody>`)
                    var hasCat = false;
                    result.category.forEach(function (val, index, arr) {
                        if(parseFloat(val.score)>0.1){
                            $('#table-result tr:last').after(`<tr>
                                                        <th scope="row">`+(index+1)+`</th>
                                                        <td>`+val.name+`</td>
                                                        <td>`+val.score+`</td>
                                                        <td>`+val.confidence+`</td>
                                                    </tr>`);
                            hasCat = true
                        }
                    })
                    if(!hasCat){
                        result.category.forEach(function (val, index, arr) {
                            if(parseFloat(val.score)>0.00001){
                                $('#table-result tr:last').after(`<tr>
                                                        <th scope="row">`+(index+1)+`</th>
                                                        <td>`+val.name+`</td>
                                                        <td>`+val.score+`</td>
                                                        <td>`+val.confidence+`</td>
                                                    </tr>`);
                                hasCat = true
                            }
                        })
                    }
                    if(!hasCat){
                        $('#table-result tr:last').after(`<tr>
                                                <th scope="row">1</th>
                                                <td>Unknown</td>
                                                <td>-</td>
                                                <td>-</td>
                                            </tr>`);
                    }

                    $('.important-words').html(`<span class="btn btn-inverse btn-sm btn-tag hide"></span></span>`);
                    result.result.keywords.forEach(function (val, index, arr) {
                        $('.important-words span:last').after(`<span class="btn btn-inverse btn-sm btn-tag">`+val+`</span></span>`);
                    });

                });
        }


    }, 500);


});