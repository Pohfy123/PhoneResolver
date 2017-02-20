@extends('masterpage')

@section('title')Home
@endsection

@section('css-js')
    <link rel="stylesheet" href="css/home.css">
@endsection

@section('content')
    <div id="fh5co-wrap">
        <header id="fh5co-hero" data-section="home" role="banner" style="background: url(outline/images/bg_2.jpg) top left; background-size: cover;" >
            <div class="fh5co-overlay"></div>
            <div class="fh5co-intro">
                <div class="container">
                    <div class="row">

                        <div class="col-md-6 fh5co-text">
                            <h2 class="to-animate intro-animate-1">Extract valuable insight from text.</h2>
                            <p class="to-animate intro-animate-2">We help you classify and extract important information from text data.</p>
                            <p class="to-animate intro-animate-3"><a href="#fh5co-features" class="btn btn-primary btn-md">Get started !</a></p>
                        </div>
                        <div class="col-md-6 text-right fh5co-intro-img to-animate intro-animate-4">
                            <img src="outline/images/iphone_6_3.png" alt="Outline Free HTML5 Responsive Bootstrap Template">
                        </div>

                    </div>
                </div>
            </div>
        </header>
        <!-- END .header -->

        <div id="fh5co-main">
            <div id="fh5co-clients">
                <div class="container">
                    <div class="row text-center">
                        <div class="col-md-4 col-sm-6 col-xs-6 to-animate">
                            <figure class="fh5co-client"><img src="img/client-eng-chula-white.png" style="height: 45px;"></figure>
                        </div>
                        <div class="col-md-4 col-sm-6 col-xs-6 to-animate">
                            <figure class="fh5co-client"><img src="img/client-chula-white.png" style="height: 45px;"></figure>
                        </div>
                        <div class="col-md-4 col-sm-6 col-xs-6 to-animate">
                            <figure class="fh5co-client"><img src="img/client-nectec-white.png" style="height: 42px;"></figure>
                        </div>
                    </div>
                </div>
            </div>
            <div id="fh5co-features" data-section="features">


                <div class="container">
                    <div class="row">
                        <div class="col-md-8 col-md-offset-2 fh5co-section-heading text-center">
                            <h2 class="fh5co-lead to-animate">Explore our features</h2>
                            <p class="fh5co-sub to-animate">Done your works with user-friendly interface or<br>powerful API for developers.</p>
                        </div>

                        <div class="col-md-3 col-sm-6 col-xs-6 col-xxs-12">
                            <a href="#" class="fh5co-feature to-animate">
                                <span class="fh5co-feature-icon"><i class="icon-tag"></i></span>
                                <h3 class="fh5co-feature-lead">Auto categorization</h3>
                                <p class="fh5co-feature-text">Website or textual data is classified by powerful text processing.</p>
                            </a>
                        </div>
                        <div class="col-md-3 col-sm-6 col-xs-6 col-xxs-12">
                            <a href="#" class="fh5co-feature to-animate">
                                <span class="fh5co-feature-icon"><i class="icon-speech"></i></span>
                                <h3 class="fh5co-feature-lead">Extract keywords</h3>
                                <p class="fh5co-feature-text">Automatically analyze important entities from websites.</p>
                            </a>
                        </div>
                        <div class="col-md-3 col-sm-6 col-xs-6 col-xxs-12">
                            <a href="#" class="fh5co-feature to-animate">
                                <span class="fh5co-feature-icon"><i class="icon-screen-smartphone"></i></span>
                                <h3 class="fh5co-feature-lead">Phone Resolver</h3>
                                <p class="fh5co-feature-text">Extract interesting information from unknown phone number.</p>
                            </a>
                        </div>
                        <div class="clearfix visible-sm-block"></div>
                        <div class="col-md-3 col-sm-6 col-xs-6 col-xxs-12">
                            <a href="#" class="fh5co-feature to-animate">
                                <span class="fh5co-feature-icon"><h2 class="thai-char">ก</h2></span>
                                <h3 class="fh5co-feature-lead">Thai-language support</h3>
                                <p class="fh5co-feature-text">We understands Thai and English.</p>
                            </a>
                        </div>

                        <div class="clearfix visible-sm-block"></div>

                        <div class="fh5co-spacer fh5co-spacer-sm"></div>

                        <!--<div class="col-md-4 col-md-offset-4 text-center to-animate">
                            <a href="#" class="btn btn-primary">View All Features</a>
                        </div>-->
                    </div>
                </div>


            </div>

            <!--

                                <div id="fh5co-features-2" data-section="design">
                                    <div class="fh5co-features-2-content">
                                        <div class="container">
                                            <div class="row">
                                                <div class="col-md-8 col-md-offset-2 fh5co-section-heading text-center">
                                                    <h2 class="fh5co-lead to-animate">Better design</h2>
                                                    <p class="fh5co-sub to-animate">Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.</p>
                                                </div>
                                                <div class="col-md-4 fh5co-text-wrap">
                                                    <div class="row text-center">
                                                        <div class="col-md-12 col-sm-6 col-xs-6 col-xxs-12 fh5co-text animate-object features-2-animate-3">
                                                            <span class="fh5co-icon"><i class="icon-screen-desktop"></i></span>
                                                            <h4 class="fh5co-uppercase-sm">Cross platform support</h4>
                                                            <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.</p>
                                                        </div>
                                                        <div class="col-md-12 col-sm-6 col-xs-6 col-xxs-12 fh5co-text animate-object features-2-animate-4">
                                                            <span class="fh5co-icon"><i class="icon-anchor"></i></span>
                                                            <h4 class="fh5co-uppercase-sm">Prototyping tools</h4>
                                                            <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.</p>
                                                        </div>

                                                    </div>
                                                </div>
                                                <div class="col-md-4 col-md-push-4 fh5co-text-wrap">
                                                    <div class="row text-center">
                                                        <div class="col-md-12 col-sm-6 col-xs-6 col-xxs-12 fh5co-text animate-object features-2-animate-5">
                                                            <span class="fh5co-icon"><i class="icon-rocket"></i></span>
                                                            <h4 class="fh5co-uppercase-sm">Powerful design</h4>
                                                            <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.</p>
                                                        </div>
                                                        <div class="col-md-12 col-sm-6 col-xs-6 col-xxs-12 fh5co-text animate-object features-2-animate-6">
                                                            <span class="fh5co-icon"><i class="icon-people"></i></span>
                                                            <h4 class="fh5co-uppercase-sm">User Collaboration</h4>
                                                            <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.</p>
                                                        </div>

                                                    </div>
                                                </div>
                                                <div class="col-md-4 col-md-pull-4 fh5co-image animate-object features-2-animate-2">
                                                    <p class="text-center">
                                                    <img src="outline/images/iphone_blank_2.png" class="" alt="Outline Free HTML5 Responsive Bootstrap Template">
                                                    </p>
                                                </div>

                                            </div>
                                        </div>
                                    </div>

                                </div>


                                <div id="fh5co-testimony" data-section="testimonies">
                                    <div class="container">
                                        <div class="row animate-box">

                                            <div class="owl-carousel">

                                                <div class="item">
                                                    <div class="col-md-3 col-sm-3 col-xs-4 col-xxs-12">
                                                        <figure class="fh5co-vcard"><img src="outline/images/user.jpg" alt="Free HTML5 Template by FREEHTML5.co" class="img-responsive"></figure>
                                                    </div>
                                                    <div class="col-md-9 col-sm-9 col-xs-8 col-xxs-12">
                                                        <blockquote>
                                                            <p>&ldquo;Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.&rdquo;</p>
                                                        </blockquote>
                                                        <p class="fh5co-author fh5co-uppercase-sm"><span>Gustav Barrow</span>, XYZ Inc.</p>
                                                    </div>
                                                </div>

                                                <div class="item">
                                                    <div class="col-md-3 col-sm-3 col-xs-4 col-xxs-12">
                                                        <figure class="fh5co-vcard"><img src="outline/images/user_2.jpg" alt="Free HTML5 Template by FREEHTML5.co" class="img-responsive"></figure>
                                                    </div>
                                                    <div class="col-md-9 col-sm-9 col-xs-8 col-xxs-12">
                                                        <blockquote>
                                                            <p>&ldquo;Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.&rdquo;</p>
                                                        </blockquote>
                                                        <p class="fh5co-author fh5co-uppercase-sm"><span>Gustav Barrow</span>, XYZ Inc.</p>
                                                    </div>
                                                </div>

                                                <div class="item">
                                                    <div class="col-md-3 col-sm-3 col-xs-4 col-xxs-12">
                                                        <figure class="fh5co-vcard"><img src="outline/images/user_3.jpg" alt="Free HTML5 Template by FREEHTML5.co" class="img-responsive"></figure>
                                                    </div>
                                                    <div class="col-md-9 col-sm-9 col-xs-8 col-xxs-12">
                                                        <blockquote>
                                                            <p>&ldquo;Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.&rdquo;</p>
                                                        </blockquote>
                                                        <p class="fh5co-author fh5co-uppercase-sm"><span>Gustav Barrow</span>, XYZ Inc.</p>
                                                    </div>
                                                </div>


                                            </div>

                                        </div>
                                    </div>
                                </div>


                                <div id="fh5co-counter" class="fh5co-bg-section" style="background-image: url(outline/images/bg_1.jpg); background-attachment: fixed;">
                                    <div class="fh5co-overlay"></div>
                                    <div class="container">
                                        <div class="row">
                                            <div class="col-md-12">
                                                <div class="fh5co-hero-wrap">
                                                    <div class="fh5co-hero-intro text-center to-animate counter-animate">
                                                        <div class="col-md-4 text-center">
                                                            <span class="fh5co-counter js-counter" data-from="0" data-to="28" data-speed="5000" data-refresh-interval="50"></span>
                                                            <span class="fh5co-counter-label">Customers</span>

                                                        </div>
                                                        <div class="col-md-4 text-center">
                                                            <span class="fh5co-counter js-counter" data-from="0" data-to="57" data-speed="5000" data-refresh-interval="50"></span>
                                                            <span class="fh5co-counter-label">Completed Apps</span>
                                                        </div>
                                                        <div class="col-md-4 text-center">
                                                            <span class="fh5co-counter js-counter" data-from="0" data-to="34023" data-speed="5000" data-refresh-interval="50"></span>
                                                            <span class="fh5co-counter-label">Downloads</span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>


                                <div id="fh5co-products" data-section="products">

                                    <div class="container">
                                        <div class="row">
                                            <div class="col-md-8 col-md-offset-2 fh5co-section-heading text-center">
                                                <h2 class="fh5co-lead animate-single product-animate-1">Other awesome Apps</h2>
                                                <p class="fh5co-sub animate-single product-animate-2">Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.</p>
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

                                <div id="fh5co-features-3" data-section="benefits">
                                    <div class="container">
                                        <div class="row">
                                            <div class="col-md-8 col-md-offset-2 fh5co-section-heading text-center">
                                                <h2 class="fh5co-lead animate-single features3-animate-1">Benefits of this App</h2>
                                                <p class="fh5co-sub animate-single features3-animate-2">Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.</p>
                                            </div>

                                            <div class="col-md-4 col-sm-6 text-center fh5co-text-wrap">
                                                <div class="fh5co-text to-animate">
                                                    <span class="fh5co-icon"><i class="icon-screen-desktop"></i></span>
                                                    <h4 class="fh5co-uppercase-sm">Cross platform support</h4>
                                                    <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.</p>
                                                </div>
                                            </div>
                                            <div class="col-md-4 col-sm-6 text-center fh5co-text-wrap">
                                                <div class="fh5co-text to-animate">
                                                    <span class="fh5co-icon"><i class="icon-graph"></i></span>
                                                    <h4 class="fh5co-uppercase-sm">Cross platform support</h4>
                                                    <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.</p>
                                                </div>
                                            </div>

                                            <div class="clearfix visible-sm-block"></div>

                                            <div class="col-md-4 col-sm-6 text-center fh5co-text-wrap">
                                                <div class="fh5co-text to-animate">
                                                    <span class="fh5co-icon"><i class="icon-anchor"></i></span>
                                                    <h4 class="fh5co-uppercase-sm">Cross platform support</h4>
                                                    <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.</p>
                                                </div>
                                            </div>

                                            <div class="col-md-4 col-sm-6 text-center fh5co-text-wrap">
                                                <div class="fh5co-text to-animate">
                                                    <span class="fh5co-icon"><i class="icon-camera"></i></span>
                                                    <h4 class="fh5co-uppercase-sm">Cross platform support</h4>
                                                    <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.</p>
                                                </div>
                                            </div>

                                            <div class="clearfix visible-sm-block"></div>

                                            <div class="col-md-4 col-sm-6 text-center fh5co-text-wrap">
                                                <div class="fh5co-text to-animate">
                                                    <span class="fh5co-icon"><i class="icon-present"></i></span>
                                                    <h4 class="fh5co-uppercase-sm">Cross platform support</h4>
                                                    <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.</p>
                                                </div>
                                            </div>
                                            <div class="col-md-4 col-sm-6 text-center fh5co-text-wrap">
                                                <div class="fh5co-text to-animate">
                                                    <span class="fh5co-icon"><i class="icon-energy"></i></span>
                                                    <h4 class="fh5co-uppercase-sm">Cross platform support</h4>
                                                    <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.</p>
                                                </div>
                                            </div>



                                        </div>
                                    </div>
                                </div>-->

            <div class="fh5co-bg-section cta" id="fh5co-cta" style="background-image: url(outline/images/hero_bg.jpg); background-attachment: fixed;">
                <div class="fh5co-overlay"></div>
                <div class="container">
                    <div class="row">
                        <div class="col-md-12">
                            <div class="fh5co-hero-wrap">
                                <div class="fh5co-hero-intro text-center">
                                    <div class="row">
                                        <div class="col-md-8 col-md-offset-2 fh5co-section-heading text-center">
                                            <h2 class="fh5co-lead to-animate">Try InsightText Demo now!</h2>
                                            <p class="fh5co-sub to-animate">Turn text into diamond.</p>
                                            <div class="to-animate"><a href="/demo" class="btn btn-primary">Try DEMO!</a></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!--<div id="fh5co-pricing" data-section="pricing">
                <div class="container">
                    <div class="row">
                        <div class="col-md-8 col-md-offset-2 fh5co-section-heading text-center">
                            <h2 class="fh5co-lead animate-single pricing-animate-1">InsightText Plans</h2>
                            <p class="fh5co-sub animate-single pricing-animate-2">Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.</p>
                        </div>

                        <div class="col-md-4 to-animate">
                                    <span href="#" class="fh5co-figure">
                                        <span class="fh5co-price">0<span>/month</span></span>
                                        <h3 class="fh5co-figure-lead">FREE</h3>
                                        <p class="fh5co-figure-text">100 queries/month</p>
                                        <a href="/demo" class="btn btn-primary btn-xs">Try for free!</a>
                                    </span>
                        </div>
                        <div class="col-md-4 to-animate">
                                    <span href="#" class="fh5co-figure">
                                        <span class="fh5co-price">$19<span>/month</span></span>
                                        <h3 class="fh5co-figure-lead">Regular</h3>
                                        <p class="fh5co-figure-text">10,000 queries/month</p>
                                        <a href="/demo" class="btn btn-primary btn-xs" disabled>Signup</a>
                                    </span>
                        </div>
                        <div class="col-md-4 to-animate">
                                    <span href="#" class="fh5co-figure active pricing-feature">
                                        <span class="fh5co-price">$49<span>/month</span></span>
                                        <h3 class="fh5co-figure-lead">Pro</h3>
                                        <p class="fh5co-figure-text">50,000 queries/month</p>
                                        <a href="/demo" class="btn btn-primary btn-xs" disabled>Signup</a>
                                    </span>
                        </div>
                    </div>
                </div>
            </div>-->

            <!--<div id="fh5co-faqs"  data-section="faqs">
                <div class="container">
                    <div class="row">
                        <div class="col-md-8 col-md-offset-2 fh5co-section-heading text-center">
                            <h2 class="fh5co-lead animate-single faqs-animate-1">Frequently Ask Questions</h2>
                            <p class="fh5co-sub animate-single faqs-animate-2">Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts.</p>
                        </div>
                    </div>
                </div>


                <div class="container">
                    <div class="faq-accordion active to-animate">
                        <span class="faq-accordion-icon-toggle active"><i class="icon-arrow-down"></i></span>
                        <h3>What is Outline?</h3>
                        <div class="faq-body" style="display: block;">
                            <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth. Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life One day however a small line of blind text by the name of Lorem Ipsum decided to leave for the far World of Grammar.</p>
                        </div>
                    </div>
                    <div class="faq-accordion to-animate">
                        <span class="faq-accordion-icon-toggle"><i class="icon-arrow-down"></i></span>
                        <h3>Is Outline Free?</h3>
                        <div class="faq-body">
                            <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth. Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life One day however a small line of blind text by the name of Lorem Ipsum decided to leave for the far World of Grammar.</p>
                        </div>
                    </div>
                    <div class="faq-accordion to-animate">
                        <span class="faq-accordion-icon-toggle"><i class="icon-arrow-down"></i></span>
                        <h3>How do I use Outline Features?</h3>
                        <div class="faq-body">
                            <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth. Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life One day however a small line of blind text by the name of Lorem Ipsum decided to leave for the far World of Grammar.</p>
                        </div>
                    </div>
                    <div class="faq-accordion to-animate">
                        <span class="faq-accordion-icon-toggle"><i class="icon-arrow-down"></i></span>
                        <h3>Which version of iOS do your apps support?</h3>
                        <div class="faq-body">
                            <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth. Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life One day however a small line of blind text by the name of Lorem Ipsum decided to leave for the far World of Grammar.</p>
                        </div>
                    </div>
                    <div class="faq-accordion to-animate">
                        <span class="faq-accordion-icon-toggle"><i class="icon-arrow-down"></i></span>
                        <h3>What languages are available?</h3>
                        <div class="faq-body">
                            <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth. Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life One day however a small line of blind text by the name of Lorem Ipsum decided to leave for the far World of Grammar.</p>
                        </div>
                    </div>
                    <div class="faq-accordion to-animate">
                        <span class="faq-accordion-icon-toggle"><i class="icon-arrow-down"></i></span>
                        <h3>I have technical problem, who do I email?</h3>
                        <div class="faq-body">
                            <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth. Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic life One day however a small line of blind text by the name of Lorem Ipsum decided to leave for the far World of Grammar.</p>
                        </div>
                    </div>
                </div>
            </div>-->

            <div id="fh5co-subscribe">
                <div class="container">
                    <div class="row animate-box">
                        <form action="#" method="post">
                            <!--<div class="col-md-3 col-sm-3">
                                <div class="form-group">
                                    <input type="text" class="form-control" placeholder="First Name">
                                </div>
                            </div>
                            <div class="col-md-3 col-sm-3">
                                <div class="form-group">
                                    <input type="text" class="form-control" placeholder="Last Name">
                                </div>
                            </div>
                            <div class="col-md-3 col-sm-3">
                                <div class="form-group">
                                    <input type="email" class="form-control" placeholder="Email">
                                </div>
                            </div>
                            <div class="col-md-3 col-sm-3">
                                <div class="form-group">
                                    <input type="submit" class="btn btn-primary" value="Subscribe">
                                </div>
                            </div>-->
                        </form>
                    </div>
                </div>
            </div>


        </div>
    </div>


    @endsection





