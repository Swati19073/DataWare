<?php
include("connection.php")
?>

<html>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<style>
.w3-sidebar a {font-family: "Roboto", sans-serif}
body,h1,h2,h3,h4,h5,h6,.w3-wide {font-family: "Montserrat", sans-serif;}
.container {
    border-radius: 5px;
    background-color: #C6ECEC  ;
padding: 10px;
    vertical-align:middle;
    margin-top: 140px;
    margin-right: 30px;
    
}

.button {
    background-color:#009999 ;
border: none;
color: white;
padding: 15px 32px;
    text-align: center;
    text-decoration: none;
display: inline-block;
    font-size: 16px;
    border-radius: 4px;
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
}

</style>
<title>Objectives</title>
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

</nav>
<div class="container" style="margin-left:250px">
<!-- Top header -->
<header class="w3-container w3-xlarge" >
<p style="text-align:center">Objectives</p>
<p style="font-size:10px; text-align:center">* Since these attributes are added as columns make sure they follow the naming convention for columns</p>
</header>
<div style="text-align:center">
			<form>
				
				<label for="select_obj">
				<span>Input objectives for the decision</span>

				<select id="select_obj" name="imperative">Select Imperative
				<option value="Minimize">Minimize</option>
				<option value="Maximize">Maximize</option>

				</select>
				</label>
				<label for="txt_obj">
				<span></span>
					<input type="text" id="txt_obj" name="txt_obj" />
				</label><br>

<button class="button" type="submit" value="Save" name="obj_save" style="margin-top:10px">Save</button>

			</form>
		</body>
	</head>
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
</html>
<?php
    if (isset($_GET["imperative"]) && isset($_GET["txt_obj"]))
    {
        $imp=$_GET["imperative"];

        $obj=$_GET["txt_obj"];
        $col=$imp."_".$obj;

       
        if(!empty($obj) && !empty($col))
        {
            $sql4="INSERT INTO objectives (imperative,verb) VALUES('$imp','$obj')";
            $sql5="ALTER TABLE alt_objectives ADD $col varchar(40)";
            
            if ($conn->query($sql4)== TRUE )
                echo " ";
            else
                echo "Error: " . $sql . "<br>" . $conn->error;
            
            if ($conn->query($sql5)== TRUE)
                echo "<script type=\"text/javascript\">".
                "alert('Successfully saved');".
                "</script>";
            else
                echo "Error: " . $sql . "<br>" . $conn->error;
        }
        else
            echo "<script type=\"text/javascript\">".
            "alert('Enter a valid value');".
            "</script>";
        
        
       
        
        
    }
    ?>
