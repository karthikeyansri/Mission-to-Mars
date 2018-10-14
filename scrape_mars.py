<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="icon" type="image" href="https://pngimg.com/uploads/mars_planet/mars_planet_PNG13.png">
    <title>Mission to Mars</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">



    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
        crossorigin="anonymous">

</head>

<body class="text-white" style="background-color:black;">
    <div class="container">

        <!-- Jumbotron -->
        <div class="jumbotron text-center" style="background-image: url(https://cdn.theatlantic.com/static/mt/assets/science/0831Pic.jpg); background-size: 100%;">
            <h1 class="display-4">Mission to Mars</h1>
            <a class="btn btn-lg text-white" style="background-color:#c1440e;" href="/scrape" role="button">Scrape New
                Data</a>
        </div>

        <!-- News Section -->
        <div class="container">
            <h3>Latest Mars News</h3>
            <h6>{{ mars_info.news_title }}</h6>
            <p>{{ mars_info.news_paragraph }}</p>
        </div>

        <div class="container">
            <div class="row">
                <!-- Left Image-->
                <div class="col-lg-8 col-md-8 col-sm-12">
                    <h3>Featured Mars Image</h3>
                    <img src="{{ mars_info.featured_image_url }}" style="max-width:100%; max-height: auto;" alt="Mars Featured Image">
                </div>
                <!-- Weather Card -->
                <div class="col-lg-4 col-md-4 col-sm-12">

                    <div class="card" style="width: 18rem;">
                        <div class="card-body text-white bg-dark">
                            <h6 class="card-title">Current Weather on Mars</h6>
                            <p class="card-text">{{ mars_info.weather_tweet }}</p>
                        </div>

                    </div>

                    <!-- Table -->
                    <br>
                    <h6>Mars Facts</h6>
                    <div style="max-width: 450px; max-height: 150px; font-size: 15px;">
                        {{ mars_info.mars_facts|safe}}
                    </div>
                </div> <!-- col4 -->
            </div><!-- Row -->
        </div><!-- Container -->

        <!-- Cards -->



        <!-- Cards -->
        <div class="card-deck" style="margin-top:100px;">
            <h3 style="padding-top:50px; text-align: center;">Mars Hemispheres</h3>
            <hr>
            <div class="row">
                <div class="card text-white bg-dark" style="margin: 30px;">
                    <img class="card-img-top" src="{{ mars_info.hmu[0]['img_url'] }}">
                    <div class="card-body">
                        <p class="card-text">{{ mars_info.hmu[0]['title'] }}</p>
                    </div>
                </div>
                <div class="card text-white bg-dark" style="margin: 30px;">
                    <img class="card-img-top" src="{{ mars_info.hmu[1]['img_url'] }}">
                    <div class="card-body">
                        <p class="card-text">{{ mars_info.hmu[1]['title'] }}</p>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="card text-white bg-dark" style="margin: 30px;">
                    <img class="card-img-top" src="{{ mars_info.hmu[2]['img_url'] }}">
                    <div class="card-body">
                        <p class="card-text">{{ mars_info.hmu[2]["title"] }}</p>
                    </div>
                </div>
                <div class="card text-white bg-dark" style="margin: 30px;">
                    <img class="card-img-top" src="{{ mars_info.hmu[3]['img_url'] }}">
                    <div class="card-body">
                        <p class="card-text">{{ mars_info.hmu[3]["title"] }}</p>
                    </div>
                </div>
            </div>
        </div>
    </div><!-- Close main container -->


    </div><!-- Close main container -->


    <!-- Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>

</body>

</html>


