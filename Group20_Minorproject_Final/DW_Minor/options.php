<?php
include("connection.php")
?>

<html>
<title>Action Page</title>
	</head>
		<body>
			<form>
				<label for="institute_name">Enter the Institute Name: </label><br>
				<input type="text" id="institute_name" name="institute_name"><br>
				<button type="submit" value="Save" name="act_save1"  >Save</button>
			</form>
		</body>
	</head>
</html>
<?php 
if(isset($_GET["institute_name"]))
{
	$option=$_GET["institute_name"];
	$sql="INSERT INTO alternatives(alt_name)VALUES('$option')";
    $sql2="SELECT id from alternatives where alt_name='$option'";
	

	if ($conn->query($sql)== TRUE) {
    echo "";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}
if ($conn->query($sql1)== TRUE) {
    echo "";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}
if ($res=$conn->query($sql2)== TRUE) {
        echo "";
        $id_val=$res.fetch_assoc($res)
        $sql1="INSERT INTO institute_attribute(alt_id)VALUES('$id_val')";
        if ($conn->query($sql1)== TRUE) {
        echo "";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
    
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

}
?>
