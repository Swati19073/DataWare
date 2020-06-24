
<?php
include("connection.php") 
?>
<html>
	<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.w3-sidebar a {font-family: "Roboto", sans-serif}
body,h1,h2,h3,h4,h5,h6,.w3-wide {font-family: "Montserrat", sans-serif;}
</style>


 
		<title>Welcome</title>
	</head>
		<body>

<!-- Sidebar/menu -->
<nav class="w3-sidebar w3-bar-block w3-white w3-collapse w3-top" style="z-index:3;width:250px" id="mySidebar">
<div class="w3-container w3-display-container w3-padding-16">
<i onclick="w3_close()" class="fa fa-remove w3-hide-large w3-button w3-display-topright"></i>
<h3 class="w3-wide"><a href="http://localhost/DW_Minor/home.php"> <b>HOME</b></a></h3>
</div>
<div class="w3-padding-64 w3-large w3-text-grey" style="font-weight:bold">
<a href="http://localhost/DW_Minor/Decision.php" class="w3-bar-item w3-button">Decision</a>
<a href="http://localhost/DW_Minor/Action.php" class="w3-bar-item w3-button">Action</a>
<a href="http://localhost/DW_Minor/Uncertainities.php" class="w3-bar-item w3-button">Uncertainties</a>
<a href="http://localhost/DW_Minor/Objectives.php" class="w3-bar-item w3-button">Objectives</a>

<a onclick="myAccFunc()" href="javascript:void(0)" class="w3-button w3-block w3-white w3-left-align" id="myBtn">
Object <i class="fa fa-caret-down"></i>
</a>
<div id="demoAcc" class="w3-bar-block w3-hide w3-padding-large w3-medium">
<a href="http://localhost/DW_Minor/Alternatives.php" class="w3-bar-item w3-button w3-light-grey"><i class="fa fa-caret-right w3-margin-right"></i>Alternatives</a>
<a href="http://localhost/DW_Minor/Action_object.php" class="w3-bar-item w3-button">Action</a>
<a href="http://localhost/DW_Minor/Objective_object.php" class="w3-bar-item w3-button">Objective</a>
<a href="http://localhost/DW_Minor/Uncertainity_object.php" class="w3-bar-item w3-button">Uncertainty</a>
</div>
</div>
<div>
<a href="javascript:void(0)" class="w3-bar-item w3-button w3-padding" onclick="document.getElementById('Team').style.display='block'">Team</a>
</div>
</nav>

<!-- !PAGE CONTENT! -->
<div class="w3-main" style="margin-left:250px">

<!-- Push down content on small screens -->
<div class="w3-hide-large" style="margin-top:83px"></div>

<!-- Top header -->
<header class="w3-container w3-xlarge">
<p class="w3-left">DIEM MODEL</p>
<p class="w3-right">

</p>
</header>

<!-- Image header -->
<div class="w3-display-container w3-container">
<img src="DW.png" alt="Logo" style="width:1100px;height:700px;">
</div>

</div>
<!-- Newsletter Modal -->
<div id="Team" class="w3-modal">
<div class="w3-modal-content w3-animate-zoom" style="padding:32px">
<div class="w3-container w3-white w3-center">
<i onclick="document.getElementById('Team').style.display='none'" class="fa fa-remove w3-right w3-button w3-transparent w3-xxlarge"></i>
<h2 class="w3-wide">Team</h2>
<p>Anamitra Maji (MT19112)</p>
<p>Pragya Dara (MT19126)</p>
<p>Swati Verma (MT19073)</p>

</div>
</div>
</div>






<script>
// Accordion
function myAccFunc() {
    var x = document.getElementById("demoAcc");
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else {
        x.className = x.className.replace(" w3-show", "");
    }
}

function w3_open() {
    document.getElementById("mySidebar").style.display = "block";
    document.getElementById("myOverlay").style.display = "block";
}

function w3_close() {
    document.getElementById("mySidebar").style.display = "none";
    document.getElementById("myOverlay").style.display = "none";
}


</script>
</body>
</html>

