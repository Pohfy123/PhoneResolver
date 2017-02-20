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


var input;
$(document).on('click','.btn-analyze1',function(){
    input = $('#input-demo-first').val().trim()
})
$(document).on('click','.btn-analyze2',function(){
    input = $('#input-demo-result').val().trim()
})

$(document).on('click','.btn-analyze',function(){
    setTimeout(function(){}, 1000);
    $('.loading').removeClass('hide')
    $('.result').addClass('hide')
    var input_type = $('#input-tag2').text()
    $.post("/api/analyze",
        {
            input_value : input,
            input_type :  input_type
        }
        , function(data, status){
            $('.loading').addClass('hide')
            $('.result').removeClass('hide')
            if (!library)
                var library = {};

            console.log("Data: " + data + "\nStatus: " + status);
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
            result.category.forEach(function (val, index, arr) {
                if(parseFloat(val.score)>0.2){
                    $('#table-result tr:last').after(`<tr>
                                                        <th scope="row">`+(index+1)+`</th>
                                                        <td>`+val.name+`</td>
                                                        <td>`+val.score+`</td>
                                                        <td>`+val.confidence+`</td>
                                                    </tr>`);
                }
            })
    });
});