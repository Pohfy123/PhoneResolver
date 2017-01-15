<!DOCTYPE html>
<html>
<title>NSC - @yield('title')</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">\

<link href="https://fonts.googleapis.com/css?family=Open+Sans:400italic,600italic,700italic,400,600,700" rel="stylesheet" type="text/css">

<!-- Loading Bootstrap -->
<link href="css/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

<!-- Loading Flat UI -->
<link href="css/flat-ui.css" rel="stylesheet">

<link rel="shortcut icon" href="img/favicon.ico">

<!-- HTML5 shim, for IE6-8 support of HTML5 elements. All other JS at the end of file. -->
<!--[if lt IE 9]>
<script src="js/vendor/html5shiv.js"></script>
<script src="js/vendor/respond.min.js"></script>
<![endif]-->

<link rel="stylesheet" href="http://www.w3schools.com/lib/w3.css">
<link rel="stylesheet" href="http://www.w3schools.com/lib/w3-theme-black.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<link href="css/template.css" rel="stylesheet">

<body id="myPage">

<!-- Navbar -->
<div class="w3-top">

    <nav class="navbar navbar-inverse navbar-embossed" role="navigation">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-collapse-01">
                <span class="sr-only">Toggle navigation</span>
            </button>
            <!--<a class="navbar-brand" href="#">Flat UI</a>-->

        </div>
        <div class="collapse navbar-collapse" id="navbar-collapse-01">
            <ul class="nav navbar-nav navbar-left">
                <li><a href="#fakelink">Home</a></li>
                <li><a href="#fakelink">Demo</a></li>
                <li><a href="#fakelink">API & Docs</a></li>
                <li><a href="#fakelink">Pricing</a></li>
                <li><a href="#fakelink">FAQ</a></li>
            </ul>
        </div><!-- /.navbar-collapse -->
    </nav><!-- /navbar -->

    <!-- Navbar on small screens -->
    <div id="navDemo" class="w3-hide w3-hide-large w3-hide-medium">
        <ul class="w3-navbar w3-left-align w3-theme">
            <li><a href="#team">Team</a></li>
            <li><a href="#work">Work</a></li>
            <li><a href="#pricing">Price</a></li>
            <li><a href="#contact">Contact</a></li>
            <li><a href="#">Search</a></li>
            <li class="w3-dropdown-hover">
                <a href="javascript:void(0);" title="Notifications">Dropdown <i class="fa fa-caret-down"></i></a>
                <div class="w3-dropdown-content w3-light-grey w3-card-4">
                    <a href="#">Link</a>
                    <a href="#">Link</a>
                    <a href="#">Link</a>
                </div>
            </li>
        </ul>
    </div>
</div>

<br>
<br>
@yield('content')



<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<!-- Footer -->
<footer class="w3-container w3-padding-32 w3-center">
    <h4>Follow Us</h4>
    <a class="w3-btn-floating w3-teal" href="javascript:void(0)" title="Facebook"><i class="fa fa-facebook"></i></a>
    <a class="w3-btn-floating w3-teal" href="javascript:void(0)" title="Twitter"><i class="fa fa-twitter"></i></a>
    <a class="w3-btn-floating w3-teal" href="javascript:void(0)" title="Google +"><i class="fa fa-google-plus"></i></a>
    <a class="w3-btn-floating w3-teal" href="javascript:void(0)" title="Google +"><i class="fa fa-instagram"></i></a>
    <a class="w3-btn-floating w3-teal w3-hide-small" href="javascript:void(0)" title="Linkedin"><i class="fa fa-linkedin"></i></a>
    <p>Powered by <a href="#RoosPoh" target="_blank">RoosPoh</a></p>


</footer>


<script src="js/vendor/jquery.min.js"></script>
<script src="js/vendor/video.js"></script>
<script src="js/flat-ui.min.js"></script>
<script src="docs/assets/js/application.js"></script>

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

</body>
</html>
