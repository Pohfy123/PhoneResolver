


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

    $('.json').html(library.json.prettyPrint({ "request": { "input": "http://wongnai.com", "type": "url", "api": "analyze", "version": "1.0.0", "resolvedPageUrl": "https://www.wongnai.com/" }, "language": "th", "result": { "keywords": [ "ร้านอาหาร", "ร้านซูชิ", "กรุงเทพมหานคร"], "contents": "ร้านอาหารแนะนำ ดูทั้งหมด  Recommended by JOHNNIE WALKER"},"category": {"d1": {"confidence": 0.49049994349479675,"value": "restaurant"},"d2": { "confidence": 0.31968462467193604, "value": "seafood restaurant"}}}));
});
$(document).on('click', '#btn-result', function() {
    $('#btn-json').removeClass('active')
    $('#btn-result').addClass('active')
    $('.table-result').removeClass('hide')
    $('.json').addClass('hide')
});