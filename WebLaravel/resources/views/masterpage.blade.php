<!DOCTYPE html>
<html>
<head>
    <title>InsighText - @yield('title')</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
<link href="https://fonts.googleapis.com/css?family=Open+Sans:400italic,600italic,700italic,400,600,700" rel="stylesheet" type="text/css">

    <!-- Loading Bootstrap -->
    <link href="css/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

    <!-- Loading Flat UI -->
    <link href="css/flat-ui.css" rel="stylesheet">

    <!-- HTML5 shim, for IE6-8 support of HTML5 elements. All other JS at the end of file. -->
    <!--[if lt IE 9]>
    <script src="js/vendor/html5shiv.js"></script>
    <script src="js/vendor/respond.min.js"></script>
    <![endif]-->

    {{--<link rel="stylesheet" href="http://www.w3schools.com/lib/w3.css">--}}
    {{--<link rel="stylesheet" href="http://www.w3schools.com/lib/w3-theme-black.css">--}}
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

    <!-- Place favicon.ico and apple-touch-icon.png in the root directory -->
    <link rel="shortcut icon" href="favicon.ico">
    <!-- Google Webfonts -->
    <link href='https://fonts.googleapis.com/css?family=Montserrat:400,700' rel='stylesheet' type='text/css'>
    <!--<link href='https://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'>-->
    <!-- Animate.css -->
    <link rel="stylesheet" href="outline/css/animate.css">
    <!-- Icomoon Icon Fonts-->
    <link rel="stylesheet" href="outline/css/icomoon.css">
    <!-- Simple Line Icons-->
    <link rel="stylesheet" href="outline/css/simple-line-icons.css">
    <!-- Magnific Popup -->
    <link rel="stylesheet" href="outline/css/magnific-popup.css">
    <!-- Owl Carousel -->
    <link rel="stylesheet" href="outline/css/owl.carousel.min.css">
    <link rel="stylesheet" href="outline/css/owl.theme.default.min.css">
    <!-- Salvattore -->
    {{--<link rel="stylesheet" href="outline/css/salvattore.css">--}}
    <!-- Theme Style -->
    <link rel="stylesheet" href="outline/css/style.css">
    <!-- Modernizr JS -->
    <script src="outline/js/modernizr-2.6.2.min.js"></script>
    <!-- FOR IE9 below -->
    <!--[if lt IE 9]>
    <script src="js/respond.min.js"></script>
    <![endif]-->
    
    <link href="css/template.css" rel="stylesheet">

    @yield('css-js')

</head>

