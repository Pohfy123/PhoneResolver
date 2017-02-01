$(document).on('click', '#btn-json', function() {
    $('#btn-json').addClass('active')
    $('#btn-result').removeClass('active')
    $('.table-result').addClass('hide')
    $('.json').removeClass('hide')

    // var jsonStr = $(".json").text();
    // var jsonObj = JSON.parse(jsonStr);
    // var jsonPretty = JSON.stringify(jsonObj, null, '\t');
    // $(".json").text(jsonPretty);

    if (!library)
        var library = {};

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

    $('.json').html(library.json.prettyPrint({ "request": { "input": "http://wongnai.com", "type": "url", "api": "analyze", "version": "1.0.0", "resolvedPageUrl": "https://www.wongnai.com/" }, "language": "th", "result": { "keywords": ["ร้านอาหาร", "ร้านซูชิ", "กรุงเทพมหานคร"], "contents": "ร้านอาหารแนะนำ ดูทั้งหมด  Recommended by JOHNNIE WALKER" }, "category": { "d1": { "confidence": 0.49049994349479675, "value": "restaurant" }, "d2": { "confidence": 0.31968462467193604, "value": "seafood restaurant" } } }));
});
$(document).on('click', '#btn-result', function() {
    $('#btn-json').removeClass('active')
    $('#btn-result').addClass('active')
    $('.table-result').removeClass('hide')
    $('.json').addClass('hide')
});

$(document).on('click', '#try-url', function() {
    $('#text2').val('https://www.wongnai.com/restaurants/158354cD-plaavy-dessert-cafe')
    resizeTextarea()
})

$(document).on('click', '#try-keyword', function() {
    $('#text2').val('Plavvy')
    resizeTextarea()
})

$(document).on('click', '#try-text', function() {
    $('#text2').val(`ร้าน Plaavy สาขานี้จะมีอาหารให้สั่งด้วย มีเมนูอยู่ไม่มากนักแต่ก็เหมาะสำหรับทานอิ่มได้แบบสบายๆ ถือว่าสะดวกสำหรับคนที่ต้องการมาทานของหวานและของคาวไปพร้อมๆกัน

วันนี้ได้ลองสั่งสปาเก็ตตี้ขี้เมากุ้ง ถ้าคนทานเผ็ดน้อยก็บอกพนักงานไปได้นะครับ เส้นเหนียวนุ่มกำลังพอดี รสชาติเข้มข้นกลมกล่อมดี เนื้อกุ้งก็สด แต่รสชาติยังไม่ค่อยเข้าไปในตัวกุ้งเท่าไหร่นัก(จืดไปหน่อย) ราคา 120 บาท โดยรวมถือว่าอร่อยใช้ได้เลย

มาในส่วนของเครื่องดื่มกันบ้าง ลองสั่งกาแฟเย็น Espresso ราคาแก้วละ 85 บาท รสชาติอาจจะดูจืดๆไปซักนิด แต่ตัวคุณภาพเม็ดกาแฟถือว่าใช่ได้เลย ถือว่าผ่าน

ส่วนขนมเค้กนั้น ส่วนตัวรู้สึกเฉยๆ อาจจะเป็นเพราะไม่ค่อยชอบทานอยู่แล้วด้วย ไม่ขอคอมเม้นท์

ส่วนการตกแต่งร้านนั้นต้องยอมรับว่าตกแต่งได้อย่างดีเยี่ยม มีมุมให้นั่งหลายมุม และใช้วัสดุที่ดูดีมีราคาจริงๆ เรียกได้ว่ามานั่งเล่น พูดคุยกับเพื่อนฝูง หรือจะพาคนรักมานั่งสวีท ก็เหมาะยิ่งนัก เงียบและส่วนตัวดี อ่านต่อได้ที่ https://www.wongnai.com/restaurants/158354cD-plaavy-dessert-cafe?ref=ct`)
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
        var text = document.getElementById('text2');

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