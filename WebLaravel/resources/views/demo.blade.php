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
    <div id="demo-page-input" class="content content-demo-input">
        <section id="fh5co-counter" class="fh5co-bg-section" style="background-image: url(outline/images/bg_1.jpg); background-attachment: fixed;">
            <div class="fh5co-overlay"></div>
            <div class="container">
                <div class="row">
                    <div class="col-md-12">
                        <div class="fh5co-hero-wrap">
                            <div class="fh5co-hero-intro text-center">
                                <div class="col-md-12 text-center">
                                    <span class="demo-intro">AUTO WEB CLASSIFICATION</span>
                                    <span class="demo-intro-label">LET AI DO FOR YOU</span>

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
                    <textarea class="input-textarea form-control" rows="1" id="text1" placeholder="Enter url, keyword, text ..."></textarea>
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
                            <p class="fh5co-sub animate-single product-animate-1 text-black">Click these blocks to try example input.</p>
                        </div>


                        <div class="col-md-3 col-sm-6 col-xs-6 col-xxs-12">
                            <a href="outline/images/product_1.jpg" class="fh5co-figure to-animate image-popup">
                                <figure>
                                    <img src="outline/images/product_1.jpg" alt="Free HTML5 Responsive Template" class="img-responsive">
                                </figure>
                                <h3 class="fh5co-figure-lead">Product Name</h3>
                                <p class="fh5co-figure-text">Far far away behind the word mountains</p>
                            </a>
                        </div>
                        <div class="col-md-3 col-sm-6 col-xs-6 col-xxs-12">
                            <a href="outline/images/product_2.jpg" class="fh5co-figure to-animate image-popup">
                                <figure>
                                    <img src="outline/images/product_2.jpg" alt="Free HTML5 Responsive Template" class="img-responsive">
                                </figure>
                                <h3 class="fh5co-figure-lead">Product Name</h3>
                                <p class="fh5co-figure-text">Far far away behind the word mountains</p>
                            </a>
                        </div>
                        <div class="clearfix visible-sm-block"></div>
                        <div class="col-md-3 col-sm-6 col-xs-6 col-xxs-12">
                            <a href="outline/images/product_3.jpg" class="fh5co-figure to-animate image-popup">
                                <figure>
                                    <img src="outline/images/product_3.jpg" alt="Free HTML5 Responsive Template" class="img-responsive">
                                </figure>
                                <h3 class="fh5co-figure-lead">Product Name</h3>
                                <p class="fh5co-figure-text">Far far away behind the word mountains</p>
                            </a>
                        </div>
                        <div class="col-md-3 col-sm-6 col-xs-6 col-xxs-12">
                            <a href="outline/images/product_4.jpg" class="fh5co-figure to-animate image-popup">
                                <figure>
                                    <img src="outline/images/product_4.jpg" alt="Free HTML5 Responsive Template" class="img-responsive">
                                </figure>
                                <h3 class="fh5co-figure-lead">Product Name</h3>
                                <p class="fh5co-figure-text">Far far away behind the word mountains</p>
                            </a>
                        </div>

                        <div class="clearfix visible-sm-block"></div>

                        <div class="fh5co-spacer fh5co-spacer-sm"></div>

                        <div class="col-md-4 col-md-offset-4 text-center to-animate">
                            <a href="#" class="btn btn-primary">View All Products</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
    <div id="demo-page-result" class="hide content fh5co-bg-section">
            <div class="container container-all row">
                <div class="col-md-4 container-left">
                    <h3><b>Input</b> <span class="tag label label-warning input-tag">URL</span></h3>
                    <textarea class="input-textarea form-control" rows="1" id="text2" placeholder="Enter url, keyword, text ..."></textarea>
                    <br>
                    <button type="button" class="btn btn-primary btn-sm btn-analyze btn-analyze2">Analyze</button>
                    <br>
                    <br>
                    <div class="try-div">
                        <h6><b>Try this things :</b></h6>
                        <h6><span class="try-it" id="try-url"> &raquo; Url: Plavvy Dessert</span></h6>
                        <h6><span class="try-it" id="try-keyword"> &raquo; Keyword: Plavvy Dessert</span></h6>
                        <h6><span class="try-it" id="try-text"> &raquo; Text: Plavvy Dessert</span></h6>
                    </div>


                </div>
                <div class="col-md-8 container-right">
                    <div style="background-color:#d6e6e6; margin: -15px -30px; padding: 20px;">
                        <div class="btn-group">
                            <button type="button" class="btn btn-primary btn-embossed btn-md active" id="btn-result"><span class="fui-eye"></span> Result</button>
                            <button type="button" class="btn btn-primary btn-embossed btn-md" id="btn-json"><span class="fui-arrow-left"></span><span class="fui-arrow-right"></span> JSON</button>
                        </div>
                    </div>
                    <div class="loading hide">
                        <svg class="hourglass" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 206" preserveAspectRatio="none">
                            <path class="middle" d="M120 0H0v206h120V0zM77.1 133.2C87.5 140.9 92 145 92 152.6V178H28v-25.4c0-7.6 4.5-11.7 14.9-19.4 6-4.5 13-9.6 17.1-17 4.1 7.4 11.1 12.6 17.1 17zM60 89.7c-4.1-7.3-11.1-12.5-17.1-17C32.5 65.1 28 61 28 53.4V28h64v25.4c0 7.6-4.5 11.7-14.9 19.4-6 4.4-13 9.6-17.1 16.9z"/>
                            <path class="outer" d="M93.7 95.3c10.5-7.7 26.3-19.4 26.3-41.9V0H0v53.4c0 22.5 15.8 34.2 26.3 41.9 3 2.2 7.9 5.8 9 7.7-1.1 1.9-6 5.5-9 7.7C15.8 118.4 0 130.1 0 152.6V206h120v-53.4c0-22.5-15.8-34.2-26.3-41.9-3-2.2-7.9-5.8-9-7.7 1.1-2 6-5.5 9-7.7zM70.6 103c0 18 35.4 21.8 35.4 49.6V192H14v-39.4c0-27.9 35.4-31.6 35.4-49.6S14 81.2 14 53.4V14h92v39.4C106 81.2 70.6 85 70.6 103z"/>
                        </svg>
                    </div>
                    <div class="result-visual hide">
                        <h1>Tables</h1>
                        <br>
                        <table class="table table-bordered table-result">
                            <thead>
                            <tr>
                                <th>#</th>
                                <th>Category</th>
                                <th>Score</th>
                                <th>Confident ?</th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr>
                                <th scope="row">1</th>
                                <td>Food</td>
                                <td>0.5342132</td>
                                <td>Yes</td>
                            </tr>
                            <tr>
                                <th scope="row">2</th>
                                <td>Restaurant</td>
                                <td>0.2323132</td>
                                <td>No</td>
                            </tr>
                            </tbody>
                        </table>
                        <br>
                        <hr>
                        <br>
                        <h1>Important words</h1>
                        <div class="form-group">
                            <button class="btn btn-inverse">ร้านอาหาร</span></button>
                            <button class="btn btn-inverse">กรุงเทพฯ</span></button>
                            <button class="btn btn-inverse">อร่อย</span></button>
                            <button class="btn btn-inverse">บริการดี</span></button>
                        </div>

                    </div>
                    <!--<pre><code id=account></code></pre>
                    <pre><code id=planets></code></pre>-->
                    <div class="result-json hide">
                        <h1>JSON from API</h1>
                        <pre class="json">
                        </pre>
                    </div>
                </div>
            </div>
    </div>
    <br>
    <br>
    
    
    <!-- jQuery -->
    <script src="outline/js/jquery.min.js"></script>
    <!-- jQuery Easing -->
    <script src="outline/js/jquery.easing.1.3.js"></script>
    <!-- Bootstrap -->
    <script src="outline/js/bootstrap.min.js"></script>
    <!-- Waypoints -->
    <script src="outline/js/jquery.waypoints.min.js"></script>
    <!-- Magnific Popup -->
    <script src="outline/js/jquery.magnific-popup.min.js"></script>
    <!-- Owl Carousel -->
    <script src="outline/js/owl.carousel.min.js"></script>
    <!-- toCount -->
    <script src="outline/js/jquery.countTo.js"></script>
    <!-- Main JS -->
    <script src="outline/js/main.js"></script>
	
@endsection