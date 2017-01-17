// auto resize textareaa
var observe;
if (window.attachEvent) {
    observe = function (element, event, handler) {
        element.attachEvent('on'+event, handler);
    };
}
else {
    observe = function (element, event, handler) {
        element.addEventListener(event, handler, false);
    };
}
$(document).ready(function(){
    var text = document.getElementById('text');
    function resize () {
        text.style.height = 'auto';
        text.style.height = text.scrollHeight+4+'px';
    }
    /* 0-timeout to get the already changed text */
    function delayedResize () {
        window.setTimeout(resize, 0);
    }
    observe(text, 'change',  resize);
    observe(text, 'cut',     delayedResize);
    observe(text, 'paste',   delayedResize);
    observe(text, 'drop',    delayedResize);
    observe(text, 'keydown', delayedResize);

    text.focus();
    text.select();
    resize();
});
// end auto resize textareaa

$(document).on('click', '#btn-json', function() {
    $('#btn-json').addClass('active')
    $('#btn-result').removeClass('active')
    $('.table-result').addClass('hide')
    $('.json').removeClass('hide')

    var jsonStr = $(".json").text();
    var jsonObj = JSON.parse(jsonStr);
    var jsonPretty = JSON.stringify(jsonObj, null, '\t');
    $(".json").text(jsonPretty);

});
$(document).on('click', '#btn-result', function() {
    $('#btn-json').removeClass('active')
    $('#btn-result').addClass('active')
    $('.table-result').removeClass('hide')
    $('.json').addClass('hide')
});
