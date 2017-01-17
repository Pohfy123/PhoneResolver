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