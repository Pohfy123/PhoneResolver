/**
 * Created by andy hulstkamp
 */

var webpage = require("webpage"),
    fs = require("fs");

var debug = false,
    pageIndex = 0,
    allLinks = [],
    url = "https://www.google.com/?hl=en",
    searchTerm = "mongodb vs couchdb",
    maxSearchPages = 3;

var createPage = function () {

    var page = webpage.create();

    //set some headers to get the content we want
    page.customHeaders = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:22.0) Gecko/20130404 Firefox/22.0",
        "Accept-Language": "en"
    };

    //smaller size might get you the mobile versions of a site
    page.viewportSize = { width: 1280, height: 800 };

    //good to debug and abort request, we do not wish to invoke cause they slow things down (e.g. tons of plugins)
    page.onResourceRequested = function (requestData, networkRequest) {
        log(["onResourceRequested", JSON.stringify(networkRequest), JSON.stringify(requestData)]);
        //in case we do not want to invoke the request
        //networkRequest.abort();
    };

    //what dd we get
    page.onResourceReceived = function (response) {
        log(["onResourceReceived", JSON.stringify(response)]);
    };

    //what went wrong
    page.onResourceError = function (error) {
        log(["onResourceError", JSON.stringify(error)]);
    };

    page.onLoadStarted = function() {
        console.log("loading page...");
    };

    page.onLoadFinished = function(status) {
        var currentUrl = page.evaluate(function() {
            return window.location.href;
        });
        console.log("onLoadFinished", currentUrl, status);
    };

    return page;
}


var collectLinks = function () {
    var hrefs = page.evaluate(function () {
        var links = document.querySelectorAll("h3.r a");
        return Array.prototype.map.call(links, function (anchor) {
            return anchor.getAttribute("href");
        });
    });
    return hrefs;
}

var search = function (url) {

    page.open(url, function () {

        //give scripts and ajax call some time to execute and throttle execution to not appear as a robot
        //google might block us
        setTimeout(function () {

            //for debugging purposes, to see whats happening
            page.render("search.png");

            //any js can be injected on the page and used inside evaluate, inject jQuery for convenience, injected returns true if all went well
            var injected = page.injectJs('../../libs/jquery-2.0.3.min.js');
            if (!injected) {
                throw Error("jquery could not be injected");
            }

            //anything that is invoked on the page must be executed inside evaluate.
            //evaluate is sandboxed, only simple types are allowed as arguments and return types
            var f = page.evaluate(function (searchTerm) {
                $("input").val(searchTerm);
                $("form").submit();
            }, searchTerm);

            //give it some time to execute
            setTimeout(function () {
                //collect links and goto next page
                collectAndNext();
            }, 2000);

        }, 2000);
    });
};

/*
 * collect all links on the search page, and use paging to go to the next page
 */
var collectAndNext = function () {

    //for debugging purposes
    page.render("./snapshots/searchPage-" + pageIndex + ".png");

    //collect all links on the page
    var links = collectLinks();
    allLinks = allLinks.concat(links);

    //evaluate and invoke request for next page
    var next = page.evaluate(function () {
        //next button on google search page
        var btn = document.getElementById("pnnext");
        //invoke click event on the next button
        var ev = document.createEvent("MouseEvent");
        ev.initEvent("click", true, true);
        btn.dispatchEvent(ev);
    });

    //allow the next page to load
    setTimeout(function () {

        //goto next page and collect link or - if we reached max . process all collected links
        //and scrape he pages
        if (++pageIndex >= maxSearchPages) {
            scrapeAll(allLinks);
        } else {
            collectAndNext();
        }
    }, 2000);
}

/**
 * scrape all pages
 * @param links
 */
var scrapeAll = function (links) {
    var index = 0;

    //scrape a page at url
    var scrapePage = function (index, url) {

        log(["scrape page ", index, url]);

        //open the page
        page.open(url, function (status) {

            log(["page loaded", status]);

            //write the content of the page as plainText to disc
            //more advanced processing could be done in page.evaluate
            fs.write("./scraped/page" + index + ".txt", page.plainText, "w");

            page.render("./snapshots/page" + index + ".png");

            //scrape next link or abort
            index++;
            var u = links[index];
            if (u) {

                //give it some time to process
                setTimeout(function () {
                    scrapePage(index, u)
                }, 7000);
            }
            else {
                phantom.exit();
            }
        })
    };
    scrapePage(index, links[index]);
}

var log = function (args) {
    if (debug) {
        console.log(args);
    }
}

var page = createPage();

// search(url);