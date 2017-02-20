; (function () {

    'use strict';

    $(document).on('click', '.btn-analyze1', function () {
        redirectToResult();
    });

    $(document).ready(function(){
        resizeTextareaFirst();
    })

    // auto resize textareaa
    function resizeTextareaFirst() {
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
            var text = document.getElementById('input-demo-first');
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
    }
    // end auto resize textareaa

    // $(document).on('click','#input-demo-first',function(){
    //     $('.loading').removeClass('hide');
    //     setTimeout(function(){
    //         $('.loading').addClass('hide');
    //         $('.result-visual').removeClass('hide')
    //     }, 3000);
    // });


    $(document).on('click', '#btn-result', function() {
        $('#btn-json').removeClass('active')
        $('#btn-result').addClass('active')
        $('.result-visual').removeClass('hide')
        $('.result-json').addClass('hide')
    });

    $(document).on('click', '#try-url-first', function() {
        $('#input-demo-first').val('https://www.wongnai.com/restaurants/1667sR-%E0%B8%81%E0%B9%8B%E0%B8%A7%E0%B8%A2%E0%B8%88%E0%B8%B1%E0%B9%8A%E0%B8%9A%E0%B8%99%E0%B8%B2%E0%B8%A2%E0%B9%80%E0%B8%AD%E0%B9%87%E0%B8%81')
        $('.input-tag').text("URL")
        resizeTextareaFirst();
    })

    $(document).on('click', '#try-keyword-first', function() {
        $('#input-demo-first').val('ซอร์เทรล สาทร Bangkok')
        $('.input-tag').text("KEYWORD")
        resizeTextareaFirst();
    })

    $(document).on('click', '#try-phone-first', function() {
        $('#input-demo-first').val('02-690-1888')
        $('.input-tag').text("PHONE-NO")
        resizeTextareaFirst();
    })

    $(document).on('click', '#try-text-first', function() {
        $('#input-demo-first').val(`Krua Dok Mai Kao has regularly been packed out since it opened back in 2004, the brainchild of a savvy owner who saw the shortage of proper standalone restaurants in the Pathumwan neighborhood. Every day, office workers and families gather at the bright and airy two-story establishment, where bare concrete pillars stretch to the high ceilings amid a homey sprawl of marble tables, wooden seats and old-style armchairs. The menu has long been renowned for its international fare and bakery goods, which we feel masks the fact that the Thai offerings here lack authentic flavors. While popular dishes like the ham and cheese spring rolls (B105), baked baby clams with butter and garlic sauce served with French bread (B145) and spicy fried crispy cat fish with salted egg (B135) are all solid enough, others seem to be overloaded with sugar. The tom yam talay haeng (seafood with spicy sauce, B155) misses the point of the traditional recipe altogether, with the sweet notes totally overpowering the sour and spicy. It’s a similar story with the yam hed khem thong (spicy golden mushroom and shrimp salad, B95), which looks impressive but is all too saccharine and completely lacking in any tart lime, and the tom yum moo toon (spicy pork stew with herbs, B135/155), which is more a sweet soup than a spicy stew. That said, the kitchen is pretty quick and uses fresh ingredients, even if these aren’t always utilized to their full-flavored potential. In any case, the bakery is without a doubt the place’s strongest suit, serving a variety of delights where excessive sweetness is a good thing, like the tiramisu cake (B105) and Thai tea crepe cake (B105). If you’re stuck in this rather limited neighborhood for dining then Krua Dok Mai Kao isn’t a bad option, though limited parking and slightly slow service when they’re busy don’t exactly help. Just be prepared for a sugar rush whatever you decide to order. Corkage B300 (wine only). - See more at: http://bk.asia-city.com/restaurants/bangkok-restaurant-reviews/krua-dok-mai-kao#sthash.mwMtxT3B.dpuf`)
        $('.input-tag').text("TEXT")
        resizeTextareaFirst();
    })

    function redirectToResult(){
        $('#demo-page-input').addClass('hide')
        $('#demo-page-result').removeClass('hide')
        $('#input-demo-result').val($('#input-demo-first').val())
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

        })
    }
} ());