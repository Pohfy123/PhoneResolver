@extends('masterpage')

@section('title')Demo
@endsection

@section('css-js')
    <link href="css/demo.css" rel="stylesheet">
    <link href="css/result.css" rel="stylesheet">
    <script src="js/demo.js"></script>
    <script src="js/result.js"></script>

    <!--Loading-->
    <link href='http://fonts.googleapis.com/css?family=Lato:900,400' rel='stylesheet' type='text/css'>
@endsection

@section('content')

    <div id="fh5co-main">
        <!--DEMO INPUT PAGE-->
        <div id="demo-page-input" class="content content-demo-input">
            <section id="fh5co-counter" class="fh5co-bg-section" style="background-image: url(outline/images/bg_2.jpg); background-attachment: fixed;">
                <div class="fh5co-overlay"></div>
                <div class="container">
                    <div class="row">
                        <div class="col-md-12">
                            <div class="fh5co-hero-wrap">
                                <div class="fh5co-hero-intro text-center">
                                    <div class="col-md-12 text-center">
                                        <span class="demo-intro">AUTO TEXT CLASSIFICATION</span>
                                        <span class="demo-intro-label">LET US DO IT FOR YOU</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            <section id="demo-2" class="fh5co-bg-section">
                <div class="searchForm animated">
                    <h3><b>Input</b></h3>
                    <div class="form-group">
                        <textarea class="input-textarea form-control" rows="1" id="input-demo-first" placeholder="Enter url, keyword, text, phone no ..."></textarea>
                    </div>
                    <div class="center">
                        <button type="button" class="btn btn-primary btn-analyze btn-analyze1">Analyze</button>
                    </div>
                </div>
                <div id="fh5co-products" data-section="products">
                    <div class="container">
                        <div class="row">
                            <div class="col-md-8 col-md-offset-2 fh5co-section-heading text-center">
                                {{--<h2 class="fh5co-lead animate-single product-animate-1">Click these blocks to try example input.</h2>--}}
                                <p class="fh5co-sub text-black">Click these blocks to try example input.</p>
                            </div>

                            <div class="col-md-3 col-sm-6 col-xs-6 col-xxs-12">
                                <span href="outline/images/product_1.jpg" class="fh5co-figure">
                                    <figure>
                                        <img src="outline/images/product_1.jpg" alt="Free HTML5 Responsive Template" class="img-responsive example-img">
                                    </figure>
                                    <h3 class="fh5co-figure-lead">URL</h3>
                                    <p class="fh5co-figure-text">รีวิวร้านก๋วยจั๊บนายเอ็ก</p>
                                    <div class="center">
                                        <button id="try-url-first" type="button" class="btn btn-primary btn-try">Try!</button>
                                    </div>
                                </span>
                            </div>
                            <div class="col-md-3 col-sm-6 col-xs-6 col-xxs-12">
                                <span href="outline/images/product_2.jpg" class="fh5co-figure">
                                    <figure>
                                        <img src="outline/images/product_2.jpg" alt="Free HTML5 Responsive Template" class="img-responsive example-img">
                                    </figure>
                                    <h3 class="fh5co-figure-lead">PHONE-NO</h3>
                                    <p class="fh5co-figure-text">Courtyard by Mariott Bangkok</p>
                                    <div class="center">
                                        <button id="try-phone-first" type="button" class="btn btn-primary btn-try">Try!</button>
                                    </div>
                                </span>
                            </div>
                            <div class="clearfix visible-sm-block"></div>
                            <div class="col-md-3 col-sm-6 col-xs-6 col-xxs-12">
                                <span href="outline/images/product_3.jpg" class="fh5co-figure">
                                    <figure>
                                        <img src="outline/images/product_3.jpg" alt="Free HTML5 Responsive Template" class="img-responsive example-img">
                                    </figure>
                                    <h3 class="fh5co-figure-lead">LONG TEXT</h3>
                                    <p class="fh5co-figure-text">Krua Dok Mai Kao has regularly been packed out since ...</p>
                                    <div class="center">
                                        <button id="try-text-first" type="button" class="btn btn-primary btn-try">Try!</button>
                                    </div>
                                </span>
                            </div>
                            <div class="col-md-3 col-sm-6 col-xs-6 col-xxs-12">
                                <span href="outline/images/product_4.jpg" class="fh5co-figure">
                                    <figure>
                                        <img src="outline/images/product_4.jpg" alt="Free HTML5 Responsive Template" class="img-responsive example-img">
                                    </figure>
                                    <h3 class="fh5co-figure-lead">Keyword</h3>
                                    <p class="fh5co-figure-text">"ซอร์เทรล สาทร", "Bangkok"</p>
                                    <div class="center">
                                        <button id="try-keyword-first" type="button" class="btn btn-primary btn-try">Try!</button>
                                    </div>
                                </span>
                            </div>

                            <div class="clearfix visible-sm-block"></div>

                            <div class="fh5co-spacer fh5co-spacer-sm"></div>

                        </div>
                    </div>
                </div>
            </section>
        </div>

        <!--RESULT PAGE-->
        <header id="fh5co-hero" role="banner" style="background: url(outline/images/bg_2.jpg) top left; background-size: cover;" >
            <div class="fh5co-overlay"></div>
                <div class="fh5co-intro">
                    <div id="demo-page-result" class="hide content">
                            <div class="container">
                                <div class="row">
                                    <div class="col-md-12">
                                        <div class="fh5co-hero-wrap">
                                            <div class="fh5co-hero-intro text-center">
                                                <div class="col-md-12 text-center">
                                                    <span class="demo-intro">AUTO TEXT CLASSIFICATION</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="container container-all row">
                                <div class="col-md-4 container-left">
                                    <h3><b>Input</b> <span class="tag label label-warning input-tag">URL</span></h3>
                                    <textarea class="input-textarea form-control" rows="1" id="input-demo-result" placeholder="Enter url, keyword, text, phone no ..."></textarea>
                                    <br>
                                    <button type="button" class="btn btn-primary btn-sm btn-analyze btn-analyze2">Analyze</button>
                                    <br>
                                    <br>
                                    <div class="try-div">
                                        <h6><b>Try these examples :</b></h6>
                                        <button type="button" class="btn btn-primary btn-xs"><span class="try-it" id="try-url"> <span class="icon-plus"></span> URL: รีวิวร้านก๋วยจั๊บนายเอ็ก</span></button>
                                        <button type="button" class="btn btn-primary btn-xs"><span class="try-it" id="try-phone"> <span class="icon-plus"></span> PHONE-NO: Courtyard by Mariott Bangkok</span></button>
                                        <button type="button" class="btn btn-primary btn-xs"><span class="try-it" id="try-text"> <span class="icon-plus"></span> LONG-TEXT: Krua Dok Mai Kao has ...</span></button>
                                        <button type="button" class="btn btn-primary btn-xs"><span class="try-it" id="try-keyword"> <span class="icon-plus"></span> KEYWORD: "ซอร์เทรล สาทร", "Bangkok"</span></button>
                                    </div>


                                </div>
                                <div class="col-md-8 container-right">
                                    <div class="result-menu">
                                        <span id="btn-result" class="result-nav-btn active"><span class="fui-eye"></span> Result</span>
                                        <span id="btn-json" class="result-nav-btn"><span class="fui-arrow-left"></span>/<span class="fui-arrow-right"></span>JSON</span>
                                    </div>
                                    <!--<div class="result-menu">
                                        <div class="btn-group">
                                            <button type="button" class="btn btn-primary btn-embossed btn-sm active" id="btn-result"><span class="fui-eye"></span> Result</button>
                                            <button type="button" class="btn btn-primary btn-embossed btn-sm" id="btn-json"><span class="fui-arrow-left"></span>/<span class="fui-arrow-right"></span>JSON</button>
                                        </div>
                                    </div>-->
                                    <div class="loading hide">
                                        <div class="sk-circle">
                                            <div class="sk-circle1 sk-child"></div>
                                            <div class="sk-circle2 sk-child"></div>
                                            <div class="sk-circle3 sk-child"></div>
                                            <div class="sk-circle4 sk-child"></div>
                                            <div class="sk-circle5 sk-child"></div>
                                            <div class="sk-circle6 sk-child"></div>
                                            <div class="sk-circle7 sk-child"></div>
                                            <div class="sk-circle8 sk-child"></div>
                                            <div class="sk-circle9 sk-child"></div>
                                            <div class="sk-circle10 sk-child"></div>
                                            <div class="sk-circle11 sk-child"></div>
                                            <div class="sk-circle12 sk-child"></div>
                                        </div>
                                        <p style="color: black;text-align: center">processing</p>
                                    </div>
                                    <section class="result hide">
                                        <div class="result-visual">
                                            <h1 class="lead">Categories</h1>

                                            <table id="table-result" class="table table-hover table-striped table-result">
                                                <thead>
                                                <tr>
                                                    <th style="border-radius: 7px 0 0 0;">#</th>
                                                    <th>Name</th>
                                                    <th>Score</th>
                                                    <th style="border-radius: 0 7px 0 0;">Confident ?</th>
                                                </tr>
                                                </thead>
                                                <tbody>
                                                    <tr></tr>
                                                </tbody>
                                            </table>
                                            <br>
                                            <br>
                                            <h1 class="lead">Important words</h1>
                                            <div class="form-group">
                                                <span class="btn btn-inverse btn-sm btn-tag">ร้านอาหาร</span></span>
                                                <span class="btn btn-inverse btn-sm btn-tag">กรุงเทพฯ</span></span>
                                                <span class="btn btn-inverse btn-sm btn-tag">อร่อย</span></span>
                                                <span class="btn btn-inverse btn-sm btn-tag">บริการดี</span></span>
                                            </div>

                                        </div>
                                        <!--<pre><code id=account></code></pre>
                                        <pre><code id=planets></code></pre>-->
                                        <div class="result-json hide">
                                            <h1 class="lead">JSON from API</h1>
                                            <pre class="json">
                                        </pre>
                                        </div>
                                    </section>

                                </div>
                            </div>
                    </div>
                </div>
            </div>
        </header>
        <br>
        <br>
    </div>
@endsection

@section('css-js-after')

@endsection