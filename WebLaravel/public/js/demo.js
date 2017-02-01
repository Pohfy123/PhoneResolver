; (function () {

    'use strict';

    $(document).on('click', '.btn-analyze1', function () {
        $('#demo-page-input').addClass('hide')
        $('#demo-page-result').removeClass('hide')
        $('#text2').val($('#text1').val())
        $(document).ready(function () {
            // auto resize textareaa for result page
            var observe;
            if (window.attachEvent) {
                observe = function (element, event, handler) {
                    element.attachEvent('on' + event, handler);
                };
            }
            else {
                observe = function (element, event, handler) {
                    element.addEventListener(event, handler, false);
                };
            }
            $(document).ready(function () {
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

        })

    });

    // auto resize textareaa
    $(document).ready(function () {
        var observe;
        if (window.attachEvent) {
            observe = function (element, event, handler) {
                element.attachEvent('on' + event, handler);
            };
        }
        else {
            observe = function (element, event, handler) {
                element.addEventListener(event, handler, false);
            };
        }
        $(document).ready(function () {
            var text = document.getElementById('text1');
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
    })
    // end auto resize textareaa

    $(document).on('click','.btn-analyze',function(){
        $('.loading').removeClass('hide');
        setTimeout(function(){
            $('.loading').addClass('hide');
            $('.result-visual').removeClass('hide')
        }, 3000);
    })


} ());