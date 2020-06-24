<?php
include("connection.php")
?>

<html>
<title>Values Page</title>
	</head>
		<body>
			<form>
				<label for="sel_alt">Select Alternatives </label>
				<select id="sel_alt">
				<option value="opt1">Option1</option>
				<option value="opt2">Option2</option>
				<option value="opt3">Option3</option>
				<option value="opt4">Option4</option>
				</select><br>
				
				<label for="sel_obj">Select objectives   </label>

				<select id="sel_obj">
				<option value="opt1">Option1</option>
				<option value="opt2">Option2</option>
				<option value="opt3">Option3</option>
				<option value="opt4">Option4</option>
				</select><br>
				<label for="t_value1">Value</label><br>
				<input type="text" id="t_value1" name="txt_action"><br>
				<button type="submit" value="Save" name="page6_save" >Save</button>
			</form>
		</body>
	</head>
</html>