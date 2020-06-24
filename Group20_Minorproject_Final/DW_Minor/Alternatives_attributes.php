<?php
include("connection.php")
?>

<html>
<title>Page 3</title>
	</head>
		<body>
			<form>
				<label for="s_action">Select Institute</label>
				<label for="txt_s_action">Action values associated with alternative </label>
				<input type="text" id="attribute" name="attribute"><br>
				<button type="submit" value="Save" name="s_action_save" >Save</button>
			</form>
		</body>
	</head>
	</html>
<select id="select_obj" name="institute">Select Institute
<option value="select institute"> Select Institute</option>

<?php
if(isset($_GET["attribute"]))
{}
	
 $sql = "select  * from alternatives";
  if($res = $conn->query($sql)){
	  echo " ";
  while($list = $res->fetch_assoc())
  { 
	$institute_name=$list["alt_name"];?>

  <option value="<?php echo $institute_name;?>"> <?php echo $institute_name;?></option>
 
  <?php
  }
  }
  ?>
  </select>
   <select id="select_obj" name="institute">Select attribute
<option value="select institute"> Select attribute</option>
<?php
$sql1 = "show columns from institute_attribute";
  if($res1 = $conn->query($sql1)){
  while($list2 = $res1->fetch_array(MYSQLI_ASSOC))
  {$institute_name1=$list2["Field"];?>
  <option value="<?php echo $institute_name1;?>"> <?php echo $institute_name1;?></option>
  <?php
  }
  }
 
  ?>
</select>
