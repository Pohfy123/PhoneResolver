$(document).on('click', '#btn-json', function() {
    $('#btn-json').addClass('active')
    $('#btn-result').removeClass('active')
    $('.result-visual').addClass('hide')
    $('.result-json').removeClass('hide')

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

    $('.json').html(library.json.prettyPrint({ "request": { "input": "https://www.wongnai.com/restaurants/1667sR-%E0%B8%81%E0%B9%8B%E0%B8 ...", "type": "url", "api": "analyze", "version": "1.0.0", "resolvedPageUrl": "https://www.wongnai.com/restaurants/1667sR-%E0%B8%81%E0%B9 ..." }, "language": "th", "result": { "keywords": ["ร้านอาหาร", "กรุงเทพฯ", "อร่อย", "บริการดี"], "contents": "ร้านอาหารแนะนำ ดูทั้งหมด  ...  " }, "category": [ { "name": "Food","score": 0.5342132,"confidence":"yes"  }, { "name": "Restaurant","score": 0.2323132,"confidence":"yes" } ] }));
});
$(document).on('click', '#btn-result', function() {
    $('#btn-json').removeClass('active')
    $('#btn-result').addClass('active')
    $('.result-visual').removeClass('hide')
    $('.result-json').addClass('hide')
});

$(document).on('click', '#try-url', function() {
    $('#input-demo-result').val('https://www.wongnai.com/restaurants/1667sR-%E0%B8%81%E0%B9%8B%E0%B8%A7%E0%B8%A2%E0%B8%88%E0%B8%B1%E0%B9%8A%E0%B8%9A%E0%B8%99%E0%B8%B2%E0%B8%A2%E0%B9%80%E0%B8%AD%E0%B9%87%E0%B8%81')
    resizeTextarea()
})

$(document).on('click', '#try-keyword', function() {
    $('#input-demo-result').val('ซอร์เทรล สาทร Bangkok')
    resizeTextarea()
})

$(document).on('click', '#try-phone', function() {
    $('#input-demo-result').val('02-690-1888')
    resizeTextarea()
})

$(document).on('click', '#try-text', function() {
    $('#input-demo-result').val(`Krua Dok Mai Kao has regularly been packed out since it opened back in 2004, the brainchild of a savvy owner who saw the shortage of proper standalone restaurants in the Pathumwan neighborhood. Every day, office workers and families gather at the bright and airy two-story establishment, where bare concrete pillars stretch to the high ceilings amid a homey sprawl of marble tables, wooden seats and old-style armchairs. The menu has long been renowned for its international fare and bakery goods, which we feel masks the fact that the Thai offerings here lack authentic flavors. While popular dishes like the ham and cheese spring rolls (B105), baked baby clams with butter and garlic sauce served with French bread (B145) and spicy fried crispy cat fish with salted egg (B135) are all solid enough, others seem to be overloaded with sugar. The tom yam talay haeng (seafood with spicy sauce, B155) misses the point of the traditional recipe altogether, with the sweet notes totally overpowering the sour and spicy. It’s a similar story with the yam hed khem thong (spicy golden mushroom and shrimp salad, B95), which looks impressive but is all too saccharine and completely lacking in any tart lime, and the tom yum moo toon (spicy pork stew with herbs, B135/155), which is more a sweet soup than a spicy stew. That said, the kitchen is pretty quick and uses fresh ingredients, even if these aren’t always utilized to their full-flavored potential. In any case, the bakery is without a doubt the place’s strongest suit, serving a variety of delights where excessive sweetness is a good thing, like the tiramisu cake (B105) and Thai tea crepe cake (B105). If you’re stuck in this rather limited neighborhood for dining then Krua Dok Mai Kao isn’t a bad option, though limited parking and slightly slow service when they’re busy don’t exactly help. Just be prepared for a sugar rush whatever you decide to order. Corkage B300 (wine only). - See more at: http://bk.asia-city.com/restaurants/bangkok-restaurant-reviews/krua-dok-mai-kao#sthash.mwMtxT3B.dpuf`);
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