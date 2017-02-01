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

        <section id="demo-2" class="fh5co-bg-section">
            <div class="searchForm animated">
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
                </div>
                <div class="col-md-8 container-right">
                    <div style="background-color:#d6e6e6; margin: -15px -30px; padding: 20px;">
                        <div class="btn-group">
                            <button type="button" class="btn btn-primary btn-embossed btn-md active" id="btn-result"><span class="fui-eye"></span> Result</button>
                            <button type="button" class="btn btn-primary btn-embossed btn-md" id="btn-json"><span class="fui-arrow-left"></span><span class="fui-arrow-right"></span> JSON</button>
                        </div>
                    </div>
                    <br>
                    <br>

                    <div class="result-visual">
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