<body id="myPage">

    {{--<!-- Navbar -->--}}
    <div id="fh5co-offcanvass">
        <ul>
            <li class="active"><a href="#" data-nav-section="home">Home</a></li>
            <li><a href="/demo">Demo</a></li>
            <li><a href="/api-docs">API &amp; DOCS</a></li>
            <!--<li><a href="/#fh5co-pricing">Pricing</a></li>-->
            <li><a href="/faq">FAQ</a></li>
        </ul>
        {{--<h3 class="fh5co-lead">Connect with us</h3>--}}
        {{--<p class="fh5co-social-icons">--}}
            {{--<a href="#"><i class="icon-twitter"></i></a>--}}
            {{--<a href="#"><i class="icon-facebook"></i></a>--}}
            {{--<a href="#"><i class="icon-instagram"></i></a>--}}
            {{--<a href="#"><i class="icon-dribbble"></i></a>--}}
            {{--<a href="#"><i class="icon-youtube"></i></a>--}}
        {{--</p>--}}
    </div>

    <div id="fh5co-menu" class="navbar collapse navbar-collapse">
        <div class="container">
            <div class="row">
                <div class="col-md-3">
                    {{--<a href="#" class="js-fh5co-nav-toggle fh5co-nav-toggle" data-toggle="collapse" data-target="#fh5co-navbar" aria-expanded="false" aria-controls="navbar"><span>Menu</span> <i></i></a>--}}
                    <a href="/" class="navbar-brand"><span>InsighText</span></a>
                </div>
                <div class="col-md-9">
                    <div style="float: right">
                        {{--<a href="#" class="js-fh5co-nav-toggle fh5co-nav-toggle nav-menu" data-toggle="collapse" data-target="#fh5co-navbar" aria-expanded="false" aria-controls="navbar"><span>Menu</span> <i></i></a>--}}
                        <a href="{{ url('/demo') }}" class="navbar-content navbar-brand"><span style="{{ Request::is('demo') ? 'border-bottom: solid !important;' : '' }}">Demo</span></a>
                        <a href="{{ url('/api-docs') }}" class="navbar-content navbar-brand"><span style="{{ Request::is('api-docs') ? 'border-bottom: solid !important;' : '' }}">API &amp; DOCS</span></a>
                        <!--<a href="{{ url('/#fh5co-pricing') }}" class="navbar-content navbar-brand"><span style="{{ Request::is('pricing') ? 'border-bottom: solid !important;' : '' }}">Pricing</span></a>-->
                        <a href="{{ url('/faq') }}" class="navbar-content navbar-brand"><span style="{{ Request::is('faq') ? 'border-bottom: solid !important;' : '' }}">FAQ</span></a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div id="fh5co-menu" class="navbar collapse nav-menu">
        <div class="container">
            <div class="row">
                <div class="col-md-3">
                    {{--<a href="#" class="js-fh5co-nav-toggle fh5co-nav-toggle" data-toggle="collapse" data-target="#fh5co-navbar" aria-expanded="false" aria-controls="navbar"><span>Menu</span> <i></i></a>--}}
                </div>
                <div class="col-md-9">
                    <div style="float: right">
                        <a href="#" class="js-fh5co-nav-toggle fh5co-nav-toggle nav-menu" data-toggle="collapse" data-target="#fh5co-navbar" aria-expanded="false" aria-controls="navbar"><span>Menu</span> <i></i></a>
                    </div>

                </div>

            </div>
        </div>
    </div>



    <div id="fh5co-page">
        <div id="fh5co-wrap">

                @yield('content')


        <footer id="fh5co-footer" style="padding: 2em;">
            <div class="fh5co-overlay"></div>
            <div class="fh5co-footer-content" style="padding: 2em 8em;">
                <div class="container">
                    <div class="row">
                        {{--<div class="col-md-3 col-sm-4 col-md-push-3">--}}
                            {{--<h3 class="fh5co-lead">About</h3>--}}
                            {{--<ul>--}}
                                {{--<li><a href="#">Tour</a></li>--}}
                                {{--<li><a href="#">Company</a></li>--}}
                                {{--<li><a href="#">Jobs</a></li>--}}
                                {{--<li><a href="#">Blog</a></li>--}}
                                {{--<li><a href="#">New Features</a></li>--}}
                                {{--<li><a href="#">Contact Us</a></li>--}}
                            {{--</ul>--}}
                        {{--</div>--}}
                        {{--<div class="col-md-3 col-sm-4 col-md-push-3">--}}
                            {{--<h3 class="fh5co-lead">Support</h3>--}}
                            {{--<ul>--}}
                                {{--<li><a href="#">Help Center</a></li>--}}
                                {{--<li><a href="#">Terms of Service</a></li>--}}
                                {{--<li><a href="#">Security</a></li>--}}
                                {{--<li><a href="#">Privacy Policy</a></li>--}}
                                {{--<li><a href="#">Careers</a></li>--}}
                                {{--<li><a href="#">More Apps</a></li>--}}
                            {{--</ul>--}}
                        {{--</div>--}}
                        {{--<div class="col-md-3 col-sm-4 col-md-push-3">--}}
                            {{--<h3 class="fh5co-lead">More Links</h3>--}}
                            {{--<ul>--}}
                                {{--<li><a href="#">Feedback</a></li>--}}
                                {{--<li><a href="#">Frequently Ask Questions</a></li>--}}
                                {{--<li><a href="#">Terms of Service</a></li>--}}
                                {{--<li><a href="#">Privacy Policy</a></li>--}}
                                {{--<li><a href="#">Careers</a></li>--}}
                                {{--<li><a href="#">More Apps</a></li>--}}
                            {{--</ul>--}}
                        {{--</div>--}}

                        {{--<div class="col-md-3 col-sm-12 col-md-pull-9">--}}
                            <div class="fh5co-footer-logo"><a href="index.html">InsighText</a></div>
                            <p class="fh5co-copyright"><small>&copy; 2015. All Rights Reserved. <br>	</small></p>
                            <p>powered by Roos &amp; Poh</p>
                        {{--<p class="fh5co-social-icons">--}}
                                {{--<a href="#"><i class="icon-twitter"></i></a>--}}
                                {{--<a href="#"><i class="icon-facebook"></i></a>--}}
                                {{--<a href="#"><i class="icon-instagram"></i></a>--}}
                                {{--<a href="#"><i class="icon-dribbble"></i></a>--}}
                                {{--<a href="#"><i class="icon-youtube"></i></a>--}}
                            {{--</p>--}}
                        {{--</div>--}}

                    </div>
                </div>
            </div>
        </footer>
    </div>




{{--<!-- Footer -->--}}
{{--<footer class="w3-container w3-padding-32 w3-center">--}}
    {{--<h4>Follow Us</h4>--}}
    {{--<a class="w3-btn-floating w3-teal" href="javascript:void(0)" title="Facebook"><i class="fa fa-facebook"></i></a>--}}
    {{--<a class="w3-btn-floating w3-teal" href="javascript:void(0)" title="Twitter"><i class="fa fa-twitter"></i></a>--}}
    {{--<a class="w3-btn-floating w3-teal" href="javascript:void(0)" title="Google +"><i class="fa fa-google-plus"></i></a>--}}
    {{--<a class="w3-btn-floating w3-teal" href="javascript:void(0)" title="Google +"><i class="fa fa-instagram"></i></a>--}}
    {{--<a class="w3-btn-floating w3-teal w3-hide-small" href="javascript:void(0)" title="Linkedin"><i class="fa fa-linkedin"></i></a>--}}
    {{--<p>Powered by <a href="#RoosPoh" target="_blank">Roos &amp; Poh</a></p>--}}


{{--</footer>--}}


<script src="js/vendor/jquery.min.js"></script>
<script src="js/vendor/video.js"></script>
{{--<script src="js/flat-ui.min.js"></script>--}}

<script>
    videojs.options.flash.swf = "js/vendors/video-js.swf"
</script>

<!-- Script For Side Navigation -->
<script>
    function w3_open() {
        var x = document.getElementById("mySidenav");
        x.style.width = "300px";
        x.style.textAlign = "center";
        x.style.fontSize = "40px";
        x.style.paddingTop = "10%";
        x.style.display = "block";
    }
    function w3_close() {
        document.getElementById("mySidenav").style.display = "none";
    }

    // Used to toggle the menu on smaller screens when clicking on the menu button
    function openNav() {
        var x = document.getElementById("navDemo");
        if (x.className.indexOf("w3-show") == -1) {
            x.className += " w3-show";
        } else {
            x.className = x.className.replace(" w3-show", "");
        }
    }
</script>
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
@yield('css-js-after')
</body>
</html>
