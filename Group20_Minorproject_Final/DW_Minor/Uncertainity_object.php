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
<title>Uncertainty Object</title>
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
<p style="text-align:center">Uncertainty Object</p>
</header>
<div style="text-align:center">
<form>

<label for="alt_values2">Select Alternative </label>
<select id="alt_values2" name="Alternative">Select Alternative
<option value="Select Alternative"> Select Alternative </option>

<?php
    
    
    $sql = "select * from alternatives ";
    if($res = $conn->query($sql)){
        
        while($list = $res->fetch_array(MYSQLI_ASSOC))
        {
            $alternate_values2=$list["alt_name"];
            ?>

<option value="<?php echo $alternate_values2;?>"> <?php echo $alternate_values2;?></option>

<?php
    }
    }
    ?>
</select><br>

<label for="un_values">Select Uncertainty </label>
<select id="un_values" name="Uncertainty">Select Uncertainty
<option value="Select Uncertainty"> Select Uncertainty </option>

<?php
    
    
    $sql2 = "show columns from alt_uncertainties";
    if($res2 = $conn->query($sql2)){
        echo " ";
        while($list2 = $res2->fetch_array(MYSQLI_ASSOC))
        {
            if($list2["Field"]!="alt_name")
                $attribute_values1=$list2["Field"];
            else
                continue;
            ?>


<option value="<?php echo $attribute_values1;?>"> <?php echo $attribute_values1 ;?></option>

<?php
    }
    }
    ?>
</select><br>
<label for="t_value">Value</label>
<input type="text" id="t_value" name="txt_val2"><br>
<button class="button" type="submit" value="Save" name="obj_save"  style="margin-top:10px">Save</button>
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
    if (isset($_GET["Alternative"]) && isset($_GET["Uncertainty"]) && isset($_GET["txt_val2"]))
    {
        $row2=$_GET["Alternative"];
        $col2=$_GET["Uncertainty"];
        $val2=$_GET["txt_val2"];
        
         if(!empty($row2) && !empty($col2) && !empty($val2) && $row2!="Select Alternative" && $col!="Select Uncertainty")
         {
        $sql4="update alt_uncertainties set $col2='$val2' where alt_name = '$row2' ";
        
        if ($conn->query($sql4)== TRUE)
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


