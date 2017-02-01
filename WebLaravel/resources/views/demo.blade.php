@extends('masterpage')

@section('title')Demo
@endsection

@section('css-js')
    <link href="css/demo.css" rel="stylesheet">
    <link href="css/result.css" rel="stylesheet">
    <script src="js/demo.js"></script>
    <script src="js/result.js"></script>
@endsection

@section('content')
    <div id="demo-page-input" class="content content-demo-input">
        <section id="demo-sec-intro" class="fh5co-bg-section" style="background-image: url(outline/images/bg_1.jpg); background-attachment: fixed; padding-top:2em; padding-bottom:1em;">
            <div class="fh5co-overlay"></div>
            <div class="container">
                <div class="row">
                    <div class="col-md-12">
                        <div class="fh5co-hero-wrap">
                            <div class="fh5co-hero-intro text-center">
                                <div class="col-md-12 text-center">
                                    <span class="demo-intro">Make categorization more EASY!</span>
                                    <span class="demo-intro-label">Let's try DEMO</span>
                                    
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section id="demo-2" class="fh5co-bg-section">
            <div class="searchForm animated">
                <h1>Try to categorize</h1>
                <a>tests</a>
                <hr>
                <h3><b>Input</b></h3>
                <div class="form-group">
                    <textarea class="input-textarea form-control" rows="1" id="text1" placeholder="Enter url, keyword, text ..."></textarea>
                </div>
                <div class="center">
                    <button type="button" class="btn btn-primary btn-analyze1">Analyze</button>
                </div>
            </div>
        </section>
    </div>
    <div id="demo-page-result" class="hide">
        <section class="page-result">
            <div class="container container-all row">
                <div class="col-md-4 container-left">
                    <h3><b>Input</b> <span class="tag label label-warning input-tag">URL</span></h3>
                    <textarea class="input-textarea form-control" rows="1" id="text2" placeholder="Enter url, keyword, text ..."></textarea>
                    <br>
                    <button type="button" class="btn btn-primary btn-sm">Analyze</button>
                    <h5>Try this things :</h5>
                    <h5 class="try-it"><span class="fui-triangle-right-large"> Url: Plavvy Dessert</h5>
                    <h5 class="try-it"><span class="fui-triangle-right-large"> Keyword: Plavvy Dessert</h5>
                    <h5 class="try-it"><span class="fui-triangle-right-large"> Text: Plavvy Dessert</h5>

                </div>
                <div class="col-md-8 container-right">
                    <div class="btn-group">
                        <button type="button" class="btn btn-primary btn-sm active" id="btn-result"><span class="fui-eye"></span> Result</button>
                        <button type="button" class="btn btn-primary btn-sm" id="btn-json"><span class="fui-arrow-left"></span><span class="fui-arrow-right"></span> JSON</button>
                    </div>
                    <br>
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
                    <pre class="json hide">
                    </pre>
                    <!--<pre><code id=account></code></pre>
                    <pre><code id=planets></code></pre>-->

                </div>
            </div>
        </section>
    </div>
   
    
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